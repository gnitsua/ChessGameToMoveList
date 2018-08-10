import unittest

from chess import Board
from chess import Piece
from chess import square

from main import game_to_move_converter


class TestConverter(unittest.TestCase):
    @classmethod
    def parse_piece_list(cls,white,black):
        board = Board()
        board.clear()
        for peice in white.split(" "):
            p = Piece.from_symbol(peice[0])
            board.set_piece_at(square(ord(peice[1]) - ord('a'), int(peice[2]) - 1), p)
        for peice in black.lower().split(" "):
            p = Piece.from_symbol(peice[0])
            board.set_piece_at(square(ord(peice[1]) - ord('a'), int(peice[2]) - 1), p)
        return board

    def test_string_input(self):
        input = "d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4"
        output = game_to_move_converter(input).split("\n")[:-1]
        ground_truth = Board()
        self.assertEqual(len(output) / 4, len(input.split(" ")))
        count = 0
        for move in input.split(" "):
            white = output[count]
            black = output[count + 1]
            possible_move = output[count + 3]
            self.assertEqual(str(self.parse_piece_list(white,black)), str(ground_truth))  # make sure the parsed board is correct

            self.assertIn(possible_move,
                          list(map(lambda x: str(x), list(ground_truth.legal_moves))))  # make sure that the move
            ground_truth.push_san(move)
            count = count + 4

    def test_string_input_white(self):
        input = "d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4"
        output = game_to_move_converter(input, only_white=True).split("\n")[:-1]
        ground_truth = Board()
        count = 0
        turn = True
        for move in input.split(" "):
            white = output[count]
            black = output[count + 1]
            possible_move = output[count + 3]
            if(turn == True):
                self.assertEqual(str(ground_truth),str(self.parse_piece_list(white,black)))  # make sure the parsed board is correct
                self.assertIn(possible_move,
                              list(map(lambda x: str(x), list(ground_truth.legal_moves))))  # make sure that the move
                count = count + 4
            ground_truth.push_san(move)
            turn = not turn
