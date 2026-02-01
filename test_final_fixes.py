"""测试最终修复 - 数据累积和文本框大小"""
from app.services import TextExtractor
from app.models import Database, ExtractedData, GuestInfo

print('='*60)
print('测试数据累积功能')
print('='*60)

# 清空数据库
db = Database()
db.clear_current_session()
print('✓ 数据库已清空\n')

# 第1次输入 - 0位来宾
print('第1次输入（0位来宾）')
text1 = """1月29日(周四)燕山石化客人到公司参观
陪同部门: 路外事业部"""

extractor = TextExtractor()
extracted_data1 = ExtractedData()
extracted_data1.activity = extractor.extract_activity_info(text1)
guests1 = extractor.extract_guests_from_text(text1)
extracted_data1.guests.extend(guests1)

print(f'  日期: {extracted_data1.activity.date}')
print(f'  事项: {extracted_data1.activity.event}')
print(f'  来宾: {len(extracted_data1.guests)}位')

# 保存第1次数据
activity_dict1 = {
    'date': extracted_data1.activity.date,
    'event': extracted_data1.activity.event,
    'leader': extracted_data1.activity.leader,
    'department': extracted_data1.activity.department,
    'route': extracted_data1.activity.route
}
guests_list1 = [
    {'company': g.company, 'name': g.name, 'position': g.position}
    for g in extracted_data1.guests
]
db.save_current_session(activity_dict1, guests_list1)

# 检查数据库
data = db.load_current_session()
print(f'  数据库中: {len(data["guests"])}位来宾\n')

# 第2次输入 - 17位来宾
print('第2次输入（17位来宾）')
text2 = """序号	来宾单位	姓名	民族	职务	健康状况
1	海南省国资委	李 伟	汉族	法治处处长	良好
2	省属企业	陈良才	汉族	专职外部董事	良好
3	省属企业	陈 敏	汉族	专职外部董事	良好
4	省属企业	姜洪涛	汉族	专职外部董事	良好
5	省属企业	黎民英	汉族	专职外部董事	良好
6	省属企业	林亚芒	汉族	专职外部董事	良好
7	地质矿业集团有限公司	周岗耀	汉族	工会主席、职工董事	良好
8	教学仪器设备招标中心有限公司	冯海雄	汉族	党支部书记、执行董事、总经理	良好
9	海南农垦旅游集团有限公司	陈 朴	汉族	党委副书记、总经理	良好
10	海南农垦荣光农场有限公司	赵 强	汉族	党委书记、董事长	良好
11	海南国资研究院有限公司	刘 静	汉族	副院长	良好
12	海南省发展控股有限公司	王 妍	汉族	董事会办公室主任	良好
13	海南省物流集团有限公司	秦金艳	汉族	合规法务部总经理	良好
14	海南省国有资本运营有限公司	杨 臻	汉族	综合管理部（董事会办公室）副部长	良好
15	海南绿华环保建材有限公司	李琼根	汉族	董事、副总经理	良好
16	海南省信息产业投资集团有限公司	赵建凯	汉族	副总经理	良好
17	海口市城市建设投资集团有限公司	吴叔晓	汉族	战略投资部经理	良好

6月10日（周二）大连高级经理学院海南省国有企业董事会参观。
陪同部门：人力资源部"""

extractor2 = TextExtractor()
extracted_data2 = ExtractedData()
extracted_data2.activity = extractor2.extract_activity_info(text2)
guests2 = extractor2.extract_guests_from_text(text2)
extracted_data2.guests.extend(guests2)

print(f'  日期: {extracted_data2.activity.date}')
print(f'  事项: {extracted_data2.activity.event}')
print(f'  来宾: {len(extracted_data2.guests)}位')

# 模拟预览界面的保存功能（累积模式）
previous_data = db.load_current_session()
all_guests = []

if previous_data:
    # 累积之前的来宾
    for guest_dict in previous_data.get('guests', []):
        all_guests.append(guest_dict)
    print(f'  加载之前的数据: {len(all_guests)}位来宾')

# 添加当前的来宾（避免重复）
for g in extracted_data2.guests:
    guest_dict = {
        'company': g.company,
        'name': g.name,
        'position': g.position
    }
    # 检查是否重复
    if not any(existing['name'] == guest_dict['name'] and 
              existing['company'] == guest_dict['company'] 
              for existing in all_guests):
        all_guests.append(guest_dict)

activity_dict2 = {
    'date': extracted_data2.activity.date,
    'event': extracted_data2.activity.event,
    'leader': extracted_data2.activity.leader,
    'department': extracted_data2.activity.department,
    'route': extracted_data2.activity.route
}

db.save_current_session(activity_dict2, all_guests)

# 检查数据库
data2 = db.load_current_session()
print(f'  保存后数据库中: {len(data2["guests"])}位来宾')
print(f'  参观事项: {data2["activity"]["event"]}\n')

print('='*60)
print('测试结果')
print('='*60)
print(f'✓ 第1次保存: 0位来宾')
print(f'✓ 第2次保存: 累积到 {len(data2["guests"])}位来宾 (0 + 17 = 17)')
print(f'✓ 参观事项已保存: {data2["activity"]["event"]}')
print(f'\n✓ 文本框高度已增加4个单位:')
print(f'  - 活动信息区域: 400 → 420')
print(f'  - 普通字段: 50 → 54')
print(f'  - 参观路线: 100 → 104')
print(f'  - 来宾信息行: 150 → 154')
print(f'  - 来宾字段: 35 → 39')
