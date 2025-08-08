import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from helper import *
from locators import Locators


class TestLogoutFromPersonalAccount:

    def test_logout_from_personal_account(self, driver):
        #регистрация
        name, password = generate_registration_data()
        email = generate_registration_user()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        #вход в аккаунт
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_IN_BUTTON)
        )
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_IN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.PERSONAL_AKK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_AKK_PROFILE))
        assert driver.current_url == Curl.site_profile

        # выход из аккаунта
        driver.find_element(*Locators.LOGOUT).click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.LOGIN_TEXT, "Вход"))
        assert driver.current_url == Curl.site_login

