# write your code here
class TicTacToe:
    field = []
    step_for = 'X'

    def field_fill(self):
        self.field = [[' ' for j in range(3)] for i in range(3)]

    def print_field(self):
        print('---------')
        for row in self.field:
            print('|', *row, '|')
        print('---------')

    def set_step(self):

        def check_coordinates():
            input_data = input('Enter the coordinates: ')
            if ' ' in input_data and input_data.replace(' ', '').isdigit():
                coll, row = [int(x) for x in input_data.split()]
                if (not (1 <= coll <= 3)) or (not (1 <= row <= 3)):
                    print('Coordinates should be from 1 to 3!')
                    return check_coordinates()
                elif self.field[3 - row][coll - 1] != ' ':
                    print('This cell is occupied! Choose another one!')
                    return check_coordinates()
                else:
                    return coll - 1, 3 - row
            else:
                print('You should enter numbers!')
                return check_coordinates()

        coordinates = check_coordinates()
        self.field[coordinates[1]][coordinates[0]] = self.step_for

    def get_game_state(self):
        count = 0
        for i in range(3):  # check up-down diagonal
            if self.field[i][i] == self.field[0][0] and self.field[i][i] != ' ':
                count += 1
                if count == 3:
                    return f'{self.step_for} wins'

        count = 0
        j = 0
        for i in range(2, -1, -1):  # check down-up diagonal
            if (self.field[i][j] == self.field[2][0]) and self.field[i][j] != ' ':
                count += 1
                j += 1
                if count == 3:
                    return f'{self.step_for} wins'

        for i in range(3):  # check in rows
            if self.field[i].count(self.field[i][0]) == 3 and self.field[i][0] != ' ':
                return f'{self.step_for} wins'

        for j in range(3):  # check in columns
            count = 0
            for i in range(3):
                if self.field[i][j] == self.field[0][j] and self.field[i][j] != ' ':
                    count += 1
                    if count == 3:
                        return f'{self.step_for} wins'

        x_count, y_count, empty_count = 0, 0, 0  # check draw
        for i in self.field:
            x_count += i.count('X')
            y_count += i.count('O')
            empty_count += i.count(' ')
        if empty_count == 0 and (0 <= abs(x_count - y_count) <= 1):
            return 'Draw'
        return 'Game not finished'

    def start_game(self):
        self.field_fill()
        state = ''
        while not ('wins' in state) and state != 'Draw':
            self.set_step()
            state = self.get_game_state()
            if self.step_for == 'O':
                self.step_for = 'X'
            else:
                self.step_for = 'O'
            self.print_field()
        print(state)


new_game = TicTacToe()
new_game.start_game()
