# WSL2自动安装脚本
# 需要以管理员身份运行PowerShell

Write-Host "=== 来宾信息提取工具 - WSL2安装脚本 ===" -ForegroundColor Green
Write-Host ""

# 检查管理员权限
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ 错误：需要管理员权限" -ForegroundColor Red
    Write-Host "请右键点击PowerShell，选择'以管理员身份运行'" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "✅ 管理员权限检查通过" -ForegroundColor Green

# 检查Windows版本
$version = [System.Environment]::OSVersion.Version
if ($version.Major -lt 10 -or ($version.Major -eq 10 -and $version.Build -lt 18362)) {
    Write-Host "❌ 错误：需要Windows 10版本1903或更高版本" -ForegroundColor Red
    Write-Host "当前版本：$($version.Major).$($version.Minor).$($version.Build)" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "✅ Windows版本检查通过" -ForegroundColor Green

# 启用WSL功能
Write-Host "📦 启用WSL功能..." -ForegroundColor Cyan
try {
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    Write-Host "✅ WSL功能已启用" -ForegroundColor Green
} catch {
    Write-Host "❌ WSL功能启用失败" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
}

# 启用虚拟机平台
Write-Host "🖥️  启用虚拟机平台..." -ForegroundColor Cyan
try {
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    Write-Host "✅ 虚拟机平台已启用" -ForegroundColor Green
} catch {
    Write-Host "❌ 虚拟机平台启用失败" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
}

# 下载WSL2内核更新包
Write-Host "⬇️  下载WSL2内核更新包..." -ForegroundColor Cyan
$kernelUrl = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
$kernelPath = "$env:TEMP\wsl_update_x64.msi"

try {
    Invoke-WebRequest -Uri $kernelUrl -OutFile $kernelPath
    Write-Host "✅ 内核更新包下载完成" -ForegroundColor Green
    
    # 安装内核更新包
    Write-Host "📦 安装WSL2内核更新..." -ForegroundColor Cyan
    Start-Process -FilePath $kernelPath -ArgumentList "/quiet" -Wait
    Write-Host "✅ WSL2内核更新安装完成" -ForegroundColor Green
} catch {
    Write-Host "❌ WSL2内核更新下载/安装失败" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🔄 需要重启计算机以完成WSL2安装" -ForegroundColor Yellow
Write-Host ""
Write-Host "重启后请运行：install_ubuntu.ps1" -ForegroundColor Cyan
Write-Host ""

$restart = Read-Host "是否现在重启计算机？(y/n)"
if ($restart -eq "y" -or $restart -eq "Y") {
    Write-Host "🔄 正在重启..." -ForegroundColor Cyan
    Restart-Computer -Force
} else {
    Write-Host "⚠️  请手动重启计算机，然后运行 install_ubuntu.ps1" -ForegroundColor Yellow
    pause
}