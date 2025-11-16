from player import Player
from board import Board
from book import Book
from tictactoe import draw_board, get_input, player_turn, check_win, check_draw, create_board
import unittest

class test_tictactoe(unittest.TestCase):

    def test_draw_board_empty(self):
        self.assertEqual(draw_board({
            '1': False,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False,
        }), True)
    
    def test_draw_board_empty_faulty(self):
        self.assertEqual(draw_board({
            '1': None,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False,
        }), False)

        self.assertEqual(draw_board({
            '1': False,
            '2': False,
            '3': False,
            '4': 10,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False,
        }), False)

        self.assertEqual(draw_board({
            '1': True,
            '2': True,
            '3': True,
            '4': True,
            '5': True,
            '6': True,
            '7': True,
            '8': True,
            '9': True,
        }), False)

    def test_draw_board_in_progress(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        self.assertEqual(draw_board({
        '1': False,
        '2': player_one,
        '3': False,
        '4': False,
        '5': player_two,
        '6': False,
        '7': player_one,
        '8': False,
        '9': False,
        }), True)

        self.assertEqual(draw_board({
            '1': player_one,
            '2': False,
            '3': player_two,
            '4': False,
            '5': player_two,
            '6': False,
            '7': False,
            '8': False,
            '9': player_one,
        }), True)
    
    def test_draw_board_in_progress_faulty(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        self.assertEqual(draw_board({
        '1': False,
        '2': player_one,
        '3': False,
        '4': "  4  ",
        '5': player_two,
        '6': False,
        '7': player_one,
        '8': False,
        '9': False,
        }), False)

        self.assertEqual(draw_board({
            '1': False,
            '2': player_one,
            '3': False,
            '4': "  4  ",
            '5': player_two,
            '6': False,
            '7': player_one,
            '8': False,
            '9': False,
        }), False)

        self.assertEqual(draw_board({
            '1': False,
            '2': player_one,
            '3': False,
            '4': False,
            '5': player_two,
            '6': False,
            '7': player_one,
            '8': False,
            '9': 100,
        }), False)
    
    def test_draw_board_full(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        self.assertEqual(draw_board({
            '1': player_one,
            '2': player_one,
            '3': player_two,
            '4': player_one,
            '5': player_two,
            '6': player_two,
            '7': player_one,
            '8': player_one,
            '9': player_two,
        }), True)

        self.assertEqual(draw_board({
            '1': player_two,
            '2': player_one,
            '3': player_two,
            '4': player_one,
            '5': player_two,
            '6': player_two,
            '7': player_one,
            '8': player_one,
            '9': player_one,
        }), True)

    def test_draw_board_full_faulty(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        self.assertEqual(draw_board({
            '1': player_one,
            '2': player_one,
            '3': player_two,
            '4': player_one,
            '5': player_two,
            '6': '  X  ',
            '7': player_one,
            '8': player_one,
            '9': player_two,
        }), False)

        self.assertEqual(draw_board({
            '1': player_two,
            '2': player_one,
            '3': player_two,
            '4': player_one,
            '5': player_two,
            '6': player_two,
            '7': player_one,
            '8': player_one,
            '9': 100,
        }), False)

        self.assertEqual(draw_board({
            '1': player_two,
            '2': player_one,
            '3': player_two,
            '4': None,
            '5': player_two,
            '6': player_two,
            '7': player_one,
            '8': player_one,
            '9': player_two,
        }), False)
    
    def test_check_draw_empty_board(self):
        test_board = Board()
        self.assertEqual(check_draw(test_board), False)

    def test_check_draw_in_progress_board(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        test_board = Board()
        test_board.set_board('1', player_one)
        test_board.set_board('9', player_two)

        self.assertEqual(check_draw(test_board), False)

    def test_check_draw_almost_full_board(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        test_board = Board()
        test_board.set_board('1', player_one)
        test_board.set_board('2', player_two)
        test_board.set_board('3', player_one)
        test_board.set_board('4', player_two)
        test_board.set_board('5', player_one)
        test_board.set_board('6', player_two)
        test_board.set_board('7', player_one)
        test_board.set_board('8', player_two)

        self.assertEqual(check_draw(test_board), False)

    def test_check_draw_full_board(self):
        player_one = Player('x', 'Player One')
        player_two = Player('x', 'Player Two')
        test_board = Board()
        test_board.set_board('1', player_one)
        test_board.set_board('2', player_two)
        test_board.set_board('3', player_one)
        test_board.set_board('4', player_two)
        test_board.set_board('5', player_one)
        test_board.set_board('6', player_two)
        test_board.set_board('7', player_one)
        test_board.set_board('8', player_two)
        test_board.set_board('9', player_one)


        self.assertEqual(check_draw(test_board), True)

    def test_create_board(self):
        test_board = create_board()
        test_board_type = type(test_board)
        
        self.assertEqual(test_board_type, Board)

    def test_player_initialization(self):
        test_player = Player('X', 'Athena')
        
        self.assertEqual(test_player.symbol, '  X  ')
        self.assertEqual(test_player.player_name, 'Athena')
        self.assertEqual(test_player.wins, 0)

    def test_player_initialization_not_equal(self):
        test_player = Player('X', 'Athena')

        self.assertNotEqual(test_player.symbol, '  P  ')
        self.assertNotEqual(test_player.player_name, 'Thor')
        self.assertNotEqual(test_player.wins, 10)

    def test_player_class_get_symbol(self):
        test_player = Player('X', 'Athena')
        self.assertEqual(test_player.get_symbol(), '  X  ')

        test_player2 = Player('W', 'Athena')
        self.assertEqual(test_player2.get_symbol(), '  W  ')

        test_player3 = Player('$', 'Athena')
        self.assertEqual(test_player3.get_symbol(), '  $  ')

    def test_player_class_get_wins(self):
        test_player = Player('X', 'Athena')
        self.assertEqual(test_player.get_wins(), 0)

        test_player2 = Player('X', 'Athena')
        test_player2.wins = 5
        self.assertEqual(test_player2.get_wins(), 5)

    def test_player_class_get_player_name(self):
        test_player = Player('X', 'Athena')
        self.assertEqual(test_player.get_player_name(), 'Athena')

        test_player2 = Player('X', 'Thor')
        self.assertEqual(test_player2.get_player_name(), 'Thor')

        test_player3 = Player('X', 'RA123')
        self.assertEqual(test_player3.get_player_name(), 'RA123')

    def test_player_class_inc_wins(self):
        test_player = Player('X', 'Athena')
        self.assertEqual(test_player.inc_wins(), True)

        test_player = Player('$', 'Thor')
        self.assertNotEqual(test_player.inc_wins(), False)

    def test_board_initialization(self):
        test_board = Board()
        board_exists = None
        if test_board.board:
            board_exists = True
        
        self.assertEqual(board_exists, True)

    def test_board_class_get_board_is_dictionary(self):
        test_board = Board()
        retrieved_board = test_board.get_board()
        board_type = type(retrieved_board)

        self.assertEqual(board_type, dict)

    def test_board_class_get_board_is_correct_length(self):
        test_board = Board()
        retrieved_board = test_board.get_board()
        board_length = len(retrieved_board)

        self.assertEqual(board_length, 9)
    
    def test_board_class_set_board(self):
        test_board = Board()
        self.assertEqual(test_board.set_board('1', 10), True)

        test_board2 = Board()
        self.assertEqual(test_board2.set_board('3', "hello"), True)
    
    def test_board_class_set_board_change_value(self):
        test_board = Board()
        test_board.set_board('1', 100)
        retrieved_board = test_board.get_board()

        self.assertEqual(retrieved_board['1'], 100)

        test_board2 = Board()
        test_board2.set_board('5', True)
        retrieved_board = test_board2.get_board()

        self.assertEqual(retrieved_board['5'], True)

    def test_board_class_set_board_add_key_value_pair(self):
        test_board = Board()
        test_board.set_board('10', 100)
        retrieved_board = test_board.get_board()

        self.assertEqual(retrieved_board['10'], 100)

    def test_board_class_set_board_add_and_change_key_value_pair(self):
        test_board = Board()
        test_board.set_board('10', 100)
        test_board.set_board('10', True)
        retrieved_board = test_board.get_board()

        self.assertEqual(retrieved_board['10'], True)

    def test_book_class_initialization(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        self.assertEqual(test_book.title, "Percy Jackson")
        self.assertEqual(test_book.author, "Rick Riordan")
        self.assertEqual(test_book.checked_out, False)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        self.assertEqual(test_book2.title, "Harry Potter")
        self.assertEqual(test_book2.author, "J.K. Rowling")
        self.assertEqual(test_book2.checked_out, False)

    def test_book_class_check_out_book(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        test_book.check_out()
        self.assertEqual(test_book.checked_out, True)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        test_book2.check_out()
        self.assertEqual(test_book2.checked_out, True)

    def test_book_class_check_out_book_already_checked_out(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        test_book.checked_out = True
        self.assertEqual(test_book.check_out(), False)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        test_book2.checked_out = True
        self.assertEqual(test_book2.check_out(), False)

    def test_book_class_return_book(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        test_book.return_book()
        self.assertEqual(test_book.checked_out, False)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        test_book2.return_book()
        self.assertEqual(test_book2.checked_out, False)
    
    def test_book_class_return_book_not_checked_out(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        self.assertEqual(test_book.return_book(), False)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        self.assertEqual(test_book2.return_book(), False)

    def test_book_class_put_hold(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        test_book.put_hold("Tony Stark")
        self.assertEqual(test_book.hold, "Tony Stark")

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        test_book2.put_hold("Steve Rogers")
        self.assertEqual(test_book2.hold, "Steve Rogers")
    
    def test_book_class_put_hold_already_on_hold(self):
        test_book = Book("Percy Jackson", "Rick Riordan")
        test_book.put_hold("Tony Stark")
        self.assertEqual(test_book.put_hold("Pepper Pots"), False)

        test_book2 = Book("Harry Potter", "J.K. Rowling")
        test_book2.put_hold("Steve Rogers")
        self.assertEqual(test_book2.put_hold("Bucky Barnes"), False)


    

