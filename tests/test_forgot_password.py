import allure
from pages.forgot_password_page import ForgotPasswordPage as FP
from pages.login_page import LoginPage as LP
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as FPL
from urls import Urls
from helpers import GeneratorData as GD

class TestForgotPassword:
    
    @allure.title('Переод на станницу ввода почты для востановления пароля после нажатия на кнопку "Восстановить пароль"')
    def test_forgot_password_link_redirects_to_restore_page(self, driver):
        login = LP(driver)
        login.open_login_page()
        login.click_restore_password()
        current_url = login.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD
        
    @allure.title('Переход на старницу востановления парола после вводы почты')   
    def test_forgot_password_allows_email_input_and_submission(self,driver):
        fp = FP(driver)
        fp.open_forgot_password_page()
        fp.find_element(FPL.EMAIL_INPUT_FIELD)
        fp.click_element(FPL.EMAIL_INPUT_FIELD)
        fp.fill_email(GD.generate_email())
        fp.click_element(FPL.RESET_PASSWORD_BUTTON)
        fp.wait_for_visible_element(FPL.SAVE_PASSWORD_BUTTON)
        c_url = fp.get_current_url()
        assert c_url == Urls.RESET_PASSWORD
        
    @allure.title('Поле ввода пароля подсвечивается после нажатия на кнопку "Показать/скрыть пароль"')
    def test_password_field_highlights_on_toggle_visibility(self,driver):
        fp = FP(driver)
        fp.open_forgot_password_page()
        fp.find_element(FPL.EMAIL_INPUT_FIELD)
        fp.click_element(FPL.EMAIL_INPUT_FIELD)
        fp.fill_email(GD.generate_email())
        fp.click_element(FPL.RESET_PASSWORD_BUTTON)
        fp.wait_for_element(FPL.NEW_PASSWORD_INPUT_FIELD)
        fp.fill_password(GD.generate_password())
        fp.click_show_and_hide_button()
        assert fp.is_new_password_field_highlighted()
