from selenium.webdriver.common.by import By


class Locators:

    NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")  # Поле "Имя" в форме регистрации
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")  # Поле "Email" в формах входа/регистрации
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")  # Поле "Пароль" в формах входа/регистрации
    LOGIN_TEXT_EMAIL_USER = (By.XPATH, "//div[label[contains(text(),'Логин')]]//input")  # Поле "Логин" в форме входа
    LOGIN_IN_BUTTON = (By.XPATH,
                "//button[contains(@class,'button_button__33qZ0') and text()='Войти']")  # Кнопка "Войти"
    REGISTER_BUTTON = (By.XPATH,
                "//button[contains(@class,'button_button__33qZ0') and text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_IN_AKK_BUTTON = (By.XPATH,
                "//button[contains(@class,'button_button_size_large__G21Vg')]")  # Кнопка "Войти в аккаунт"
    LOGOUT = (By.XPATH,
                 "//button[contains(@class,'Account_button__14Yp3') and text()='Выход']")  # Кнопка выхода из аккаунта
    REGISTER_LINK = (By.XPATH,
                "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH,
                "//a[@class='Auth_link__1fOlj' and text()='Войти']")  # Ссылка "Войти"
    RECOVER_PASSWORD_LINK = (By.XPATH,
                "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")  # Ссылка восстановления пароля
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH,
                          "//p[contains(@class,'AppHeader_header__linkText__3q_va') and text()='Конструктор']")  # Кнопка "Конструктор"
    PERSONAL_AKK_BUTTON = (By.XPATH,
                           "//p[contains(@class,'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    PLACE_AN_ORDER_BUTTON = (By.XPATH,
                             "//button[contains(@class,'button_button_size_large__G21Vg') and text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    PERSONAL_AKK_PROFILE = (By.XPATH, "//div[@class='Profile_profile__3dzvr']")  # Контейнер профиля в ЛК
    CONSTRUCTOR_BUN = (By.XPATH,
                "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")  # Секция конструктора бургеров
    BUNS_BUTTON = (By.XPATH, ".//span[contains(text(),'Булки')]")  # Кнопка категории "Булки"
    SAUCES_BUTTON = (By.XPATH, ".//span[contains(text(),'Соусы')]")  # Кнопка категории "Соусы"
    FILLINGS_BUTTON = (By.XPATH, ".//span[contains(text(),'Начинки')]")  # Кнопка категории "Начинки"
    BUNS_OF_TYPE = (By.XPATH,
                    "//h2[text()='Булки']/following-sibling::ul[contains(@class,'BurgerIngredients_ingredients__list__2A-mT')][1]")  # Секция булок
    SAUCES_OF_TYPE = (By.XPATH,
                      "//h2[text()='Соусы']/following-sibling::ul[contains(@class,'BurgerIngredients_ingredients__list__2A-mT')][1]")  # Секция соусов
    FILLINGS_OF_TYPE = (By.XPATH,
                        "//h2[text()='Начинки']/following-sibling::ul[contains(@class,'BurgerIngredients_ingredients__list__2A-mT')][1]")  # Секция начинок

    LOGIN_TEXT = (By.XPATH, "//h2[text()='Вход']")  # Заголовок формы входа
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение о некорректном пароле