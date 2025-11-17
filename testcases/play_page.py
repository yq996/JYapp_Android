import time

import allure

from testcases.base_page import BasePage

class PlayPage(BasePage):
    #key值
    PLAY_IPC = "play_0" #进入设备拉流界面
    PTZ_BTN = "ptzControlBtnKey" #点击云台控制
    REFRESH_BTN = "refreshIndicatorKey" #设备刷新
    PTZ_UP = "ptzUpKey" #云台控制上
    PTZ_DOWN="ptzDownKey"#云台控制下
    PTZ_LEFT="ptzLeftKey"#云台控制左
    PTZ_RIGHT="ptRightKey"#云台控制右
    LIVEMENU="liveMenuKey"#快捷按钮
    PRENIEW="preview_touch_key"#竖屏+横屏拉流界面
    DISMISS="dismissFamilyVoiceDialog" #亲人声音克隆取消
    TAKEPIC="takePicKey" #截图
    RECORD="recordKey" #录像
    FULLSCREEN="fullScreenKey"#全屏
    TALK="_talkMenuKey"




    def enter_play_page(self):
        self.click(self.PLAY_IPC)
        self.click(self.DISMISS)

    @allure.step("云台控制页测试")
    def play_video(self):
        self.scroll(self.REFRESH_BTN)
        self.click(self.PLAY_IPC)
        self.click(self.DISMISS)
        self.click(self.PTZ_BTN)
        self.long_click(self.PTZ_LEFT)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例1-UP")
    def play_video1(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_UP)
        self.long_click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例2-DOWN")
    def play_video2(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_DOWN)
        self.long_click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例3-LEFT")
    def play_video3(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_LEFT)
        self.long_click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例4-RIGHT")
    def play_video4(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_RIGHT)
        self.long_click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例5-UP")
    def play_video5(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_UP)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例6-DOWN")
    def play_video6(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_DOWN)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例7-LEFT")
    def play_video7(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_LEFT)
        self.click(self.PTZ_BTN)

    @allure.step("云台控制测试用例8-RIGHT")
    def play_video8(self):
        self.click(self.PTZ_BTN)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_RIGHT)
        self.click(self.PTZ_BTN)

    @allure.step("截图-录像-全屏测试用例")
    def take_pic(self):
        self.click(self.PRENIEW)
        self.click(self.TAKEPIC)
        self.click(self.RECORD)
        time.sleep(10)
        self.click(self.RECORD)
        self.click(self.RECORD)
        time.sleep(10)
        self.click(self.RECORD)
        self.click(self.TAKEPIC)

    @allure.step("快捷功能测试用例")
    def quick_play(self):
        self.click(self.LIVEMENU)
        # 在 Native 上点击坐标 (200, 200)
        self.switch_context(self.tap_x_y, 200, 200)

    allure.step("对讲功能")
    def talk_play(self):
        self.click(self.TALK)
        time.sleep(10)











