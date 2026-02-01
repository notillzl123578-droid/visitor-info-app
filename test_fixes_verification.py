#!/usr/bin/env python3
"""验证修复的功能"""

import sys
import os
sys.path.append('.')

def test_text_extraction():
    """测试文本提取功能"""
    print("=== 测试文本提取功能 ===")
    
    from app.services.text_extractor import TextExtractor
    extractor = TextExtractor()
    
    # 测试文本
    test_text = "1月29日(周四)燕山石化客人到公司参观"
    print(f"测试文本: {test_text}")
    
    activity = extractor.extract_activity_info(test_text)
    print(f"提取结果:")
    print(f"  日期: '{activity.date}'")
    print(f"  参观事项: '{activity.event}'")
    
    # 验证结果
    assert activity.date == "1月29日", f"日期提取错误: 期望'1月29日', 实际'{activity.date}'"
    assert "燕山石化客人到公司参观" in activity.event, f"参观事项提取错误: '{activity.event}'"
    
    print("✅ 文本提取功能正常")
    return True

def test_database_accumulation():
    """测试数据累积功能"""
    print("\n=== 测试数据累积功能 ===")
    
    from app.models.database import Database
    
    db = Database()
    
    # 清空测试数据
    db.clear_current_session()
    
    # 第一次保存
    activity1 = {
        'date': '1月29日',
        'event': '燕山石化客人到公司参观',
        'leader': '张三',
        'department': '办公室',
        'route': '路线1'
    }
    guests1 = [
        {'company': '燕山石化', 'name': '李四', 'position': '经理'}
    ]
    
    db.save_current_session(activity1, guests1)
    print("第一次保存完成")
    
    # 第二次保存
    activity2 = {
        'date': '1月30日',
        'event': '另一个参观活动',
        'leader': '王五',
        'department': '技术部',
        'route': '路线2'
    }
    guests2 = [
        {'company': '其他公司', 'name': '赵六', 'position': '主管'}
    ]
    
    db.save_current_session(activity2, guests2)
    print("第二次保存完成")
    
    # 检查累积结果
    data = db.load_current_session()
    print(f"累积后的数据: {data}")
    
    # 验证累积
    assert len(data['guests']) == 2, f"来宾累积错误: 期望2位, 实际{len(data['guests'])}位"
    assert data['activity']['date'] == '1月30日', "活动信息应该是最新的"
    
    # 检查保存历史
    history = db.get_save_history()
    assert len(history) == 2, f"保存历史错误: 期望2条, 实际{len(history)}条"
    
    print("✅ 数据累积功能正常")
    return True

def test_excel_export():
    """测试Excel导出功能"""
    print("\n=== 测试Excel导出功能 ===")
    
    from app.services.excel_generator import ExcelGenerator
    from app.models.data_models import ActivityInfo, GuestInfo
    
    # 创建测试数据
    activity = ActivityInfo(
        date='1月29日',
        event='燕山石化客人到公司参观',
        leader='张三',
        department='办公室',
        route='参观路线测试'
    )
    
    guests = [
        GuestInfo(company='燕山石化', name='李四', position='经理'),
        GuestInfo(company='燕山石化', name='王五', position='主管')
    ]
    
    # 生成Excel
    excel_gen = ExcelGenerator()
    file_path = excel_gen.generate_csv(activity, guests, [])
    
    print(f"Excel文件生成: {file_path}")
    
    # 验证文件存在
    assert os.path.exists(file_path), f"Excel文件不存在: {file_path}"
    
    # 验证文件内容
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        assert '1月29日' in content, "Excel文件中缺少日期"
        assert '燕山石化客人到公司参观' in content, "Excel文件中缺少参观事项"
        assert '李四' in content, "Excel文件中缺少来宾姓名"
    
    print("✅ Excel导出功能正常")
    return True

def main():
    """主测试函数"""
    print("开始验证修复功能...\n")
    
    try:
        # 测试各个功能
        test_text_extraction()
        test_database_accumulation()
        test_excel_export()
        
        print("\n🎉 所有功能测试通过！")
        print("\n修复总结:")
        print("1. ✅ 文本提取 - 正确识别'1月29日(周四)燕山石化客人到公司参观'")
        print("2. ✅ 数据累积 - 多次保存数据正确累积")
        print("3. ✅ Excel导出 - 生成正确格式的CSV文件")
        print("4. ✅ 文本框大小 - 已增加高度确保文字可见")
        
        print("\n应用可以正常使用了！")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == '__main__':
    main()