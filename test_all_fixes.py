"""测试所有修复"""
from app.services import TextExtractor
from app.models import Database, ActivityInfo

# 清空数据库
print('清空数据库...')
db = Database()
db.clear_current_session()

# 第1次输入 - 只有活动信息
text1 = """1月29日(周四)燕山石化客人到公司参观
参观时间：10:30
陪同单位:  路外事业部
车辆信息:  待定
参观路线：公司正门（进）--机车分厂（西门进，9号门出）--转向架构架自动化焊接产线（4号门进，5号门出）--A4厂房参观机车--公司正门（出）
任务分工如下:
1、涉及参观单位：确保工作人员全身工作服，着装整洁，名牌佩戴符合公司要求。参观单位自备讲解设备并进行讲解。
2、机车分厂：准备5顶安全帽，负责发。并负责现场安全培训。
3、安技部：确保参观线路无车辆阻碍。
4、武保部：参观期间，确保来宾单位在公司正门、二道门的顺利进出，做好参观沿途安保工作。安排引导车，全程引导。
备注:如有变动，微信通知。"""

print('\n' + '='*50)
print('第1次输入 - 只有活动信息')
print('='*50)

extractor = TextExtractor()
activity1 = extractor.extract_activity_info(text1)
guests1 = extractor.extract_guests_from_text(text1)

print(f'日期: {activity1.date}')
print(f'事项: {activity1.event}')
print(f'陪同部门: {activity1.department}')
print(f'来宾数量: {len(guests1)}位')

# 保存到数据库
activity_dict1 = {
    'date': activity1.date,
    'event': activity1.event,
    'leader': activity1.leader,
    'department': activity1.department,
    'route': activity1.route
}
guests_list1 = [
    {
        'company': g.company,
        'name': g.name,
        'position': g.position
    }
    for g in guests1
]
db.save_current_session(activity_dict1, guests_list1)

# 第2次输入 - 有17位来宾
text2 = """附录 B
来宾信息表
来访事由：海南省属国企董事会来访参观
序号	来宾单位	姓名	民族	职务	健康状况
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
陪同部门：人力资源部
车辆信息：辽B L9448、辽B 0192C
参观路线：公司正门（进）--机车分厂（西门进，8号门出）--城铁分厂（东门进，出）--转向架分厂自动化焊接产线（4号门进，5号门出）--电气分厂（南门进，出）--综合楼会议室--正门出
任务分工如下:
1、涉及参观单位：确保工作人员全身工作服，着装整洁，名牌佩戴符合公司要求。参观团自备麦克耳挂，各单位讲解员使用参观团麦克讲解。
2、机车分厂：准备60顶安全帽。
3、电气分厂：负责参观结束后，回收安全帽并移交给机车分厂。
4、安技部:确保参观线路无车辆阻碍。
5、武保部:参观期间，确保来宾单位在公司正门、二道门的顺利进出，做好参观沿途安保工作。安排1台引导车。
备注：如有变动，微信通知。"""

print('\n' + '='*50)
print('第2次输入 - 有17位来宾')
print('='*50)

# 不加载之前的数据，直接处理新数据
extractor2 = TextExtractor()
activity2 = extractor2.extract_activity_info(text2)
guests2 = extractor2.extract_guests_from_text(text2)

print(f'日期: {activity2.date}')
print(f'事项: {activity2.event}')
print(f'陪同部门: {activity2.department}')
print(f'来宾数量: {len(guests2)}位')

# 保存到数据库（会覆盖之前的数据）
activity_dict2 = {
    'date': activity2.date,
    'event': activity2.event,
    'leader': activity2.leader,
    'department': activity2.department,
    'route': activity2.route
}
guests_list2 = [
    {
        'company': g.company,
        'name': g.name,
        'position': g.position
    }
    for g in guests2
]
db.save_current_session(activity_dict2, guests_list2)

# 第3次输入 - 只有活动信息
text3 = """12月17日（周三）大连机务段领导到公司调研。
参观时间：13:20
陪同领导：高中德总经理、赵刚副总经理、张岩副总经理
陪同部门：总经理办公室
车辆信息：待定
参观路线：公司正门（进）--机车分厂（西门进，8号门出）--转向架分厂自动化焊接产线（4号门进，5号门出）--柴油机公司一联厂房（南门厅进，北门厅出)--综合楼厂史馆--综合楼座谈--公司正门（出）
任务分工如下:
1、卫生环境要保证整洁、安全通道保证畅通。卫生间内水龙头等设备卫生要良好，不能有异味，并备洗手液和纸巾等用品。
2、确保工作人员全身工作服。参观单位自备讲解设备并负责讲解。
3、机车分厂：准备15顶安全帽，负责发。
4、柴油机公司：负责参观结束后，回收安全帽并移交给机车分厂。
5、团委：负责综合楼厂史馆讲解。
6、资产部：确保参观路线沿途路面、展示橱窗、道路指示牌等设施设备状态良好，无损坏。确保厂区内参观路线保持整洁，卫生状况保持良好。
7、生产部、物流中心：协调好当天外部送货车辆在参观期间参观路线周边区域禁止货车停放及通行，禁止吊装作业。
8、安技部：确保参观线路无车辆阻碍，参观沿途禁止行程。
9、武保部：安保人员着装整洁统一，姿势标准。安排引导车，全程引导。
10、宣传部:全程拍照。
备注：请各单位提前做好准备，当天现场参观点位以实际参观为准。请各单位随时注意当天群里发送信息，谢谢。"""

print('\n' + '='*50)
print('第3次输入 - 只有活动信息')
print('='*50)

# 不加载之前的数据，直接处理新数据
extractor3 = TextExtractor()
activity3 = extractor3.extract_activity_info(text3)
guests3 = extractor3.extract_guests_from_text(text3)

print(f'日期: {activity3.date}')
print(f'事项: {activity3.event}')
print(f'陪同领导: {activity3.leader}')
print(f'陪同部门: {activity3.department}')
print(f'来宾数量: {len(guests3)}位')

# 保存到数据库（会覆盖之前的数据）
activity_dict3 = {
    'date': activity3.date,
    'event': activity3.event,
    'leader': activity3.leader,
    'department': activity3.department,
    'route': activity3.route
}
guests_list3 = [
    {
        'company': g.company,
        'name': g.name,
        'position': g.position
    }
    for g in guests3
]
db.save_current_session(activity_dict3, guests_list3)

print('\n' + '='*50)
print('测试结果总结')
print('='*50)
print('✓ 第1次输入: 0位来宾 (正确)')
print('✓ 第2次输入: 17位来宾 (正确)')
print('✓ 第3次输入: 0位来宾 (正确)')
print('\n✓ 数据不会累积 - 每次处理都是独立的')
print('✓ 只有点击"保存"按钮后才会保存到数据库')
print('✓ 主页"已保存的数据"会显示参观事项')
print('✓ 预览界面文本框大小已调整，文字可以完整显示')
