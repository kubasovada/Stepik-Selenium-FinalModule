from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page  h1")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, "#messages .alertinner > p:first-child strong")

