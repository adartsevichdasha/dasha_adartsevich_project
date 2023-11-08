def test_sign_up_page(sign_up_page, maximize_window):
    sign_up_page.open()
    sign_up_page.check_all_elements_present()
    sign_up_page.check_languages('it', 'Registrati')
    sign_up_page.check_redirection_to_main_page()
    sign_up_page.check_redirection_to_login_page()
    sign_up_page.check_questions_widget_search()
    sign_up_page.check_registration_with_all_empty_fields()
