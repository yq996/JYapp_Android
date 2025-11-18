import time
import allure
from appium_flutter_finder.flutter_finder import FlutterElement
from typing import Callable

class BasePage:
    def __init__(self, driver, finder):
        self.driver = driver
        self.finder = finder

    def get_element_key(self, key,timeout=5):
        try:
            self.driver.execute_script(
                'flutter:waitFor',
                self.finder.by_value_key(key),
                timeout * 1000  # 毫秒
            )
        except Exception:
            raise AssertionError(f"超时未找到 Flutter 元素：{key}")
        return FlutterElement(self.driver, self.finder.by_value_key(key))


    def get_element_text(self, text,timeout=5):
        try:
            self.driver.execute_script(
                'flutter:waitFor',
                self.finder.by_text(text),
                timeout * 1000  # 毫秒
            )
        except Exception:
            raise AssertionError(f"超时未找到 Flutter 元素：{text}")
        return FlutterElement(self.driver, self.finder.by_text(text))

    def click(self, key):
        el = self.get_element_key(key)
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
        el = self.get_element_key(key)
        el.send_keys(text)

    @allure.step("通过文本断言")
    def assert_element_text(self,expected_text,timeout=1):
        el=None
        for _ in range(timeout):
             try:
                el=self.get_element_text(expected_text)
                break
             except Exception:
                 time.sleep(1)
        if el is None:
            assert False,f"未找到文本{expected_text}"
        assert el.text==expected_text,f"期望文本：{expected_text},实际结果：{el.text}"

    @allure.step("通过key值断言")
    def assert_element_key(self,Expect_key,value,timeout=1):
        el = None
        for _ in range(timeout):
            try:
                el = self.get_element_key(Expect_key)
                break
            except Exception:
                time.sleep(1)
        if el is None:
            assert False, f"未找到key值{Expect_key}"
        assert el.text == value, f"期望key的值：{value},实际结果：{el.text}"

    def wait(self, sec:int):
        time.sleep(sec)

    def tap_x_y(self,x,y):
        self.driver.tap([(x,y)],500)

    def switch_context(self,func: Callable, *args):
        contexts = self.driver.contexts
        native_context = next(c for c in contexts if 'NATIVE_APP' in c)
        self.driver.switch_to.context(native_context)

        func(*args)

        flutter_context = next(c for c in contexts if 'FLUTTER' in c)
        self.driver.switch_to.context(flutter_context)
