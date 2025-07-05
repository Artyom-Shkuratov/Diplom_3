import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from urls import Urls
from locators.constructor_page_locators import ConstructorPageLocators as CPL


class ConstructorPage(BasePage):

    @allure.step('Открыть страницу "Конструктор"')
    def open_constructor_page(self):
        self.go_to_url(Urls.MAIN_PAGE)

    @allure.step('Создание заказа из конструктора')
    def create_burger_order(self):
        self.wait_for_visible_element(CPL.CRATOR_BUN_N_200i)
        self.drag_and_drop_bun()
        self.wait_for_visible_element(CPL.BURGER_BASKET)
        self.click_create_order()
    
    @allure.step('Ожидание загрузки страницы конструктора')
    def wait_constructor_page_loading(self):
        self.wait_for_page_loading(CPL.CREATE_ORDER_BUTTON)
            
        
    @allure.step('Клик по кнопке "Войти в аккаунт" на главной странице конструктора')
    def click_login_button_on_main_page(self):
        self.wait_for_visible_element(CPL.LOGIN_BUTTON)
        self.click_element(CPL.LOGIN_BUTTON)

        
    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click_element(CPL.CONSTRUCTOR_BUTTON)

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
        self.wait_until_visible(CPL.MODAL_ORDER_NUMBER)
        self.wait_for_non_placeholder_order_number(CPL.MODAL_ORDER_NUMBER)
        order_number = self.get_element_text(CPL.MODAL_ORDER_NUMBER)
        return f'0{order_number}'

    @allure.step('Проверка, что модальное окно ингредиента отображается')
    def is_ingredient_modal_window_displayed(self):
        return self.is_element_displayed(CPL.INGRIDIENT_MODAL_WINDOW)
    
    @allure.step('Ожидание отображения модального окна ингредиента')
    def wait_for_ingredient_modal_window(self):
        self.wait_for_visible_element(CPL.INGRIDIENT_MODAL_WINDOW)

    @allure.step('Проверка, что модальное окно ингредиента исчезло')
    def is_ingredient_modal_window_disappeared(self):
        return self.wait_until_element_disappears(CPL.INGRIDIENT_MODAL_WINDOW)

    @allure.step('Ожидание появления корректного номера заказа в модальном окне')
    def wait_for_order_number_to_appear(self):
        self.wait_until_visible(CPL.MODAL_ORDER_NUMBER)
        self.wait_for_non_placeholder_order_number(CPL.MODAL_ORDER_NUMBER)

    @allure.step('Получение значения счетчика  элемента ')
    def get_counter_number_bun(self):
        text = self.get_text_element(CPL.COUNTER_CRATOR_BUN_N_200i)
        return int(text) if text.isdigit() else 0

    @allure.step('Закрытие модального окна')
    def close_modal_window(self):
        self.click_element(CPL.MODAL_WINDOW_CLOSE_BUTTON)

    @allure.step('Закрытие окна заказа и переход в ленту заказов')
    def close_order_modal_and_go_to_feed(self):
        self.close_modal_window()
        self.click_element(CPL.ORDER_LIST_BUTTON)

    @allure.step('Закрытие окна заказа и переход в профиль')
    def close_order_modal_and_go_to_profile(self):
        self.close_modal_window()
        self.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переход в ленту заказов')
    def go_to_order_feed(self):
        self.click_element(CPL.ORDER_LIST_BUTTON)

    @allure.step('Переход в личный кабинет')
    def go_to_profile(self):
        self.click_element(CPL.PERSONAL_ACCOUNT_BUTTON)