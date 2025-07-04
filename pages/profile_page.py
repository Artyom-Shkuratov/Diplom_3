import allure
from pages.base_page import BasePage
from urls import Urls
from locators.profile_page_locators import ProfilePageLocators as PP


class ProfilePage(BasePage):
    @allure.step('Открыть страницу "Профиль"')
    def open_profile_page(self):
        self.go_to_url(Urls.PERSONAL_ACCOUNT)
    
    @allure.step('Открыть страницу "История заказов"')   
    def open_order_history_page(self):
        self.go_to_url(Urls.ORDERS_HISTORY)

        
    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders(self):
        self.click_element(PP.ORDER_HISTORY_BUTTON)
        
    @allure.step('Клик по кнопке "Выход"')
    def click_logout(self):
        self.click_element(PP.LOGOUT_BUTTON)
        
    @allure.step('Получение списка заказов')
    def get_orders_in_profile(self):
        return self.find_elemets(PP.ORDER_LIST_ITEMS)
    
    @allure.step('Получение номера последнего заказа из истории заказов')
    def get_last_order_number_from_history(self):
        order_items = self.get_orders_in_profile()
        if not order_items:
            raise AssertionError("История заказов пуста")
        first_item = order_items[0]
        number_elem = first_item.find_element(*PP.ORDER_NUMBER_IN_ITEM)
        return number_elem.text.strip()  