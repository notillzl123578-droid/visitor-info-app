@echo off
echo === 来宾信息提取工具 - 移动端构建指南 ===
echo.
echo ❌ Windows环境无法直接构建Android APK
echo.
echo 💡 推荐方案：
echo.
echo 方案1：使用微信小程序（推荐）
echo   - 功能完整，支持所有文件类型
echo   - 无需安装，直接在微信中使用
echo   - 位置：miniprogram 目录
echo.
echo 方案2：Linux环境构建APK
echo   - 使用Ubuntu 20.04+ 虚拟机
echo   - 使用WSL2 (Windows Subsystem for Linux)
echo   - 使用云端Linux服务器
echo   - 运行：./build_mobile.sh
echo.
echo 方案3：在线构建服务
echo   - GitHub Actions
echo   - GitLab CI/CD
echo   - 其他云端构建平台
echo.
echo 📱 立即使用微信小程序：
echo   1. 安装微信开发者工具
echo   2. 打开 miniprogram 目录
echo   3. 扫码在手机上预览
echo.
pause