@echo off
chcp 65001 >nul
title 本地构建Android APK

cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║              🏠 本地构建Android APK (个人使用)                 ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 💡 本地构建的优势：
echo    ✅ 代码完全保密，不上传到任何地方
echo    ✅ 一次配置，终身使用
echo    ✅ 构建速度快，完全可控
echo.
echo ⚠️  需要安装WSL2 (Windows的Linux子系统)
echo    📦 磁盘空间需求：约6GB
echo    ⏱️  首次配置时间：约1-2小时
echo    🚀 后续构建时间：5-10分钟
echo.

:MENU
echo 📋 请选择操作：
echo.
echo [1] 🔧 开始安装WSL2环境 (首次使用)
echo [2] 📱 构建APK (环境已配置)
echo [3] 📖 查看详细指南
echo [4] 🚪 退出
echo.
set /p choice="请选择 (1-4): "

if "%choice%"=="1" goto INSTALL
if "%choice%"=="2" goto BUILD
if "%choice%"=="3" goto GUIDE
if "%choice%"=="4" goto EXIT
echo 无效选择，请重新输入
goto MENU

:INSTALL
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    🔧 安装WSL2环境                           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 📋 安装步骤：
echo.
echo 步骤1：安装WSL2
echo   👉 需要管理员权限
echo   👉 会自动重启电脑
echo.
echo 步骤2：配置Ubuntu
echo   👉 重启后自动配置
echo   👉 安装构建工具
echo.
echo 步骤3：构建APK
echo   👉 首次构建较慢
echo   👉 后续构建很快
echo.
echo ⚠️  重要提示：
echo    • 确保网络连接稳定
echo    • 准备约6GB磁盘空间
echo    • 整个过程需要1-2小时
echo.
set /p install_choice="确定开始安装？(y/n): "

if /i "%install_choice%"=="y" (
    echo.
    echo 🚀 启动安装程序...
    echo.
    echo 📖 详细指南已打开，请按照指南操作
    start "" "LOCAL_BUILD_GUIDE.md"
    echo.
    echo 🔧 请按照以下步骤操作：
    echo.
    echo 1. 以管理员身份打开PowerShell
    echo    (右键开始按钮 → Windows PowerShell (管理员))
    echo.
    echo 2. 进入项目目录：
    echo    cd "D:\krio\文件\文件合并\python-mobile-app"
    echo.
    echo 3. 运行安装脚本：
    echo    .\install_wsl2.ps1
    echo.
    echo 4. 重启电脑后运行：
    echo    .\install_ubuntu.ps1
    echo.
    pause
)
goto MENU

:BUILD
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                      📱 构建APK                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 🔍 检查WSL2环境...

wsl --list --verbose >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ WSL2未安装，请先选择选项1安装环境
    pause
    goto MENU
)

echo ✅ WSL2环境检测通过
echo.
echo 📱 开始构建APK...
echo.
echo 🔧 构建命令：
echo    1. 启动Ubuntu
echo    2. 进入项目目录：cd ~/visitor-app
echo    3. 构建APK：buildozer android debug
echo    4. 复制APK：cp bin/*.apk /mnt/c/Users/%USERNAME%/Desktop/
echo.
echo 💡 提示：首次构建需要30-60分钟，后续构建5-10分钟
echo.
set /p build_choice="是否自动执行构建？(y/n): "

if /i "%build_choice%"=="y" (
    echo.
    echo 🚀 启动Ubuntu构建...
    wsl -d Ubuntu-20.04 bash -c "cd ~/visitor-app 2>/dev/null || (echo '复制项目文件...' && cp -r /mnt/d/krio/文件/文件合并/python-mobile-app ~/visitor-app && cd ~/visitor-app); echo '开始构建APK...'; buildozer android debug; echo '复制APK到桌面...'; cp bin/*.apk /mnt/c/Users/%USERNAME%/Desktop/ 2>/dev/null; echo '构建完成！APK已复制到桌面'"
    echo.
    echo 🎉 构建完成！请检查桌面上的APK文件
) else (
    echo.
    echo 📋 手动构建步骤：
    echo    1. 在开始菜单搜索并打开"Ubuntu"
    echo    2. 运行：cd ~/visitor-app
    echo    3. 运行：buildozer android debug
    echo    4. 运行：cp bin/*.apk /mnt/c/Users/%USERNAME%/Desktop/
)
pause
goto MENU

:GUIDE
start "" "LOCAL_BUILD_GUIDE.md"
echo ✅ 已打开详细构建指南
pause
goto MENU

:EXIT
cls
echo.
echo 👋 感谢使用本地APK构建工具！
echo.
echo 💡 记住：
echo    • 环境只需配置一次
echo    • 后续构建非常快速
echo    • 代码完全保密，不上传任何地方
echo.
echo 📱 构建完成后，将APK传输到Android手机安装即可！
echo.
pause
exit