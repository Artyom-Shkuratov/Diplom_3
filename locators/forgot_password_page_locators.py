from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    # Поле ввода Email
    EMAIL_INPUT_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input"
    # Кнопка "Восстановить"
    RESET_PASSWORD_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    # Поле ввода нового пароля
    NEW_PASSWORD_INPUT_FIELD = By.XPATH, ".//div[contains(@class, 'input')][.//label[text()='Пароль']]//input"
    # Поле "Введите код из письма"
    CONFIRMATION_CODE_INPUT_FIELD = By.XPATH, ".//label[text()='Введите код из письма']/following-sibling::input"
    # Иконка-глаз (показать/скрыть пароль) 
    TOGGLE_PASSWORD_VISIBILITY_ICON = By.CSS_SELECTOR, "div.input__icon.input__icon-action"
    # Кнопка "Сохранить" 
    SAVE_PASSWORD_BUTTON = By.XPATH, ".//button[text()='Сохранить']"
    