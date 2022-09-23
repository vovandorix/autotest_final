from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        #непонятка начало-----------------------
        self.should_not_be_success_message()
        self.should_dissapear_of_success_message()
        # непонятка конец-------------------------

        self.should_be_product_elements()
        self.add_to_basket()
        self.product_page_messages()

    def should_be_product_elements(self):
        assert self.is_element_present(*ProductPageLocators.ADD2BASKET_BTN), "Add to basket button is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"


    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD2BASKET_BTN)
        add_to_basket_button.click()
        #self.solve_quiz_and_get_code()



    def product_page_messages(self):
        product_name= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE)
        assert product_name.text == added_name.text, 'Product not in basket'
        assert product_price.text == added_price.text, 'Price incorrect'

        print('-------ok------')

    # совсем непонятное как в base_page
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        print('FUNCTION 1 IS ENDED!!!')

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message disappeared, but should not be"
        print('FUNCTION 2 IS ENDED!!!')












