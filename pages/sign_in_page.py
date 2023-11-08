from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


flags = (By.XPATH, '//*[@class="languages-flag-menu"]')
picture = (By.XPATH, '//*[@class="login100-pic js-tilt"]')
logo = (By.XPATH, '//*[@class="logo-bg-label"]')
form = (By.ID, 'form-login')
button = (By.XPATH, '//*[@class="login100-form-btn button-loading"]')
registration = (By.LINK_TEXT, 'Sign up')
forgot_password = (By.LINK_TEXT, 'Forgot password?')
questions = (By.ID, 'userhorn-widget')
chat = (By.XPATH, '//*[@class="userhorn-chat-container"]')
old_web = (By.LINK_TEXT, 'Old Web')


class SignIn(BasePage):
    page_url = 'https://new.cubux.net/login'

    def check_all_elements_present(self):
        flags_block = self.find(flags)
        page_picture = self.find(picture)
        logo_text = self.find(logo)
        sign_up_form = self.find(form)
        login_button = self.find(button)
        registration_button = self.find(registration)
        recover_password_button = self.find(forgot_password)
        questions_widget = self.find(questions)
        chat_widget = self.find(chat)
        old_web_link = self.find(old_web)
        assert flags_block is not None
        assert page_picture is not None
        assert logo_text is not None
        assert logo_text.text == 'www.cubux.net'
        assert sign_up_form is not None
        assert registration_button is not None
        assert login_button is not None
        assert recover_password_button is not None
        assert questions_widget is not None
        assert chat_widget is not None
        assert old_web_link is not None

    def check_languages(self, language, main_text):
        self.driver.find_element(By.XPATH, f'//*[@class="languages-menu-item language--{language}"]').click()
        title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert title.text == main_text
        self.driver.find_element(By.XPATH, '//*[@href="/login?switch-language=en"]').click()

    def check_redirection_to_main_page(self):
        self.find(logo).click()
        start_button = self.driver.find_element(By.XPATH, '//*[@class="theme-btn btn-style-one"]')
        assert start_button is not None
        self.driver.get('https://new.cubux.net/login')

    def check_redirection_to_login_page(self):
        self.find(registration).click()
        page_title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert page_title.text == 'Sign up'
        self.driver.get('https://new.cubux.net/login')

    def check_sent_message_in_chat(self, message_text):
        self.find(chat).click()
        iframes = self.driver.find_elements(By.TAG_NAME, 'iframe')
        current_iframe = iframes[0]
        self.driver.switch_to.frame(current_iframe)
        self.driver.find_element(By.ID, 'widget-chat-answer').send_keys(f'{message_text}')
        self.driver.find_elements(By.XPATH, '//*[@class="answer-button"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'p')))
        sent_message = self.driver.find_element(By.TAG_NAME, 'p')
        assert sent_message.text == message_text
        self.driver.find_element(By.XPATH, '//*[@class="fa fa-times"]').click()
        self.driver.switch_to.default_content()

    def check_questions_widget_opens(self):
        self.find(questions).click()
        iframes = self.driver.find_elements(By.TAG_NAME, 'iframe')
        current_iframe = iframes[1]
        self.driver.switch_to.frame(current_iframe)
        title = self.driver.find_element(By.XPATH, '//*[@class="search-bar-subheader"]')
        assert title.text == 'Welcome to cubux.net support community'

    def check_questions_widget_ask_button(self):
        self.driver.find_element(By.XPATH, '//*[@class="search-button-add-topic"]').click()
        field = self.driver.find_element(By.XPATH, '//*[@class="modal-title"]')
        assert field.text == 'Ask a question'
        self.driver.find_elements(By.XPATH, '//*[@class="close"]')[1].click()
        self.driver.find_element(By.ID, 'main-modal-close').click()
        self.driver.switch_to.default_content()

    def check_login_with_all_empty_fields(self):
        self.find(button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                            (By.XPATH, '//*[@class="validation-error"]')))
        warning_1 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[0]
        warning_2 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[1]
        assert warning_1.text == 'E-mail cannot be blank.'
        assert warning_2.text == 'Password cannot be blank.'

    def check_login_with_password_empty(self, email):
        self.driver.find_element(By.ID, 'loginform-username').send_keys(f'{email}')
        self.find(button).click()
        warning_1 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[0]
        warning_2 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[1]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(warning_2))
        assert warning_1.text == ''
        assert warning_2.text == 'Password cannot be blank.'
        self.driver.find_element(By.ID, 'loginform-username').clear()

    def check_login_with_email_empty(self, password):
        self.driver.find_element(By.ID, 'loginform-password').send_keys(password)
        self.find(button).click()
        warning_1 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[0]
        warning_2 = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[1]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(warning_1))
        assert warning_1.text == 'E-mail cannot be blank.'
        assert warning_2.text == ''
        self.driver.find_element(By.ID, 'loginform-password').clear()

    def check_login_with_invalid_data(self, invalid_email, invalid_password):
        self.driver.find_element(By.ID, 'loginform-username').send_keys(f'{invalid_email}')
        self.driver.find_element(By.ID, 'loginform-password').send_keys(invalid_password)
        self.find(button).click()
        warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[1]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(warning))
        assert warning.text == 'Incorrect username or password'
        self.driver.find_element(By.ID, 'loginform-username').clear()
        self.driver.find_element(By.ID, 'loginform-password').clear()

    def check_login_with_valid_data(self, valid_email, valid_password):
        self.driver.find_element(By.ID, 'loginform-username').send_keys(f'{valid_email}')
        self.driver.find_element(By.ID, 'loginform-password').send_keys(valid_password)
        self.find(button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                            (By.XPATH, '//*[@class="main-hex column-right"]')))
        page = self.driver.find_element(By.XPATH, '//*[@class="main-hex column-right"]')
        assert page is not None
