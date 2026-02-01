#!/usr/bin/env python3
"""测试历史界面修复"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_history_screen():
    """测试历史界面"""
    print("=== 测试历史界面修复 ===")
    
    try:
        # 导入历史界面
        from app.ui.history_screen import HistoryScreen
        from app.models.database import Database
        
        print("✓ 历史界面模块导入成功")
        
        # 创建数据库实例
        db = Database()
        print("✓ 数据库初始化成功")
        
        # 创建历史界面实例
        history_screen = HistoryScreen()
        print("✓ 历史界面创建成功")
        
        # 测试刷新方法（这是之前崩溃的地方）
        history_screen.refresh_history()
        print("✓ 历史界面刷新成功")
        
        print("\n🎉 历史界面修复成功！不会再崩溃了")
        return True
        
    except Exception as e:
        print(f"❌ 历史界面测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    test_history_screen()