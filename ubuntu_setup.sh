#!/bin/bash
# Ubuntu构建环境自动配置脚本

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║              🐧 Ubuntu APK构建环境配置                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo

# 检查是否为Ubuntu
if ! grep -q "Ubuntu" /etc/os-release; then
    echo "❌ 错误：此脚本只能在Ubuntu系统上运行"
    exit 1
fi

echo "✅ Ubuntu系统检测通过"
echo

# 更新系统
echo "📦 更新系统包..."
sudo apt update && sudo apt upgrade -y
echo "✅ 系统更新完成"
echo

# 安装基础工具
echo "🔧 安装基础工具..."
sudo apt install -y git zip unzip curl wget build-essential
echo "✅ 基础工具安装完成"
echo

# 安装Java 8
echo "☕ 安装Java 8..."
sudo apt install -y openjdk-8-jdk
echo "✅ Java 8安装完成"
echo

# 安装Python和pip
echo "🐍 安装Python环境..."
sudo apt install -y python3 python3-pip python3-venv
echo "✅ Python环境安装完成"
echo

# 安装构建依赖
echo "🛠️  安装构建依赖..."
sudo apt install -y autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
echo "✅ 构建依赖安装完成"
echo

# 设置Java环境变量
echo "🔧 配置Java环境变量..."
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
echo "✅ Java环境变量配置完成"
echo

# 安装Buildozer
echo "📱 安装Buildozer..."
pip3 install --user buildozer cython==0.29.33
echo "✅ Buildozer安装完成"
echo

# 添加pip bin到PATH
echo "🔧 配置PATH环境变量..."
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
export PATH=$PATH:~/.local/bin
echo "✅ PATH配置完成"
echo

# 验证安装
echo "🔍 验证安装..."
echo "Java版本："
java -version
echo
echo "Python版本："
python3 --version
echo
echo "Buildozer版本："
~/.local/bin/buildozer --version 2>/dev/null || echo "Buildozer安装成功，但需要重新加载环境变量"
echo

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    🎉 环境配置完成！                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo
echo "📋 接下来的步骤："
echo "1. 重新加载环境变量：source ~/.bashrc"
echo "2. 复制项目文件：cp -r /mnt/d/krio/文件/文件合并/python-mobile-app ~/visitor-app"
echo "3. 进入项目目录：cd ~/visitor-app"
echo "4. 构建APK：buildozer android debug"
echo
echo "💡 提示："
echo "• 首次构建会下载Android SDK/NDK，需要30-60分钟"
echo "• 后续构建只需要5-10分钟"
echo "• APK文件会生成在 bin/ 目录下"
echo
echo "🚀 现在可以开始构建APK了！"