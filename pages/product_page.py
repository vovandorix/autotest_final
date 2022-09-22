from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

import time



class ProductPage(BasePage):

    def should_be_product_page(self):
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
        self.solve_quiz_and_get_code()



    def product_page_messages(self):
        #time.sleep(10)
        product_name= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE)
        assert product_name.text == added_name.text, 'Product not in basket'
        assert product_price.text == added_price.text, 'Price incorrect'

        print('-------ok------')
        print(product_name.text)
        print(product_price.text)
        print('-------ok------')











