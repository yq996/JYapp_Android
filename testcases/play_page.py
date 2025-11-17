import allure

from testcases.base_page import BasePage

class PlayPage(BasePage):
    #key值
    PLAY_IPC = "play_0" #进入设备拉流界面
    PTZ_BTN = "ptzControlBtnKey" #点击云台控制
    REFRESH_BTN = "refreshIndicatorKey"
    PTZ_UP = "ptzUpKey" #云台控制上
    PTZ_DOWN="ptzDownKey"#云台控制下
    PTZ_LEFT="ptzLeftKey"#云台控制左
    PTZ_RIGHT="ptRightKey"#云台控制右
    FULLSCREEN="fullScreenKey"#全屏
    LIVEMENU="liveMenuKey"#快捷按钮
    PRENIEW="preview_touch_key"#竖屏+横屏拉流界面
    DISMISS="dismissFamilyVoiceDialog"

    @allure.step("云台控制页测试")
    def play_video(self):
        self.scroll(self.REFRESH_BTN)
        self.click(self.PLAY_IPC)
        self.click(self.DISMISS)
        self.click(self.PTZ_BTN)
        self.long_click(self.PTZ_LEFT)
        self.click(self.PTZ_BTN)

