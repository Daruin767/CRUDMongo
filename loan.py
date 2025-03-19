class Loan:
    def __init__(self, user_name, book_name, loan_date, return_date):
        self.user_name = user_name
        self.book_name = book_name
        self.loan_date = loan_date
        self.return_date = return_date

    def toDBCollection(self):
        return {
            'user_name': self.user_name,
            'book_name': self.book_name,
            'loan_date': self.loan_date,
            'return_date': self.return_date
        }
