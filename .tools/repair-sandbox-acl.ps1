# repair-sandbox-acl.ps1
# One-click repair for the DSH workspace-write sandbox on this machine.
#
# Symptom:
#   SetNamedSecurityInfoW failed (Win32 5): grantWrite(E:\mywork\AOS)
#
# Root cause (confirmed 2026-09-22):
#   E:\mywork\AOS and E:\mywork are owned by BUILTIN\Administrators; all ACEs
#   are inherited. HUAWEI is a member of Administrators, but UAC split the
#   token, so the unelevated process is neither the owner nor privileged and
#   cannot edit the DACL. Editing the DACL requires the owner (or an elevated
#   token carrying SeTakeOwnershipPrivilege), so elevation is unavoidable.
#
# Usage (from an ORDINARY, non-elevated PowerShell - it self-elevates):
#   powershell -NoProfile -ExecutionPolicy Bypass -File E:\mywork\AOS\.tools\repair-sandbox-acl.ps1
#
# It will show a UAC prompt ("Do you want to allow this app to make changes
# to your device?"). Answer Yes. A log is written to:
#   E:\mywork\AOS\.tools\repair-sandbox-acl.log

param([switch]$Elevated)

$repo = 'E:\mywork\AOS'
$log  = 'E:\mywork\AOS\.tools\repair-sandbox-acl.log'
$self = $MyInvocation.MyCommand.Path

function Log([string]$Text) {
    Write-Host $Text
    Add-Content -LiteralPath $log -Value $Text -Encoding UTF8
}

# ---------------------------------------------------------------- self-elevate
$id = [Security.Principal.WindowsIdentity]::GetCurrent()
$isAdmin = ([Security.Principal.WindowsPrincipal]$id).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host 'Not elevated - requesting elevation (answer Yes to the UAC prompt)...'
    # clear any stale log first, then relaunch this same script elevated
    Remove-Item -LiteralPath $log -Force -ErrorAction SilentlyContinue
    $args = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', "`"$self`"", '-Elevated')
    try {
        Start-Process -FilePath 'powershell.exe' -ArgumentList $args -Verb RunAs -Wait
    } catch {
        Write-Host ''
        Write-Host "Elevation was refused or failed: $($_.Exception.Message)"
        Write-Host 'Nothing was changed. Re-run this script and answer Yes to the UAC prompt.'
        exit 4
    }
    if (Test-Path -LiteralPath $log) {
        Write-Host ''
        Write-Host '--- log from the elevated run ---'
        Get-Content -LiteralPath $log | ForEach-Object { Write-Host $_ }
    } else {
        Write-Host 'No log was produced - the elevated run did not start.'
    }
    exit 0
}

# ------------------------------------------------------------- elevated branch
Remove-Item -LiteralPath $log -Force -ErrorAction SilentlyContinue
Log ("repair-sandbox-acl  {0}" -f (Get-Date -Format s))
Log ("elevated        : {0}" -f $isAdmin)
Log ("running as      : {0}" -f $id.Name)

$me = "$env:USERDOMAIN\$env:USERNAME"

# before
Log ''
Log '=== BEFORE ==='
Log ("owner(repo)     : {0}" -f (Get-Acl -LiteralPath $repo).Owner)
Log ("owner(parent)   : {0}" -f (Get-Acl -LiteralPath 'E:\mywork').Owner)

# repair repo, then parent (both levels must be caller-owned to be safe)
Log ''
Log '=== REPAIR ==='
foreach ($target in @($repo, 'E:\mywork')) {
    Log ("takeown /F {0} /D Y" -f $target)
    (& takeown.exe /F $target /D Y 2>&1) | ForEach-Object { Log ('  ' + $_) }

    Log ("icacls {0} /grant {1}:(OI)(CI)F" -f $target, $me)
    (& icacls.exe $target /grant "${me}:(OI)(CI)F" 2>&1) | ForEach-Object { Log ('  ' + $_) }
}

Log ("icacls {0} /grant {1}:(OI)(CI)F /T   (walks the whole tree; be patient)" -f $repo, $me)
(& icacls.exe $repo /grant "${me}:(OI)(CI)F" /T 2>&1) | ForEach-Object { Log ('  ' + $_) }

# after
Log ''
Log '=== AFTER ==='
$ownerRepo   = (Get-Acl -LiteralPath $repo).Owner
$ownerParent = (Get-Acl -LiteralPath 'E:\mywork').Owner
Log ("owner(repo)     : {0}" -f $ownerRepo)
Log ("owner(parent)   : {0}" -f $ownerParent)
Log 'icacls(repo), first 10 lines:'
(& icacls.exe $repo 2>&1) | Select-Object -First 10 | ForEach-Object { Log ('  ' + $_) }

# write test
Log ''
Log '=== WRITE TEST ==='
$probe = Join-Path $repo '.acl-repair-probe.tmp'
try {
    Set-Content -LiteralPath $probe -Value 'probe' -Encoding UTF8 -ErrorAction Stop
    Log ("write test      : OK ({0})" -f $probe)
    Remove-Item -LiteralPath $probe -Force
    Log 'write test      : probe removed'
} catch {
    Log ("write test      : FAILED - {0}" -f $_.Exception.Message)
}

$ok = ($ownerRepo -replace '^.*\\', '') -eq $env:USERNAME
Log ''
if ($ok) {
    Log 'VERDICT         : owner is now HUAWEI - the DSH sandbox should work. No restart needed.'
} else {
    Log 'VERDICT         : owner is still not HUAWEI - send me this log.'
}
Log ("log             : {0}" -f $log)
