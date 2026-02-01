@echo off
chcp 65001 >nul
echo ========================================
echo 来宾信息提取工具 - 打包脚本
echo ========================================
echo.

echo [1/5] 检查PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller未安装，正在安装...
    pip install pyinstaller
) else (
    echo ✓ PyInstaller已安装
)
echo.

echo [2/5] 检查PyInstaller路径...
python -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo ❌ PyInstaller路径有问题，尝试重新安装...
    pip uninstall pyinstaller -y
    pip install pyinstaller
) else (
    echo ✓ PyInstaller路径正常
)
echo.

echo [3/5] 清理旧文件...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist "来宾信息提取工具.spec" del "来宾信息提取工具.spec"
echo ✓ 清理完成
echo.

echo [4/5] 开始打包...
echo 这可能需要几分钟，请耐心等待...
echo 使用python -m PyInstaller命令...
python -m PyInstaller --name="来宾信息提取工具" --windowed --onefile --add-data "C:/Windows/Fonts/msyh.ttc;." main.py
echo.

if exist "dist\来宾信息提取工具.exe" (
    echo [5/5] 打包成功！
    echo.
    echo ========================================
    echo ✓ 打包完成！
    echo ========================================
    echo.
    echo 文件位置: dist\来宾信息提取工具.exe
    echo 文件大小: 
    dir "dist\来宾信息提取工具.exe" | find "来宾信息提取工具.exe"
    echo.
    echo 下一步:
    echo 1. 测试运行: 双击 dist\来宾信息提取工具.exe
    echo 2. 分发给用户: 将exe文件发送给其他人
    echo.
    echo 注意: 如果在其他电脑上运行出现字体问题，
    echo 请确保目标电脑安装了微软雅黑字体
    echo.
) else (
    echo [5/5] 打包失败！
    echo.
    echo 可能的原因:
    echo 1. 内存不足
    echo 2. 磁盘空间不足
    echo 3. 杀毒软件阻止
    echo.
    echo 解决方法:
    echo 1. 关闭其他程序释放内存
    echo 2. 清理磁盘空间
    echo 3. 临时关闭杀毒软件
    echo 4. 查看上方错误信息
    echo.
)

pause
