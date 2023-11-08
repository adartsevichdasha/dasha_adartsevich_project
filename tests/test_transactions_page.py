def test_transactions_page(transactions, maximize_window):
    transactions.check_categories_displayed_in_transactions()
    transactions.check_create_transfer_transaction(70)
    transactions.create_unconfirmed_expenses_transaction(20)
    transactions.create_unconfirmed_incomes_transaction(56)
    transactions.confirm_unconfirmed_transaction()
    transactions.check_incomes_filter()
    transactions.check_expenses_filter()
    transactions.check_delete_bulk_transactions()
