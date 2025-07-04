import allure
from pages.login_page import LoginPage as LP
from pages.constructor_page import ConstructorPage as CP
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.profile_page_locators import ProfilePageLocators as PPL
from locators.login_page_locators import LoginPageLocators as LPL
from urls import Urls


class TestProfile:
    
    @allure.title('Переход на страницу профиля для залогиненного пользователя')
    def test_should_navigate_to_profile_page_from_main_page(self, driver, register_user):
        
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_element(CPL.PERSONAL_ACCOUNT_BUTTON)

        profile = CP(driver)
        profile.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)
        profile.wait_for_page_loading(PPL.PROFILE_BUTTON)
        
        current_url = profile.get_current_url()
        assert current_url == Urls.PERSONAL_ACCOUNT
        
        
    @allure.title('Переход на страницу истории заказов')    
    def test_should_open_order_history_from_profile_page(self,driver,register_user):
        
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_element(CPL.PERSONAL_ACCOUNT_BUTTON)

        profile = CP(driver)
        profile.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)
        profile.wait_for_page_loading(PPL.PROFILE_BUTTON)
        profile.click_element(PPL.ORDER_HISTORY_BUTTON)
        
        current_url = profile.get_current_url()
        assert current_url == Urls.ORDERS_HISTORY 
        
        
        
    @allure.title('Выход из профиля')
    def test_should_logout_user_from_profile(self,driver,register_user):
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_element(CPL.PERSONAL_ACCOUNT_BUTTON)

        profile = CP(driver)
        profile.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)
        profile.wait_for_page_loading(PPL.PROFILE_BUTTON)
        profile.click_element(PPL.LOGOUT_BUTTON)
        profile.wait_for_page_loading(LPL.LOGIN_BUTTON)
        
        current_url = profile.get_current_url()
        assert current_url == Urls.LOGIN_PAGE
        assert login_page.is_element_displayed(LPL.LOGIN_BUTTON)
        