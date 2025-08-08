from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from helper import *
from locators import Locators
from curl import *


class TestTransferToPersonalAccount:

    def test_transfer_personal_account_click_constructor(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        login_with_data_credentials(driver)
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.PERSONAL_AKK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_AKK_PROFILE))
        assert driver.current_url == Curl.site_profile

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))

    def test_transfer_personal_account_click_logo(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.LOGIN_IN_AKK_BUTTON).click()
        login_with_data_credentials(driver)
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.PERSONAL_AKK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_AKK_PROFILE))
        assert driver.current_url == Curl.site_profile

        driver.find_element(*Locators.LOGO).click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.PLACE_AN_ORDER_BUTTON, "Оформить заказ"))

