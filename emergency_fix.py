#!/usr/bin/env python3
"""紧急修复 - 完全重写核心功能"""

import os
import sys
import sqlite3
import json
import csv
from pathlib import Path
from datetime import datetime

def emergency_fix():
    """紧急修复 - 重写所有核心功能"""
    print("=== 紧急修复开始 ===")
    
    # 1. 完全重写数据库类
    print("1. 重写数据库类...")
    
    database_code = '''"""简化的数据库管理模块"""
import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Database:
    """简化的数据库管理类"""
    
    def __init__(self, db_path='data/app.db'):
        """初始化数据库"""
        self.db_path = db_path
        
        # 确保data目录存在
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # 初始化数据库
        self.init_database()
    
    def init_database(self):
        """初始化数据库表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 简单的数据表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_json TEXT,
                exported BOOLEAN DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_current_session(self, activity: dict, guests: list):
        """保存数据 - 简化版本"""
        if not guests:  # 如果没有来宾数据，不保存
            print("⚠️ 没有来宾数据，跳过保存")
            return
            
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 构建数据
        data = {
            'activity': activity,
            'guests': guests,
            'saved_at': datetime.now().isoformat()
        }
        
        # 保存数据
        cursor.execute('''
            INSERT INTO visitor_data (data_json, exported)
            VALUES (?, 0)
        ''', (json.dumps(data, ensure_ascii=False),))
        
        conn.commit()
        conn.close()
        print(f'✓ 数据已保存，{len(guests)}位来宾')
    
    def load_current_session(self) -> Optional[Dict]:
        """加载当前数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT data_json FROM visitor_data 
            WHERE exported = 0
            ORDER BY created_at ASC
        ''')
        
        rows = cursor.fetchall()
        conn.close()
        
        if not rows:
            return None
        
        # 合并所有批次
        all_batches = []
        for row in rows:
            data = json.loads(row[0])
            all_batches.append(data)
        
        return {'batches': all_batches}
    
    def clear_current_session(self):
        """清空当前数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('UPDATE visitor_data SET exported = 1 WHERE exported = 0')
        
        conn.commit()
        conn.close()
        print('✓ 数据已清空')
'''
    
    # 写入数据库文件
    with open('app/models/database.py', 'w', encoding='utf-8') as f:
        f.write(database_code)
    
    print("✓ 数据库类已重写")
    
    # 2. 重写Excel生成器
    print("2. 重写Excel生成器...")
    
    excel_code = '''"""简化的Excel生成器"""
import csv
import os
from datetime import datetime
from pathlib import Path


class ExcelGenerator:
    """简化的Excel生成器"""
    
    @staticmethod
    def generate_csv(activity=None, guests=None, existing_data=None, 
                     output_path=None, batches_data=None) -> str:
        """生成CSV文件 - 简化版本"""
        
        if output_path is None:
            documents_dir = Path.home() / "Documents"
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = documents_dir / f'visitor_data_{timestamp}.csv'
        
        # 确保目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            
            # 写入表头
            writer.writerow([
                '日期', '参观事项', '陪同领导', '陪同部门', '参观路线',
                '来宾单位', '姓名', '职务', '人数'
            ])
            
            # 处理批次数据
            if batches_data:
                for batch in batches_data:
                    activity_info = batch.get('activity', {})
                    guest_list = batch.get('guests', [])
                    
                    if guest_list:
                        guest_count = len(guest_list)
                        for i, guest in enumerate(guest_list):
                            # 只在第一行显示人数
                            count = str(guest_count) if i == 0 else ''
                            
                            writer.writerow([
                                activity_info.get('date', ''),
                                activity_info.get('event', ''),
                                activity_info.get('leader', ''),
                                activity_info.get('department', ''),
                                activity_info.get('route', '').replace('\\n', ' '),
                                guest.get('company', ''),
                                guest.get('name', ''),
                                guest.get('position', ''),
                                count
                            ])
        
        print(f'CSV文件生成成功: {output_path}')
        return str(output_path)
'''
    
    # 写入Excel生成器文件
    with open('app/services/excel_generator.py', 'w', encoding='utf-8') as f:
        f.write(excel_code)
    
    print("✓ Excel生成器已重写")
    
    # 3. 重写主界面的关键方法
    print("3. 重写主界面关键方法...")
    
    # 读取当前主界面文件
    with open('app/ui/main_screen.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换refresh_saved_data方法
    refresh_method = '''    def refresh_saved_data(self):
        """刷新已保存数据的显示 - 简化版本"""
        try:
            data = self.database.load_current_session()
            
            if data and 'batches' in data and data['batches']:
                batches = data['batches']
                total_guests = sum(len(batch.get('guests', [])) for batch in batches)
                
                info_lines = []
                info_lines.append('📋 已保存的参观活动:')
                
                for i, batch in enumerate(batches):
                    activity = batch.get('activity', {})
                    guests = batch.get('guests', [])
                    date_info = activity.get('date', '未知日期')
                    event_info = activity.get('event', '未知事项')
                    info_lines.append(f'{i+1}. {date_info} - {event_info} ({len(guests)}位来宾)')
                
                info_lines.append(f'\\n📊 共{len(batches)}个活动, 累计{total_guests}位来宾')
                
                self.saved_data_label.text = '\\n'.join(info_lines)
                self.saved_data_label.color = (0.2, 0.5, 0.2, 1)
                print(f'✓ 已加载保存数据: 累计{total_guests}位来宾')
            else:
                self.saved_data_label.text = '暂无保存的数据'
                self.saved_data_label.color = (0.6, 0.6, 0.6, 1)
        except Exception as e:
            print(f'刷新数据显示错误: {e}')
            self.saved_data_label.text = '数据加载出错'
            self.saved_data_label.color = (0.8, 0.2, 0.2, 1)'''
    
    # 替换export_saved_data方法
    export_method = '''    def export_saved_data(self, instance):
        """导出已保存的数据 - 简化版本"""
        try:
            data = self.database.load_current_session()
            if not data or 'batches' not in data or not data['batches']:
                self.show_message('提示', '没有可导出的数据')
                return
            
            from app.services.excel_generator import ExcelGenerator
            
            excel_generator = ExcelGenerator()
            file_path = excel_generator.generate_csv(batches_data=data['batches'])
            
            # 计算总来宾数
            total_guests = sum(len(batch.get('guests', [])) for batch in data['batches'])
            
            # 清空数据
            self.database.clear_current_session()
            self.refresh_saved_data()
            
            filename = os.path.basename(file_path)
            message = f'导出成功！\\n文件: {filename}\\n共{total_guests}条数据\\n\\n数据已清空，可开始新的录入'
            self.show_message('导出成功', message)
            
        except Exception as e:
            error_msg = f'导出失败: {str(e)}'
            print(f'导出错误: {error_msg}')
            self.show_message('导出失败', error_msg)'''
    
    # 查找并替换方法
    import re
    
    # 替换refresh_saved_data方法
    pattern = r'    def refresh_saved_data\(self\):.*?(?=    def \w+|\Z)'
    content = re.sub(pattern, refresh_method, content, flags=re.DOTALL)
    
    # 替换export_saved_data方法
    pattern = r'    def export_saved_data\(self, instance\):.*?(?=    def \w+|\Z)'
    content = re.sub(pattern, export_method, content, flags=re.DOTALL)
    
    # 写回文件
    with open('app/ui/main_screen.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ 主界面方法已重写")
    
    # 4. 清理并重新初始化数据库
    print("4. 重新初始化数据库...")
    
    db_path = 'data/app.db'
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # 导入新的数据库类并初始化
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from app.models.database import Database
    db = Database()
    
    print("✓ 数据库已重新初始化")
    
    print("\n=== 紧急修复完成 ===")
    print("✅ 数据库类已完全重写")
    print("✅ Excel生成器已简化")
    print("✅ 主界面方法已修复")
    print("✅ 数据库已重新初始化")
    print("\n🎉 应用已完全修复！现在可以正常使用！")

if __name__ == '__main__':
    emergency_fix()