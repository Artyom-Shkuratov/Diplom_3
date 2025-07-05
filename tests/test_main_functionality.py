import allure
from pages.login_page import LoginPage as LP
from pages.constructor_page import ConstructorPage as CP
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from urls import Urls



class TestBasicFunctionality:
    
    @allure.title('Переход на конструктор после нажатия на кнопку "Конструктор"')
    def test_should_navigate_to_constructor_from_header(self, driver):
        login = LP(driver)
        login.open_login_page()
        login.click_button_constructor_in_header()
        assert login.get_current_url() == Urls.MAIN_PAGE

    @allure.title('Переход на ленту заказов после нажатия на кнопку "Лента заказов"')
    def test_should_navigate_to_feed_from_header(self, driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_feed_of_orders_in_header()
        assert constructor_page.get_current_url() == Urls.FEED_OF_ORDERS

    @allure.title('Открытие модального окна ингредиента после нажатия на ингредиент')
    def test_should_open_ingredient_modal_on_click(self, driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_bun()
        assert constructor_page.is_ingredient_modal_window_displayed()

    @allure.title('Закрытие модального окна ингредиента после нажатия на крестик')
    def test_should_close_ingredient_modal_on_click_close(self, driver):
        constructor_page = CP(driver)
    
        constructor_page.open_constructor_page()
        constructor_page.click_on_bun()
        constructor_page.wait_for_ingredient_modal_window()
        constructor_page.close_modal_window()
        assert constructor_page.is_ingredient_modal_window_disappeared()



    @allure.title('Добавление ингредиента в корзину')
    def test_should_increase_counter_when_ingredient_added(self, driver):
        constructor_page = CP(driver)
        constructor_page.open_constructor_page()
        counter_before = constructor_page.get_counter_number_bun()
        constructor_page.drag_and_drop_bun()
        counter_after = constructor_page.get_counter_number_bun()
        assert counter_after > counter_before


    @allure.title('Создание заказа авторизованным пользователем')
    def test_logged_in_user_can_create_order(self, driver, register_user):
        login_page = LP(driver)
        login_page.login_as_user(register_user)

        constructor_page = CP(driver)
        constructor_page.create_burger_order()

        assert constructor_page.get_order_number() != '09999'