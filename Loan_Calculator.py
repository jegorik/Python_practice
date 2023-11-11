import argparse
import math
import sys
#Example of user_input: --type=diff --principal=1000000 --periods=10 --interest=10

class LoanCalculator:
    args = None
    VALID_ARGUMENTS = ['payment', 'principal', 'periods', 'interest']

    def __init__(self):
        # Parse command line arguments, validate them, and perform calculations
        self.args = self.parse_arguments()
        self.validate_arguments()
        self.calculate_user_input()

    @staticmethod
    def parse_arguments():
        # Set up ArgumentParser to handle command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--payment', type=float)
        parser.add_argument('--principal', type=int)
        parser.add_argument('--periods', type=int)
        parser.add_argument('--interest', type=float)
        parser.add_argument('--type')
        # Parse and return the command line arguments
        return parser.parse_args()

    def validate_arguments(self):
        # Validate the payment type and numeric arguments to ensure they are not negative
        if self.args.type not in ["annuity", "diff"]:
            sys.exit("Incorrect parameters")

        for argument in self.VALID_ARGUMENTS:
            value = getattr(self.args, argument)
            if value is not None and value < 0:
                sys.exit("Incorrect parameters")

    def calculate_user_input(self):
        # Determine the type of calculation based on the provided arguments
        if self.args.payment is None:
            if all([self.args.principal, self.args.periods, self.args.interest]):
                self.calculate_months_to_pay()
                return
        elif self.args.principal is None:
            if all([self.args.payment, self.args.periods, self.args.interest]):
                self.calculate_loan_principal()
                return
        elif self.args.periods is None:
            if all([self.args.payment, self.args.principal, self.args.interest]):
                self.calculate_monthly_payment()
                return

        # If none of the conditions match, print an error message
        print("Incorrect parameters")

    def calculate_months_to_pay(self):
        # Calculate the number of months needed to repay the loan
        payment = self.args.payment
        principal = self.args.principal
        interest_rate = self.interest_rate()

        months_amount = math.ceil(math.log(payment / (payment - interest_rate * principal), 1 + interest_rate))

        years, months = divmod(months_amount, 12)

        total_paid = months_amount * payment

        if months > 0:
            years += months // 12
            months %= 12

        # Print the result
        print(self.print_months_to_pay(years, months))
        print(self.calculate_overpayment(total_paid, principal))

    def calculate_monthly_payment(self):
        # Calculate the monthly payment based on the loan parameters
        principal = self.args.principal
        periods = self.args.periods
        interest_rate = self.interest_rate()
        type_of_payment = self.args.type
        total_paid = 0

        if type_of_payment == 'diff':
            # For differentiated payments, calculate and print payments for each month
            total_paid = self.calculate_diff_payment(periods, principal, interest_rate)
        elif type_of_payment == 'annuity':
            # For annuity payments, calculate and print the monthly payment
            total_paid = self.calculate_annuity_payment(periods, principal, interest_rate)

        # Print the result
        print(self.calculate_overpayment(total_paid, principal))

    @staticmethod
    def calculate_diff_payment(periods, principal, interest_rate):
        # Calculate differentiated payments for each month and print the results
        total_paid = 0
        for month in range(0, periods):
            result = math.ceil(
                round(principal / periods + interest_rate * (principal - ((principal * month - 1) / periods)),
                      2))
            total_paid += result
            print(f'Month {month + 1}: payment is {result}')
        print()
        return total_paid

    @staticmethod
    def calculate_annuity_payment(periods, principal, interest_rate):
        # Calculate annuity payments and print the monthly payment
        result = math.ceil(principal * (interest_rate * pow(1 + interest_rate, periods)) / (
                pow(1 + interest_rate, periods) - 1))
        total_paid = result * periods
        print(f'Your monthly payment = {result}!')
        return total_paid

    def calculate_loan_principal(self):
        # Calculate the loan principal based on the provided payments, periods, and interest rate
        payments = self.args.payment
        periods = self.args.periods
        interest_rate = self.interest_rate()
        principal = math.floor(payments / (interest_rate * pow(1 + interest_rate, periods) / (
                pow(1 + interest_rate, periods) - 1)))
        total_loan = payments * periods
        # Print the result
        print(f'Your loan principal = {principal}!')
        print(self.calculate_overpayment(total_loan, principal))

    def interest_rate(self):
        # Calculate and return the monthly interest rate
        interest = self.args.interest
        return interest / (12 * 100)

    @staticmethod
    def print_months_to_pay(years, months):
        # Print a formatted message indicating the time needed to repay the loan
        years_str = f'{years} {"years" if years != 1 else "year"} ' if years != 0 else ''
        months_str = f'{months} {"months" if months != 1 else "month"}' if months != 0 else ''

        if years_str and months_str:
            middle_str = 'and '
        else:
            middle_str = ''

        return f'It will take {years_str}{middle_str}{months_str}to repay this loan!'

    @staticmethod
    def calculate_overpayment(total_amount, principal):
        # Calculate and return the total overpayment
        return f'Total Overpayment: {math.ceil(total_amount - principal)}'

def main():
    # Instantiate the LoanCalculator class
    LoanCalculator()

if __name__ == '__main__':
    # Run the main function if the script is executed directly
    main()
