import allure
from pages.base_page import BasePage
from data import format_locators
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
        
    @allure.step('Ожидание отображения поля "Новый пароль"')
    def wait_for_new_password_input(self):
        self.wait_for_visible_element(FP.NEW_PASSWORD_INPUT_FIELD)
        
    @allure.step('Поиск поля ввода "Email" на странице восстановления пароля')
    def find_email_input_field(self):
        return self.find_element(FP.EMAIL_INPUT_FIELD)
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_reset_password_button(self):
        self.click_element(FP.RESET_PASSWORD_BUTTON)

    @allure.step('Ожидание отображения кнопки "Сохранить пароль"')
    def wait_for_save_password_button(self):
        self.wait_for_visible_element(FP.SAVE_PASSWORD_BUTTON)

    @allure.step('Клик по полю ввода "Email" на странице восстановления пароля')
    def click_email_input_field(self):
        self.click_element(FP.EMAIL_INPUT_FIELD)
        
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
        parent_div = input_element.find_element(*format_locators)
        
        classes = parent_div.get_attribute("class")
        print("PARENT DIV CLASSES:", classes)  # DEBUG
        
        return "input_status_active" in classes