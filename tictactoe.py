from player import Player
from board import Board
import os
import time
import sys

def draw_board(dictionary):
    # Clear everything in the console
    os.system('clear')
    # Checks to make sure everything in the dictionary is a string, if not it prints an error message.
    for i in dictionary:
        if type(dictionary[i]) == Player or dictionary[i] == False:
            continue
        else:
            print("Error with the board.")
            return False
    
    # Spots for the board that are going to be used to print.
    spot_dict = {}
    
    # For loop that puts the items from the dictionary into the variables for printing
    spotCounter = 1
    for i in dictionary: 
        if dictionary[i] == False:
            spot_dict[str(spotCounter)] = ('  ' + str(spotCounter) + '  ')
        else:
            spot_dict[str(spotCounter)] = dictionary[i].get_symbol()
        
        spotCounter += 1

    # draw the board
    print('\n')
    print(spot_dict['1'], spot_dict['2'], spot_dict['3'], "\n")
    print(spot_dict['4'], spot_dict['5'], spot_dict['6'], "\n")
    print(spot_dict['7'], spot_dict['8'], spot_dict['9'], "\n")

    return True

def get_input(prompt):
    valid = False
    user_input = None
    while valid == False:
        user_input = input(prompt)
        if not user_input:
            print("Nothing was entered, please try again...")
        elif len(user_input) > 1:
            print("Too many characters, please try again...")
        else:
            valid = True
        os.system('clear')
    return user_input


def player_turn(player, board):
    game_board = board.get_board()
    draw_board(game_board)
    print(player.get_player_name() + ", it's your turn!" )
    turn_input = get_input("Pick a spot on the board: ")
    if turn_input in game_board:
        if game_board[turn_input] != False:
            print("That space is already taken, please try again...")
            time.sleep(1.5)
            player_turn(player, board)
        else:
            game_board[turn_input] = player
            return
    else:
        print("That space is invalid, please try again...")
        time.sleep(1.5)
        player_turn(player, board)

def check_win(board):
    game_board = board.get_board()

    if game_board['1'] != False and game_board['1'] == game_board['2'] and game_board['2'] == game_board['3']:
        victor = game_board['1']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)

    if game_board['1'] != False and game_board['1'] == game_board['4'] and game_board['4'] == game_board['7']:
        victor = game_board['1']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)

    if game_board['1'] != False and game_board['1'] == game_board['5'] and game_board['5'] == game_board['9']:
        victor = game_board['1']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)

    if game_board['7'] != False and game_board['7'] == game_board['8'] and game_board['8'] == game_board['9']:
        victor = game_board['7']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)

    if game_board['3'] != False and game_board['3'] == game_board['6'] and game_board['6'] == game_board['9']:
        victor = game_board['3']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)

    if game_board['3'] != False and game_board['3'] == game_board['5'] and game_board['5'] == game_board['7']:
        victor = game_board['3']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)
    
    if game_board['2'] != False and game_board['2'] == game_board['5'] and game_board['5'] == game_board['8']:
        victor = game_board['2']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)
    
    if game_board['4'] != False and game_board['4'] == game_board['5'] and game_board['5'] == game_board['6']:
        victor = game_board['4']
        victor.inc_wins()
        victor_name = victor.get_player_name()
        print(victor_name + " has won the game! Total wins: " + str(victor.get_wins()))
        time.sleep(1)
        print("To play again, press 'y'.  If you would like to be done, press any other character.")
        time.sleep(0.25)
        play_again = get_input("What would you like to do: ")
        if play_again == 'y':
            return True
        else:
            sys.exit(0)
    return False

def check_draw(board):
    game_board = board.get_board()
    space_counter = 0

    for i in game_board:
        "entered"
        if game_board[i] == False:
            print('False')
            space_counter += 1
    
    if space_counter == 0:
        return True
    else:
        return False

def create_board():
    return Board()

def main():
    os.system('clear')
    gameBoard = create_board()
    playing = True
    playerOne = Player(get_input("Player one, pick a letter or character for your TicTacToe symbol: "), "Player one")
    playerTwo = Player(get_input("Player two, pick a letter or character for your TicTacToe symbol: "), "Player two")
    while playing == True:
        player_turn(playerOne, gameBoard)
        if check_win(gameBoard) == True:
            gameBoard = create_board()
            continue
        if check_draw(gameBoard) == True:
            print("The game was a draw! Resetting the board...")
            time.sleep(1.5)
            gameBoard = create_board()
            continue
        player_turn(playerTwo, gameBoard)
        if check_win(gameBoard) == True:
            gameBoard = create_board()
            continue
        if check_draw(gameBoard) == True:
            print("The game was a draw! Resetting the board...")
            time.sleep(1.5)
            gameBoard = create_board()
            continue

if __name__ == "__main__":
    main()
