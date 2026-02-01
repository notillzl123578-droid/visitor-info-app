#!/usr/bin/env python3
"""测试重复数据修复"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Database

def test_duplicate_fix():
    """测试重复数据修复"""
    print("=== 测试重复数据修复 ===")
    
    # 使用测试数据库
    db = Database('data/test_duplicate_fix.db')
    
    # 测试数据
    activity = {
        'date': '6月10日',
        'event': '测试参观',
        'leader': '张三',
        'department': '办公室',
        'route': '展厅A'
    }
    guests = [
        {'company': '测试公司', 'name': '李四', 'position': '经理'}
    ]
    
    print("1. 第一次保存数据...")
    db.save_current_session(activity, guests)
    
    print("2. 第二次保存相同数据（应该被跳过）...")
    db.save_current_session(activity, guests)
    
    print("3. 第三次保存相同数据（应该被跳过）...")
    db.save_current_session(activity, guests)
    
    print("4. 检查数据库中的数据...")
    data = db.load_current_session()
    
    if data and 'batches' in data:
        batches = data['batches']
        print(f"✓ 数据库中共有{len(batches)}个批次")
        
        if len(batches) == 1:
            print("✅ 重复数据修复成功！只保存了一份数据")
        else:
            print(f"❌ 重复数据修复失败！保存了{len(batches)}份数据")
            return False
    else:
        print("❌ 数据加载失败")
        return False
    
    print("5. 保存不同的数据（应该成功）...")
    activity2 = {
        'date': '6月11日',
        'event': '另一个参观',
        'leader': '王五',
        'department': '技术部',
        'route': '展厅B'
    }
    guests2 = [
        {'company': '另一个公司', 'name': '赵六', 'position': '总监'}
    ]
    
    db.save_current_session(activity2, guests2)
    
    print("6. 再次检查数据库...")
    data = db.load_current_session()
    
    if data and 'batches' in data:
        batches = data['batches']
        print(f"✓ 数据库中共有{len(batches)}个批次")
        
        if len(batches) == 2:
            print("✅ 不同数据保存成功！")
            for i, batch in enumerate(batches):
                activity_info = batch.get('activity', {})
                guests_info = batch.get('guests', [])
                print(f"  批次{i+1}: {activity_info.get('date')} - {activity_info.get('event')} ({len(guests_info)}位来宾)")
        else:
            print(f"❌ 数据保存异常！应该有2个批次，实际有{len(batches)}个")
            return False
    
    # 清理测试数据库
    if os.path.exists('data/test_duplicate_fix.db'):
        os.remove('data/test_duplicate_fix.db')
    
    print("\n✅ 重复数据修复测试通过！")
    return True

if __name__ == '__main__':
    test_duplicate_fix()