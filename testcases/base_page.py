import time
import allure
from appium_flutter_finder.flutter_finder import FlutterElement

class BasePage:
    def __init__(self, driver, finder):
        self.driver = driver
        self.finder = finder

    def get_element(self, key):
        return FlutterElement(self.driver, self.finder.by_value_key(key))

    def get_element_text(self, text):
        return FlutterElement(self.driver, self.finder.by_text(text))

    def click(self, key):
        el = self.get_element(key)
        el.click()
        self.wait(3)


    def send_keys(self, key, text):
        el = self.get_element(key)
        el.send_keys(text)

    @allure.step("断言")
    def assert_element_text(self,text):
        el = self.get_element_text(text)
        assert el.text==text

    @allure.step("断言")
    def assert_element_key(self,key,value):
        el = self.get_element_text(key)
        assert el.text==value

    def wait(self, sec:int):
        time.sleep(sec)
