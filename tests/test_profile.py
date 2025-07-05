import allure
from pages.login_page import LoginPage as LP
from pages.profile_page import ProfilePage as PP
from pages.constructor_page import ConstructorPage as CP
from urls import Urls


class TestProfile:

    @allure.title('Переход на страницу профиля для залогиненного пользователя')
    def test_should_navigate_to_profile_page_from_main_page(self, driver, register_user):
        login_page = LP(driver)
        profile_page = PP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        profile_page.click_button_profile_in_header()
        profile_page.wait_for_profile_page_to_load()
        current_url = profile_page.get_current_url()
        
        assert current_url == Urls.PERSONAL_ACCOUNT, f'Current url: {current_url}'

    @allure.title('Переход на страницу истории заказов')
    def test_should_open_order_history_from_profile_page(self, driver, register_user):
        login_page = LP(driver)
        profile_page = PP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        profile_page.click_button_profile_in_header()
        profile_page.wait_for_profile_page_to_load()
        profile_page.go_to_order_history()
       
        current_url = profile_page.get_current_url()
        assert current_url == Urls.ORDERS_HISTORY

    @allure.title('Выход из профиля')
    def test_should_logout_user_from_profile(self, driver, register_user):
        login_page = LP(driver)
        profile_page = PP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        profile_page.click_button_profile_in_header()
        profile_page.wait_for_profile_page_to_load()
        profile_page.click_logout()
        login_page.wait_login_page_loading()
        
        current_url = login_page.get_current_url()
        assert current_url == Urls.LOGIN_PAGE

  
       