import time

import allure

from testcases.base_page import BasePage

class PlayPage(BasePage):
    #key值
    PLAY_IPC = "play_0" #选择第一个设备，进入设备拉流界面
    PTZ_BTN = "ptzControlBtnKey" #点击云台控制
    PTZ_UP = "ptzUpKey" #云台控制上
    PTZ_DOWN="ptzDownKey"#云台控制下
    PTZ_LEFT="ptzLeftKey"#云台控制左
    PTZ_RIGHT="ptRightKey"#云台控制右
    LIVEMENU="liveMenuKey"#快捷按钮
    PersonManage="PersonPage_InkWell_CaretakerManagement"
    AddCaretake="CaretakerSettingMain_ElevatedButton_addCaretake"
    EditText_Name="AddCaretakerPage2_CustomEditText_Name"
    ADD_BIRTHDAY = "AddCaretakerPage2_ListView_Birthday"
    SOLAR_YEAR = "SolarDatePicker_ListWheelScrollView_Year"
    SOLAR_MONTH = "SolarDatePicker_ListWheelScrollView_Month"
    SOLAR_DATE = "SolarDatePicker_ListWheelScrollView_Date"
    LUNAR_YEAR = "LunarDatePicker_ListWheelScrollView_Year"
    LUNAR_MONTH = "LunarDatePicker_ListWheelScrollView_Month"
    LUNAR_DATE = "LunarDatePicker_ListWheelScrollView_Date"
    SURE_BIRTHDAY = "DayPickerBottomSheet_ElevatedButton_Sure"
    SAVE_CARED_PERSON="AddCaretakerPage2_ElevatedButton_save"
    TimePicker="AddClockPage_TimePicker"
    TimePickerHour="TimePicker_ListWheelScrollView_Hour"
    TimePickerHourMin="TimePicker_ListWheelScrollView_Min"


    #


    PRENIEW="Preview_Key"#竖屏+横屏拉流界面
    DISMISS="dismissFamilyVoiceDialog" #亲人声音克隆取消
    TAKEPIC="takePicKey" #截图
    RECORD="recodeKey" #录像
    FULLSCREEN="fullScreenKey"#全屏
    TALK="_talkMenuKey"#对讲
    MENUCARE="menuCareKey"#看护助手
    MENUSETTING="menuSettingKey"#设备设置

    localWeather ="localWeatherBtnKey" #当地天气
    leaveMessage ="leaveMessageBtnKey" #留言记录
    callHistory ="callHistoryBtnKey" #呼叫记录
    previewSleep ="previewSleepKey"#休眠
    toWakeUp ="toWakeUpKey"#去唤醒
    previewSetMute = "previewSetMuteKey" #设置静音

    changeRes ="changeResolutionKey" #切换分辨率
    ResRadio ="resolutionRadioKey"#清晰度选择
    ResSubmit ="resolutionSubmitKey"#清晰度确认





    @allure.step("进入设备拉流界面")
    def enter_play_page(self):
        self.click("key",self.PLAY_IPC)
        self.click("key",self.DISMISS)

    @allure.step(f"选择生日")
    def Birthday(self, BIRTHDAYtype):
        if BIRTHDAYtype == "阳历":
            self.click("text", "阳历")
            self.scroll("key", self.SOLAR_YEAR, 0, -100)
            self.scroll("key", self.SOLAR_MONTH, 0, -100)
            self.scroll("key", self.SOLAR_DATE, 0, -100)
        elif BIRTHDAYtype == "农历":
            self.click("text", "农历")
            self.scroll("key", self.LUNAR_YEAR, 0, -100)
            self.scroll("key", self.LUNAR_MONTH, 0, -100)
            self.scroll("key", self.LUNAR_DATE, 0, -100)
        self.click("key", self.SURE_BIRTHDAY)

    @allure.step("云台控制测试用例1-UP")
    def play_video1(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_UP)
        self.long_click(self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例2-DOWN")
    def play_video2(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_DOWN)
        self.long_click(self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例3-LEFT")
    def play_video3(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_LEFT)
        self.long_click(self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例4-RIGHT")
    def play_video4(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_RIGHT)
        self.long_click(self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例5-UP")
    def play_video5(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_UP)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例6-DOWN")
    def play_video6(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_DOWN)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例7-LEFT")
    def play_video7(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_LEFT)
        self.click("key",self.PTZ_BTN)

    @allure.step("云台控制测试用例8-RIGHT")
    def play_video8(self):
        self.click("key",self.PTZ_BTN)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_RIGHT)
        self.click("key",self.PTZ_BTN)

    @allure.step("全屏云台控制测试用例1-UP")
    def full_play_video1(self):
        self.click("key",self.PRENIEW)
        self.click("key",self.FULLSCREEN)
        self.click("key", self.PTZ_UP)
        self.long_click(self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)



    @allure.step("全屏云台控制测试用例2-DOWN")
    def full_play_video2(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_DOWN)
        self.long_click(self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例3-LEFT")
    def full_play_video3(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_LEFT)
        self.long_click(self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例4-RIGHT")
    def full_play_video4(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_RIGHT)
        self.long_click(self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例5-UP")
    def full_play_video5(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.PTZ_UP)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例6-DOWN")
    def full_play_video6(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.PTZ_DOWN)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例7-LEFT")
    def full_play_video7(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.PTZ_LEFT)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏云台控制测试用例8-RIGHT")
    def full_play_video8(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.PTZ_RIGHT)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏休眠-去唤醒-静音测试用例")
    def full_sleep_wake_voice(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.previewSleep)
        self.click("key", self.toWakeUp)
        self.click("key", self.previewSetMute)
        self.click("key", self.previewSetMute)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏切换分辨率测试用例")
    def full_chang_Resolution(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.changeRes)
        self.click("text", "流畅")
        self.click("text", "超清")
        self.click("key", self.ResSubmit)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)

    @allure.step("全屏截图-录像")
    def take_pic(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.TAKEPIC)
        time.sleep(3)
        self.click("key", self.RECORD)
        time.sleep(10)
        self.click("key", self.RECORD)
        self.click("key", self.RECORD)
        time.sleep(10)
        self.click("key", self.RECORD)
        self.click("key", self.TAKEPIC)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)



    @allure.step("截图-录像")
    def full_take_pic(self):
        self.click("key",self.PRENIEW)
        self.click("key",self.TAKEPIC)
        time.sleep(3)
        self.click("key",self.RECORD)
        time.sleep(10)
        self.click("key",self.RECORD)
        self.click("key",self.RECORD)
        time.sleep(10)
        self.click("key",self.RECORD)
        self.click("key",self.TAKEPIC)

    @allure.step("对讲功能")
    def full_talk_play(self):
        self.click("key", self.PRENIEW)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.TALK)
        time.sleep(10)
        self.click("key", self.FULLSCREEN)
        self.click("key", self.PRENIEW)


    @allure.step("快捷功能测试用例")
    def quick_play(self,BIRTHDAYtype):
        # 被看护人管理
        self.click("key",self.LIVEMENU)
        # 在 Native 上点击坐标 (200, 200)
        # self.switch_context(self.tap_x_y, 200, 200)
        self.click("text","被看护人管理")
        self.click("text", "添加被看护人")
        self.send_keys("key",self.EditText_Name,"lisi")
        self.click("key", self.ADD_BIRTHDAY)
        self.Birthday(BIRTHDAYtype)
        self.click("key", self.SAVE_CARED_PERSON)
        self.driver.back()



    @allure.step("对讲功能")
    def talk_play(self):
        self.click("key",self.TALK)
        time.sleep(10)

    @allure.step("看护助手测试用例")
    def care_play(self):
        self.click("key",self.MENUCARE)

    @allure.step("设备设置测试用例")
    def setting_play(self):
        self.click("key",self.MENUSETTING)

    @allure.step("天气设置测试用例")
    def set_weather(self):
        self.click("key",self.localWeather)


    @allure.step("留言记录测试用例")
    def leave_Message(self):
        self.click("key",self.leaveMessage)


    @allure.step("呼叫记录测试用例")
    def call_History(self):
        self.click("key",self.callHistory)

    @allure.step("休眠-去唤醒-静音测试用例")
    def sleep_wake_voice(self):
        self.click("key",self.PRENIEW)
        self.click("key",self.previewSleep)
        self.click("key",self.toWakeUp)
        self.click("key",self.previewSetMute)
        self.click("key",self.previewSetMute)
        self.click("key", self.PRENIEW)

    @allure.step("切换分辨率测试用例")
    def chang_Resolution(self):
        self.click("key",self.PRENIEW)
        self.click("key",self.changeRes)
        self.click("text", "流畅")
        self.click("text","超清")
        self.click("key",self.ResSubmit)
        self.click("key", self.PRENIEW)













