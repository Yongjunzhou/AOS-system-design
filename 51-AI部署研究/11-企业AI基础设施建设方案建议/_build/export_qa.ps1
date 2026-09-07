$ErrorActionPreference = 'Stop'
$src = 'E:\mywork\AOS\51-AI部署研究\11-企业AI基础设施建设方案建议\11-企业AI基础设施建设方案建议.pptx'
$out = 'E:\mywork\AOS\51-AI部署研究\11-企业AI基础设施建设方案建议\_build\qa'
if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
$ppt = New-Object -ComObject PowerPoint.Application
try {
  $pres = $ppt.Presentations.Open($src, $true, $false, $false)
  $pres.Export($out, 'PNG', 1400, 788)
  $pres.Close()
  Write-Output ('exported to ' + $out)
} finally {
  $ppt.Quit()
}
