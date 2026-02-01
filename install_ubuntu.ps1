# Ubuntu安装和配置脚本
# 在WSL2安装完成并重启后运行

Write-Host "=== Ubuntu安装和APK构建环境配置 ===" -ForegroundColor Green
Write-Host ""

# 设置WSL2为默认版本
Write-Host "🔧 设置WSL2为默认版本..." -ForegroundColor Cyan
try {
    wsl --set-default-version 2
    Write-Host "✅ WSL2已设为默认版本" -ForegroundColor Green
} catch {
    Write-Host "❌ 设置WSL2默认版本失败" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
}

# 安装Ubuntu
Write-Host "📦 安装Ubuntu 20.04..." -ForegroundColor Cyan
Write-Host "⚠️  首次安装需要设置用户名和密码" -ForegroundColor Yellow
try {
    wsl --install -d Ubuntu-20.04
    Write-Host "✅ Ubuntu安装完成" -ForegroundColor Green
} catch {
    Write-Host "❌ Ubuntu安装失败，尝试从Microsoft Store安装" -ForegroundColor Red
    Write-Host "请访问：https://www.microsoft.com/store/productId/9N6SVWS3RX71" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "📋 接下来的步骤：" -ForegroundColor Yellow
Write-Host "1. 启动Ubuntu（在开始菜单搜索Ubuntu）" -ForegroundColor White
Write-Host "2. 设置用户名和密码" -ForegroundColor White
Write-Host "3. 运行以下命令配置构建环境：" -ForegroundColor White
Write-Host ""

$setupScript = @"
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装基础工具
sudo apt install -y git zip unzip curl wget

# 安装Java 8
sudo apt install -y openjdk-8-jdk

# 安装Python和pip
sudo apt install -y python3 python3-pip

# 安装构建依赖
sudo apt install -y autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 设置Java环境
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=`$PATH:`$JAVA_HOME/bin' >> ~/.bashrc

# 安装Buildozer
pip3 install --user buildozer cython==0.29.33

# 添加到PATH
echo 'export PATH=`$PATH:~/.local/bin' >> ~/.bashrc

# 重新加载环境
source ~/.bashrc

echo "✅ 构建环境配置完成！"
echo "📱 现在可以构建APK了："
echo "   1. 复制项目文件到Ubuntu"
echo "   2. 运行：buildozer android debug"
"@

Write-Host $setupScript -ForegroundColor Cyan

# 将脚本保存到文件
$setupScript | Out-File -FilePath "ubuntu_setup.sh" -Encoding UTF8
Write-Host ""
Write-Host "📄 配置脚本已保存为：ubuntu_setup.sh" -ForegroundColor Green
Write-Host "在Ubuntu中运行：bash ubuntu_setup.sh" -ForegroundColor Cyan

Write-Host ""
Write-Host "🚀 快速构建APK步骤：" -ForegroundColor Yellow
Write-Host "1. 启动Ubuntu" -ForegroundColor White
Write-Host "2. 运行：bash ubuntu_setup.sh" -ForegroundColor White
Write-Host "3. 复制项目：cp -r /mnt/d/krio/文件/文件合并/python-mobile-app ~/visitor-app" -ForegroundColor White
Write-Host "4. 进入目录：cd ~/visitor-app" -ForegroundColor White
Write-Host "5. 构建APK：buildozer android debug" -ForegroundColor White

pause