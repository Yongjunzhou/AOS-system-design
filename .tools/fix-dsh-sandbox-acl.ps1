# fix-dsh-sandbox-acl.ps1
# Repair the Windows ACL precondition of the DSH workspace-write sandbox.
#
# Symptom it fixes:
#   SetNamedSecurityInfoW failed (Win32 5): grantWrite(E:\mywork\AOS)
#
# Root cause (confirmed on this machine 2026-09-22):
#   E:\mywork\AOS is owned by BUILTIN\Administrators and every ACE on it is
#   inherited. The DSH host runs unelevated, and in an unelevated token
#   BUILTIN\Administrators is deny-only rather than an enabled SID, so the
#   host is not recognised as the owner and cannot edit the DACL.
#   The sandbox requires: "Granted directories must be caller-owned".
#
# Run this ONCE from an ELEVATED PowerShell (Run as administrator):
#   powershell -NoProfile -ExecutionPolicy Bypass -File E:\mywork\AOS\.tools\fix-dsh-sandbox-acl.ps1
# or from PowerShell 7:
#   pwsh -NoProfile -ExecutionPolicy Bypass -File E:\mywork\AOS\.tools\fix-dsh-sandbox-acl.ps1
#
# It repairs, verifies, and writes a full transcript to:
#   E:\mywork\_dsh-workspace\fix-dsh-sandbox-acl.log
# so the result can be read without copying anything out of the terminal.

$repo = 'E:\mywork\AOS'
$log  = 'E:\mywork\_dsh-workspace\fix-dsh-sandbox-acl.log'

function Write-Log([string]$Text) {
    Write-Host $Text
    Add-Content -LiteralPath $log -Value $Text -Encoding UTF8
}

# fresh log
$logDir = Split-Path -Parent $log
if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
Set-Content -LiteralPath $log -Value "fix-dsh-sandbox-acl  $(Get-Date -Format s)" -Encoding UTF8

# --- 0. must be elevated -----------------------------------------------------
$isAdmin = ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

Write-Log ("elevated       : {0}" -f $isAdmin)
Write-Log ("running as     : {0}" -f ([Security.Principal.WindowsIdentity]::GetCurrent().Name))
if (-not $isAdmin) {
    Write-Log ''
    Write-Log 'STOP: this window is NOT elevated.'
    Write-Log 'Right-click PowerShell -> "Run as administrator", then run the same command again.'
    exit 3
}

# --- 1. the volume must be able to carry ACLs --------------------------------
$drive = (Get-Item -LiteralPath $repo).PSDrive.Name
$fs    = (Get-Volume -DriveLetter $drive).FileSystemType
Write-Log ("volume {0}      : {1}" -f $drive, $fs)
if ($fs -ne 'NTFS') {
    Write-Log ''
    Write-Log "STOP: a $fs volume carries no NTFS security descriptors; repair is impossible."
    Write-Log 'Move the repository to an NTFS volume instead.'
    exit 2
}

# --- 2. before ---------------------------------------------------------------
Write-Log ''
Write-Log '=== BEFORE ==='
Write-Log ('owner          : {0}' -f (Get-Acl -LiteralPath $repo).Owner)
Write-Log 'icacls:'
(icacls $repo) | ForEach-Object { Write-Log ('  ' + $_) }

# --- 3. repair ---------------------------------------------------------------
$me = "$env:USERDOMAIN\$env:USERNAME"
Write-Log ''
Write-Log '=== REPAIR ==='
Write-Log ("target account : {0}" -f $me)

Write-Log ("takeown /F {0} /D Y" -f $repo)
(takeown /F $repo /D Y) | ForEach-Object { Write-Log ('  ' + $_) }

Write-Log ("icacls {0} /grant {1}:(OI)(CI)F" -f $repo, $me)
(icacls $repo /grant "${me}:(OI)(CI)F") | ForEach-Object { Write-Log ('  ' + $_) }

Write-Log ("icacls {0} /grant {1}:(OI)(CI)F /T  (this walks the whole tree; be patient)" -f $repo, $me)
(icacls $repo /grant "${me}:(OI)(CI)F" /T) | ForEach-Object { Write-Log ('  ' + $_) }

# --- 4. after -----------------------------------------------------------------
Write-Log ''
Write-Log '=== AFTER ==='
$ownerAfter = (Get-Acl -LiteralPath $repo).Owner
Write-Log ('owner          : {0}' -f $ownerAfter)
Write-Log 'icacls (first 12 lines):'
(icacls $repo) | Select-Object -First 12 | ForEach-Object { Write-Log ('  ' + $_) }

# --- 5. prove it: can this account write into the workspace? ------------------
Write-Log ''
Write-Log '=== WRITE TEST ==='
$probe = Join-Path $repo '.acl-repair-probe.tmp'
try {
    Set-Content -LiteralPath $probe -Value 'probe' -Encoding UTF8 -ErrorAction Stop
    Write-Log ("write test     : OK ({0} created)" -f $probe)
    Remove-Item -LiteralPath $probe -Force
    Write-Log 'write test     : probe removed'
} catch {
    Write-Log ("write test     : FAILED - {0}" -f $_.Exception.Message)
}

$ok = ($ownerAfter -replace '^.*\\', '') -eq $env:USERNAME
Write-Log ''
Write-Log ("VERDICT        : {0}" -f $(if ($ok) { 'owner is now the current user - DSH sandbox should work without restarting it' } else { 'owner is still not the current user - send me this log' }))
Write-Log ("log written to : {0}" -f $log)
