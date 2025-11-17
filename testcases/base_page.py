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
        self.wait(2)

    def long_click(self,key):
        finder = self.finder.by_value_key(key)
        options={
            "durationMilliseconds": 3000,
            "frequency": 60
        }
        self.driver.execute_script('flutter:longTap', finder,options)

    def scrollIntoView(self):
        self.driver.execute_script(
            'flutter:scrollIntoView',
            self.finder.by_value_key("play_0"),
            {"alignment": 0.1}
        )

    def scroll(self,key):
        finder = self.finder.by_value_key(key)
        scroll_value = {
            "dx": 0,
            "dy": 500,
            "durationMilliseconds": 200,
            "frequency": 60,
        }
        self.driver.execute_script('flutter:scroll', finder, scroll_value)

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
