import random


class PencilGame:
    players_names = ['John', 'Jack']
    pencils = '|'
    current_player = ''

    def create_pencils(self):
        while True:
            try:
                pencils_amount = int(input('How many pencils would you like to use: \n'))
                if pencils_amount > 0:
                    self.pencils *= pencils_amount
                    break
                else:
                    print('The number of pencils should be positive.')
            except ValueError:
                print('The number of pencils should be numeric')

    def choose_player(self):
        while True:
            user_player_input = input(f'Who will be the first ({(', '.join(self.players_names))}): \n')
            if user_player_input in self.players_names:
                self.current_player = user_player_input
                break
            else:
                print(f'Choose between {(' and '.join(self.players_names))}')

    def print_table(self):
        print(self.pencils)

    def start_game(self):
        self.create_pencils()
        self.choose_player()
        self.print_table()
        self.game_process()

    def player_turn(self, pencils_amount, current_player):
        print(f"{current_player}'s turn:")
        if current_player == self.players_names[0]:
            return self.human_turn(pencils_amount)
        else:
            bot_action = self.bot_turn(pencils_amount)
            print(bot_action)
            return bot_action

    def human_turn(self, pencils_amount):
        while True:
            player_action = input()
            if player_action.isdigit() and 1 <= int(player_action) <= 3:
                if int(player_action) <= pencils_amount:
                    return int(player_action)
                else:
                    print('Too many pencils were taken')
            else:
                print("Possible values: '1', '2' or '3'")

    def bot_turn(self, pencils_amount):
        if pencils_amount % 4 == 1:
            return random.randint(1, min(3, pencils_amount))
        else:
            return (pencils_amount - 1) % 4

    def game_process(self):
        pencils_amount = len(self.pencils)
        while pencils_amount > 0:
            action = self.player_turn(pencils_amount, self.current_player)
            pencils_amount -= action
            self.pencils = '|' * pencils_amount
            self.print_table()
            self.current_player = self.change_player(self.current_player)
            self.winner_check()

    def change_player(self, current_player):
        return self.players_names[0] if current_player == self.players_names[1] else self.players_names[1]

    def winner_check(self):
        if len(self.pencils) == 0:
            print(f'{self.current_player} Won!')


def main():
    new_pencil_game = PencilGame()
    new_pencil_game.start_game()


if __name__ == '__main__':
    main()
