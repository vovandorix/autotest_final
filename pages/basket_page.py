from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_elements()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "Invalid basket URL"

    def should_be_basket_elements(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), "Basket header is not presented"
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), "Basket content info is not presented"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
            "Basket title should be not presented, but it's not!!!"
        print('basket_empty_FUNCTION IS ENDED!!!')

    def should_be_is_disappeared_basket_title(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_TITLE), \
            "Basket title should be disappeared, but it's not!!!"
        print('basket_disappear_FUNCTION IS ENDED!!!')

    def should_be_empty_message(self):
        empty_message=self.browser.find_element(*BasketPageLocators.BASKET_CONTENT_INFO)
        assert empty_message.text.split('.')[0]=='Your basket is empty', 'There is no message that the basket is empty'


