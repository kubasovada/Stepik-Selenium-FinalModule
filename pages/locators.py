from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page  h1")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, "#messages .alertinner > p:first-child strong")

class BasketPagelocators:
    PRODUCT_LIST = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, ".page_inner #content_inner p")


