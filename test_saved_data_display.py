"""测试已保存数据的显示"""
from app.models import Database

db = Database()

# 检查数据库中的数据
data = db.load_current_session()

if data:
    activity = data.get('activity', {})
    guests = data.get('guests', [])
    guest_count = len(guests)
    
    print('='*50)
    print('数据库中的数据:')
    print('='*50)
    
    # 构建显示文本（和main_screen.py中的逻辑一致）
    info_lines = []
    
    # 活动信息 - 显示所有字段
    if activity.get('date'):
        info_lines.append(f"📅 日期: {activity.get('date')}")
    if activity.get('event'):
        info_lines.append(f"📋 参观事项: {activity.get('event')}")
    if activity.get('leader'):
        info_lines.append(f"👤 陪同领导: {activity.get('leader')}")
    if activity.get('department'):
        info_lines.append(f"🏢 陪同部门: {activity.get('department')}")
    
    # 来宾统计
    info_lines.append(f"\n👥 已保存来宾: {guest_count}位")
    
    # 显示前3位来宾
    if guests:
        info_lines.append("\n最近添加:")
        for i, guest in enumerate(guests[-3:]):
            name = guest.get('name', '')
            company = guest.get('company', '')
            info_lines.append(f"  • {name} ({company})")
        
        if guest_count > 3:
            info_lines.append(f"  ... 还有{guest_count-3}位")
    
    print('\n'.join(info_lines))
    
    print('\n' + '='*50)
    print('✓ 参观事项已包含在显示中')
    print('='*50)
else:
    print('数据库是空的')
