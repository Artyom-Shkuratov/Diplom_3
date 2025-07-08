from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    # Заголовок страницы "Лента заказов"
    ORDER_FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    # Надпись "Выполнено за все время:"
    ORDERS_TOTAL_LABEL = (By.XPATH, ".//p[text()='Выполнено за все время:']")
    # Кнопка "Лента Заказов" в шапке
    ORDER_LIST_BUTTON = By.XPATH, ".//a[@href='/feed' and contains(., 'Лента Заказов')]"
    # Значение общего количества выполненных заказов 
    ORDERS_TOTAL_VALUE = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text_type_digits-large")
    # Надпись "Выполнено за сегодня:"
    ORDERS_TODAY_LABEL = (By.XPATH, ".//p[text()='Выполнено за сегодня:']")
    # Значение количества выполненных заказов за сегодня 
    ORDERS_TODAY_VALUE = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    # Подзаголовок "Готовы:" перед списком заказов со статусом "готов"
    ORDERS_READY_LABEL = (By.XPATH, ".//p[text()='Готовы:']")
    # Подзаголовок "В работе:" перед списком заказов в процессе
    ORDERS_IN_PROGRESS_LABEL = (By.XPATH, ".//p[text()='В работе:']")
    # Список заказов со статусом "готов" 
    ORDERS_READY_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")
    # Список заказов в работе 
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderList__cBvyi')][1]/li")
    # Сообщение "Все текущие заказы готовы!", если список готовых заказов пуст
    ALL_ORDERS_READY_TEXT = (By.XPATH, ".//li[text()='Все текущие заказы готовы!']")
    # Список готовых заказов (по номерам)
    ORDERS_READY_NUMBERS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")
    #Первый заказ в списке 
    FIRST_ORDER_HISTORY_ITEM = (By.CSS_SELECTOR, 'li.OrderHistory_listItem__2x95r a.OrderHistory_link__1iNby')
    # Модальное окно с информацией о заказе
    ORDER_MODAL = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    # Заголовок модального окна
    ORDER_MODAL_CONTENT_TITLE = (By.XPATH, '//p[text()="Cостав"]')
    # Список номеров заказов в ленте закзаов
    ORDER_NUMBERS_IN_FEED = By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6"