from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USER=(By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')





class BasePageLocators():
    pass



