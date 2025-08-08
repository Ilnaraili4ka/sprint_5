import random
from faker import Faker
from data import Credentials
from locators import Locators


def generate_registration_user():
    new_user = f"ilnara_Zakirova_27_{random.randint(100, 999)}@yandex.ru"
    return new_user

faker = Faker()
def generate_registration_data():
    name = faker.name()
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, password

def login_with_data_credentials (driver):
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_IN_BUTTON).click()