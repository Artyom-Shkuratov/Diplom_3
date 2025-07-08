from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    # Кнопка показать/скрыть пароль (иконка-глаз)
    PASSWORD_TOGGLE_ICON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action")
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
