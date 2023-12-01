from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.common.exceptions import NoSuchElementException


class Expenses(BasePage):
    page_url = 'https://new.cubux.net/team/301102/expense/details'

    def check_page_layout(self):
        self.driver.get('https://new.cubux.net/login')
        self.login_user('test3@test.com', 12345678)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Expenses"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Expenses"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="btn-icon _size2 '
                                                                                       '_extra-space"]')))
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _extra-space"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@class="hex-container _hex-'
                                                                                       'cont-size1"]')))
        layout_1 = self.driver.find_element(By.XPATH, '//*[@class="hex-container _hex-cont-size1"]')
        assert layout_1 is not None
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2"]').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@class="layout-list2"]')))
        layout_2 = self.driver.find_element(By.XPATH, '//*[@class="layout-list2"]')
        assert layout_2 is not None

    def check_add_operation(self, cost):
        self.driver.find_elements(By.CLASS_NAME, 'Button_link__5qRQJ')[5].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="rc-dialog-body"]'
                                                                               )))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[1].click()
        category = self.driver.find_elements(By.XPATH, '//*[@class="hex-text"]')[12]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(category))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[12].click()
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        date = self.driver.find_elements(By.XPATH, '//*[@class="hex-text"]')[2].text
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(cost)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-expense"]').click()
        self.driver.get('https://new.cubux.net/team/301091/expense/details')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        self.driver.implicitly_wait(10)
        expense_date = self.driver.find_elements(By.TAG_NAME, 'time')[0].text
        cost_info = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-expense"]')[0].text
        assert expense_date == date
        assert cost_info == f'- AFN {cost}'

    def check_change_operation(self, value):
        self.driver.find_elements(By.XPATH, '//*[@title="Edit"]')[0].click()
        self.driver.implicitly_wait(10)
        for i in range(0, 6):
            self.driver.find_element(By.XPATH, '//*[@class="currency "]').send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@class="currency "]').send_keys(value)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@value="{value}"]')))
        self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size4 color-expense"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        cost = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-expense"]')[0].text
        assert cost == f'- AFN {value}'

    def check_total_category_expenses_is_calculated(self, value_2):
        cost_1 = self.driver.find_elements(By.XPATH, '//*[@class="list-value _large"]')[0].text
        list_of_cost_1 = cost_1.split()
        value = list_of_cost_1[1]
        if ',' in value:
            new_value = value.replace(',', '')
        else:
            new_value = value
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ icon _size1 _extra-space color-expense"]')\
            .click()
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[4].click()
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[4].click()
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(value_2)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-expense"]').click()
        category_cost = int(new_value) + value_2
        category_cost_1 = str(category_cost)
        category_cost_2 = list(category_cost_1)
        if len(category_cost_2) > 3:
            category_cost_2.insert(-3, ',')
            category_cost_3 = ''.join(category_cost_2)
        else:
            category_cost_3 = category_cost_1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="list-value '
                                                                                              '_large"]')))
        cost_2 = self.driver.find_elements(By.XPATH, '//*[@class="list-value _large"]')[0].text
        assert cost_2 == f'AFN {category_cost_3}'

    def check_total_expenses_calculated(self):
        global new_list
        total_cost = self.driver.find_element(By.XPATH, '//*[@class="value"]').text
        all_categories = self.driver.find_elements(By.XPATH, '//*[@class="list-value _large"]')
        list_of_category_cost = []
        new_list = []
        for i in all_categories:
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
            list_2.insert(-3, ',')
            list_3 = ''.join(list_2)
        else:
            list_3 = total
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        assert total_cost == f'AFN {list_3}'

    def check_add_category(self):
        all_categories = self.driver.find_elements(By.XPATH, '//*[@class="list-first list-full"]')
        number_of_categories = len(all_categories)
        self.driver.find_element(By.CLASS_NAME, 'list-add').click()
        self.driver.find_element(By.XPATH, '//*[@placeholder="Category name"]').send_keys('test')
        self.driver.find_element(By.XPATH, '//*[@placeholder="0"]').send_keys(60)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-expense"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="list-first list-full"]')))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="list-first list-full"]')))
        new_all_categories = self.driver.find_elements(By.XPATH, '//*[@class="list-first list-full"]')
        new_number_of_categories = len(new_all_categories)
        assert new_number_of_categories == number_of_categories + 1

    def check_all_time_date_filter(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn-filter color-expense"]')[0].click()
        start_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[0].text
        end_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[1].text
        month_title = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        assert start_date == 'start'
        assert end_date == '— end'
        assert month_title == ''

    def check_year_date_filter(self):
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn-filter color-expense"]')[0].click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="sub-title"]')))
        current_date = datetime.datetime.now()
        current_year = current_date.year
        first_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[0].text
        second_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[1].text
        month_title = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        assert first_date == f'01/01/{current_year}'
        assert second_date == f'— 31/12/{current_year}'
        assert month_title == f'{current_year}'

    def check_month_date_filter(self):
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn-filter color-expense"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="sub-title"]'
                                                                                    )))
        date = datetime.datetime.now()
        current_month = date.strftime('%B %Y')
        current_date = date.strftime('%m/%Y')
        first_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[0].text
        second_date = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[1].text
        month_title = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        assert first_date == f'01/{current_date}'
        assert second_date == f'— 30/{current_date}'
        assert month_title == f'{current_month}'

    def check_delete_operation(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        all_transactions = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@title="Delete"]')))
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        all_transactions_2 = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        assert all_transactions_2 == (all_transactions - 1)
