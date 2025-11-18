import allure

from testcases.base_page import BasePage


class Device(BasePage):

    DEVICES="homeDeviceKey" #设备列表界面
    REFRESH_BTN = "refreshIndicatorKey"  # 设备刷新

    @allure.step("设备列表界面测试用例")
    def devices_home(self):
        self.click(self.DEVICES)
        self.scroll(self.REFRESH_BTN)
