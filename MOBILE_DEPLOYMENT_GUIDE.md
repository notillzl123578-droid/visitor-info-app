# 移动端部署指南

## 方案选择

您有两个主要选择来在手机上使用来宾信息提取工具：

### 方案1：Android APK（推荐）
将现有Python应用打包为Android APK，可以在Android手机上直接安装使用。

### 方案2：微信小程序（已有）
您已经有一个功能完整的微信小程序版本，可以直接在微信中使用。

---

## 方案1：Android APK 部署

### 前置要求
1. **Linux环境**（推荐Ubuntu 20.04+）
2. **Python 3.8+**
3. **Java JDK 8**
4. **Android SDK**
5. **Buildozer工具**

### 安装步骤

#### 1. 安装系统依赖
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 设置Java环境
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
```

#### 2. 安装Buildozer
```bash
pip3 install --user buildozer
pip3 install --user cython==0.29.33
```

#### 3. 初始化Android环境
```bash
# 进入项目目录
cd python-mobile-app

# 初始化buildozer（首次运行会下载Android SDK/NDK）
buildozer android debug
```

#### 4. 构建APK
```bash
# 构建调试版APK
buildozer android debug

# 构建发布版APK（需要签名）
buildozer android release
```

#### 5. 安装到手机
```bash
# 通过ADB安装
adb install bin/visitorinfo-2.0-arm64-v8a-debug.apk

# 或者直接将APK文件传输到手机安装
```

### 移动版功能限制
- **不支持.doc文件**：移动版暂时只支持文本输入和图片OCR
- **简化OCR**：使用系统内置OCR功能
- **本地存储**：数据保存在应用私有目录
- **CSV导出**：导出到手机下载目录

---

## 方案2：微信小程序（推荐快速使用）

### 优势
- **无需安装**：直接在微信中使用
- **功能完整**：支持文本、图片、Word、Excel文件
- **云端处理**：OCR识别更准确
- **即时分享**：可以直接分享给其他人

### 使用方法
1. 在微信中搜索小程序（如果已发布）
2. 或者扫描小程序二维码
3. 直接使用，无需安装

### 小程序功能
- ✅ 文本输入
- ✅ 图片OCR识别
- ✅ Word文档解析
- ✅ Excel文件导入
- ✅ 数据累积保存
- ✅ CSV文件导出

---

## 推荐方案

### 立即使用：微信小程序
如果您需要立即在手机上使用，推荐使用已有的微信小程序版本：
- 功能最完整
- 无需安装配置
- 支持所有文件类型
- OCR识别准确

### 长期使用：Android APK
如果您希望有独立的手机应用：
- 需要Linux环境编译
- 功能相对简化
- 可以离线使用
- 更好的隐私保护

---

## 快速测试

### 测试微信小程序
1. 打开 `miniprogram` 目录
2. 使用微信开发者工具打开
3. 在手机微信中扫码预览

### 测试Android编译
```bash
# 在Linux环境中
cd python-mobile-app
buildozer android debug
```

---

## 故障排除

### Buildozer常见问题
1. **Java版本错误**：确保使用JDK 8
2. **权限问题**：确保有写入权限
3. **网络问题**：首次构建需要下载大量文件
4. **内存不足**：编译需要至少4GB RAM

### 解决方案
```bash
# 清理构建缓存
buildozer android clean

# 重新构建
buildozer android debug

# 查看详细日志
buildozer android debug --verbose
```

---

## 联系支持

如果在部署过程中遇到问题，请提供：
1. 操作系统信息
2. 错误日志
3. 具体的错误步骤

我们会协助您完成移动端部署。