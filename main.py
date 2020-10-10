from random import *


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class PlaceOfMoveException(Exception):
    def __init__(self):
        self.txt = "ERROR You make turn into occupied field"


class SkippedEndException(Exception):
    def __init__(self):
        self.txt = "ERROR You 2 players are winners, so you skip end of the game"


class TicTacToe(object):
    field = []

    def __init__(self, name_first_player, name_second_player):
        player = randint(0, 1)
        self.field = [[-1] * 3, [-1] * 3, [-1] * 3]
        self.winner = "Nobody"
        if player == 0:
            self.cross_name = name_first_player
            self.circle_name = name_second_player
            self.current_player = 1
        else:
            self.cross_name = name_second_player
            self.circle_name = name_first_player
            self.current_player = 1
        print("Cross - " + self.cross_name)
        print("Circle - " + self.circle_name)

    def make_turn(self, x_coordinate, y_coordinate):
        try:
            x_coordinate -= 1
            y_coordinate -= 1
            if self.field[y_coordinate][x_coordinate] == -1:
                self.field[y_coordinate][x_coordinate] = self.current_player
                self.current_player = (1+self.current_player) % 2
            else:
                raise PlaceOfMoveException()
        except IndexError:
            print('x and y must be between 1 and 3')
        except PlaceOfMoveException as pme:
            print(pme.txt)

    def is_win(self):
        cross_win = False
        circle_win = False
        for i in range(0, 2):
            if self.field[0][i] == self.field[1][i] == self.field[2][i]:
                if self.field[0][i] == 1:
                    cross_win = True
                if self.field[0][i] == 0:
                    circle_win = True
            if self.field[i][0] == self.field[i][1] == self.field[i][2]:
                if self.field[i][0] == 1:
                    cross_win = True
                if self.field[i][0] == 0:
                    circle_win = True
        if self.field[0][0] == self.field[1][1] == self.field[2][2]:
            if self.field[0][0] == 1:
                cross_win = True
            if self.field[0][0] == 0:
                circle_win = True
        if self.field[0][2] == self.field[1][1] == self.field[2][0]:
            if self.field[1][1] == 1:
                cross_win = True
            if self.field[1][1] == 0:
                circle_win = True
        try:
            if not cross_win and not circle_win:
                self.winner = "Nobody"
            elif cross_win and circle_win:
                raise SkippedEndException()
            elif circle_win:
                self.winner = self.circle_name
            elif cross_win:
                self.winner = self.cross_name
        except SkippedEndException as see:
            print(see.txt)
        return self.winner

    def is_final(self):
        self.is_win()
        is_end = "NOT END"
        is_full = True
        for x in range(0, 2):
            for y in range(0, 2):
                if self.field[x][y] == -1:
                    is_full = False
        if self.winner != "Nobody" or is_full:
            is_end = "END"
        return is_end

    def whose_turn(self):
        if self.current_player:
            return self.cross_name
        return self.circle_name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ttt = TicTacToe("IVAN", "QWER")
    ttt.make_turn(1, 1)
    ttt.make_turn(2, 2)
    ttt.make_turn(1, 2)
    print(ttt.is_final())
    print(ttt.is_win())
    ttt.make_turn(2, 1)
    ttt.make_turn(1, 3)
    ttt.make_turn(2, 3)
    print(ttt.is_final())
    print(ttt.is_win())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
