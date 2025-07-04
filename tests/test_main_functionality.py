import allure
from pages.login_page import LoginPage as LP
from pages.constructor_page import ConstructorPage as CP
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from urls import Urls



class TestBasicFunctionality:
    
    @allure.title('Переход на конструктор после нажатия на кнопку "Конструктор"')
    def test_should_navigate_to_constructor_from_header(self,driver):
        login = LP(driver)
        login.open_login_page()
        login.find_element(CPL.CONSTRUCTOR_BUTTON)
        login.click_element(CPL.CONSTRUCTOR_BUTTON)
        current_url = login.get_current_url()
        assert current_url == Urls.MAIN_PAGE
        
    
    @allure.title('Переход на ленту заказов после нажатия на кнопку "Лента заказов"')
    def test_should_navigate_to_feed_from_header(self,driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.find_element(CPL.ORDER_LIST_BUTTON)
        constructor_page.click_element(CPL.ORDER_LIST_BUTTON)
        constructor_page.wait_for_page_loading(OFPL.FIRST_ORDER_HISTORY_ITEM)
        current_url = constructor_page.get_current_url()
        assert constructor_page.is_element_displayed(OFPL.FIRST_ORDER_HISTORY_ITEM)
        assert current_url == Urls.FEED_OF_ORDERS
    
    @allure.title('Открытие модального окна ингридиента после нажатия на ингридиент')
    def test_should_open_ingredient_modal_on_click(self,driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.find_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.click_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.wait_for_visible_element(CPL.INGRIDIENT_MODAL_WINDOW)
        assert constructor_page.is_element_displayed(CPL.INGRIDIENT_MODAL_WINDOW)
     
    
    @allure.title('Закрытие модального окна ингридиента после нажатия на крестик')    
    def test_should_open_ingredient_modal_on_click(self,driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.find_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.click_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.wait_for_visible_element(CPL.INGRIDIENT_MODAL_WINDOW) 
        constructor_page.check_element_is_clickable(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        constructor_page.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        assert constructor_page.wait_until_element_disappears(CPL.INGRIDIENT_MODAL_WINDOW)
      
    
    @allure.title('Добавление ингридиента в корзину')
    def test_should_increase_counter_when_ingredient_added(self,driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.find_element(CPL.CRATOR_BUN_N_200i)
        counter_bun_before = constructor_page.get_counter_number(CPL.COUNTER_CRATOR_BUN_N_200i)
        constructor_page.drag_and_drop_bun()
        constructor_page.wait_for_visible_element(CPL.BURGER_BASKET)
        counter_bun_after = constructor_page.get_counter_number(CPL.COUNTER_CRATOR_BUN_N_200i)
        assert counter_bun_after > counter_bun_before 
        assert constructor_page.is_element_displayed(CPL.BURGER_BASKET)
    
    @allure.title('Создание заказа авторизированным пользователем')
    def test_logged_in_user_can_create_order(self,driver,register_user):
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_page_loading(CPL.PERSONAL_ACCOUNT_BUTTON)
        
        constructor_page = CP(driver)
        constructor_page.wait_for_visible_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.drag_and_drop_bun()
        constructor_page.wait_for_visible_element(CPL.BURGER_BASKET)
        constructor_page.click_create_order()
        order_number=constructor_page.get_order_number()
        constructor_page.check_element_is_clickable(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        assert constructor_page.is_element_displayed(CPL.MODAL_ORDER_NUMBER),'Окно заказа не открылось'
        assert order_number != 9999
        
        
        
        
        
    