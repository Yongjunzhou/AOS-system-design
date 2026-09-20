# crop-cover.ps1 — 裁剪封面 PNG：去掉左 60px 书脊，得 800×1132 前封（EPUB 封面 + PDF 封面页）
# 用法：powershell -ExecutionPolicy Bypass -File crop-cover.ps1 <源PNG> <输出PNG>
param([string]$src, [string]$dst)
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Bitmap]::FromFile((Resolve-Path $src))
$rect = [System.Drawing.Rectangle]::new(60, 0, 800, 1132)
$crop = $img.Clone($rect, $img.PixelFormat)
$crop.Save($dst, [System.Drawing.Imaging.ImageFormat]::Png)
$img.Dispose(); $crop.Dispose()
Write-Output "cover cropped: $dst"
