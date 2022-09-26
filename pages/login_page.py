from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Invalid login URL"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER), "Login user input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login button is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_1), "Registration password first input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_2), "Registration password second input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Registration button is not presented"


    def register_new_user(self, email, password):
        input_email=self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input_email.send_keys(email)
        input_pass1=self.browser.find_element(*LoginPageLocators.REG_PASS_1)
        input_pass1.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS_2)
        input_pass2.send_keys(password)
        reg_btn=self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()
