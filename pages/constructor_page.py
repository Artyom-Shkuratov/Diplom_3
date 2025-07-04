import allure
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from locators.constructor_page_locators import ConstructorPageLocators as CPL


class ConstructorPage(BasePage):

    @allure.step('Открыть страницу "Конструктор"')
    def open_constructor_page(self):
        self.go_to_url(Urls.MAIN_PAGE)
    
    @allure.step('Клик по кнопке "Создать заказ"')
    def click_create_order(self):
        self.click_element(CPL.CREATE_ORDER_BUTTON)
    
    @allure.step('Клик по булочке и появление окна ингридиента')
    def click_on_bun(self):
        self.click_element(CPL.CRATOR_BUN_N_200i)
        self.wait_for_visible_element(CPL.INGRIDIENT_MODAL_WINDOW)
     
    @allure.step('Перетаскивание ингридиента в корзину')   
    def drag_and_drop_bun(self):
        if self.browser_name == "chrome":
            self.drag_and_drop_element_in_chrome(CPL.CRATOR_BUN_N_200i, CPL.BASKET_CONTAINER)
        elif self.browser_name == 'firefox':
            self.drag_and_drop_element_in_firefox(CPL.CRATOR_BUN_N_200i, CPL.BASKET_CONTAINER)
    
    
    @allure.step('Получение номера заказа и добавление нуля в начало номера заказа')
    def get_order_number(self):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        wait.until(EC.visibility_of_element_located(CPL.MODAL_ORDER_NUMBER))
        element = self.driver.find_element(*CPL.MODAL_ORDER_NUMBER)
        wait.until(lambda driver: element.text != '9999' and element.text.strip() != '')
        order_number = element.text
        return f'0{order_number}'
    
    @allure.step('Ожидание появления корректного номера заказа в модальном окне')
    def wait_for_order_number_to_appear(self):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        wait.until(EC.visibility_of_element_located(CPL.MODAL_ORDER_NUMBER))
        element = self.driver.find_element(*CPL.MODAL_ORDER_NUMBER)
        wait.until(lambda driver: element.text.strip().isdigit() and element.text != '9999')


    @allure.step('Получение значения счетчика для элемента: {locator}')
    def get_counter_number(self, locator):
        text = self.get_text_element(locator)
        return int(text) if text.isdigit() else 0
    
    @allure.step('Закрытие модального окна')
    def close_modal_window(self):
        self.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)
        
   