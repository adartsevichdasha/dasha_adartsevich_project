import datetime
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


class Credit(BasePage):
    page_url = 'https://new.cubux.net/team/301102/credit'

    def check_add_credit(self, credit_name, credit_value, current_number_on_buttons):
        self.driver.get('https://new.cubux.net/login')
        self.login_user('test3@test.com', 12345678)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Credits"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Credits"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="hex-block '
                                                                                         '_hex-block-size1"]')))
        button = self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit _inp-size2 selected"]')
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="btn-filter color-credit _inp-size2 selected"]'),
            f'Actual ({current_number_on_buttons})'))
        actual_button_text = button.text
        number_of_actual_credits = actual_button_text.split()
        number = str(number_of_actual_credits[1])
        number_2 = int(number[1:-1])
        list_of_credits = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                    '//*[@type="text"]')))
        self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0].send_keys(credit_name)
        self.driver.find_elements(By.XPATH, '//*[@type="text"]')[2].send_keys('2')
        self.driver.find_elements(By.XPATH, '//*[@class="currency"]')[0].send_keys('3')
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ inline"]').click()
        select = self.driver.find_elements(By.TAG_NAME, 'select')[1]
        dropdown = Select(select)
        dropdown.select_by_value('1008727')
        self.driver.find_elements(By.XPATH, '//*[@class="currency"]')[1].send_keys(credit_value)
        self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0].click()
        sleep(4)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '//*[@class="rc-dialog-close"]')))
        self.driver.find_element(By.XPATH, '//*[@class="rc-dialog-close"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        list_of_credits_updated = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        actual_button_text_updated = self.driver.find_element(By.XPATH,'//*[@class="btn-filter color-credit _inp-size2 '
                                                                       'selected"]').text
        assert actual_button_text_updated == f'Actual ({number_2 + 1})'
        assert len(list_of_credits_updated) == (len(list_of_credits) + 1)

    def check_edit_credit_name(self, new_name):
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[3].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="0"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC"]')[1].click()
        old_name = self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(old_name))
        old_name_value = old_name.get_attribute('value')
        old_name_length = len(old_name_value)
        self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0].click()
        for i in range(0, old_name_length):
            self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0].send_keys(Keys.BACKSPACE)
        self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0].send_keys(new_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@value='
                                                                                         f'"{new_name}"]')))
        self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0].click()
        sleep(3)
        updated_credit_title = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[0].text
        assert updated_credit_title == f'Credits: {new_name}'

    def check_create_payments_plan(self, value_1, value_2):
        self.driver.find_element(By.XPATH, '//*[@class="Button_link__5qRQJ"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="text"]')))
        self.driver.find_element(By.XPATH, '//*[@type="text"]').click()
        list_of_entered_dates = []
        self.driver.find_element(By.XPATH, '//*[@aria-label="Choose Sunday, 5 November 2023"]').click()
        sleep(4)
        first_date = self.driver.find_elements(By.XPATH, '//*[@type="text"]')[0]
        first_date_value = first_date.get_attribute('value')
        first_date_updated = datetime.datetime.strptime(first_date_value, '%d/%m/%Y')
        list_of_entered_dates.append(first_date_updated)
        self.driver.find_element(By.XPATH, '//*[@class="currency"]').send_keys(value_1)
        self.driver.find_elements(By.XPATH, '//*[@type="text"]')[1].click()
        self.driver.find_element(By.XPATH, '//*[@aria-label="Choose Friday, 1 December 2023"]').click()
        sleep(5)
        second_date = self.driver.find_elements(By.XPATH, '//*[@type="text"]')[1]
        second_date_value = second_date.get_attribute('value')
        second_date_updated = datetime.datetime.strptime(second_date_value, '%d/%m/%Y')
        list_of_entered_dates.append(second_date_updated)
        current_date = datetime.datetime.now()
        new_list_of_entered_dates = []
        for i in list_of_entered_dates:
            if i > current_date or i == current_date:
                new_list_of_entered_dates.append(i)
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')[2].click()
        sleep(5)
        final_date = sorted(new_list_of_entered_dates)[0]
        final_date_updated = final_date.strftime('%d/%m/%Y')
        remain_to_fee_sum = value_1 + value_2
        remain_to_fee = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        next_payment_date = self.driver.find_elements(By.XPATH, '//*[@class="value"]')[2].text
        assert remain_to_fee == f'Remain to fee: AFN {remain_to_fee_sum}'
        assert next_payment_date == final_date_updated

    def check_pay_now_positive_case(self, payment_sum):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        remain_to_fee = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        remain_to_fee_1 = remain_to_fee.split()
        remain_to_fee_2 = int(remain_to_fee_1[-1])
        already_paid = self.driver.find_elements(By.XPATH, '//*[@class="value"]')[0].text
        already_paid_1 = already_paid.split()
        already_paid_2 = int(already_paid_1[-1])
        self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')[0].click()
        set_sum = self.driver.find_element(By.CLASS_NAME, 'currency')
        set_sum_value = set_sum.get_attribute('value')
        set_sum_length = len(set_sum_value)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'currency')))
        self.driver.find_element(By.CLASS_NAME, 'currency').click()
        for i in range(0, set_sum_length):
            self.driver.find_element(By.CLASS_NAME, 'currency').send_keys(Keys.DELETE)
        self.driver.find_element(By.CLASS_NAME, 'currency').send_keys(payment_sum)
        self.driver.find_element(By.XPATH, '//*[@type="text"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        sleep(3)
        already_paid_final = self.driver.find_elements(By.XPATH, '//*[@class="value"]')[0].text
        paid_sum = already_paid_2 + payment_sum
        remain_to_pay_final = self.driver.find_elements(By.XPATH, '//*[@class="sub-title"]')[2].text
        sum_1 = remain_to_fee_2 - payment_sum
        assert remain_to_pay_final == f'Remain to fee: AFN {sum_1}'
        assert already_paid_final == f'AFN {paid_sum}'

    def check_edit_credit_info(self, new_sum):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Credits"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Credits"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        sleep(3)
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[3].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="Button_button__'
                                                                                   'QS2NC"]')))
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@title="Edit"]').click()
        old_sum = self.driver.find_element(By.CLASS_NAME, 'currency')
        old_sum_value = old_sum.get_attribute('value')
        old_sum_length = len(old_sum_value)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'currency')))
        self.driver.find_element(By.CLASS_NAME, 'currency').click()
        for i in range(0, old_sum_length):
            self.driver.find_element(By.CLASS_NAME, 'currency').send_keys(Keys.DELETE)
        self.driver.find_element(By.CLASS_NAME, 'currency').send_keys(new_sum)
        self.driver.find_element(By.XPATH, '//*[@type="text"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__today-button"]').click()
        new_date = self.driver.find_element(By.XPATH, '//*[@type="text"]').get_attribute('value')
        self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'time')))
        sleep(2)
        updated_date = self.driver.find_element(By.TAG_NAME, 'time').text
        updated_sum = self.driver.find_element(By.XPATH, '//*[@class="list-value color-income"]').text
        assert updated_date == new_date
        assert updated_sum == f'+ AFN {new_sum}'

    def check_delete_actual_credit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Credits"]')))
        self.driver.find_element(By.XPATH, '//*[@title="Credits"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        sleep(3)
        actual_button_text = self.driver.find_element(By.XPATH,'//*[@class="btn-filter color-credit _inp-size2 '
                                                               'selected"]').text
        number_of_actual_credits = actual_button_text.split()
        number = str(number_of_actual_credits[1])
        number_2 = int(number[1:-1])
        list_of_credits = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[3].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="Button_button__QS2NC btn color-danger"]'), 'Delete'))
        self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn color-danger"]').click()
        delete_button = self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(delete_button))
        delete_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="btn-filter color-credit _inp-size2 selected"]'),
            f'Actual ({number_2 - 1})'))
        list_of_credits_updated = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        actual_button_text_updated = self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit '
                                                                        '_inp-size2 selected"]').text
        assert actual_button_text_updated == f'Actual ({number_2 - 1})'
        assert len(list_of_credits_updated) == (len(list_of_credits) - 1)

    def check_complete_credit(self):
        finished_credits = self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit _inp-size2"]').text
        number_of_finished_credits = finished_credits.split()
        number = str(number_of_finished_credits[1])
        number_2 = int(number[1:-1])
        list_of_actual_credits = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit _inp-size2"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        list_of_finished_credits = self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit _inp-size2"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="hex-block _hex-block-size1"]')))
        self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')[-1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')))
        complete_button = self.driver.find_elements(By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')[1]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(complete_button))
        complete_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                                    'ConfirmDialog_button__vzjDJ')))
        confirm_button = self.driver.find_elements(By.CLASS_NAME, 'ConfirmDialog_button__vzjDJ')[0]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(confirm_button))
        confirm_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')))
        cancel_button = self.driver.find_element(By.XPATH, '//*[@class="Button_button__QS2NC btn color-credit"]')
        assert cancel_button is not None
        self.driver.find_element(By.XPATH, '//*[@title="Credits"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        finished_credits_final = self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit '
                                                                    '_inp-size2"]').text
        assert finished_credits_final == f'Finished ({number_2 + 1})'
        list_of_actual_credits_updated = self.driver.find_elements(By.XPATH, '//*[@class="hex-name"]')
        assert len(list_of_actual_credits_updated) == (len(list_of_actual_credits) - 1)
        self.driver.find_element(By.XPATH, '//*[@class="btn-filter color-credit _inp-size2"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@class="Button_link__5qRQJ hex-btn"]')))
        list_of_finished_credits_updated = self.driver.find_elements(By.XPATH, '//*[@class="Button_link__5qRQJ '
                                                                               'hex-btn"]')
        assert len(list_of_finished_credits_updated) == (len(list_of_finished_credits) + 1)
