from random import *
import argparse


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
        print("First turn cross - " + self.cross_name)
        print("second turn circle - " + self.circle_name)

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

    def who_win(self):
        cross_win = False
        circle_win = False
        for i in range(0, 3):
            if self.field[0][i] == self.field[1][i] and self.field[0][i] == self.field[2][i]:
                if self.field[0][i] == 1:
                    cross_win = True
                if self.field[0][i] == 0:
                    circle_win = True
            if self.field[i][0] == self.field[i][1] and self.field[i][0] == self.field[i][2]:
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
                self.winner = "Both"
                raise SkippedEndException()
            elif circle_win:
                self.winner = self.circle_name
            elif cross_win:
                self.winner = self.cross_name
        except SkippedEndException as see:
            print(see.txt)
        return self.winner

    def is_final(self):
        self.who_win()
        is_end = False
        is_full = True
        for x in range(0, 3):
            for y in range(0, 3):
                if self.field[x][y] == -1:
                    is_full = False
        if (self.winner != "Nobody") or is_full:
            is_end = True
        return is_end

    def whose_turn(self):
        if self.current_player:
            return self.cross_name
        return self.circle_name

    def print_field(self):
        field = [[-1]*3, [-1]*3, [-1]*3]
        for y in range(3):
            for x in range(3):
                if self.field[2-y][x] == -1:
                    field[y][x] = " "
                elif self.field[2-y][x] == 1:
                    field[y][x] = "X"
                else:
                    field[y][x] = 0
        print("---------")
        for y in range(3):
                print(str(field[y][0]) + " | " + str(field[y][1]) + " | " + str(field[y][2]))
                print("---------")


if __name__ == '__main__':
    turn = 0
    print("please, input name of first player")
    first_player_name = input()
    print("please, input name of second player")
    second_player_name = input()
    tic_tac_toe_game = TicTacToe(first_player_name, second_player_name)
    parser = argparse.ArgumentParser(description='turn')
    parser.add_argument('x', type=str, help='Input dir for videos')
    parser.add_argument('y', type=str, help='Output dir for image')
    while not tic_tac_toe_game.is_final():
        print(str(tic_tac_toe_game.whose_turn()) + " plaese, input coordinates for turn")
        try:
            tic_tac_toe_game.make_turn(int(input()), int(input()))
            tic_tac_toe_game.print_field()
        except ValueError:
            print("Input error - coordinates are two integer from 1 to 3 in two lines(1 number 1 line)")
    print(str(tic_tac_toe_game.who_win()) + " win")
