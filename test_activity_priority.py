#!/usr/bin/env python3
"""测试活动信息优先级修复"""

import sys
import os
sys.path.append('.')

def test_activity_priority():
    """测试活动信息优先级"""
    print("=== 测试活动信息优先级修复 ===")
    
    from app.models.database import Database
    
    db = Database()
    
    # 清空测试数据
    db.clear_current_session()
    print("已清空旧数据")
    
    # 第一次保存：6月10日海南省国企董事会参观
    activity1 = {
        'date': '6月10日',
        'event': '海南省国有企业董事会参观',
        'leader': '',
        'department': '人力资源部',
        'route': '公司正门（进）--机车分厂（西门进，8号门出）--城铁分厂（东门进，出）--转向架分厂自动化焊接产线（4号门进，5号门出）--电气分厂（南门进，出）--综合楼会议室--正门出'
    }
    guests1 = [
        {'company': '海南省国资委', 'name': '李伟', 'position': '法治处处长'},
        {'company': '省属企业', 'name': '陈良才', 'position': '专职外部董事'},
        {'company': '省属企业', 'name': '陈敏', 'position': '专职外部董事'},
        # 模拟17位来宾中的前3位
    ]
    
    db.save_current_session(activity1, guests1)
    print(f"第一次保存完成: {activity1['date']} - {activity1['event']}")
    
    # 第二次保存：1月29日燕山石化参观
    activity2 = {
        'date': '1月29日',
        'event': '燕山石化客人到公司参观',
        'leader': '',
        'department': '路外事业部',
        'route': '公司正门（进）--机车分厂（西门进，9号门出）--转向架构架自动化焊接产线（4号门进，5号门出）--A4厂房参观机车--公司正门（出）'
    }
    guests2 = [
        {'company': '中国石化集团北京燕山石油化工有限公司', 'name': '毕舒伟', 'position': '副主任'},
        {'company': '中国石化集团北京燕山石油化工有限公司', 'name': '任连宝', 'position': '机车主管'},
    ]
    
    db.save_current_session(activity2, guests2)
    print(f"第二次保存完成: {activity2['date']} - {activity2['event']}")
    
    # 检查累积结果
    data = db.load_current_session()
    print(f"\n累积后的结果:")
    print(f"活动信息: {data['activity']}")
    print(f"来宾数量: {len(data['guests'])}位")
    
    # 验证结果
    final_activity = data['activity']
    final_guests = data['guests']
    
    # 验证活动信息应该是第一次的
    expected_date = '6月10日'
    expected_event = '海南省国有企业董事会参观'
    
    if final_activity['date'] == expected_date:
        print(f"✅ 日期正确: {final_activity['date']}")
    else:
        print(f"❌ 日期错误: 期望'{expected_date}', 实际'{final_activity['date']}'")
    
    if final_activity['event'] == expected_event:
        print(f"✅ 参观事项正确: {final_activity['event']}")
    else:
        print(f"❌ 参观事项错误: 期望'{expected_event}', 实际'{final_activity['event']}'")
    
    # 验证来宾累积
    if len(final_guests) == 5:  # 3 + 2
        print(f"✅ 来宾累积正确: {len(final_guests)}位")
    else:
        print(f"❌ 来宾累积错误: 期望5位, 实际{len(final_guests)}位")
    
    # 显示所有来宾
    print(f"\n所有来宾:")
    for i, guest in enumerate(final_guests):
        print(f"  {i+1}. {guest['company']} - {guest['name']} - {guest['position']}")
    
    print(f"\n🎉 修复验证完成！")
    return True

if __name__ == '__main__':
    test_activity_priority()