from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Invalid URL"
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER), "Login user input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login button is not presented"
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_1), "Registration password first input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_2), "Registration password second input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Registration button is not presented"
        #assert True