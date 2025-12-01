import time
import allure
from appium_flutter_finder.flutter_finder import FlutterElement
from typing import Callable

class BasePage:
    def __init__(self, driver, finder):
        self.driver = driver
        self.finder = finder

    @allure.step("定位元素")
    def get_element(self, locator_type,locator_value,timeout=5):
        if locator_type == "key":
            try:
                self.driver.execute_script(
                    'flutter:waitFor',
                    self.finder.by_value_key(locator_value),
                    timeout * 1000  # 毫秒
                )
            except Exception:
                raise AssertionError(f"超时未找到 Flutter 元素：{locator_value}")
            return FlutterElement(self.driver, self.finder.by_value_key(locator_value))
        elif locator_type == "text":
            try:
                self.driver.execute_script(
                    'flutter:waitFor',
                    self.finder.by_text(locator_value),
                    timeout * 1000  # 毫秒
                )
            except Exception:
                raise AssertionError(f"超时未找到 Flutter 元素：{locator_value}")
            return FlutterElement(self.driver, self.finder.by_text(locator_value))
        return None

    @allure.step("点击操作")
    def click(self, locator_type,locator_value):
        global el
        if locator_type == "key":
            el = self.get_element("key",locator_value)
        elif locator_type == "text":
            el = self.get_element("text",locator_value)
        el.click()
        self.wait(2)

    @allure.step("长按操作")
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

    @allure.step("滑动")
    def scroll(self,locator_type,locator_value,x,y):
        global finder
        if locator_type == "type":
            finder = self.finder.by_type(locator_value)
        elif locator_type == "key":
            finder = self.finder.by_value_key(locator_value)
        scroll_value = {
            "dx": x,
            "dy": y, #正数向下滑动
            "durationMilliseconds": 200,
            "frequency": 60,
        }
        self.driver.execute_script('flutter:scroll', finder, scroll_value)

    @allure.step(f"输入文本")
    def send_keys(self, key, text):
        el = self.get_element("key",key)
        el.send_keys(text)

    @allure.step("断言")
    def assert_element(self,locator_type,locator_value,Expect_value=None,timeout=1):
        el=None
        if locator_type == "text":
            for _ in range(timeout):
                 try:
                    el=self.get_element("text",locator_value)
                    break
                 except Exception:
                     time.sleep(1)
            if el is None:
                assert False,f"未找到文本{locator_value}"
            assert el.text==locator_value,f"期望文本：{locator_value},实际结果：{el.text}"
        elif locator_type == "key":
            for _ in range(timeout):
                try:
                    el = self.get_element("key", locator_value)
                    break
                except Exception:
                    time.sleep(1)
            if el is None:
                assert False, f"未找到key值{locator_value}"
            assert el.text ==Expect_value , f"期望key的值：{Expect_value},实际结果：{el.text}"

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
