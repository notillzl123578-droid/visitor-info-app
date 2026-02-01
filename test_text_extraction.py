"""测试文本提取功能"""
from app.services.text_extractor import TextExtractor

# 第1次数据：只有活动信息
text1 = """1月29日(周四)燕山石化客人到公司参观
参观时间：10:30
陪同单位: 路外事业部
车辆信息: 待定
参观路线：公司正门（进）--机车分厂（西门进，9号门出）--转向架构架自动化焊接产线（4号门进，5号门出）--A4厂房参观机车--公司正门（出）"""

# 第2次数据：有17位来宾
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
参观时间：8:40
陪同部门：人力资源部"""

print('=' * 60)
print('测试第1次数据（只有活动信息）')
print('=' * 60)

extractor = TextExtractor()
activity1 = extractor.extract_activity_info(text1)
guests1 = extractor.extract_guests_from_text(text1)

print(f'\n结果:')
print(f'  日期: {activity1.date}')
print(f'  事项: {activity1.event}')
print(f'  陪同部门: {activity1.department}')
print(f'  参观路线: {activity1.route[:50]}...')
print(f'  来宾数量: {len(guests1)}位')

print('\n' + '=' * 60)
print('测试第2次数据（17位来宾）')
print('=' * 60)

activity2 = extractor.extract_activity_info(text2, activity1)
guests2 = extractor.extract_guests_from_text(text2)

print(f'\n结果:')
print(f'  日期: {activity2.date}')
print(f'  事项: {activity2.event}')
print(f'  来宾数量: {len(guests2)}位')

if guests2:
    print(f'\n前3位来宾:')
    for i, g in enumerate(guests2[:3], 1):
        print(f'  {i}. {g.company} - {g.name} - {g.position}')
    if len(guests2) > 3:
        print(f'  ... 还有{len(guests2)-3}位')

print('\n' + '=' * 60)
print(f'总结: 第1次{len(guests1)}位来宾，第2次{len(guests2)}位来宾')
print('=' * 60)
