from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


picture = (By.XPATH, '//*[@alt="New Web Preview"]')
form = (By.ID, 'form-signup')
button = (By.XPATH, '//*[@class="login100-form-btn button-loading"]')
login = (By.XPATH, '//*[@href="/login"]')
captcha = (By.ID, 'registerform-verifycode_captcha')
logo = (By.XPATH, '//*[@class="logo-bg-label"]')
questions = (By.ID, 'userhorn-widget')
chat = (By.XPATH, '//*[@class="userhorn-chat-container"]')
flags = (By.XPATH, '//*[@class="languages-flag-menu"]')
name = (By.ID, 'registerform-name')


class SignUp(BasePage):
    page_url = 'https://new.cubux.net/login/register?switch-language=ru'

    def check_all_elements_present(self):
        flags_block = self.find(flags)
        page_picture = self.find(picture)
        logo_text = self.find(logo)
        sign_up_form = self.find(form)
        register_button = self.find(button)
        login_button = self.find(login)
        captcha_box = self.find(captcha)
        questions_widget = self.find(questions)
        chat_widget = self.find(chat)
        assert flags_block is not None
        assert page_picture is not None
        assert logo_text is not None
        assert logo_text.text == 'www.cubux.net'
        assert sign_up_form is not None
        assert register_button is not None
        assert login_button is not None
        assert captcha_box is not None
        assert questions_widget is not None
        assert chat_widget is not None

    def check_languages(self, language, main_text):
        self.driver.find_element(By.XPATH, f'//*[@class="languages-menu-item language--{language}"]').click()
        title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert title.text == main_text

    def check_redirection_to_main_page(self):
        self.find(logo).click()
        start_button = self.driver.find_element(By.XPATH, '//*[@class="theme-btn btn-style-one"]')
        assert start_button is not None
        self.driver.get('https://new.cubux.net/login/register?switch-language=ru')

    def check_redirection_to_login_page(self):
        self.find(login).click()
        page_title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert page_title.text == 'Войти'
        self.driver.get('https://new.cubux.net/login/register?switch-language=ru')

    def check_questions_widget_search(self):
        self.find(questions).click()
        iframes = self.driver.find_elements(By.TAG_NAME, 'iframe')
        current_iframe = iframes[4]
        self.driver.switch_to.frame(current_iframe)
        self.driver.find_element(By.XPATH, '//*[@type="search"]').send_keys('dgbgye')
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="search-results-empty"]'), 'Ничего не найдено'))
        result = self.driver.find_element(By.XPATH, '//*[@class="search-results-empty"]')
        assert result.text == 'Ничего не найдено'
        self.driver.switch_to.default_content()

    def check_registration_with_all_empty_fields(self):
        self.driver.get('https://new.cubux.net/login/register?switch-language=ru')
        self.find(button).click()
        name_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[0]
        surname_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[1]
        email_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[2]
        password_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[3]
        country_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[4]
        captcha_warning = self.driver.find_elements(By.XPATH, '//*[@class="validation-error"]')[5]
        (WebDriverWait(self.driver, 10)
         .until(EC.text_to_be_present_in_element((By.XPATH, '//*[@class="validation-error"]')
                                                 ,'Необходимо заполнить «Имя».')))
        assert name_warning.text == 'Необходимо заполнить «Имя».'
        assert surname_warning.text == 'Необходимо заполнить «Фамилия».'
        assert email_warning.text == 'Необходимо заполнить «E-mail».'
        assert password_warning.text == 'Необходимо заполнить «Пароль».'
        assert country_warning.text == 'Необходимо заполнить «Страна».'
        assert captcha_warning.text == 'Вы — человек?'
