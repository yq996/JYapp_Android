import functools
import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium_flutter_finder.flutter_finder import FlutterElement
from typing import Callable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self, driver, finder):
        self.driver = driver
        self.finder = finder

    # 定义一个通用的重试装饰器
    @staticmethod
    def retry_on_failure(retries=3, delay=1):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for i in range(retries):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        print(f"操作 [{func.__name__}] 失败，正在进行第 {i + 1} 次重试... 错误: {e}")
                        time.sleep(delay)
                raise AssertionError(f"经过 {retries} 次重试后仍然失败: {last_exception}")

            return wrapper

        return decorator

    @allure.step("定位元素")
    @retry_on_failure(retries=3)  # 给定位增加重试
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
    @retry_on_failure(retries=3)  # 给定位增加重试
    def click(self, locator_type,locator_value):
        global el
        if locator_type == "key":
            el = self.get_element("key",locator_value)
        elif locator_type == "text":
            el = self.get_element("text",locator_value)
        el.click()
        self.wait(2)

    @allure.step("长按操作")
    @retry_on_failure(retries=3)  # 给定位增加重试
    def long_click(self,key):
        finder = self.finder.by_value_key(key)
        options={
            "durationMilliseconds": 3000,
            "frequency": 60
        }
        self.driver.execute_script('flutter:longTap', finder,options)

    @allure.step("滑动到固定位置")
    @retry_on_failure(retries=3)  # 给定位增加重试
    def scrollIntoView(self,Expect_value):
        self.driver.execute_script(
            'flutter:scrollIntoView',
            self.finder.by_text(Expect_value),
            {"alignment": 0.1}
        )

    @allure.step("滑动")
    @retry_on_failure(retries=3)  # 给定位增加重试
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
    @retry_on_failure(retries=3)  # 给定位增加重试
    def send_keys(self, locator_type,locator_value,entext_value):
        global el
        if locator_type == "key":
            el = self.get_element("key", locator_value)
        elif locator_type == "text":
            el = self.get_element("text", locator_value)
        el.send_keys(entext_value)


    @allure.step("断言存在")
    @retry_on_failure(retries=3)  # 给定位增加重试
    def assert_true(self,locator_type,Expect_value):
        if locator_type == "text":
            self.driver.execute_script(
                'flutter:assertVisible',
                {'text': Expect_value },
                1000
            )
        elif locator_type == "key":
            self.driver.execute_script(
                'flutter:assertVisible',
                {'key': Expect_value},
                1000
            )

    @allure.step("滑动断言")
    @retry_on_failure(retries=3)  # 给定位增加重试
    def scroll_assert(self, expect_value,scroll_list, max_swipes=20):
        """
        滑动列表，直到目标文本出现断言通过
        expect_value: 要断言可见的文本
        max_swipes: 最大滑动次数，防止无限循环
        """
        for i in range(max_swipes):
            try:
                # 尝试断言目标文本可见
                self.driver.execute_script(
                    'flutter:assertVisible',
                    {'text': expect_value},
                    1000
                )
                # 如果断言通过，结束函数
                return
            except Exception:
                # 如果断言失败，滑动列表
                self.scroll("key", scroll_list, 0, -200)

    @allure.step("断言不存在")
    @retry_on_failure(retries=3)  # 给定位增加重试
    def assert_false(self, Expect_value, locator_type):
        if locator_type == "text":
            self.driver.execute_script(
                'flutter:assertNotVisible',
                {'text': Expect_value}
            )
        elif locator_type == "key":
            self.driver.execute_script(
                'flutter:assertNotVisible',
                {'key': Expect_value}
            )

    @staticmethod
    def wait(sec:int):
        time.sleep(sec)

    @retry_on_failure(retries=3)  # 给定位增加重试
    def tap_x_y(self,x,y):
        self.driver.tap([(x,y)],500)

    @retry_on_failure(retries=3)  # 给定位增加重试
    def switch_context(self,func: Callable, *args):
        contexts = self.driver.contexts
        native_context = next(c for c in contexts if 'NATIVE_APP' in c)
        self.driver.switch_to.context(native_context)

        func(*args)

        flutter_context = next(c for c in contexts if 'FLUTTER' in c)
        self.driver.switch_to.context(flutter_context)
