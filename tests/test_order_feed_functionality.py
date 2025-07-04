import allure
from pages.constructor_page import ConstructorPage as CP
from pages.login_page import LoginPage as LP
from pages.order_feed_page import OrderFeedPage as OF
from pages.profile_page import ProfilePage as PP
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.profile_page_locators import ProfilePageLocators as PPL
from helpers import GeneratorData as GD


class TestOrderFeedFunctionality:
    
    
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_popup_opens_on_click(self, driver, register_user):
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_page_loading(CPL.PERSONAL_ACCOUNT_BUTTON)
        
        orders = OF(driver)
        orders.open_order_feed_page()
        orders.wait_for_page_loading(OFPL.ORDERS_TOTAL_LABEL)
        orders.open_first_order_from_history()
        assert orders.is_element_displayed(OFPL.ORDER_MODAL), f'Модальное окно заказа не открылось'
        assert orders.is_element_displayed(OFPL.ORDER_MODAL_CONTENT_TITLE)
    
    @allure.title('Заказы пользователя отображаются в ленте заказов')
    def test_user_orders_displayed_in_order_feed(self, driver, register_user):
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
        constructor_page.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        constructor_page.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)
        
        profile = PP(driver)
        profile.wait_for_page_loading(PPL.ORDER_HISTORY_BUTTON)
        profile.click_element(PPL.ORDER_HISTORY_BUTTON)
        profile.wait_for_visible_element(CPL.FIRST_ORDER_NUMBER)
        profile.get_text_element(CPL.FIRST_ORDER_NUMBER)
        profile.click_element(CPL.ORDER_LIST_BUTTON)
        constructor_page.wait_for_visible_element(OFPL.ORDERS_TOTAL_VALUE)
        
        order_feed = OF(driver)
        orders_list=order_feed.get_order_numbers()
        
        assert order_number in orders_list
      
        
    @allure.title('Общее количество выполненных заказов увеличивается при создании нового заказа')  
    def test_total_completed_orders_counter_increments_on_new_order(self,driver,register_user):
        
        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_page_loading(CPL.PERSONAL_ACCOUNT_BUTTON)
        
        feed_page=OF(driver)
        feed_page.click_element(CPL.ORDER_LIST_BUTTON)
        feed_page.wait_for_page_loading(OFPL.ORDERS_TOTAL_VALUE)
        total_completed_orders_before=feed_page.get_total_completed_orders_all_time()
        feed_page.click_element(CPL.CONSTRUCTOR_BUTTON)
        feed_page.click_element(CPL.CONSTRUCTOR_BUTTON)
        
        constructor_page = CP(driver)
        constructor_page.wait_for_visible_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.drag_and_drop_bun()
        constructor_page.wait_for_visible_element(CPL.BURGER_BASKET)
        constructor_page.click_create_order()
        constructor_page.wait_for_order_number_to_appear()
        constructor_page.wait_until_element_disappears(CPL.MODAL_WINDOW_OVERLAY)
        constructor_page.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        constructor_page.click_element(CPL.ORDER_LIST_BUTTON)
        
        feed_page.wait_for_page_loading(OFPL.ORDER_FEED_TITLE)
        total_completed_orders_after=feed_page.get_total_completed_orders_all_time()
        
        assert total_completed_orders_before < total_completed_orders_after, (
            f'Счётчик выполненных заказов за сегодня не увеличился.\n'
            f'Было: {total_completed_orders_before}, Стало: {total_completed_orders_after}'
        )
                                                                                
    @allure.title('Количество выполненных заказов за сегодня увеличивается при создании нового заказа')
    def test_today_completed_orders_counter_increments_on_new_order(self,driver,register_user):

        login_page = LP(driver)
        login_page.open_login_page()
        login_page.fill_email(register_user["email"])
        login_page.fill_password(register_user["password"])
        login_page.click_login_button()
        login_page.wait_for_page_loading(CPL.PERSONAL_ACCOUNT_BUTTON)

        feed_page = OF(driver)
        feed_page.click_element(CPL.ORDER_LIST_BUTTON)
        feed_page.wait_for_page_loading(OFPL.ORDERS_TODAY_LABEL)
        total_today_before = feed_page.get_total_completed_orders_today()

        feed_page.click_element(CPL.CONSTRUCTOR_BUTTON)
        feed_page.click_element(CPL.CONSTRUCTOR_BUTTON)

        constructor_page = CP(driver)
        constructor_page.wait_for_visible_element(CPL.CRATOR_BUN_N_200i)
        constructor_page.drag_and_drop_bun()
        constructor_page.wait_for_visible_element(CPL.BURGER_BASKET)
        constructor_page.click_create_order()
        constructor_page.wait_for_order_number_to_appear()
        constructor_page.wait_until_element_disappears(CPL.MODAL_WINDOW_OVERLAY)
        constructor_page.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        constructor_page.click_element(CPL.ORDER_LIST_BUTTON)

        feed_page.wait_for_page_loading(OFPL.ORDERS_TODAY_LABEL)
        feed_page.refresh_page_and_wait(OFPL.ORDERS_TODAY_LABEL)
        total_today_after = feed_page.get_total_completed_orders_today()

        assert total_today_before < total_today_after, (
            f'Счётчик выполненных заказов за сегодня не увеличился.\n'
            f'Было: {total_today_before}, Стало: {total_today_after}'
        )
        
    @allure.title('Номер заказа появляется в разделе "В работе"')
    def test_new_order_number_appears_in_in_progress_section(self,driver,register_user):
        
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
        
        constructor_page.wait_for_order_number_to_appear()
        order_number = constructor_page.get_order_number()

        constructor_page.wait_until_element_disappears(CPL.MODAL_WINDOW_OVERLAY)
        constructor_page.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        constructor_page.click_element(CPL.ORDER_LIST_BUTTON)

        feed_page = OF(driver)
        feed_page.wait_for_page_loading(OFPL.ORDERS_IN_PROGRESS_LIST)
        feed_page.wait_for_visible_element(OFPL.ORDERS_IN_PROGRESS_LIST)
        in_progress_orders = feed_page.get_orders_in_progress_numbers()

        assert order_number in in_progress_orders, (
            f'Номер заказа {order_number} не найден в разделе "В работе". '
            f'Список заказов в разделе: {in_progress_orders}'
        )