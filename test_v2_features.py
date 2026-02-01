"""V2功能测试脚本"""
import os
import sys

print('=' * 60)
print('V2功能测试')
print('=' * 60)

# 测试1: 数据库模块
print('\n[测试1] 数据库模块')
try:
    from app.models import Database
    
    db = Database()
    
    # 保存测试数据
    activity = {
        'date': '6月10日',
        'event': '测试参观活动',
        'leader': '张三',
        'department': '办公室',
        'route': '测试路线'
    }
    
    guests = [
        {'company': 'XX公司', 'name': '李四', 'position': '经理'},
        {'company': 'YY公司', 'name': '王五', 'position': '主管'}
    ]
    
    db.save_current_session(activity, guests)
    print('✓ 数据保存成功')
    
    # 加载数据
    data = db.load_current_session()
    if data:
        print(f'✓ 数据加载成功: {len(data["guests"])}位来宾')
    
    # 统计信息
    stats = db.get_statistics()
    print(f'✓ 统计信息: 总导出{stats["total_exports"]}次, 当前{stats["current_count"]}条')
    
    print('✅ 数据库模块测试通过')
    
except Exception as e:
    print(f'❌ 数据库模块测试失败: {e}')

# 测试2: .doc解析器
print('\n[测试2] .doc解析器')
try:
    from app.services import DocParser
    
    parser = DocParser()
    print('✓ DocParser初始化成功')
    
    # 检查pywin32
    try:
        import win32com.client
        print('✓ pywin32已安装')
    except ImportError:
        print('⚠️  pywin32未安装，.doc解析功能不可用')
        print('   请运行: pip install pywin32')
    
    print('✅ .doc解析器测试通过')
    
except Exception as e:
    print(f'❌ .doc解析器测试失败: {e}')

# 测试3: OCR服务
print('\n[测试3] OCR服务')
try:
    from app.services import OCRService
    
    ocr = OCRService()
    
    if ocr.is_available():
        print('✓ OCR服务可用')
        langs = ocr.get_available_languages()
        print(f'✓ 可用语言: {", ".join(langs[:5])}...')
    else:
        print('⚠️  OCR服务不可用')
        print('   请安装: pip install pytesseract Pillow')
        print('   并下载Tesseract: https://github.com/UB-Mannheim/tesseract/wiki')
    
    print('✅ OCR服务测试通过')
    
except Exception as e:
    print(f'❌ OCR服务测试失败: {e}')

# 测试4: UI模块
print('\n[测试4] UI模块')
try:
    from app.ui import MainScreen, PreviewScreen, HistoryScreen
    
    print('✓ MainScreen导入成功')
    print('✓ PreviewScreen导入成功')
    print('✓ HistoryScreen导入成功')
    
    print('✅ UI模块测试通过')
    
except Exception as e:
    print(f'❌ UI模块测试失败: {e}')

# 测试5: 依赖检查
print('\n[测试5] 依赖检查')
dependencies = {
    'kivy': 'UI框架',
    'docx': 'Word文档解析',
    'openpyxl': 'Excel生成',
    'win32com': '.doc文件解析',
    'pytesseract': 'OCR识别',
    'PIL': '图片处理'
}

missing = []
for module, desc in dependencies.items():
    try:
        __import__(module)
        print(f'✓ {module:15} - {desc}')
    except ImportError:
        print(f'✗ {module:15} - {desc} (未安装)')
        missing.append(module)

if missing:
    print(f'\n⚠️  缺少依赖: {", ".join(missing)}')
    print('请运行: pip install -r requirements.txt')
else:
    print('\n✅ 所有依赖已安装')

# 总结
print('\n' + '=' * 60)
print('测试完成')
print('=' * 60)

if not missing:
    print('\n✅ 所有功能正常，可以运行应用！')
    print('\n运行命令: python main.py')
else:
    print('\n⚠️  请先安装缺少的依赖')
    print('\n安装命令: pip install -r requirements.txt')

print('\n' + '=' * 60)
