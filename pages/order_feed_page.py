import allure
from pages.base_page import BasePage
from urls import Urls
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL


class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу "Лента заказов"')
    def open_order_feed_page(self):
        self.go_to_url(Urls.FEED_OF_ORDERS)

    @allure.step('Кликнуть первый заказ в "Ленте заказов" и дождаться открытия модального окна')
    def open_first_order_from_history(self):
        self.check_element_is_clickable(OFPL.FIRST_ORDER_HISTORY_ITEM)
        self.click_element(OFPL.FIRST_ORDER_HISTORY_ITEM)
        self.wait_for_visible_element(OFPL.ORDER_MODAL)
        self.wait_for_visible_element(OFPL.ORDER_MODAL_CONTENT_TITLE)
        
    @allure.step('Ожидание полной загрузки ленты заказов')
    def wait_for_order_feed_loaded(self):
        self.wait_for_page_loading(OFPL.ORDERS_TOTAL_LABEL)
        self.wait_for_visible_element(OFPL.FIRST_ORDER_HISTORY_ITEM)
        
    @allure.step('Открытие страницы "Лента заказов"')
    def go_to_order_feed(self):
        self.wait_for_visible_element(OFPL.ORDER_LIST_BUTTON)
        self.click_element(OFPL.ORDER_LIST_BUTTON)
        self.wait_for_visible_element(OFPL.ORDERS_TOTAL_VALUE)      
            
    @allure.step('Получение заголовка')    
    def get_title(self):
        return self.get_text_element(OFPL.ORDER_MODAL_CONTENT_TITLE)
    
    @allure.step('Получение списка номеров готовых заказов')
    def get_ready_order_numbers(self):
        order_elements = self.find_elements(OFPL.ORDERS_READY_NUMBERS)
        return [elem.text.strip() for elem in order_elements if elem.text.strip()]
    
    @allure.step('Проверка, что модальное окно заказа отображается')
    def is_order_modal_opened(self):
        return self.is_element_displayed(OFPL.ORDER_MODAL)
        
    @allure.step('Получение списка номеров заказов из ленты заказов')
    def get_order_numbers(self):
        self.wait_for_visible_element(OFPL.ORDER_NUMBERS_IN_FEED)
        order_elements = self.find_elements(OFPL.ORDER_NUMBERS_IN_FEED)
        order_numbers = []

        for elem in order_elements:
            full_text = elem.text.strip()
            if full_text.startswith('#'):
                number = full_text[1:8]  # обрезаем # и берём 7 цифр
                order_numbers.append(number)

        return order_numbers

    @allure.step('Получение числа выполненных заказов за всё время')
    def get_total_completed_orders_all_time(self):
        self.wait_for_visible_element(OFPL.ORDERS_TOTAL_VALUE)
        total_text = self.driver.find_element(*OFPL.ORDERS_TOTAL_VALUE).text
        return int(total_text.replace(' ', ''))
    
    @allure.step('Получение числа выполненных заказов за сегодня')
    def get_total_completed_orders_today(self):
        self.wait_for_visible_element(OFPL.ORDERS_TODAY_VALUE)
        total_text = self.driver.find_element(*OFPL.ORDERS_TODAY_VALUE).text
        return int(total_text.replace(' ', ''))
            
    @allure.step('Получение номеров заказов в разделе "В работе"')
    def get_orders_in_progress_numbers(self):
        self.wait_for_visible_element(OFPL.ORDERS_IN_PROGRESS_LIST)
        elements = self.driver.find_elements(*OFPL.ORDERS_IN_PROGRESS_LIST)
        return [el.text.strip() for el in elements]    
       
    @allure.step('Ожидание появления счётчика заказов за сегодня')
    def wait_for_orders_today_counter(self):
        self.wait_for_visible_element(OFPL.ORDERS_TODAY_VALUE)