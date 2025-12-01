from testcases.base_page import  BasePage
import allure
class LoginPage(BasePage):
    #key值
    USERNAME = "LoginPage_UserName_InputField"
    PASSWORD = "LoginPage_PassWord_InputField"
    AGREEMENT = "LoginPage_Agreement_CheckBox"
    LOGIN_BUTTON = "LoginPage_Login_Button"

    @allure.step("1.登陆页测试用例执行")
    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click("key",self.AGREEMENT)
        self.click("key",self.LOGIN_BUTTON)
        self.assert_element("text","设备显示")
