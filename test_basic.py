"""基础测试 - 不需要安装依赖"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(__file__))

from app.services.text_extractor import TextExtractor
from app.models.data_models import ExtractedData, GuestInfo

# 测试文本
test_text = """
12月9日（周二）国资委领导到公司调研

调研时间：2024年12月9日 14:00-16:00

陪同领导：张三、李四

陪同部门：办公室、人力资源部

调研路线：公司大厅 → 展厅 → 生产车间 → 会议室
"""

def test_text_extraction():
    """测试文本提取"""
    print("=" * 50)
    print("测试文本提取功能")
    print("=" * 50)
    
    extractor = TextExtractor()
    activity = extractor.extract_activity_info(test_text)
    
    print(f"\n提取结果:")
    print(f"日期: {activity.date}")
    print(f"参观事项: {activity.event}")
    print(f"陪同领导: {activity.leader}")
    print(f"陪同部门: {activity.department}")
    print(f"参观路线: {activity.route}")
    
    # 验证结果
    success = True
    
    if activity.date != "12月9日":
        print(f"❌ 日期提取错误: 期望'12月9日'，实际'{activity.date}'")
        success = False
    else:
        print("✅ 日期提取正确")
    
    if "国资委领导到公司调研" not in activity.event:
        print(f"❌ 参观事项提取错误: {activity.event}")
        success = False
    else:
        print("✅ 参观事项提取正确")
    
    if "张三" not in activity.leader:
        print(f"❌ 陪同领导提取错误: {activity.leader}")
        success = False
    else:
        print("✅ 陪同领导提取正确")
    
    if "办公室" not in activity.department:
        print(f"❌ 陪同部门提取错误: {activity.department}")
        success = False
    else:
        print("✅ 陪同部门提取正确")
    
    if "公司大厅" not in activity.route:
        print(f"❌ 参观路线提取错误: {activity.route}")
        success = False
    else:
        print("✅ 参观路线提取正确")
    
    return success

def test_data_models():
    """测试数据模型"""
    print("\n" + "=" * 50)
    print("测试数据模型")
    print("=" * 50)
    
    # 创建测试数据
    data = ExtractedData()
    data.activity.date = "12月9日"
    data.activity.event = "国资委领导到公司调研"
    
    data.guests = [
        GuestInfo(company="海南省国资委", name="李伟", position="法治处处长"),
        GuestInfo(company="省属企业", name="陈良才", position="专职外部董事"),
        GuestInfo(company="省属企业", name="陈敏", position="专职外部董事")
    ]
    
    print(f"\n活动信息:")
    print(f"  日期: {data.activity.date}")
    print(f"  事项: {data.activity.event}")
    
    print(f"\n来宾信息 (共{data.total_count}位):")
    for i, guest in enumerate(data.guests, 1):
        print(f"  {i}. {guest.name} - {guest.position} ({guest.company})")
    
    assert data.total_count == 3, "总人数计算错误"
    print("\n✅ 数据模型测试通过")
    
    return True

def test_csv_generation():
    """测试CSV生成（不需要openpyxl）"""
    print("\n" + "=" * 50)
    print("测试CSV生成")
    print("=" * 50)
    
    import csv
    from datetime import datetime
    
    # 创建测试数据
    activity = {
        'date': '12月9日',
        'event': '国资委领导到公司调研',
        'leader': '张三、李四',
        'department': '办公室、人力资源部',
        'route': '公司大厅 → 展厅 → 生产车间'
    }
    
    guests = [
        {'company': '海南省国资委', 'name': '李伟', 'position': '法治处处长'},
        {'company': '省属企业', 'name': '陈良才', 'position': '专职外部董事'},
        {'company': '省属企业', 'name': '陈敏', 'position': '专职外部董事'}
    ]
    
    # 生成CSV
    output_path = 'test_output.csv'
    total_count = len(guests)
    
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        
        # 写入表头
        writer.writerow([
            '日期', '参观事项', '陪同领导', '陪同部门', '参观路线',
            '来宾单位', '姓名', '职务', '人数'
        ])
        
        # 写入数据
        for i, guest in enumerate(guests):
            count = str(total_count) if i == 0 else ''
            writer.writerow([
                activity['date'],
                activity['event'],
                activity['leader'],
                activity['department'],
                activity['route'],
                guest['company'],
                guest['name'],
                guest['position'],
                count
            ])
    
    print(f"\n✅ CSV文件生成成功: {output_path}")
    
    # 验证文件内容
    with open(output_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        print(f"\n文件内容预览:")
        lines = content.split('\n')[:5]
        for line in lines:
            print(f"  {line}")
        
        assert "12月9日" in content, "日期未写入"
        assert "李伟" in content, "来宾姓名未写入"
        assert "法治处处长" in content, "职务未写入"
        assert "3" in content, "总人数未写入"
    
    print("\n✅ CSV生成测试通过")
    return True

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("来宾信息提取工具 - 基础功能测试")
    print("=" * 60)
    
    all_passed = True
    
    try:
        if not test_text_extraction():
            all_passed = False
    except Exception as e:
        print(f"\n❌ 文本提取测试失败: {e}")
        all_passed = False
    
    try:
        if not test_data_models():
            all_passed = False
    except Exception as e:
        print(f"\n❌ 数据模型测试失败: {e}")
        all_passed = False
    
    try:
        if not test_csv_generation():
            all_passed = False
    except Exception as e:
        print(f"\n❌ CSV生成测试失败: {e}")
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ 所有测试通过！")
        print("\n下一步:")
        print("1. 安装依赖: pip install -r requirements.txt")
        print("2. 运行完整测试: python test_parser.py")
        print("3. 运行应用: python main.py")
    else:
        print("❌ 部分测试失败，请检查错误信息")
    print("=" * 60)
