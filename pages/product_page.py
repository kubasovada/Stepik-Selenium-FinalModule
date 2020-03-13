from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add_to_basket button is not presented"

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def give_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def give_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def give_basket_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        return cart_price

    def should_be_success_message(self, name):
        self.name = name
        message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        assert  self.name in message, "Product is not added to basket"

    def should_be_cart_value(self, price):
        self.price = price
        assert self.give_basket_price() == self.price, "The cost of the basket doesn't match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), "Success message appeared but shouldnt"

    def should_message_to_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), "Message did not disappear after adding product to basket"