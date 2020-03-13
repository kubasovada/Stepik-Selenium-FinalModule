from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password="GhbdtnCntgbr123"):
        email_f = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_f.clear()
        email_f.send_keys(email)
        pass_f1 = self.browser.find_element(*LoginPageLocators.PASS_FIELD1)
        pass_f1.clear()
        pass_f1.send_keys(password)
        pass_f2 = self.browser.find_element(*LoginPageLocators.PASS_FIELD2)
        pass_f2.clear()
        pass_f2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()



