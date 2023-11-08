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

    def login_user(self, email, password):
        self.driver.find_element(By.ID, 'loginform-username').send_keys(f'{email}')
        self.driver.find_element(By.ID, 'loginform-password').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@class="login100-form-btn button-loading"]').click()
