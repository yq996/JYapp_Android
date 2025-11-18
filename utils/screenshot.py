import allure

def screenshot(driver):
    driver.get_screenshot_as_file("flutter_screenshot.png")
    allure.attach.file("flutter_screenshot.png",name="个人中心截图",attachment_type=allure.attachment_type.PNG)
