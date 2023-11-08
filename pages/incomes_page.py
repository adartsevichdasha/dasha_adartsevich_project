from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Incomes(BasePage):
    page_url = 'https://new.cubux.net/team/301091/income/details'

    def check_page_layout(self):
        self.driver.get('https://new.cubux.net/login')
        self.login_user('test3@test.com', 12345678)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Incomes"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Incomes"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="btn-icon _size2 '
                                                                                       '_extra-space"]')))
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _extra-space"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="hex-container '
                                                                                       '_hex-cont-size1"]')))
        layout_1 = self.driver.find_element(By.XPATH, '//*[@class="hex-container _hex-cont-size1"]')
        assert layout_1 is not None
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="layout-list2"]')))
        layout_2 = self.driver.find_element(By.XPATH, '//*[@class="layout-list2"]')
        assert layout_2 is not None

    def check_add_category(self, category_name):
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _extra-space"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-btn"]')))
        all_categories = self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')
        number_of_categories = len(all_categories)
        self.driver.implicitly_wait(10)
        button = self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[1]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[1].click()
        self.driver.find_element(By.XPATH, '//*[@placeholder="Category name"]').send_keys(category_name)
        self.driver.find_element(By.XPATH, '//*[@placeholder="0"]').send_keys(50)
        self.driver.find_element(By.XPATH,
                                     '//*[@class="Button_button__QS2NC btn _inp-size4 color-income"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-name HexPage_largeOnly__IWJzX"]')))
        new_all_categories = self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')
        new_number_of_categories = len(new_all_categories)
        assert new_number_of_categories == number_of_categories + 1

    def check_add_operation(self, sum):
        category_cost = self.driver.find_elements(By.XPATH, '//*[@class="hex-value _hex-value-size2"]')[0].text
        category_cost_list = category_cost.split()
        cost = category_cost_list[1]
        if ',' in cost:
            new_cost = int(cost.replace(',', ''))
        else:
            new_cost = int(cost)
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="Button_link_'
                                                                                              '_5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[0].click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[1].click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(sum)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-income"]').click()
        self.driver.get('https://new.cubux.net/team/301091/income/hex')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-btn"]')))
        updated_category_cost = int(new_cost) + sum
        category_cost_1 = str(updated_category_cost)
        category_cost_2 = list(category_cost_1)
        if len(category_cost_2) > 3:
            new_category_cost = category_cost_2.insert(-3, ',')
        else:
            new_category_cost = category_cost_2
        category_cost_3 = ''.join(new_category_cost)
        cost_2 = self.driver.find_elements(By.XPATH, '//*[@class="hex-value _hex-value-size2"]')[0].text
        assert cost_2 == f'AFN {category_cost_3}'

    def check_change_operation(self, value):
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2"]').click()
        self.driver.find_elements(By.XPATH, '//*[@title="Edit"]')[0].click()
        for i in range(0, 6):
            self.driver.find_element(By.XPATH, '//*[@class="currency "]').send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@class="currency "]').send_keys(value)
        self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size4 color-income"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="list-value '
                                                                                              'color-income"]')))
        self.driver.implicitly_wait(10)
        cost = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-income"]')[0].text
        assert cost == f'+ AFN {value}'

    def check_total_incomes_calculated(self):
        global new_list
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        button = self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _extra-space"]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _extra-space"]').click()
        total_income_cost = self.driver.find_element(By.XPATH, '//*[@class="value"]').text
        all_income_categories = self.driver.find_elements(By.XPATH, '//*[@class="hex-value _hex-value-size2"]')
        list_of_category_cost = []
        new_list = []
        for i in all_income_categories:
            category_cost = i.text
            cost = category_cost.split()
            if len(cost) != 0:
                list_of_category_cost.append(cost[1])
        for number in list_of_category_cost:
            if ',' in number:
                new_number = number.replace(',', '')
                new_list.append(int(new_number))
            else:
                new_list.append(int(number))
        total = sum(new_list)
        list_2 = list(str(total))
        if len(list_2) > 3:
            new_category_cost = list_2.insert(-3, ',')
        else:
            new_category_cost = list_2
        list_3 = ''.join(new_category_cost)
        assert total_income_cost == f'AFN {list_3}'

    def check_delete_operation(self):
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        all_transactions = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_elements(By.XPATH, '//*[@title="Delete"]')[0].click()
        confirm_button = self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(confirm_button))
        self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0].click()
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        all_transactions_2 = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        assert all_transactions_2 == (all_transactions - 1)
