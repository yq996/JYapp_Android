import allure


def screenshot(driver):
    # 初始化 driver 后，先切换到原生上下文截图
        contexts = driver.contexts
        # 找到原生上下文（通常包含 'NATIVE_APP'）
        native_context = next(c for c in contexts if 'NATIVE_APP' in c)
        driver.switch_to.context(native_context)

        # 现在可以正常截图
        driver.get_screenshot_as_file("flutter_screenshot.png")
        allure.attach.file("flutter_screenshot.png",name="个人中心截图",attachment_type=allure.attachment_type.PNG)

        # 截图后可切回 Flutter 上下文继续操作
        flutter_context = next(c for c in contexts if 'FLUTTER' in c)
        driver.switch_to.context(flutter_context)