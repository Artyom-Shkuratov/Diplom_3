import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL
from locators.profile_page_locators import ProfilePageLocators as PPL
from locators.login_page_locators import LoginPageLocators as LPL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.browser_name = driver.capabilities.get("browserName", "").lower()
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Нажать кнопку "Лента заказов" в хедере и дождаться загрузки страницы')
    def click_button_feed_of_orders_in_header(self):
        self.click_element(CPL.ORDER_LIST_BUTTON)
        self.wait_for_visible_element(OFPL.ORDERS_TOTAL_VALUE)

    @allure.step('Нажать кнопку "Конструктор" в хедере и дождаться загрузки страницы')
    def click_button_constructor_in_header(self):
        self.click_element(CPL.CONSTRUCTOR_BUTTON)
        self.wait_for_visible_element(CPL.CRATOR_BUN_N_200i)

    
    @allure.step('Нажать кнопку "Личный кабинет" в хедере и дождаться загрузки профиля')
    def click_button_profile_in_header(self):
        self.wait.until(EC.invisibility_of_element_located(CPL.MODAL_WINDOW_OVERLAY))
        self.click_element(PPL.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_visible_element(PPL.ORDER_HISTORY_BUTTON)
            
    @allure.step('Получение текущей страницы')    
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переход на страницу {url}')
    def go_to_url(self, url):
        self.driver.get(url)
    
    @allure.step('Проверка наличия элемента')
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Ожидание видимости элемента')
    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_page_loading(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator))   
    
    @allure.step('Клик по элементу в chrome')
    def click_in_chrome(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    @allure.step('Клик по элементу в firefox')
    def click_in_firefox(self, locator):
        target = self.check_element_is_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
        ActionChains(self.driver).move_to_element(target).click().perform()
        
    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.wait_for_visible_element(CPL.ORDER_LIST_BUTTON)
        self.click_element(CPL.ORDER_LIST_BUTTON)
                
    @allure.step('Клик по элементу')
    def click_element(self, locator):
        try:
            if self.browser_name == "chrome":
                self.click_in_chrome(locator)
            elif self.browser_name == "firefox":
                self.click_in_firefox(locator)
        except ElementClickInterceptedException:
            element = self.wait_for_visible_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Ожидание кликабельности элемента и клик по нему')
    def wait_clikable_with_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step('Ожидание кликабельности элемента') 
    def wait_clikable_without_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
   
    @allure.step('Поиск элемента')   
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    
    @allure.step('Перетаскивание элемента в Chrome')
    def drag_and_drop_element_in_chrome(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    
    @allure.step('Перетаскивание элемента  в Firefox')
    def drag_and_drop_element_in_firefox(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        script = """
            function simulateDragDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();

                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragEnterEvent);

                var dragOverEvent = new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragOverEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)
        
        
    @allure.step('Скролл до элемента  и клик по нему')
    def scroll_and_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    
    @allure.step('Получение текста элемента')
    def get_text_element(self,locator):
        self.wait.until(lambda driver: driver.find_element(*locator).text.strip() != "")
        return self.driver.find_element(*locator).text.strip()
    
    @allure.step('Заполнение поля ')
    def fill_placeholder(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
        
    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))    
    
    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    
    @allure.step('Проверка отображения модального окна')
    def is_displayed_opened_modal_window(self,locator):
        return self.find_element(locator).is_displayed()

    
    @allure.step('Проверка закрытия модального окна')
    def is_closed_modal_window(self,locator):
        return not self.find_element(locator).is_displayed()
    
    @allure.step('Проверка отображения элемента')
    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except Exception:
            return False
     
    @allure.step('Ожидание, пока элемент исчезнет')
    def wait_until_element_disappears(self, locator, timeout=7):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
        
    
    @allure.step('Кликнуть по элементу через JavaScript')
    def click_element_by_js(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step('Ожидание видимости элемента')
    def wait_until_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.5)
        return wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Ожидание, пока текст элемента станет корректным')
    def wait_for_non_placeholder_order_number(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.5)
        element = self.driver.find_element(*locator)
        wait.until(lambda driver: element.text.strip().isdigit() and element.text != '9999')
        
