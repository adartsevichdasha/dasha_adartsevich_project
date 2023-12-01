def test_credit(credit, maximize_window):
    credit.check_add_credit('credit_name', 80, 17)
    credit.check_edit_credit_name('test_new_name')
    credit.check_create_payments_plan(40, 40)
    credit.check_pay_now_positive_case(30)
    credit.check_edit_credit_info(23)
    credit.check_delete_actual_credit()
    credit.check_complete_credit()
