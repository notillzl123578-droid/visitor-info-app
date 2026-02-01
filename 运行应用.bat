@echo off
chcp 65001 >nul
echo ========================================
echo 来宾信息提取工具
echo ========================================
echo.
echo 正在启动应用...
echo.
python main.py
if errorlevel 1 (
    echo.
    echo ========================================
    echo 启动失败！
    echo ========================================
    echo.
    echo 可能的原因:
    echo 1. Python未安装
    echo 2. 依赖未安装
    echo.
    echo 解决方法:
    echo 1. 安装Python: https://www.python.org/
    echo 2. 安装依赖: pip install kivy python-docx openpyxl
    echo.
)
pause
