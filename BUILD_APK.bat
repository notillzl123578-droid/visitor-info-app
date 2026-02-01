@echo off
chcp 65001 >nul
title 来宾信息提取工具 - Android APK构建

:MAIN
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                  📱 Android APK 构建工具                      ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 🎯 选择构建方法：
echo.
echo [1] 🤖 GitHub Actions自动构建 (推荐)
echo     ✅ 最简单，无需本地环境
echo     ✅ 云端构建，自动下载APK
echo     ✅ 适合所有用户
echo.
echo [2] 🪟 WSL2本地构建
echo     ✅ 本地控制，构建速度快
echo     ⚠️  需要安装Linux子系统
echo     ⚠️  需要管理员权限
echo.
echo [3] 📖 查看详细构建指南
echo.
echo [4] 🚪 退出
echo.
set /p choice="请选择 (1-4): "

if "%choice%"=="1" goto GITHUB
if "%choice%"=="2" goto WSL2
if "%choice%"=="3" goto GUIDE
if "%choice%"=="4" goto EXIT
goto MAIN

:GITHUB
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                🤖 GitHub Actions 自动构建                     ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 📋 步骤：
echo.
echo 1️⃣ 创建GitHub账号 (如果没有)
echo    👉 访问：https://github.com
echo.
echo 2️⃣ 创建新仓库
echo    👉 仓库名：visitor-info-app
echo    👉 设为Public (免费账号需要)
echo.
echo 3️⃣ 上传项目代码
echo    👉 将整个 python-mobile-app 文件夹上传到仓库
echo.
echo 4️⃣ 等待自动构建
echo    👉 访问仓库的 Actions 页面
echo    👉 等待构建完成 (15-30分钟)
echo.
echo 5️⃣ 下载APK
echo    👉 在 Artifacts 部分下载 visitor-info-apk
echo.
echo 📖 详细指南：GITHUB_BUILD_GUIDE.md
echo.
start "" "GITHUB_BUILD_GUIDE.md"
echo ✅ 已打开详细指南文档
echo.
pause
goto MAIN

@echo off
chcp 65001 >nul
title 来宾信息提取工具 - Android APK构建

:MAIN
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                  📱 Android APK 构建工具                      ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 🎯 选择构建方法：
echo.
echo [1] 🏠 本地构建APK (推荐个人使用)
echo     ✅ 完全本地，代码不离开您的电脑
echo     ✅ 一次配置，后续快速构建
echo     ⚠️  需要安装WSL2 (Windows Linux子系统)
echo.
echo [2] 🤖 GitHub云端构建
echo     ✅ 无需本地环境配置
echo     ⚠️  需要上传代码到GitHub
echo     ⚠️  适合开源项目
echo.
echo [3] 📖 查看详细构建指南
echo.
echo [4] 🚪 退出
echo.
set /p choice="请选择 (1-4): "

if "%choice%"=="1" goto LOCAL
if "%choice%"=="2" goto GITHUB
if "%choice%"=="3" goto GUIDE
if "%choice%"=="4" goto EXIT
goto MAIN

:LOCAL
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                🏠 本地构建APK (推荐个人使用)                   ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 💡 为什么选择本地构建？
echo    ✅ 代码完全保密，不上传到任何地方
echo    ✅ 一次配置，后续构建只需几分钟
echo    ✅ 完全控制构建过程
echo.
echo 📋 构建步骤：
echo.
echo 1️⃣ 安装WSL2 (Windows Linux子系统)
echo    👉 需要管理员权限，会自动重启电脑
echo.
echo 2️⃣ 配置Ubuntu构建环境
echo    👉 安装Java、Python、Android构建工具
echo.
echo 3️⃣ 构建APK
echo    👉 首次构建约30-60分钟，后续5-10分钟
echo.
echo ⏱️ 总时间：首次约2小时，后续几分钟
echo 💾 磁盘空间：约6GB
echo.
echo 🚀 开始本地构建？
set /p local_choice="输入 y 开始安装，其他键返回: "

if /i "%local_choice%"=="y" (
    echo.
    echo 🔧 准备启动WSL2安装...
    echo.
    echo ⚠️  重要提示：
    echo    1. 需要以管理员身份运行
    echo    2. 安装过程中会重启电脑
    echo    3. 首次构建需要下载约3GB文件
    echo.
    echo 📖 详细指南已打开：LOCAL_BUILD_GUIDE.md
    start "" "LOCAL_BUILD_GUIDE.md"
    echo.
    echo 🚀 请按照以下步骤操作：
    echo.
    echo 步骤1：以管理员身份打开PowerShell
    echo 步骤2：运行：.\install_wsl2.ps1
    echo 步骤3：重启电脑后运行：.\install_ubuntu.ps1
    echo 步骤4：在Ubuntu中构建APK
    echo.
    pause
)
goto MAIN

:GUIDE
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    📖 构建指南文档                            ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 📄 可用文档：
echo.
echo 1. GITHUB_BUILD_GUIDE.md - GitHub自动构建指南
echo 2. WINDOWS_APK_BUILD_GUIDE.md - Windows完整构建指南
echo 3. MOBILE_DEPLOYMENT_GUIDE.md - 移动端部署指南
echo 4. MOBILE_QUICK_START.md - 快速开始指南
echo.
echo 🚀 打开所有指南文档...
start "" "GITHUB_BUILD_GUIDE.md"
start "" "WINDOWS_APK_BUILD_GUIDE.md"
start "" "MOBILE_DEPLOYMENT_GUIDE.md"
start "" "MOBILE_QUICK_START.md"
echo.
echo ✅ 已打开所有指南文档
pause
goto MAIN

:EXIT
cls
echo.
echo 👋 感谢使用来宾信息提取工具！
echo.
echo 💡 推荐使用GitHub Actions自动构建，最简单快捷！
echo.
echo 📱 构建完成后，将APK传输到Android手机安装即可使用。
echo.
pause
exit

:ERROR
echo.
echo ❌ 发生错误，请检查输入
pause
goto MAIN