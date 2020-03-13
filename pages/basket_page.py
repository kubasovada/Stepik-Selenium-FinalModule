from .base_page import BasePage
from .locators import BasePageLocators, BasketPagelocators

class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert not self.is_element_present(*BasketPagelocators.PRODUCT_LIST), "There are items in basket but shouldnt be"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPagelocators.EMPTY_BASKET), "Empty basket text is not presented"
