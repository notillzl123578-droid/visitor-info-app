"""使用真实数据测试"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.services.text_extractor import TextExtractor
from app.models.data_models import GuestInfo

# 真实测试数据
real_text = """
附录 B来宾信息表
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

备注：如有变动，微信通知。
"""

def test_real_data_extraction():
    """测试真实数据提取"""
    print("=" * 60)
    print("真实数据提取测试")
    print("=" * 60)
    
    extractor = TextExtractor()
    activity = extractor.extract_activity_info(real_text)
    
    print(f"\n【活动信息提取结果】")
    print(f"日期: {activity.date}")
    print(f"参观事项: {activity.event}")
    print(f"陪同领导: {activity.leader}")
    print(f"陪同部门: {activity.department}")
    print(f"参观路线: {activity.route[:100]}..." if len(activity.route) > 100 else f"参观路线: {activity.route}")
    
    # 验证提取结果
    print(f"\n【验证结果】")
    
    if activity.date == "6月10日":
        print("✅ 日期提取正确: 6月10日")
    else:
        print(f"❌ 日期提取错误: 期望'6月10日'，实际'{activity.date}'")
    
    if "大连高级经理学院海南省国有企业董事会参观" in activity.event:
        print("✅ 参观事项提取正确")
    else:
        print(f"⚠️ 参观事项: {activity.event}")
    
    if activity.department == "人力资源部":
        print("✅ 陪同部门提取正确: 人力资源部")
    else:
        print(f"⚠️ 陪同部门: {activity.department}")
    
    if "公司正门" in activity.route:
        print("✅ 参观路线提取正确")
    else:
        print(f"⚠️ 参观路线: {activity.route}")
    
    # 模拟表格提取（因为这是文本，实际需要Word文档）
    print(f"\n【来宾信息（从文本模拟）】")
    guests = [
        GuestInfo(company="海南省国资委", name="李伟", position="法治处处长"),
        GuestInfo(company="省属企业", name="陈良才", position="专职外部董事"),
        GuestInfo(company="省属企业", name="陈敏", position="专职外部董事"),
        GuestInfo(company="省属企业", name="姜洪涛", position="专职外部董事"),
        GuestInfo(company="省属企业", name="黎民英", position="专职外部董事"),
        GuestInfo(company="省属企业", name="林亚芒", position="专职外部董事"),
        GuestInfo(company="地质矿业集团有限公司", name="周岗耀", position="工会主席、职工董事"),
        GuestInfo(company="教学仪器设备招标中心有限公司", name="冯海雄", position="党支部书记、执行董事、总经理"),
        GuestInfo(company="海南农垦旅游集团有限公司", name="陈朴", position="党委副书记、总经理"),
        GuestInfo(company="海南农垦荣光农场有限公司", name="赵强", position="党委书记、董事长"),
        GuestInfo(company="海南国资研究院有限公司", name="刘静", position="副院长"),
        GuestInfo(company="海南省发展控股有限公司", name="王妍", position="董事会办公室主任"),
        GuestInfo(company="海南省物流集团有限公司", name="秦金艳", position="合规法务部总经理"),
        GuestInfo(company="海南省国有资本运营有限公司", name="杨臻", position="综合管理部（董事会办公室）副部长"),
        GuestInfo(company="海南绿华环保建材有限公司", name="李琼根", position="董事、副总经理"),
        GuestInfo(company="海南省信息产业投资集团有限公司", name="赵建凯", position="副总经理"),
        GuestInfo(company="海口市城市建设投资集团有限公司", name="吴叔晓", position="战略投资部经理"),
    ]
    
    print(f"共{len(guests)}位来宾:")
    for i, guest in enumerate(guests[:5], 1):
        print(f"  {i}. {guest.name} - {guest.position} ({guest.company})")
    print(f"  ... 还有{len(guests)-5}位来宾")
    
    # 生成CSV测试
    print(f"\n【生成CSV文件】")
    import csv
    output_path = 'test_real_output.csv'
    
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        
        # 写入表头
        writer.writerow([
            '日期', '参观事项', '陪同领导', '陪同部门', '参观路线',
            '来宾单位', '姓名', '职务', '人数'
        ])
        
        # 写入数据
        for i, guest in enumerate(guests):
            count = str(len(guests)) if i == 0 else ''
            writer.writerow([
                activity.date,
                activity.event,
                activity.leader,
                activity.department,
                activity.route.replace('\n', ' '),
                guest.company,
                guest.name,
                guest.position,
                count
            ])
    
    print(f"✅ CSV文件生成成功: {output_path}")
    
    # 显示CSV内容预览
    with open(output_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()[:6]
        print(f"\n【CSV文件预览（前5行）】")
        for line in lines:
            print(f"  {line.strip()}")
    
    print(f"\n" + "=" * 60)
    print("✅ 真实数据测试完成！")
    print("=" * 60)

if __name__ == '__main__':
    test_real_data_extraction()
