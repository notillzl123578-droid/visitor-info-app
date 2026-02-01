#!/usr/bin/env python3
"""测试紧急修复后的功能"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Database
from app.services.excel_generator import ExcelGenerator

def test_emergency_fix():
    """测试紧急修复后的功能"""
    print("=== 测试紧急修复后的功能 ===")
    
    # 1. 测试数据库初始化
    print("1. 测试数据库初始化...")
    db = Database()
    print("✓ 数据库初始化成功")
    
    # 2. 测试保存数据
    print("2. 测试保存数据...")
    
    # 第一批数据
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
    print("✓ 第一批数据保存成功")
    
    # 第二批数据
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
    print("✓ 第二批数据保存成功")
    
    # 3. 测试加载数据
    print("3. 测试加载数据...")
    data = db.load_current_session()
    
    if data and 'batches' in data:
        batches = data['batches']
        print(f"✓ 加载成功，共{len(batches)}个批次")
        
        total_guests = 0
        for i, batch in enumerate(batches):
            activity = batch.get('activity', {})
            guests = batch.get('guests', [])
            total_guests += len(guests)
            print(f"  批次{i+1}: {activity.get('date')} - {activity.get('event')} ({len(guests)}位来宾)")
        
        print(f"✓ 总计{total_guests}位来宾")
    else:
        print("❌ 数据加载失败")
        return False
    
    # 4. 测试Excel导出
    print("4. 测试Excel导出...")
    
    try:
        excel_generator = ExcelGenerator()
        file_path = excel_generator.generate_csv(batches_data=data['batches'])
        
        # 检查文件是否存在
        if os.path.exists(file_path):
            print(f"✓ Excel导出成功: {file_path}")
            
            # 读取文件内容验证
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                print(f"✓ 文件包含{len(lines)}行数据（含表头）")
                
                # 显示前几行
                for i, line in enumerate(lines[:5]):
                    print(f"  行{i+1}: {line.strip()}")
        else:
            print("❌ Excel文件未生成")
            return False
            
    except Exception as e:
        print(f"❌ Excel导出失败: {e}")
        return False
    
    # 5. 测试清空数据
    print("5. 测试清空数据...")
    db.clear_current_session()
    
    data_after_clear = db.load_current_session()
    if data_after_clear is None:
        print("✓ 数据清空成功")
    else:
        print("❌ 数据清空失败")
        return False
    
    print("\n=== 所有测试通过！紧急修复成功！ ===")
    return True

if __name__ == '__main__':
    success = test_emergency_fix()
    if success:
        print("\n🎉 应用已完全修复，可以正常使用！")
    else:
        print("\n❌ 测试失败，需要进一步检查")