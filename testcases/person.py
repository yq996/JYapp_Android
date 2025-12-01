import allure

from testcases.base_page import BasePage


class Person(BasePage):

    PERSON="homePersonKey"

    @allure.step("个人界面测试用例")
    def person_home(self):
        self.click("key",self.PERSON)
