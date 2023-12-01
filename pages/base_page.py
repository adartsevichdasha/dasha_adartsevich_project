from selenium.webdriver.common.by import By


class BasePage:
    page_url = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.page_url)
        self.driver.implicitly_wait(5)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
