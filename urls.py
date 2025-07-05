class Urls:
    # url раздела "Конструктор"
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    # url раздела "Авторизация"
    LOGIN_PAGE = MAIN_PAGE + "login"
    # url раздела "Восстановление пароля"
    FORGOT_PASSWORD = MAIN_PAGE + "forgot-password"
    # url раздела "Личный кабинет
    PERSONAL_ACCOUNT = MAIN_PAGE + "account/profile"
    # url  "Сбросить пароль"
    RESET_PASSWORD = MAIN_PAGE + "reset-password"
    # url раздела "История заказов"
    ORDERS_HISTORY = MAIN_PAGE + "account/order-history"
    # url раздела "Лента заказов"
    FEED_OF_ORDERS = MAIN_PAGE + "feed"
    
class ApiUrls:
    
    CREATE_USER = Urls.MAIN_PAGE + '/api/auth/register'
    DELETE_USER = Urls.MAIN_PAGE + '/api/auth/user'
    LOGIN_USER = Urls.MAIN_PAGE + '/api/auth/login'
    CREATE_ORDER = Urls.MAIN_PAGE + '/api/orders'
    