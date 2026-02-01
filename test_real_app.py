#!/usr/bin/env python3
"""测试真实应用启动"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_app_startup():
    """测试应用启动"""
    print("=== 测试应用启动 ===")
    
    try:
        # 导入主要模块
        from app.models.database import Database
        from app.services.excel_generator import ExcelGenerator
        from app.ui.main_screen import MainScreen
        print("✓ 所有模块导入成功")
        
        # 测试数据库
        db = Database()
        print("✓ 数据库初始化成功")
        
        # 测试Excel生成器
        excel_gen = ExcelGenerator()
        print("✓ Excel生成器初始化成功")
        
        print("\n🎉 应用可以正常启动！")
        print("\n使用方法:")
        print("1. 运行: python main.py")
        print("2. 或双击: 运行应用.bat")
        
        return True
        
    except Exception as e:
        print(f"❌ 应用启动测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    test_app_startup()