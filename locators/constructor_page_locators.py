from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    # Локаторы для хедера (верхней навигации)
    # Кнопка "Личный Кабинет" в шапке
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account' and contains(., 'Личный Кабинет')]"
    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = By.XPATH, ".//a[@href='/' and contains(., 'Конструктор')]"
    # Кнопка "Лента Заказов" в шапке
    ORDER_LIST_BUTTON = By.XPATH, ".//a[@href='/feed' and contains(., 'Лента Заказов')]"
    # Логотип сайта в шапке, ведущий на главную страницу
    MAIN_LOGO_HEADER = By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]//a[@href='/']"
    
    # Блок "Соберите бургер"
    # Заголовок "Соберите бургер" на главной странице
    LOGO_CREATE_BURGER = By.XPATH, ".//h1[text()='Соберите бургер']"
    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    # Ингредиент "Краторная булка N-200i"
    CRATOR_BUN_N_200i = By.XPATH, ".//p[text()='Краторная булка N-200i']/ancestor::a"
    # Счётчик количества для "Краторной булки"
    COUNTER_CRATOR_BUN_N_200i = By.XPATH, ".//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter_counter__num')]"
    # Элемент в корзине конструктора
    BURGER_BASKET = By.XPATH, ".//span[contains(@class, 'constructor-element__text')]"
    #Корзина    
    BASKET_CONTAINER = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Модальные окна: ингредиента и заказа
    INGRIDIENT_MODAL_WINDOW = By.CSS_SELECTOR, "div.Modal_modal__container__Wo2l_"
    # Заголовок модального окна ингредиента
    MODAL_INGREDIENT_TITLE = By.XPATH, "//h2[text()='Детали ингредиента']"
    # Кнопка закрытия модального окна
    MODAL_WINDOW_CLOSE_BUTTON = By.CSS_SELECTOR, "button.Modal_modal__close__TnseK"
    # Заголовок с номером заказа в модальном окне (при оформлении)
    MODAL_ORDER_OPENED = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and string-length(text()) > 0]"
    # Номер заказа в модальном окне (само число)
    MODAL_ORDER_NUMBER = By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m"
    # Номер первого заказа в истории
    FIRST_ORDER_NUMBER = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')][1]/p[1]"
    #Оверлей модального окна
    MODAL_WINDOW_OVERLAY = ("css selector", "div.Modal_modal_overlay__x2ZCr")