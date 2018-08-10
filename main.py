import chess
import argparse
import math
import csv

def game_to_move_converter(game_string, only_white=False):
    moves = game_string.split(" ")
    board = chess.Board()
    white_move = True
    returnval = ""
    for move in moves:
        state = str(board).replace("\n", " ").split(" ")
        black = []
        white = []
        counter = 0

        for pos in state:
            if (pos != '.'):
                col = str(int(math.floor((7 - counter) / 8)) + 8)
                row = 'abcdefgh'[counter % 8]
                if (pos.upper() == pos):
                    piece = pos.upper() + row + col
                    white.append(piece)
                else:
                    piece = pos.upper() + row + col
                    black.append(piece)
            counter = counter + 1

        move = str(board.push_san(move))

        if (only_white == False or (only_white == True and white_move == True)):
            returnval += " ".join(map(str, white)) + '\n'
            returnval += " ".join(map(str, black)) + '\n'

            returnval += move[0:2].upper() + '\n'# print move using final position notation
            returnval += move + '\n'
        white_move = not white_move
    return returnval[:-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py')
    parser.add_argument('--file', nargs='?', type=str, help='input csv to read from (no header, one game per line)')
    parser.add_argument('--one_side', nargs='?', type=str, help='use WHITE to return only white moves')
    parser.add_argument('game', nargs='?', type=str, help='game string to parse (space seperated)')

    args = parser.parse_args()
    if(args.file != None):
        with open(args.file, "r") as input:
            games = csv.reader(input, delimiter=',')
            for game in games:
                print(game_to_move_converter(game[0], only_white=args.one_side=="WHITE"))
    elif(args.game != None):
        print(game_to_move_converter(args.game, only_white=args.one_side == "WHITE"))
    else:
        print(parser.print_help())