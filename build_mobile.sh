#!/bin/bash
# 移动端构建脚本

echo "=== 来宾信息提取工具 - 移动端构建 ==="

# 检查系统
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ 错误：需要Linux环境来构建Android APK"
    echo "💡 建议："
    echo "   1. 使用Ubuntu 20.04+ 虚拟机"
    echo "   2. 使用WSL2 (Windows Subsystem for Linux)"
    echo "   3. 使用云端Linux服务器"
    exit 1
fi

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到Python3"
    echo "安装命令：sudo apt install python3 python3-pip"
    exit 1
fi

# 检查Java
if ! command -v java &> /dev/null; then
    echo "❌ 错误：未找到Java"
    echo "安装命令：sudo apt install openjdk-8-jdk"
    exit 1
fi

echo "✅ 环境检查通过"

# 安装系统依赖
echo "📦 安装系统依赖..."
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 设置Java环境
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

# 安装Buildozer
echo "🔧 安装Buildozer..."
pip3 install --user buildozer
pip3 install --user cython==0.29.33

# 添加到PATH
export PATH=$PATH:~/.local/bin

# 检查buildozer
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer安装失败"
    echo "请手动添加到PATH：export PATH=\$PATH:~/.local/bin"
    exit 1
fi

echo "✅ Buildozer安装成功"

# 构建APK
echo "🏗️  开始构建APK..."
echo "⚠️  首次构建会下载Android SDK/NDK，需要较长时间和网络连接"

# 清理之前的构建
buildozer android clean

# 构建调试版APK
buildozer android debug

if [ $? -eq 0 ]; then
    echo "🎉 构建成功！"
    echo "📱 APK文件位置：bin/visitorinfo-2.0-arm64-v8a-debug.apk"
    echo ""
    echo "📋 安装方法："
    echo "   1. 将APK文件传输到Android手机"
    echo "   2. 在手机上启用'未知来源'安装"
    echo "   3. 点击APK文件安装"
    echo ""
    echo "🔧 或使用ADB安装："
    echo "   adb install bin/visitorinfo-2.0-arm64-v8a-debug.apk"
else
    echo "❌ 构建失败"
    echo "💡 常见解决方案："
    echo "   1. 检查网络连接"
    echo "   2. 确保有足够磁盘空间（至少5GB）"
    echo "   3. 检查Java版本：java -version"
    echo "   4. 重新运行：buildozer android debug --verbose"
fi