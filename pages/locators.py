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


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6 h1')
    PRODUCT_PRICE=(By.CSS_SELECTOR, '.col-sm-6 .price_color')
    ADD2BASKET_BTN = (By.CSS_SELECTOR, '#add_to_basket_form button')

    ADDED_NAME=(By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    ADDED_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, '.btn-group a.btn-default')

class BasketPageLocators():
    BASKET_HEADER=(By.CSS_SELECTOR,'.page-header h1')
    BASKET_TITLE=(By.CSS_SELECTOR,'basket-title')
    BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    BASKET_CONTENT_INFO = (By.CSS_SELECTOR, '#content_inner p')



