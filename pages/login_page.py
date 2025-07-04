import allure
from pages.base_page import BasePage
from urls import Urls
from locators.login_page_locators import LoginPageLocators as LP
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as FP
from locators.constructor_page_locators import ConstructorPageLocators as CP

class LoginPage(BasePage):
    @allure.step('Открыть страницу "Вход"')
    def open_login_page(self):
        self.go_to_url(Urls.LOGIN_PAGE)
    
    @allure.step('Заполнение поля "Email"')   
    def fill_email(self, email):
        self.wait_for_visible_element(LP.EMAIL_INPUT)
        self.click_element(LP.EMAIL_INPUT)
        self.fill_placeholder(LP.EMAIL_INPUT, email)
    
    @allure.step('Заполнение поля "Пароль"')   
    def fill_password(self,password):
        self.wait_for_visible_element(LP.PASSWORD_INPUT)
        self.click_element(LP.PASSWORD_INPUT)
        self.fill_placeholder(LP.PASSWORD_INPUT, password)     
    
    @allure.step('Клик по кнопке "Вход"')
    def click_login_button(self):
        self.wait_clikable_with_click(LP.LOGIN_BUTTON)
    
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_restore_password(self):
        self.click_element(LP.FORGOT_PASSWORD_LINK)
        
    @allure.step('Авторизация')   
    def authorization(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()
        self.wait_for_page_loading(CP.CREATE_ORDER_BUTTON)