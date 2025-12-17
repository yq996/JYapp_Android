import json
import time
import allure
import pytest
from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement
from appium.options.common import AppiumOptions
from pyexpat.errors import messages
from testcases.devices_page import Device
from testcases.login_page import LoginPage
from testcases.message import Message
from testcases.person import Person
from testcases.play_page import PlayPage
from utils.read_json import get_data
from utils.record_video import *
from utils.get_devices import make_devices_list
from utils.start_appium import start_appium

class TestFlutterApp:

    devices = make_devices_list(4723,8300)  # 这里确保一个端口只对应一个设备
    @pytest.fixture(params=devices,autouse=True)  #params=devices → pytest 会为每个设备生成一份独立的测试实例（fixture 参数化）
    # request.param 就是 当前测试实例对应的那个参数，也就是 devices 列表中的一个元素。
    def setup_and_teardown(self,request):
        self.udid = request.param["udid"]
        caps = {
            "platformName": "Android",
            "udid":self.udid ,
            "deviceName": self.udid,
    	    "appPackage": "com.pwithe.JYApps",
            "appActivity": "com.pwithe.jyapps.MainActivity",
            "automationName": "flutter",
            "systemPort": request.param["systemPort"],
            # "noReset": True,
        }
        options = AppiumOptions()
        options.load_capabilities(caps)

        self.driver = webdriver.Remote(f"http://127.0.0.1:{request.param['port']}", options=options)
        self.finder = FlutterFinder()

        yield

        if self.driver is not None:
            self.driver.quit()

    data=get_data()
    @pytest.mark.parametrize("case",data)
    def test_1(self,case):
        allure.dynamic.title(f"{self.udid}设备用例执行")
        login_page = LoginPage(self.driver, self.finder)
        play_page = PlayPage(self.driver, self.finder)
        message_page=Message(self.driver, self.finder)
        person_page=Person(self.driver, self.finder)
        device_page=Device(self.driver, self.finder)

        # 登录操作
        login_page.login(case["login"]["username"], case["login"]["password"],case["login"]["expect_value"])
        # person_page.personal_change()
        # person_page.personal_login_out()
        # person_page.personal_login_out1()
        # person_page.manage()
        # person_page.delete_user()
        # play_page.enter_play_page()
        # play_page.play_video1()
        # play_page.play_video2()
        # play_page.play_video3()
        # play_page.play_video4()
        # play_page.play_video5()
        # play_page.play_video6()
        # play_page.play_video7()
        # play_page.play_video8()
        # play_page.full_play_video1()
        # play_page.full_play_video2()
        # play_page.full_play_video3()
        # play_page.full_play_video4()
        # play_page.full_play_video5()
        # play_page.full_play_video6()
        # play_page.full_play_video7()
        # play_page.full_play_video8()
        # play_page.full_sleep_wake_voice()
        # play_page.full_chang_Resolution()
        # play_page.full_talk_play()
        # play_page.full_take_pic()
        # play_page.take_pic()
        # play_page.talk_play()
        # play_page.care_play()
        # self.driver.back()
        # play_page.setting_play()
        # self.driver.back()
        # play_page.quick_play()
        # play_page.set_weather()
        # self.driver.back()
        # play_page.leave_Message()
        # self.driver.back()
        # play_page.call_History()
        # self.driver.back()
        # time.sleep(3)
        # play_page.chang_Resolution()
        # play_page.sleep_wake_voice()
        # self.driver.back()
        # message_page.message_home()
        person_page.cared_person1()
        # person_page.cared_person2()
        # device_page.devices_home()





if __name__ == '__main__':
    pytest.main(["-vs", __file__])

