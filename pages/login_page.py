from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' missing from url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_USER_EMAIL)
        email_input.send_keys(email)
        
        password_input_1 = self.browser.find_element(*LoginPageLocators.REG_USER_PSW_1)
        password_input_1.send_keys(password)
        
        password_input_2 = self.browser.find_element(*LoginPageLocators.REG_USER_PSW_2)
        password_input_2.send_keys(password)
        
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()