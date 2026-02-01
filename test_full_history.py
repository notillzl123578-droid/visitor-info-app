#!/usr/bin/env python3
"""测试完整历史记录功能"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Database
from app.services.excel_generator import ExcelGenerator

def test_full_history():
    """测试完整历史记录功能"""
    print("=== 测试完整历史记录功能 ===")
    
    # 清理旧数据库
    if os.path.exists('data/app.db'):
        os.remove('data/app.db')
        print("✓ 清理旧数据库")
    
    # 1. 初始化数据库
    db = Database()
    print("✓ 数据库初始化")
    
    # 2. 保存一些测试数据
    print("\n--- 保存测试数据 ---")
    activity1 = {
        'date': '6月10日',
        'event': '测试参观1',
        'leader': '张三',
        'department': '办公室',
        'route': '展厅A'
    }
    guests1 = [
        {'company': '公司A', 'name': '李四', 'position': '经理'},
        {'company': '公司A', 'name': '王五', 'position': '主管'}
    ]
    
    db.save_current_session(activity1, guests1)
    
    activity2 = {
        'date': '6月11日',
        'event': '测试参观2',
        'leader': '赵六',
        'department': '技术部',
        'route': '展厅B'
    }
    guests2 = [
        {'company': '公司B', 'name': '孙七', 'position': '总监'}
    ]
    
    db.save_current_session(activity2, guests2)
    
    # 3. 导出Excel并记录历史
    print("\n--- 导出Excel ---")
    data = db.load_current_session()
    excel_generator = ExcelGenerator()
    file_path = excel_generator.generate_csv(batches_data=data['batches'])
    
    # 计算总来宾数
    total_guests = sum(len(batch.get('guests', [])) for batch in data['batches'])
    filename = os.path.basename(file_path)
    
    # 添加到导出历史
    db.add_export_history(filename, file_path, total_guests, data['batches'])
    
    # 清空当前数据
    db.clear_current_session()
    
    print(f"✓ 导出完成: {filename}")
    
    # 4. 测试统计信息
    print("\n--- 测试统计信息 ---")
    stats = db.get_statistics()
    print(f"总导出次数: {stats['total_exports']}")
    print(f"总数据条数: {stats['total_rows']}")
    print(f"当前未导出: {stats['current_count']}")
    
    if stats['total_exports'] == 1 and stats['total_rows'] == 3 and stats['current_count'] == 0:
        print("✅ 统计信息正确")
    else:
        print("❌ 统计信息错误")
        return False
    
    # 5. 测试历史记录查询
    print("\n--- 测试历史记录查询 ---")
    history = db.get_export_history()
    
    if len(history) == 1:
        record = history[0]
        print(f"✓ 历史记录: {record['filename']}")
        print(f"  导出时间: {record['exported_at']}")
        print(f"  文件路径: {record['file_path']}")
        print(f"  数据条数: {record['row_count']}")
        
        if record['filename'] == filename and record['row_count'] == 3:
            print("✅ 历史记录正确")
        else:
            print("❌ 历史记录错误")
            return False
    else:
        print(f"❌ 历史记录数量错误，期望1条，实际{len(history)}条")
        return False
    
    # 6. 测试历史界面
    print("\n--- 测试历史界面 ---")
    try:
        from app.ui.history_screen import HistoryScreen
        
        history_screen = HistoryScreen()
        history_screen.refresh_history()
        print("✅ 历史界面刷新成功")
    except Exception as e:
        print(f"❌ 历史界面测试失败: {e}")
        return False
    
    # 7. 测试删除历史记录
    print("\n--- 测试删除历史记录 ---")
    record_id = history[0]['id']
    db.delete_history_record(record_id)
    
    history_after_delete = db.get_export_history()
    if len(history_after_delete) == 0:
        print("✅ 历史记录删除成功")
    else:
        print("❌ 历史记录删除失败")
        return False
    
    print("\n🎉 完整历史记录功能测试通过！")
    return True

if __name__ == '__main__':
    success = test_full_history()
    if success:
        print("\n🎉 历史记录功能完全恢复！")
    else:
        print("\n❌ 测试失败，需要进一步检查")