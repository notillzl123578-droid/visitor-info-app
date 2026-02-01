# 🤖 GitHub Actions自动构建APK指南

## 🎯 最简单的APK构建方法

使用GitHub Actions在云端自动构建APK，无需本地Linux环境！

## 📋 步骤

### 1. 创建GitHub账号
如果还没有GitHub账号：
- 访问：https://github.com
- 点击"Sign up"注册账号

### 2. 创建新仓库
1. 登录GitHub后点击右上角的"+"
2. 选择"New repository"
3. 仓库名称：`visitor-info-app`
4. 设为Public（免费账号需要公开仓库才能使用Actions）
5. 点击"Create repository"

### 3. 上传项目代码

#### 方法A：使用GitHub网页界面
1. 在新创建的仓库页面，点击"uploading an existing file"
2. 将整个`python-mobile-app`文件夹拖拽到页面上
3. 等待上传完成
4. 填写提交信息："Initial commit"
5. 点击"Commit changes"

#### 方法B：使用Git命令行
```bash
# 在python-mobile-app目录中打开命令行
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/visitor-info-app.git
git push -u origin main
```

### 4. 启动自动构建
1. 代码上传后，GitHub会自动检测到`.github/workflows/build-android.yml`
2. 访问仓库的"Actions"页面
3. 会看到构建任务正在运行
4. 等待构建完成（大约15-30分钟）

### 5. 下载APK
1. 构建完成后，在Actions页面点击最新的构建任务
2. 在"Artifacts"部分下载`visitor-info-apk`
3. 解压下载的文件，获得APK

## 🔧 构建配置说明

我已经为您创建了完整的GitHub Actions配置文件：
- `.github/workflows/build-android.yml`

这个配置会：
- ✅ 自动安装Ubuntu环境
- ✅ 安装Java 8和Python
- ✅ 安装所有构建依赖
- ✅ 使用Buildozer构建APK
- ✅ 自动上传构建结果

## 📱 APK功能

构建的APK包含：
- ✅ 文本输入和编辑
- ✅ 基础OCR功能（图片识别）
- ✅ 数据保存和管理
- ✅ CSV文件导出
- ✅ 蓝白色美观界面

## 🚀 快速开始

1. **立即构建**：
   - 创建GitHub仓库
   - 上传`python-mobile-app`文件夹
   - 等待自动构建完成

2. **下载安装**：
   - 下载构建好的APK
   - 传输到Android手机
   - 启用"未知来源"安装

## 📞 需要帮助？

如果在GitHub构建过程中遇到问题：
1. 检查Actions页面的构建日志
2. 确保仓库是Public（免费账号限制）
3. 确保所有文件都已正确上传

构建成功后，您就有了一个完整的Android应用！