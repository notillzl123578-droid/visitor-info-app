"""测试解析功能"""
from app.services import WordParser, TextExtractor, ExcelGenerator
from app.models import ExtractedData

# 测试文本
test_text = """
12月9日（周二）国资委领导到公司调研

调研时间：2024年12月9日 14:00-16:00

陪同领导：张三、李四

陪同部门：办公室、人力资源部

调研路线：公司大厅 → 展厅 → 生产车间 → 会议室

附录 B来宾信息表
来访事由：海南省属国企董事会来访参观
序号 来宾单位 姓名 民族 职务 健康状况
1 海南省国资委 李伟 汉族 法治处处长 良好
2 省属企业 陈良才 汉族 专职外部董事 良好
3 省属企业 陈敏 汉族 专职外部董事 良好
"""

def test_text_extraction():
    """测试文本提取"""
    print("=" * 50)
    print("测试文本提取")
    print("=" * 50)
    
    extractor = TextExtractor()
    activity = extractor.extract_activity_info(test_text)
    
    print(f"\n提取结果:")
    print(f"日期: {activity.date}")
    print(f"参观事项: {activity.event}")
    print(f"陪同领导: {activity.leader}")
    print(f"陪同部门: {activity.department}")
    print(f"参观路线: {activity.route}")
    
    assert activity.date == "12月9日", f"日期提取错误: {activity.date}"
    assert "国资委领导到公司调研" in activity.event, f"参观事项提取错误: {activity.event}"
    assert "张三" in activity.leader, f"陪同领导提取错误: {activity.leader}"
    assert "办公室" in activity.department, f"陪同部门提取错误: {activity.department}"
    assert "公司大厅" in activity.route, f"参观路线提取错误: {activity.route}"
    
    print("\n✅ 文本提取测试通过")

def test_excel_generation():
    """测试Excel生成"""
    print("\n" + "=" * 50)
    print("测试Excel生成")
    print("=" * 50)
    
    # 创建测试数据
    data = ExtractedData()
    
    extractor = TextExtractor()
    data.activity = extractor.extract_activity_info(test_text)
    
    # 手动添加来宾（模拟Word解析结果）
    from app.models import GuestInfo
    data.guests = [
        GuestInfo(company="海南省国资委", name="李伟", position="法治处处长"),
        GuestInfo(company="省属企业", name="陈良才", position="专职外部董事"),
        GuestInfo(company="省属企业", name="陈敏", position="专职外部董事")
    ]
    
    # 生成Excel
    generator = ExcelGenerator()
    output_path = generator.generate_csv(
        data.activity,
        data.guests,
        output_path='test_output.csv'
    )
    
    print(f"\n✅ Excel生成成功: {output_path}")
    
    # 验证文件内容
    with open(output_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        print(f"\n文件内容预览:")
        print(content[:500])
        
        assert "12月9日" in content, "日期未写入"
        assert "李伟" in content, "来宾姓名未写入"
        assert "法治处处长" in content, "职务未写入"
        assert "3" in content, "总人数未写入"
    
    print("\n✅ Excel生成测试通过")

if __name__ == '__main__':
    test_text_extraction()
    test_excel_generation()
    print("\n" + "=" * 50)
    print("所有测试通过！")
    print("=" * 50)
