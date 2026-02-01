"""测试第3次数据"""
from app.services.text_extractor import TextExtractor

# 第3次数据：只有活动信息，没有来宾
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

print('=' * 60)
print('测试第3次数据（只有活动信息，没有来宾）')
print('=' * 60)

extractor = TextExtractor()
activity = extractor.extract_activity_info(text3)
guests = extractor.extract_guests_from_text(text3)

print(f'\n结果:')
print(f'  日期: {activity.date}')
print(f'  事项: {activity.event}')
print(f'  陪同领导: {activity.leader}')
print(f'  陪同部门: {activity.department}')
print(f'  来宾数量: {len(guests)}位')

print('\n' + '=' * 60)
print(f'结论: 第3次数据应该是0位来宾')
print('=' * 60)

# 检查数据库
print('\n检查数据库中的数据:')
from app.models import Database
db = Database()
data = db.load_current_session()
if data:
    print(f'  数据库中有数据！')
    print(f'  来宾数量: {len(data.get("guests", []))}位')
    print(f'  这就是为什么显示19位的原因！')
else:
    print(f'  数据库是空的')
