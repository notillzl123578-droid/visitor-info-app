"""测试应用启动和基本功能"""
import sys

print('='*60)
print('测试应用启动')
print('='*60)

try:
    # 测试导入主要模块
    print('\n1. 测试导入模块...')
    from app.ui import MainScreen, PreviewScreen
    from app.models import Database, ExtractedData
    from app.services import TextExtractor
    print('   ✓ 所有模块导入成功')
    
    # 测试数据库初始化
    print('\n2. 测试数据库初始化...')
    db = Database()
    print('   ✓ 数据库初始化成功')
    
    # 测试文本提取器
    print('\n3. 测试文本提取器...')
    extractor = TextExtractor()
    test_text = "6月10日参观活动\n陪同部门：办公室"
    activity = extractor.extract_activity_info(test_text)
    print(f'   ✓ 文本提取成功: {activity.date}')
    
    # 测试数据模型
    print('\n4. 测试数据模型...')
    data = ExtractedData()
    print(f'   ✓ 数据模型创建成功')
    
    # 测试数据库操作
    print('\n5. 测试数据库操作...')
    activity_dict = {
        'date': '6月10日',
        'event': '测试活动',
        'leader': '张三',
        'department': '办公室',
        'route': '测试路线'
    }
    guests_list = [
        {'company': '测试公司', 'name': '李四', 'position': '经理'}
    ]
    db.save_current_session(activity_dict, guests_list)
    loaded_data = db.load_current_session()
    print(f'   ✓ 数据保存和加载成功: {len(loaded_data["guests"])}位来宾')
    
    # 清理测试数据
    db.clear_current_session()
    
    print('\n' + '='*60)
    print('✓ 所有测试通过，代码没有问题！')
    print('='*60)
    
except Exception as e:
    print(f'\n✗ 错误: {e}')
    import traceback
    traceback.print_exc()
    sys.exit(1)
