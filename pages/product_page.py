from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    product_name = ""
    product_price = ""
    
    def add_product_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_product_description()
        self.should_be_add_to_basket_button()
        
        add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()
        
        # self.solve_quiz_and_get_code()
        self.should_be_message_about_adding()
        self.check_message_about_adding()
        
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button is not presented"
    
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Product description is not presented"
    
    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
    
    def should_not_be_message_about_adding(self):
        assert self.is_element_not_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def check_message_about_adding(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        assert len(msg_lst) == 3, "Some messages not presented"
        
        assert self.product_name == msg_lst[0].text, "Wrong product name added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong product price added to basket"
