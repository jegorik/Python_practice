import random


class BillSplitter:

    def __init__(self):
        self.friends_list = {}

    def create_list(self):
        number_of_friends = self.validate_input('Enter the number of friends joining (including you):\n', int)
        if number_of_friends > 0:
            print('Enter the name of every friend (including you), each on a new line:')
            for _ in range(number_of_friends):
                name = input()
                self.friends_list[name] = 0
            return True
        else:
            print('No one is joining for the party')
            return False

    def split_bill(self):
        total_bill = self.validate_input('Enter the total split_bill value:\n', float)
        lucky = self.choose_lucky()
        friends = len(self.friends_list)
        if lucky:
            self.friends_list.pop(lucky)
            self.friends_list = {key: self.calculate_split(total_bill, friends - 1) for key in self.friends_list}
            self.friends_list.update({lucky: 0})
        else:
            self.friends_list = {key: self.calculate_split(total_bill, friends) for key in self.friends_list}

    @staticmethod
    def calculate_split(total_bill, friends):
        return round(total_bill / friends, 2)

    def print_friends_list(self):
        print(self.friends_list)

    @staticmethod
    def validate_input(prompt, data_type):
        error_messages = {
            int: 'Please enter a valid integer',
            float: 'Please enter a valid number'
        }

        while True:
            try:
                value = data_type(input(prompt))
                return value
            except ValueError:
                print(error_messages.get(data_type))

    def choose_lucky(self):
        while True:
            user_input = input(f'Do you want to use the "Who is lucky?" feature? Write Yes/No: \n').capitalize()
            if 'Yes' in user_input:
                lucky = random.choice((list(self.friends_list.keys())))
                print(f'{lucky} is the lucky one!')
                return lucky
            elif 'No' in user_input:
                return print(f'No one is going to be lucky')
            else:
                print('Please enter Yes or No')


def main():
    bill_splitter = BillSplitter()
    if bill_splitter.create_list():
        bill_splitter.split_bill()
        bill_splitter.print_friends_list()


if __name__ == "__main__":
    main()
