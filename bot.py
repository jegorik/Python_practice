import datetime


class ChatBot:
    def __init__(self):
        self.name = 'Aid'
        self.birthdate = datetime.date.today().year
        self.greet()

    def greet(self):
        print(f'Hello! My name is {self.name}.')
        print(f'I was created in {self.birthdate}.')
        user_name = input('Please, remind me your name.\n')
        print(f'What a great name you have, {user_name}!')

    def guess_user_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5, and 7.')
        user_age = self.calculate_user_age()
        print(f"Your age is {user_age}; that's a good time to start programming!")

    def calculate_user_age(self):
        reminders = [3, 5, 7]
        multipliers = [70, 21, 15]
        user_inputs = self.validate_user_input(reminders)
        user_age = sum(value * multiplier for value, multiplier in zip(user_inputs, multipliers)) % 105
        return user_age

    @staticmethod
    def count_numbers():
        number = input('Now I will prove to you that I can count to any number you want.\n')
        for i in range(0, int(number) + 1):
            print(f'{i} !')
        print('Completed, have a nice day!')

    @staticmethod
    def validate_user_input(reminders):
        user_inputs = []
        for reminder in reminders:
            while True:
                value = input(f'Reminder {reminder}: ')
                if value.isdigit():
                    user_inputs.append(int(value))
                    break
                else:
                    print('Please, enter a number.')
        return user_inputs

    @staticmethod
    def test():
        print("Let's test your programming knowledge.")
        print(""" Why do we use methods?
            1. To repeat a statement multiple times.
            2. To decompose a program into several small subroutines.
            3. To determine the execution time of a program.
            4. To interrupt the execution of a program.""")
        while True:
            user_input = input()
            if user_input.isdigit():
                answer = int(user_input)
                if answer == 2:
                    print('Congratulations, have a nice day!')
                    break
                else:
                    print('Please, try again.')
            else:
                print('Please, enter a number.')


chat_bot = ChatBot()
chat_bot.guess_user_age()
chat_bot.count_numbers()
chat_bot.test()
