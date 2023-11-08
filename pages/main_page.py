from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


button = (By.XPATH, '//*[@type="button"]')
menu_item_1 = (By.ID, 'menu-item-5477')
menu_item_2 = (By.ID, 'menu-item-5479')
menu_item_3 = (By.ID, 'menu-item-5478')
menu_item_4 = (By.ID, 'menu-item-5481')
menu_item_5 = (By.ID, 'menu-item-5480')
titles = (By.XPATH, '//*[@class="title"]')
buttons_2 = (By.XPATH, '//*[@class="txt"]')
sign_in_page_title = (By.XPATH, '//*[@class="login100-form-title"]')
toggle = (By.XPATH, '//*[@class="boll"]')
register_button = (By.XPATH, '//*[@class="theme-btn plan-btn"]')


class MainPage(BasePage):
    page_url = 'https://www.cubux.net/ru/'

    def start_button_is_on_page(self):
        start_btn = self.find_all(button)[2]
        assert start_btn is not None
        assert start_btn.text == 'Начать'

    def start_button_opens_pop_up(self):
        self.find_all(button)[2].click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((
                                      By.XPATH, '//*[@class="modal-title mb-3 text-center"]')))
        pop_up_title = self.driver.find_element(By.XPATH, '//*[@class="modal-title mb-3 text-center"]')
        assert pop_up_title.text == 'Войти в Cubux.net'

    def start_with_browser(self):
        self.driver.find_element(By.XPATH, '//*[@class="btn btn-success media_obj btn-lg btn_login--browser btn-round"]'
                                 ).click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//*[@class="login100-form-title"]')))
        title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert title.text == 'Sign in'
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def start_pop_up_redirection_to_sign_up(self):
        self.driver.find_element(By.XPATH, '//*[@class="text-success fw-bold"]').click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        title = self.driver.find_element(By.XPATH, '//*[@class="login100-form-title"]')
        assert title.text == 'Регистрация'
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def start_pop_up_apple_redirection(self):
        self.driver.find_elements(By.XPATH, '//*[@class="btn__store_badge__link app_link_btn"]')[7].click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        title = self.driver.find_element(By.XPATH, '//*[@class="we-localnav__title__product"]')
        assert title.text == 'App Store'
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def google_play_redirection_without_signin(self):
        self.driver.find_elements(By.XPATH, '//*[@class="btn__store_badge__link app_link_btn"]')[6].click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        logo = self.driver.find_element(By.XPATH, '//*[@aria-label="Google Play logo"]')
        assert logo.text == 'google_logo Play'
        self.driver.find_element(By.XPATH, '//*[@aria-label="Install"]').click()
        text = self.driver.find_element(By.XPATH, '//*[@class="PNenzf"]')
        assert text.text == 'Please sign in'
        cancel_btn = self.driver.find_elements(By.XPATH, '//*[@data-id="IbE0S"]')[1].click()
        assert cancel_btn is None
        self.driver.find_element(By.XPATH, '//*[@aria-label="Install"]').click()
        self.driver.find_elements(By.XPATH, '//*[@data-id="EBS5u"]')[1].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'headingText')))
        title = self.driver.find_element(By.ID, 'headingText')
        assert title.text == 'Sign in'
        self.driver.close()
        self.driver.switch_to.window(current_window)
        self.driver.get('https://www.cubux.net/ru/')

    def check_menu_items(self):
        self.find(menu_item_1).click()
        title = self.find_all(titles)[0]
        assert title.text == 'ВыГоды'
        self.find(menu_item_2).click()
        title = self.find_all(titles)[1]
        assert title.text == 'ЦеНы'
        self.find(menu_item_3).click()
        title = self.driver.find_element(By.XPATH, '//*[@class="sec-title text-center"]')
        assert title.text == 'Основные функции'
        self.find(menu_item_4).click()
        title = self.find_all(titles)[10]
        assert title.text == 'FAQ'
        self.find(menu_item_5).click()
        item_title = self.find_all(titles)[11]
        assert item_title.text == 'БлОг'
        self.driver.get('https://www.cubux.net/ru/')

    def switch_languages(self):
        self.find_all(button)[0].click()
        self.driver.find_elements(By.XPATH, '//*[@href="https://www.cubux.net/"]')[1].click()
        start_btn = self.find_all(button)[2]
        assert start_btn.text == 'Start'
        self.find_all(button)[0].click()
        self.driver.find_elements(By.XPATH, '//*[@href="https://www.cubux.net/ru/"]')[1].click()
        start_btn = self.find_all(button)[2]
        assert start_btn.text == 'Начать'
        self.find_all(button)[0].click()
        self.driver.find_elements(By.XPATH, '//*[@href="https://www.cubux.net/cs/"]')[1].click()
        start_btn = self.find_all(button)[2]
        assert start_btn.text == 'Začít'
        self.find_all(button)[0].click()
        self.driver.find_elements(By.XPATH, '//*[@href="https://www.cubux.net/ur/"]')[1].click()
        start_btn = self.find_all(button)[2]
        assert start_btn.text == 'شروع کرنے کے لئے'
        self.driver.get('https://www.cubux.net/ru/')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="fas fa-times"]')))
        self.driver.find_element(By.XPATH, '//*[@class="fas fa-times"]').click()

    def register_button_redirection(self):
        self.driver.execute_script("window.scrollTo(135, 210);")
        self.driver.find_element(By.XPATH, '//*[@type="email"]').send_keys('test@test.com')
        self.driver.find_elements(By.XPATH, '//*[@class="theme-btn btn-style-two"]')[0].click()
        title = self.driver.find_element(By.XPATH, '//*[@class="login100"]')
        assert title.text == 'Регистрация'
        self.driver.get('https://www.cubux.net/ru/')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))

    def google_play_redirection(self):
        self.driver.execute_script("window.scrollTo(135, 564);")
        google_play_button = self.driver.find_elements(By.XPATH, '//*[@title="Google Play"]')[0]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(google_play_button))
        self.driver.find_elements(By.XPATH, '//*[@title="Google Play"]')[0].click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        logo = self.driver.find_element(By.XPATH, '//*[@aria-label="Google Play logo"]')
        install_button = self.driver.find_elements(By.XPATH, '//*[@class="VfPpkd-Jh9lGc"]')[0]
        assert logo.text == 'google_logo Play'
        assert install_button is not None
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def apple_store_redirection(self):
        self.driver.find_elements(By.XPATH, '//*[@class="btn__store_badge__link app_link_btn"]')[1].click()
        current_window = self.driver.current_window_handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        title = self.driver.find_element(By.XPATH, '//*[@class="we-localnav__title__product"]')
        assert title.text == 'App Store'
        self.driver.close()
        self.driver.switch_to.window(current_window)

    def check_toggle_switch(self):
        price_blocks = self.driver.find_elements(By.XPATH, '//*[@class="price-block col-lg-4 col-md-6 col-sm-12"]')[0:2]
        price_blocks_2 = self.driver.find_elements(By.XPATH,
                                                   '//*[@class="price-block col-lg-4 col-md-6 col-sm-12"]')[3:4]
        self.find(toggle).click()
        found_prices = self.driver.find_elements(By.XPATH, '//*[@class="price-block col-lg-4 col-md-6 col-sm-12"]')[3:4]
        self.driver.find_element(By.XPATH, '//*[@class="boll"]').click()
        found_prices_2 = self.driver.find_elements(By.XPATH,
                                                   '//*[@class="price-block col-lg-4 col-md-6 col-sm-12"]')[0:2]
        assert len(found_prices) == len(price_blocks_2)
        assert len(found_prices_2) == len(price_blocks)
