from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from helper import *
from locators import Locators
from selenium.webdriver.common.by import By

class TestTransferToSection:

    def test_buns_section_activation(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        active_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BUNS_OF_TYPE))
        assert active_tab.is_displayed()

    def test_sauces_section_activation(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        active_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SAUCES_OF_TYPE))
        assert active_tab.is_displayed()

    def test_fillings_section_activation(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUN))
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        active_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.FILLINGS_OF_TYPE))
        assert active_tab.is_displayed()