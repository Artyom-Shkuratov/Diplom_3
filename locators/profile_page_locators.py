from selenium.webdriver.common.by import By

class ProfilePageLocators:
    # Кнопка Профиль 
    PROFILE_BUTTON = (By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']")
    # Кнопка Личный Кабинет
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account' and contains(., 'Личный Кабинет')]"
    # Кнопка История заказов
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href='/account/order-history' and text()='История заказов']")
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    # Общий список заказов 
    ORDER_LIST_ITEMS = (By.CSS_SELECTOR, "ul.OrderHistory_list__KcLDB li")
    # Номер заказа
    ORDER_NUMBER_IN_ITEM = (By.CSS_SELECTOR, 'p.text_type_digits-default')
    

