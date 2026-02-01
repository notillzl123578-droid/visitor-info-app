@echo off
chcp 65001 >nul
echo ========================================
echo 启动V2美化版本
echo ========================================
echo.
echo 正在清除缓存...
rd /s /q app\__pycache__ 2>nul
rd /s /q app\ui\__pycache__ 2>nul
rd /s /q app\models\__pycache__ 2>nul
rd /s /q app\services\__pycache__ 2>nul
echo 缓存已清除
echo.
echo 正在启动应用...
python main.py
pause
