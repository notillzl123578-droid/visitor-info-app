# 🏠 本地构建Android APK指南

## 🎯 目标
在您的Windows电脑上本地构建APK，无需上传代码到任何地方

## 💡 为什么需要Linux环境？
Android APK构建工具（Buildozer）只能在Linux系统上运行，所以我们需要在Windows上安装一个Linux子系统（WSL2）。

## 🚀 本地构建步骤

### 步骤1：安装WSL2（一次性设置）

1. **以管理员身份打开PowerShell**
   - 右键点击"开始"按钮
   - 选择"Windows PowerShell (管理员)"

2. **运行安装脚本**
   ```powershell
   # 进入项目目录
   cd "D:\krio\文件\文件合并\python-mobile-app"
   
   # 运行WSL2安装脚本
   .\install_wsl2.ps1
   ```

3. **重启电脑**
   - 脚本会提示重启，选择"y"自动重启

### 步骤2：配置Ubuntu环境

1. **重启后运行Ubuntu配置**
   ```powershell
   # 以管理员身份打开PowerShell
   cd "D:\krio\文件\文件合并\python-mobile-app"
   
   # 运行Ubuntu安装脚本
   .\install_ubuntu.ps1
   ```

2. **启动Ubuntu**
   - 在开始菜单搜索"Ubuntu"
   - 首次启动会要求设置用户名和密码

3. **配置构建环境**
   ```bash
   # 在Ubuntu终端中运行
   bash ubuntu_setup.sh
   ```

### 步骤3：构建APK

1. **复制项目到Ubuntu**
   ```bash
   # 在Ubuntu终端中
   cp -r /mnt/d/krio/文件/文件合并/python-mobile-app ~/visitor-app
   cd ~/visitor-app
   ```

2. **构建APK**
   ```bash
   # 首次构建（需要下载Android SDK，比较慢）
   buildozer android debug
   
   # 构建完成后，APK文件在：
   # bin/visitorinfo-2.0-arm64-v8a-debug.apk
   ```

3. **复制APK到Windows**
   ```bash
   # 复制APK到Windows桌面
   cp bin/*.apk /mnt/c/Users/$(whoami)/Desktop/
   ```

## ⏱️ 时间预估

- **首次安装WSL2**：30-60分钟（包括下载和重启）
- **配置环境**：15-30分钟
- **首次构建APK**：30-60分钟（下载Android SDK）
- **后续构建**：5-10分钟

## 📱 安装APK到手机

1. **传输APK**
   - 通过USB数据线
   - 通过QQ/微信发送给自己
   - 通过蓝牙传输

2. **安装APK**
   - 在手机设置中启用"未知来源"安装
   - 点击APK文件安装

## 🔧 故障排除

### WSL2安装失败
- 确保Windows版本是Windows 10 1903+或Windows 11
- 在BIOS中启用虚拟化功能
- 以管理员身份运行PowerShell

### 构建失败
```bash
# 清理构建缓存
buildozer android clean

# 重新构建
buildozer android debug --verbose
```

### 网络问题
- 首次构建需要下载大量文件（约2-3GB）
- 确保网络连接稳定
- 可以使用手机热点如果WiFi不稳定

## 💾 磁盘空间需求

- WSL2 Ubuntu：约2GB
- Android SDK/NDK：约3GB
- 构建缓存：约1GB
- **总计需要约6GB空闲空间**

## 🎉 完成后

构建成功后，您将得到：
- `visitorinfo-2.0-arm64-v8a-debug.apk` - 可安装的Android应用
- 完全本地构建，无需上传任何代码
- 可以重复构建和修改

## 🚀 快速开始

如果您想立即开始：

1. **运行一键安装**：
   ```powershell
   # 以管理员身份运行
   .\BUILD_APK.bat
   # 选择选项2：WSL2本地构建
   ```

2. **按照提示操作**：
   - 安装WSL2
   - 重启电脑
   - 配置Ubuntu
   - 构建APK

整个过程完全在您的电脑上进行，代码不会离开您的机器！