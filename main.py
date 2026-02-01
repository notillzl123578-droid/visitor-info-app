"""应用入口"""
import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from app.ui import MainScreen, PreviewScreen, HistoryScreen


class VisitorInfoApp(App):
    """来宾信息提取应用"""
    
    def build(self):
        """构建应用"""
        # 注册中文字体
        self.register_chinese_fonts()
        
        sm = ScreenManager()
        
        # 添加主界面
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)
        
        # 添加预览界面
        preview_screen = PreviewScreen(name='preview')
        sm.add_widget(preview_screen)
        
        # 添加历史记录界面
        history_screen = HistoryScreen(name='history')
        sm.add_widget(history_screen)
        
        return sm
    
    def register_chinese_fonts(self):
        """注册中文字体"""
        # Windows系统字体路径
        font_paths = [
            'C:/Windows/Fonts/msyh.ttc',      # 微软雅黑
            'C:/Windows/Fonts/simhei.ttf',    # 黑体
            'C:/Windows/Fonts/simsun.ttc',    # 宋体
            'C:/Windows/Fonts/simkai.ttf',    # 楷体
        ]
        
        # 尝试注册第一个可用的字体
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    LabelBase.register(
                        name='Roboto',  # Kivy默认字体名
                        fn_regular=font_path
                    )
                    print(f'✓ 已注册中文字体: {font_path}')
                    break
                except Exception as e:
                    print(f'注册字体失败: {font_path}, 错误: {e}')
                    continue


if __name__ == '__main__':
    VisitorInfoApp().run()
