from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")

class MainPageLocators:
    pass
    
class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    REG_USER_EMAIL = (By.ID, "id_registration-email")
    REG_USER_PSW_1 = (By.ID, "id_registration-password1")
    REG_USER_PSW_2 = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
