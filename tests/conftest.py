import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.sign_up_page import SignUp
from pages.sign_in_page import SignIn
from pages.expenses_page import Expenses
from pages.credits_page import Credit
from pages.incomes_page import Incomes
from pages.transactions_page import Transactions


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def sign_up_page(driver):
    return SignUp(driver)


@pytest.fixture()
def sign_in_page(driver):
    return SignIn(driver)


@pytest.fixture()
def expenses(driver):
    return Expenses(driver)


@pytest.fixture()
def incomes(driver):
    return Incomes(driver)


@pytest.fixture()
def credit(driver):
    return Credit(driver)


@pytest.fixture()
def transactions(driver):
    return Transactions(driver)
