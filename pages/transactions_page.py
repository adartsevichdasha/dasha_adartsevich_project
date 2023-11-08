from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Transactions(BasePage):
    page_url = 'https://new.cubux.net/team/301091/balance'

    def check_categories_displayed_in_transactions(self):
        self.driver.get('https://new.cubux.net/login')
        self.login_user('test3@test.com', 12345678)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="hex-'
                                                                                         'index"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Incomes"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="Button_button__'
                                                                                   'QS2NC btn-filter color-income"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn-filter color-income"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'time')))
        self.driver.find_elements(By.XPATH, '//*[@class="list"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_transactions = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        self.driver.find_element(By.XPATH, '//*[@title="Balance"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        self.driver.find_element(By.XPATH, '//*[@class="rc-select rc-select-multiple rc-select-show-search"]').click()
        self.driver.find_elements(By.XPATH, '//*[@class="rc-select-item rc-select-item-option"]')[3].click()
        self.driver.find_element(By.XPATH, '//*[@placeholder="Search"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        sleep(5)
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_category_transactions = len(self.driver.find_elements(By.XPATH, '//*[@class="list-value color-income '
                                                                                'BalancePage-table_colAmount__r1eLm"]'))
        assert list_of_category_transactions == list_of_transactions
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="rc-select-'
                                                                                   'selection-item-remove"]')))
        self.driver.find_element(By.XPATH, '//*[@class="rc-select-selection-item-remove"]').click()

    def check_create_transfer_transaction(self, tr_sum):
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-calendar"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="list-value color-calendar BalancePage-table_colAmount__r1eLm"]')))
        all_transfer_transactions = (
            self.driver.find_elements(
                By.XPATH, '//*[@class="list-value color-calendar BalancePage-table_colAmount__r1eLm"]'))
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ icon _size1 color-balance _space"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class='
                                                                                              '"hex-btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-'
                                                                                              'btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[4].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-'
                                                                                              'btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-'
                                                                                              'btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[5].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="hex-'
                                                                                              'btn"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="hex-btn"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@name="amount"]').send_keys(tr_sum)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-balance"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="list-value color-calendar BalancePage-table_colAmount__r1eLm"]')))
        transaction = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-calendar '
                                                          'BalancePage-table_colAmount__r1eLm"]')[0].text
        updated_transfer_transactions = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-calendar '
                                                                            'BalancePage-table_colAmount__r1eLm"]')
        assert transaction == f'⇒ AFN {tr_sum}'
        assert len(updated_transfer_transactions) == len(all_transfer_transactions) + 1

    def create_unconfirmed_expenses_transaction(self, cost):
        unconfirmed_expense_transactions = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-expense"]')
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ icon _size1 color-expense _space"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[12].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(cost)
        self.driver.find_elements(By.XPATH, '//*[@class="checkbox"]')[-1].click()
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-expense"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="list-value color-expense"]')))
        sleep(3)
        updated_unconfirmed_expense_transactions = self.driver.find_elements(By.XPATH, '//*[@class="list-value '
                                                                                       'color-expense"]')
        title = self.driver.find_element(By.XPATH, '//*[@class="sub-title"]').text
        assert title is not None
        assert title == 'Unconfirmed transactions'
        expense_transaction = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-expense"]')[-1].text
        assert expense_transaction == f'- AFN {cost}'
        assert len(updated_unconfirmed_expense_transactions) == len(unconfirmed_expense_transactions) + 1

    def create_unconfirmed_incomes_transaction(self, cost):
        unconfirmed_income_transactions = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-income"]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="Button_link__5qRQJ icon _size1 color-income _extra-space"]')))
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ icon _size1 color-income '
                                           '_extra-space"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[4].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-center"]')[2].click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(cost)
        self.driver.find_elements(By.XPATH, '//*[@class="checkbox"]')[-1].click()
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn _inp-size4 color-income"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="list-value color-income"]')))
        sleep(3)
        updated_unconfirmed_transactions = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-income"]')
        title = self.driver.find_element(By.XPATH, '//*[@class="sub-title"]').text
        assert title is not None
        assert title == 'Unconfirmed transactions'
        expense_transaction = self.driver.find_elements(By.XPATH, '//*[@class="list-value color-income"]')[-1].text
        assert expense_transaction == f'+ AFN {cost}'
        assert len(updated_unconfirmed_transactions) == len(unconfirmed_income_transactions) + 1

    def confirm_unconfirmed_transaction(self):
        self.driver.find_elements(By.XPATH, '//*[@class="category-path"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn-icon _size2 '
                                                                                   '_back"]')))
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _back"]').click()
        title = self.driver.find_element(By.XPATH, '//*[@class="title"]').text
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        list_of_transactions = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        self.driver.find_element(By.XPATH, '//*[@title="Balance"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ btn-icon _size2"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn color-warn"]')))
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn '
                                           'color-warn"]').click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                 '//*[@class="rc-dialog-content"]')))
        if title == 'Expenses':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Expenses"]'
                                                                                       '')))
            self.driver.find_element(By.XPATH, '//*[@title="Expenses"]').click()
        else:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Incomes"]')))
            self.driver.find_element(By.XPATH, '//*[@title="Incomes"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        sleep(5)
        list_of_transactions_updated = len(self.driver.find_elements(By.TAG_NAME, 'time'))
        assert list_of_transactions_updated == list_of_transactions + 1

    def check_delete_bulk_transactions(self):
        self.driver.find_element(By.XPATH, '//*[@title="Balance"]').click()
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_all_transaction = self.driver.find_elements(By.XPATH, '//*[@type="checkbox"]')[1:]
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_elements(By.XPATH, '//*[@type="checkbox"]')[0].click()
        delete_number = self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn color-danger"]').text
        number = int(delete_number)
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn color-danger"]').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn color-danger"]'),
            f'Delete {number} transactions'))
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn '
                                           'color-danger"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@type='
                                                                                              '"checkbox"]')))
        list_of_all_transaction_updated = self.driver.find_elements(By.XPATH, '//*[@type="checkbox"]')[1:]
        assert len(list_of_all_transaction_updated) == len(list_of_all_transaction) - number

    def check_incomes_filter(self):
        self.driver.find_element(By.XPATH, '//*[@title="Balance"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_all_transactions = self.driver.find_elements(By.CLASS_NAME, 'list-value')
        list_of_incomes = []
        for i in list_of_all_transactions:
            if '+' in i.text or '⇒' in i.text:
                list_of_incomes.append(i.text)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-income"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_all_transactions_filtered = self.driver.find_elements(By.CLASS_NAME, 'list-value')
        assert len(list_of_all_transactions_filtered) == len(list_of_incomes)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def check_expenses_filter(self):
        self.driver.find_element(By.XPATH, '//*[@class="btn-icon _size2 _back"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Balance"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Balance"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_all_transactions = self.driver.find_elements(By.CLASS_NAME, 'list-value')
        list_of_expenses = []
        for i in list_of_all_transactions:
            if '-' in i.text or '⇒' in i.text:
                list_of_expenses.append(i.text)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-expense"]').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="btn _inp-size2 color-back"]').click()
            except NoSuchElementException:
                break
        list_of_all_transactions_filtered = self.driver.find_elements(By.CLASS_NAME, 'list-value')
        assert len(list_of_all_transactions_filtered) == len(list_of_expenses)
