---
name: env-dsh-pwsh-sandbox-acl
description: 环境故障与修法：DSH 的 pwsh 沙箱曾全部命令失败（SetNamedSecurityInfoW Win32 5），根因是 E:\mywork\AOS 缺属于本用户的显式 WRITE_DAC ACE；已修，附复现、修法与一条误判纠正
metadata:
  type: pending
---

**2026-09-22 发生并已修复。** 故障期间在 DSH 会话中执行任何 `pwsh` 命令，都在沙箱建立阶段失败，命令本身根本没跑起来：

```
SetNamedSecurityInfoW failed (Win32 5): grantWrite(E:\mywork\AOS)
```

**故障特征**（四条探测结论）：与命令内容无关；与命令的工作目录无关（授权根恒取会话工作区）；每次新建进程都重新失败，不是缓存；**普通文件读写完全正常**（同期用文件工具写入 `.claude/memory/` 与 `.tools/` 均成功）。因此坏点唯一：给工作区根目录改 DACL 这一步被拒。

**根因**：`E:\mywork\AOS` 与 `E:\mywork` 的**属主是 `BUILTIN\Administrators`**，且目录上全部 ACE 都是继承来的（`(I)`），没有一条属于本用户。本用户 `HUAWEI-CHOW\HUAWEI` 虽在管理员组内（`net localgroup Administrators` 可见），但 UAC 拆分令牌使非提权进程的令牌里没有管理员组（`is in Admins: False`），于是它**既不是属主、也没有显式 `WRITE_DAC`**，改 DACL 被 Win32 5 拒。这与 `@deepseek-ai/dsh-sandbox-windows-acl` 的既有约束一致：「Granted directories must be caller-owned」，且 `AclWriteGrant` fail-closed，授权失败即不启动子进程。

**已排除**：卷类型（`E:` 为 NTFS，非 FAT/exFAT）；目录为联接或符号链接；DSH 以管理员身份启动（宿主是非提权身份，`elevated: False`）。

**修法**（管理员窗口执行；真正生效的是 `icacls` 那条）：

```powershell
icacls "E:\mywork"     /grant "${env:USERDOMAIN}\${env:USERNAME}:(OI)(CI)F"
icacls "E:\mywork\AOS" /grant "${env:USERDOMAIN}\${env:USERNAME}:(OI)(CI)F" /T
```

**纠正一条先前误判**：修复当日一度以为生效原因是 `takeown` 改了属主，**实际不是**——`takeown /F <dir> /D Y` 在本机报「错误: /D 只能与 /R 一起指定」而未改属主（修好后属主仍是 `BUILTIN\Administrators`）。生效的是 `icacls` 补的那条**显式完全控制 ACE**：完全控制含 `WRITE_DAC`，沙箱因而无需属主身份即可改 DACL。故**修法不必夺属主，补显式授权即可**。

**修好后目录上的关键 ACE**（沙箱能力 ACE 与显式授权并存）：

```
E:\mywork\AOS S-1-4-935922043-301527324:(OI)(CI)(W,D,DC)   <- 沙箱写入能力 SID
              HUAWEI-CHOW\HUAWEI:(OI)(CI)(F)                <- 本次补的显式授权
              HUAWEI-CHOW\HUAWEI:(I)(OI)(CI)(F)
```

**注意授权不随 git 同步**：上述 ACE 是本机、本路径的安全描述符，克隆到别的机器或换路径后不会带过去，需重新补一次。

**顺带确认的沙箱边界**：受限令牌里 `Authenticated Users` 缺席导致 WMI 命名空间检查失败，故 `Get-CimInstance`／`Get-ComputerInfo` 在受沙箱限制的命令里一律报"拒绝访问"（`0x80041003`）。这不是故障。

**故障期间的影响**：`git log`／`git status`／`node .tools/*.js`／md2pdf 全部不可用，只能用文件工具读写；记忆机制那条线里"用提交号对账"因此停摆。

**同轮留下的工具**：`.tools/repair-sandbox-acl.ps1`（自提权版一键修复，推荐复用）、`.tools/fix-dsh-sandbox-acl.ps1`（早期非自提权版，保留作参考）。
