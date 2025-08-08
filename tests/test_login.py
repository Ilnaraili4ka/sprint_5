from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from helper import *
from locators import Locators


class TestSuccessLoginCredentials:

    def test_success_login_mine_site(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        login_with_data_credentials(driver)

        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))

    def test_success_login_personal_account(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.PERSONAL_AKK_BUTTON).click()
        login_with_data_credentials(driver)

        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))

    def test_success_login_register_form(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        login_with_data_credentials(driver)

        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))

    def test_success_login_recovery_password(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        login_with_data_credentials(driver)

        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))



