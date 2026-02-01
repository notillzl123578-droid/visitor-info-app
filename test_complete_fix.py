#!/usr/bin/env python3
"""完整功能测试"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Database
from app.services.excel_generator import ExcelGenerator

def test_complete_workflow():
    """测试完整工作流程"""
    print("=== 完整功能测试 ===")
    
    # 清理旧数据库
    if os.path.exists('data/app.db'):
        os.remove('data/app.db')
        print("✓ 清理旧数据库")
    
    # 1. 初始化
    db = Database()
    print("✓ 数据库初始化")
    
    # 2. 第一次处理数据
    print("\n--- 第一次处理数据 ---")
    activity1 = {
        'date': '6月10日',
        'event': '海南省国企董事会参观',
        'leader': '张三',
        'department': '办公室',
        'route': '展厅A -> 展厅B'
    }
    guests1 = [
        {'company': '海南省国企', 'name': '李四', 'position': '董事长'},
        {'company': '海南省国企', 'name': '王五', 'position': '总经理'}
    ]
    
    db.save_current_session(activity1, guests1)
    
    # 3. 重复处理相同数据（应该被跳过）
    print("\n--- 重复处理相同数据（应该被跳过）---")
    db.save_current_session(activity1, guests1)
    
    # 4. 第二次处理不同数据
    print("\n--- 第二次处理不同数据 ---")
    activity2 = {
        'date': '1月29日',
        'event': '燕山石化参观',
        'leader': '赵六',
        'department': '技术部',
        'route': '生产车间 -> 控制室'
    }
    guests2 = [
        {'company': '燕山石化', 'name': '孙七', 'position': '厂长'}
    ]
    
    db.save_current_session(activity2, guests2)
    
    # 5. 检查累积数据
    print("\n--- 检查累积数据 ---")
    data = db.load_current_session()
    
    if data and 'batches' in data:
        batches = data['batches']
        total_guests = sum(len(batch.get('guests', [])) for batch in batches)
        
        print(f"✓ 累积数据: {len(batches)}个批次, {total_guests}位来宾")
        
        for i, batch in enumerate(batches):
            activity = batch.get('activity', {})
            guests = batch.get('guests', [])
            print(f"  批次{i+1}: {activity.get('date')} - {activity.get('event')} ({len(guests)}位来宾)")
        
        # 验证数据正确性
        if len(batches) == 2 and total_guests == 3:
            print("✅ 数据累积正确！")
        else:
            print(f"❌ 数据累积错误！期望2个批次3位来宾，实际{len(batches)}个批次{total_guests}位来宾")
            return False
    else:
        print("❌ 数据加载失败")
        return False
    
    # 6. 导出Excel
    print("\n--- 导出Excel ---")
    excel_generator = ExcelGenerator()
    file_path = excel_generator.generate_csv(batches_data=data['batches'])
    
    if os.path.exists(file_path):
        print(f"✓ Excel导出成功: {file_path}")
        
        # 验证文件内容
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            print(f"✓ 文件包含{len(lines)}行数据")
            
            # 应该有4行：1行表头 + 3行数据
            if len(lines) == 4:
                print("✅ Excel文件内容正确！")
            else:
                print(f"❌ Excel文件内容错误！期望4行，实际{len(lines)}行")
                return False
    else:
        print("❌ Excel文件未生成")
        return False
    
    # 7. 清空数据
    print("\n--- 清空数据 ---")
    db.clear_current_session()
    
    data_after_clear = db.load_current_session()
    if data_after_clear is None:
        print("✅ 数据清空成功！")
    else:
        print("❌ 数据清空失败")
        return False
    
    print("\n🎉 完整功能测试通过！")
    print("\n总结:")
    print("✅ 数据保存功能正常")
    print("✅ 重复数据检测正常")
    print("✅ 数据累积功能正常")
    print("✅ Excel导出功能正常")
    print("✅ 数据清空功能正常")
    
    return True

if __name__ == '__main__':
    success = test_complete_workflow()
    if success:
        print("\n🎉 所有问题已修复！应用可以正常使用！")
    else:
        print("\n❌ 测试失败，需要进一步检查")