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
    expenses.input_cost_value(30)
    expenses.check_created_operation(30)


def test_edit_operation(expenses):
    expenses.click_edit_button()
    expenses.set_new_value(1)
    expenses.check_saved_changes(1)

def test_category_cost_calculation(expenses):
    expenses.open_main_page()
    expenses.login_user('test3@test.com', 12345678)
    expenses.open_expenses_page()
    expenses.check_total_category_cost_value()


