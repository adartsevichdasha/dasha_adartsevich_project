def test_incomes_page(incomes, maximize_window):
    incomes.check_page_layout()
    incomes.check_add_category('test_category')
    incomes.check_add_operation(40)
    incomes.check_change_operation(3)
    incomes.check_total_incomes_calculated()
    incomes.check_delete_operation()
