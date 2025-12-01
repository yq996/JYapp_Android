import allure

from testcases.base_page import BasePage


class Message(BasePage):
    MESSAGE="homeMessageKey"

    @allure.step("消息界面测试用例")
    def message_home(self):
        self.click("key",self.MESSAGE)
        self.scroll("type","MessagePager",0,-500)


