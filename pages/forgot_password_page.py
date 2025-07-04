import allure
from pages.base_page import BasePage
from urls import Urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as FP

class ForgotPasswordPage(BasePage):
    
    @allure.step('Открыть страницу "Восстановить пароль"')
    def open_forgot_password_page(self):
        self.go_to_url(Urls.FORGOT_PASSWORD)
        
    @allure.step('Заполнение поля "Email"')
    def fill_email(self,email):
        self.click_element(FP.EMAIL_INPUT_FIELD)
        self.fill_placeholder(FP.EMAIL_INPUT_FIELD, email)
        
    @allure.step('Заполнение поля "Пароль"')
    def fill_password(self,password):
        self.click_element(FP.NEW_PASSWORD_INPUT_FIELD)
        self.fill_placeholder(FP.NEW_PASSWORD_INPUT_FIELD, password)
        
    @allure.step('Клик по кнопке "Показать/скрыть пароль"')   
    def click_show_and_hide_button(self):
        self.click_element(FP.TOGGLE_PASSWORD_VISIBILITY_ICON)
    
    
    @allure.step('Проверка, что поле ввода нового пароля подсвечено')
    def is_new_password_field_highlighted(self):
        input_element = self.find_element(FP.NEW_PASSWORD_INPUT_FIELD)
        parent_div = input_element.find_element("xpath", "./..")
        return "input_status_active" in parent_div.get_attribute("class")
    