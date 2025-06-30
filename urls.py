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

    # адрес API для регистрации пользователя
    CREATE_USER = MAIN_PAGE + 'api/auth/register'
    # адрес API для удаления пользователя
    DELETE_USER = MAIN_PAGE + 'api/auth/user'
    # адрес API для авторизация пользователя
    LOGIN_USER = MAIN_PAGE + 'api/auth/login'