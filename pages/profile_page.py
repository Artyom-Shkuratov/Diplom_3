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
        
    @allure.step('Переход в историю заказов из профиля')
    def go_to_order_history(self):
        self.wait_for_page_loading(PP.ORDER_HISTORY_BUTTON)
        self.click_element(PP.ORDER_HISTORY_BUTTON)
    
    
   
    @allure.step('Ожидание загрузки страницы профиля')
    def wait_for_profile_page_to_load(self):
        self.wait_for_visible_element(PP.LOGOUT_BUTTON)
        
    @allure.step('Ожидание загрузки истории заказов')
    def wait_for_orders_page_to_load(self):
        self.wait_for_visible_element(PP.ORDER_LIST_ITEMS)
    

    
    @allure.step('Переход из профиля в ленту заказов')
    def go_to_order_feed_from_profile(self):
        self.wait_for_page_loading(PP.ORDER_HISTORY_BUTTON)
        self.click_element(PP.ORDER_HISTORY_BUTTON) 
    
    
        
            
    @allure.step('Клик по кнопке "Выход"')
    def click_logout(self):
        self.click_element(PP.LOGOUT_BUTTON)
        
    @allure.step('Переход из профиля в ленту заказов')
    def go_to_order_feed_from_profile(self):
        self.wait_for_page_loading(PP.PROFILE_BUTTON)
        self.click_element(PP.PROFILE_BUTTON)
        self.click_element(PP.ORDER_HISTORY_BUTTON)
        self.wait_for_page_loading(PP.ORDER_LIST_ITEMS)
        
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
    
    