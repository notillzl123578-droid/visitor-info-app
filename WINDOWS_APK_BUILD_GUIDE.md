# 🪟 Windows环境下构建Android APK完整指南

## 🎯 目标
在Windows系统上构建来宾信息提取工具的Android APK

## 📋 方案选择

### 方案A：WSL2 + Ubuntu（推荐）
在Windows上安装Linux子系统，然后构建APK

### 方案B：GitHub Actions（最简单）
使用GitHub自动构建，无需本地环境

### 方案C：虚拟机
安装Ubuntu虚拟机进行构建

---

## 🚀 方案A：WSL2安装和构建

### 步骤1：安装WSL2

1. **以管理员身份打开PowerShell**
```powershell
# 启用WSL功能
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 启用虚拟机平台
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 重启计算机
Restart-Computer
```

2. **重启后，下载WSL2内核更新包**
   - 访问：https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
   - 下载并安装

3. **设置WSL2为默认版本**
```powershell
wsl --set-default-version 2
```

4. **安装Ubuntu**
```powershell
# 安装Ubuntu 20.04
wsl --install -d Ubuntu-20.04
```

### 步骤2：配置Ubuntu环境

1. **启动Ubuntu**
```bash
# 设置用户名和密码（首次启动时）
```

2. **更新系统**
```bash
sudo apt update && sudo apt upgrade -y
```

3. **安装构建依赖**
```bash
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
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
source ~/.bashrc
```

### 步骤3：安装Buildozer

```bash
# 安装Buildozer
pip3 install --user buildozer cython==0.29.33

# 添加到PATH
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### 步骤4：复制项目文件

```bash
# 在Ubuntu中创建项目目录
mkdir -p ~/visitor-app
cd ~/visitor-app

# 从Windows复制文件（假设Windows项目在D:\krio\文件\文件合并）
cp -r /mnt/d/krio/文件/文件合并/python-mobile-app/* .
```

### 步骤5：构建APK

```bash
# 进入项目目录
cd ~/visitor-app

# 首次构建（会下载Android SDK/NDK，需要时间和网络）
buildozer android debug

# 如果成功，APK文件在：bin/visitorinfo-2.0-arm64-v8a-debug.apk
```

---

## 🤖 方案B：GitHub Actions自动构建（推荐）

### 优势
- 无需本地Linux环境
- 自动化构建
- 构建结果可下载

### 步骤

1. **创建GitHub仓库**
   - 在GitHub上创建新仓库
   - 将项目代码上传

2. **推送代码**
```bash
# 在项目目录中
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/visitor-info-app.git
git push -u origin main
```

3. **自动构建**
   - 推送后GitHub Actions会自动开始构建
   - 在仓库的Actions页面查看进度
   - 构建完成后下载APK文件

---

## 💻 方案C：虚拟机

### 步骤

1. **下载VirtualBox**
   - 访问：https://www.virtualbox.org/
   - 下载并安装

2. **下载Ubuntu ISO**
   - 访问：https://ubuntu.com/download/desktop
   - 下载Ubuntu 20.04 LTS

3. **创建虚拟机**
   - 分配至少4GB内存
   - 创建20GB硬盘空间
   - 安装Ubuntu

4. **按照方案A的步骤2-5进行构建**

---

## 🎯 推荐流程

### 快速开始（GitHub Actions）
1. 创建GitHub账号
2. 上传项目代码
3. 等待自动构建
4. 下载APK文件

### 本地开发（WSL2）
1. 安装WSL2和Ubuntu
2. 配置构建环境
3. 本地构建和测试

---

## 📱 APK安装

构建完成后：

1. **传输APK到手机**
   - 通过USB传输
   - 通过云盘分享
   - 通过邮件发送

2. **安装APK**
   - 在手机设置中启用"未知来源"
   - 点击APK文件安装
   - 需要Android 5.0+

---

## 🆘 故障排除

### WSL2安装问题
- 确保Windows版本支持WSL2（Windows 10 版本1903+）
- 在BIOS中启用虚拟化
- 以管理员身份运行命令

### 构建失败
- 检查网络连接（首次构建需下载大量文件）
- 确保有足够磁盘空间（至少5GB）
- 检查Java版本：`java -version`

### 常见错误
```bash
# 清理构建缓存
buildozer android clean

# 重新构建
buildozer android debug --verbose
```

---

## 📞 需要帮助？

如果遇到问题，请提供：
1. 选择的构建方案
2. 具体错误信息
3. 操作系统版本
4. 执行的命令

我会协助您解决构建问题！