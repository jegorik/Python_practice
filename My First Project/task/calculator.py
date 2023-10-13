class FinancialCalculator:
    def __init__(self):
        self.prices = {'Bubblegum': 2, 'Toffee': 0.2, 'Ice cream': 5, 'Milk chocolate': 4, 'Doughnut': 2.5,
                       'Pancake': 3.2}
        self.profit_by_product = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680,
                                  'Doughnut': 1075, 'Pancake': 80}
        self.staff_expenses = {}
        self.other_expenses = {}

    def make_user_request(self, request):
        request = request.lower()
        dictionaries = {'prices': self.prices, 'profit': self.profit_by_product, 'staff expenses': self.staff_expenses,
                        'other expenses': self.other_expenses}
        headers = {'prices': 'Prices:', 'profit': 'Earned amount:', 'staff expenses': 'Staff expenses:',
                   'other expenses': 'Other expenses:'}
        footers = {
            'profit': f'Income: ${self.get_profit_by_product()}',
            'staff expenses': self.get_staff_expenses(),
            'other expenses': self.get_other_expenses(),
            'net income': self.get_net_income()
        }

        dic = dictionaries.get(request, None)
        header = headers.get(request, None)
        footer = footers.get(request, None)

        self.print_user_request(dic, header, footer)

    def get_net_income(self):
        total = self.get_profit_by_product() - self.get_staff_expenses() - self.get_other_expenses()
        return f'Net income: ${total}'

    def get_profit_by_product(self):
        return sum(self.profit_by_product.values())

    def set_staff_expenses(self, value):
        self.staff_expenses.update({'staff expenses': value})

    def set_other_expenses(self, value):
        self.other_expenses.update({'other expenses': value})

    def get_staff_expenses(self):
        return sum(self.staff_expenses.values())

    def get_other_expenses(self):
        return sum(self.other_expenses.values())

    @staticmethod
    def print_user_request(dic, header, footer):
        if dic and header:
            print(header)
            for key, value in dic.items():
                print(f'{key}: ${value}')
        if footer:
            print('\n' + footer)

    @staticmethod
    def validate_user_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print('Please enter a number')


financial_calculator = FinancialCalculator()
financial_calculator.make_user_request('profit')
financial_calculator.set_staff_expenses(financial_calculator.validate_user_input('Staff expenses: \n'))
financial_calculator.set_other_expenses(financial_calculator.validate_user_input('Other expenses: \n'))
financial_calculator.make_user_request('net income')
