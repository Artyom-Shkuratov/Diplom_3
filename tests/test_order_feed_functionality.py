import allure
from pages.constructor_page import ConstructorPage as CP
from pages.login_page import LoginPage as LP
from pages.order_feed_page import OrderFeedPage as OF
from pages.profile_page import ProfilePage as PP


class TestOrderFeedFunctionality:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_popup_opens_on_click(self, driver, register_user):
        login_page = LP(driver)
        login_page.login_as_user(register_user)

        orders = OF(driver)
        orders.open_order_feed_page()
        orders.wait_for_order_feed_loaded()
        orders.open_first_order_from_history()

        assert orders.is_order_modal_opened(), 'Модальное окно заказа не открылось'


    @allure.title('Заказы пользователя отображаются в ленте заказов')
    def test_user_orders_displayed_in_order_feed(self, driver, register_user):
        login_page = LP(driver)
        login_page.login_as_user(register_user)

        constructor_page = CP(driver)
        constructor_page.create_burger_order()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal_and_go_to_profile()

        profile = PP(driver)
        profile.go_to_order_history()
        profile.go_to_order_feed_from_profile()

        feed = OF(driver)
        assert order_number in feed.get_order_numbers()


    @allure.title('Общее количество выполненных заказов увеличивается при создании нового заказа')
    def test_total_completed_orders_counter_increments_on_new_order(self, driver, register_user):
        
        login_page = LP(driver)
        login_page.login_as_user(register_user)
        login_page.click_order_feed_button()

        feed = OF(driver)
        feed.go_to_order_feed()
        before = feed.get_total_completed_orders_all_time()

        constructor_page = CP(driver)
        constructor_page.go_to_constructor()
        constructor_page.create_burger_order()
        constructor_page.close_order_modal_and_go_to_feed()
        
        feed.go_to_order_feed()
        after = feed.get_total_completed_orders_all_time()
        assert before < after, f'Было: {before}, Стало: {after}'


    @allure.title('Количество выполненных заказов за сегодня увеличивается при создании нового заказа')
    def test_today_completed_orders_counter_increments_on_new_order(self, driver, register_user):
        login_page = LP(driver)
        login_page.login_as_user(register_user)

        feed = OF(driver)
        feed.go_to_order_feed()
        feed.wait_for_orders_today_counter()
        before = feed.get_total_completed_orders_today()

        constructor_page = CP(driver)
        constructor_page.go_to_constructor()
        constructor_page.create_burger_order()
        constructor_page.close_modal_window()
        feed = OF(driver)
        
        feed.go_to_order_feed()
        after = feed.get_total_completed_orders_today()
        feed.go_to_order_feed()
        
        feed.wait_for_orders_today_counter()
        after = feed.get_total_completed_orders_today()
        assert before < after, f'Было: {before}, Стало: {after}'


    @allure.title('Номер заказа появляется в разделе "В работе"')
    def test_new_order_number_appears_in_in_progress_section(self, driver, register_user):
        login_page = LP(driver)
        login_page.login_as_user(register_user)

        constructor_page = CP(driver)
        constructor_page.create_burger_order()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal_and_go_to_feed()
        constructor_page.go_to_order_feed
        feed = OF(driver)
        
        assert order_number in feed.get_orders_in_progress_numbers()
