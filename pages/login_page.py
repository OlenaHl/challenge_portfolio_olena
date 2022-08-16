from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='sign in']"
    scouts_panel_field_xpath = "//*[text()='scouts panel']"
    remind_password_button_xpath = "//*[text()='remind password']"
    english_button_xpath = "//*[text()='english']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
