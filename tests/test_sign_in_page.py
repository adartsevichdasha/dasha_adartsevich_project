def test_sign_in_page(sign_in_page, maximize_window):
    sign_in_page.open()
    sign_in_page.check_all_elements_present()
    sign_in_page.check_login_with_all_empty_fields()
    sign_in_page.check_languages('de', 'Anmelden')
    sign_in_page.check_login_with_password_empty('test@test.com')
    sign_in_page.check_redirection_to_main_page()
    sign_in_page.check_login_with_email_empty(12345)
    sign_in_page.check_redirection_to_login_page()
    sign_in_page.check_login_with_invalid_data('test@test.com', 12345)
    sign_in_page.check_sent_message_in_chat('random')
    sign_in_page.check_questions_widget_opens()
    sign_in_page.check_questions_widget_ask_button()
    sign_in_page.check_login_with_valid_data('test3@test.com', 12345678)