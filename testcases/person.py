import allure

from testcases.base_page import BasePage


class Person(BasePage):

    PERSON="homePersonKey"
    CARED_PERSON="PersonPage_InkWell_CaretakerManagement"
    ADD_CARETAKER="CaretakerSettingMain_ElevatedButton_addCaretaker"
    ADD_NAME="AddCaretakerPage2_CustomEditText_Name"
    ADD_BIRTHDAY="AddCaretakerPage2_ListView_Birthday"
    SOLAR_YEAR="SolarDatePicker_ListWheelScrollView_Year"
    SOLAR_MONTH="SolarDatePicker_ListWheelScrollView_Month"
    SOLAR_DATE="SolarDatePicker_ListWheelScrollView_Date"
    SURE_BIRTHDAY="DayPickerBottomSheet_ElevatedButton_Sure"
    SAVE_CARED_PERSON="AddCaretakerPage2_ElevatedButton_save"
    LUNAR_YEAR="LunarDatePicker_ListWheelScrollView_Year"
    LUNAR_MONTH="LunarDatePicker_ListWheelScrollView_Month"
    LUNAR_DATE="LunarDatePicker_ListWheelScrollView_Date"
    SELECT_LUNAR="DayPickerBottomSheet_CalendarTypeOption_Lunar"
    PERSON_VOICE="PersonPage_InkWell_FamilyVoiceManagement"
    ADD_VOICE="AddFamilyVoicePage_ListView_BasicInfo"
    ADD_VOICE_NAME="AddFamilyVoicePage_InputNameBottomSheet"
    ADD_VOICE_TEXTFIELD="InputNameBottomSheet_TextField_Name"
    PERSONAL="PersonPage_to_PersonPersonalPage"
    CHANGE_PASSWORD="ChangePassword_Button"
    OLD_PASSWORD="ChangePasswordPage_OldPasswordField"
    NEW_PASSWORD="PasswordTextField_New_Pwd"
    SURE_PASSWORD="PasswordTextField_Confirm_Pwd"
    SURE_CHANGE_PASSWORD="PasswordTextField_Button"
    LOGIN_OUT="Logout_Button"
    SURE_LOGIN_OUT="Logout_ConfirmButton"
    CANCEL_LOGIN_OUT="Logout_CancelButton"
    DELETE_USER="DeleteUser_Button"
    DELETE_AGREE="Agree_AgreementCheckbox"
    DELETE_CONFIRM="Confirm_DeleteButton"
    DELETE_CANCEL="Cancel_DeleteButton"
    DELETE_CANCEL_TWO="Cancel_Delete_User"
    DELETE_CONFIRM_TWO="Confirm_Delete_User"
    CARED_SCROLL_LIST="CaretakerSettingMain_ListView_scroll"
    @allure.step("个人界面测试用例")
    def person_home(self):
        self.click("key",self.PERSON)

    @allure.step("被看护人管理测试用例-阳历生日添加")
    def cared_person1(self):
        self.click("key",self.PERSON)
        self.click("key",self.CARED_PERSON)
        self.click("text","添加被看护人")
        self.send_keys("key",self.ADD_NAME,"1111")
        self.click("key",self.ADD_BIRTHDAY)
        self.scroll("key",self.SOLAR_YEAR,0,-100)
        self.scroll("key", self.SOLAR_MONTH, 0, -100)
        self.scroll("key",self.SOLAR_DATE,0,-100)
        self.click("key",self.SURE_BIRTHDAY)
        self.click("key",self.SAVE_CARED_PERSON)
        self.scroll_assert("酷酷酷",self.CARED_SCROLL_LIST)



    @allure.step("被看护人管理测试用例-农历生日添加")
    def cared_person2(self):
        self.click("key", self.PERSON)
        self.click("key", self.CARED_PERSON)
        self.click("key", self.ADD_CARETAKER)
        self.send_keys("key", self.ADD_NAME, "阿斯顿")
        self.click("key", self.ADD_BIRTHDAY)
        self.click("key", self.SELECT_LUNAR)
        self.scroll("key", self.LUNAR_YEAR, 0, -100)
        self.scroll("key", self.LUNAR_MONTH, 0, -100)
        self.scroll("key", self.LUNAR_DATE, 0, -100)
        self.click("key", self.SURE_BIRTHDAY)
        self.click("key", self.SAVE_CARED_PERSON)
        self.driver.back()

    # @allure.step("添加亲人声音-阳历时间")
    # def person_voice(self):
    #     self.click("key",self.PERSON)
    #     self.click("key",self.PERSON_VOICE)
    #     self.click("key",self.ADD_VOICE)
    #     self.click("key",self.ADD_VOICE_NAME)
    #     self.send_keys("key",self.ADD_VOICE_TEXTFIELD,"声音1")

    @allure.step("个人中心测试用例-修改密码")
    def personal_change(self):
        self.click("key",self.PERSON)
        self.click("key",self.PERSONAL)
        self.click("key",self.CHANGE_PASSWORD)
        self.send_keys("key",self.OLD_PASSWORD,"yanqing123!")
        self.send_keys("key",self.NEW_PASSWORD,"yanqing123!")
        self.send_keys("key",self.SURE_PASSWORD,"yanqing123!")
        self.click("key",self.SURE_CHANGE_PASSWORD)
        # self.assert_true("text","密码修改成功！请重新登陆！")

    @allure.step("个人中心测试用例-退出登录")
    def personal_login_out(self):
        self.click("key",self.PERSON)
        self.click("key",self.PERSONAL)
        self.click("key",self.LOGIN_OUT)
        self.click("key", self.CANCEL_LOGIN_OUT)
        self.click("key", self.LOGIN_OUT)
        self.click("key",self.SURE_LOGIN_OUT)

    @allure.step("个人中心测试用例-取消退出登录")
    def personal_login_out1(self):
        self.click("key", self.PERSON)
        self.click("key", self.PERSONAL)
        self.click("key", self.LOGIN_OUT)
        self.click("key", self.CANCEL_LOGIN_OUT)

    allure.step("权限管理")
    def manage(self):
        self.click("key", self.PERSON)
        self.click("key", self.PERSONAL)
        self.click("key","RightsManagement_Button")
        self.driver.back()

    @allure.step("个人中心测试用例-账号注销-最后取消")
    def delete_user(self):
        self.click("key", self.PERSON)
        self.click("key", self.PERSONAL)
        self.click("key",self.DELETE_USER)
        self.click("key", self.DELETE_AGREE)
        self.click("key", self.DELETE_CONFIRM)
        self.click("key", self.DELETE_CANCEL_TWO)

    @allure.step("个人中心测试用例-账号注销-开始取消")
    def delete_user1(self):
        self.click("key", self.PERSON)
        self.click("key", self.PERSONAL)
        self.click("key",self.DELETE_USER)
        self.click("key", self.DELETE_CANCEL)

    @allure.step("个人中心测试用例-账号注销-确认注销账号")
    def delete_user2(self):
        self.click("key", self.PERSON)
        self.click("key", self.PERSONAL)
        self.click("key",self.DELETE_USER)
        self.click("key", self.DELETE_AGREE)
        self.click("key", self.DELETE_CONFIRM)
        self.click("key", self.DELETE_CANCEL_TWO)