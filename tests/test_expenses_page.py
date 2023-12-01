def test_page_layout(expenses):
    expenses.open_main_page()
    expenses.login_user('test3@test.com', 12345678)
    expenses.open_expenses_page()
    expenses.check_hex_layout()
    expenses.check_list_layout()


def test_create_operation(expenses):
    expenses.open_main_page()
    expenses.login_user('test3@test.com', 12345678)
    expenses.open_expenses_page()
    expenses.click_create_button()
    expenses.select_account()
    expenses.select_category()
    expenses.select_date()
    expenses.check_created_operation(30)
