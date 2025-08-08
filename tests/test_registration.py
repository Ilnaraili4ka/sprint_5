from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from helper import *
from locators import Locators
from data import *


class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):
        name, password = generate_registration_data()
        email = generate_registration_user()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.LOGIN_TEXT, "Вход"))
        current_url = driver.current_url
        assert current_url == Curl.site_login


    def test_failed_registration_password_5_symbol(self, driver):
        name = generate_registration_data()
        email = generate_registration_user()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password_5_symbol)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD))

