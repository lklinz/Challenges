from colorama import Fore,Style
import os
import time

def remaining(starting_x,starting_y,x,y):
    remaining_for_x = starting_x - x
    remaining_for_y = starting_y - y
    return remaining_for_x,remaining_for_y

def bigger(x_win,y_win,x,y):
    if x>y:
        x_win += 1
    elif x<y:
        y_win += 1
    elif x == y:
        x_win += 0
        y_win += 0
    return x_win,y_win

def print_board(remaine):
    if 79 <remaine<=99:
        print(Fore.YELLOW + '|99~79|')
        print(Fore.YELLOW+'|79~59|')
        print(Fore.YELLOW+'|59~39|')
        print(Fore.YELLOW+'|39~19|')
        print(Fore.YELLOW+'|19~0|')
    elif 59 <remaine<=79:
        print(Fore.BLACK + '|99~79|')
        print(Fore.YELLOW+'|79~59|')
        print(Fore.YELLOW+'|59~39|')
        print(Fore.YELLOW+'|39~19|')
        print(Fore.YELLOW+'|19~0|')
    elif 39 <remaine<=59:
        print(Fore.BLACK + '|99~79|')
        print(Fore.BLACK+'|79~59|')
        print(Fore.YELLOW+'|59~39|')
        print(Fore.YELLOW+'|39~19|')
        print(Fore.YELLOW+'|19~0|')
    elif 19 <remaine<=39:
        print(Fore.BLACK + '|99~79|')
        print(Fore.BLACK+'|79~59|')
        print(Fore.BLACK+'|59~39|')
        print(Fore.YELLOW+'|39~19|')
        print(Fore.YELLOW+'|19~0|')
    else:
        print(Fore.BLACK + '|99~79|')
        print(Fore.BLACK+'|79~59|')
        print(Fore.BLACK+'|59~39|')
        print(Fore.BLACK+'|39~19|')
        print(Fore.YELLOW+'|19~0|')
    print()

def winner(x_win,y_win,starting_x,starting_y):
    turn = 0
    while x_win + y_win != 9 and x_win != 5 and y_win !=5:

        print(Fore.CYAN+"X'board")
        print_board(starting_x)
        print(Fore.CYAN+"Y'board")
        print_board(starting_y)

        if turn == 0 or x > y or x==y:
            if turn == 0:
                print(Fore.GREEN + 'First turn')
            elif x>y:
                print(Fore.LIGHTMAGENTA_EX+'X won and can start this round')
            elif x==y:
                print(Fore.LIGHTRED_EX+'Draw.Replay')

            print(Style.RESET_ALL+"Enter your x")       
            x = int(input())
            while x > starting_x:
                print('Your number is out of range. Please enter again')
                x = int(input())
    
            time.sleep(3)  # Give Player 1 a moment to read the input
            os.system('cls' if os.name == 'nt' else 'clear') 

            print(f'X win is: {x_win},Y win is {y_win}')

            if x > 9:
                print('X chose White')
            else:
                print('X chose Black')

        #Print the board for Y player to see if X's light is on or off without modifying the remaining of x and y
            for_y_board = remaining(starting_x,starting_y,x,0)
            print(Fore.CYAN + "X's Board")
            print_board(for_y_board[0])
            print(Fore.CYAN + "Y's Board")
            print_board(for_y_board[1])

            print(Style.RESET_ALL+"Enter your y")
            y = int(input())
            while y > starting_y:
                print('Your number is out of range. Please enter again ')
                y = int(input())

            time.sleep(3)  # Give Player 1 a moment to read the input
            os.system('cls' if os.name == 'nt' else 'clear') 

            if y > 9:
                print('Y chose White')
            else:
                print('Y chose Black')

        elif y > x:

            print(Fore.LIGHTMAGENTA_EX + 'Y won and can start this round')

            print(Style.RESET_ALL+"Enter your y")
            y = int(input())
            while y > starting_y:
                print('Your number is out of range. Please enter again ')
                y = int(input())
            time.sleep(3)  # Give Player 1 a moment to read the input
            os.system('cls' if os.name == 'nt' else 'clear') 

            print(f'X win is: {x_win},Y win is {y_win}')

            if y > 9:
                print('Y chose White')
            else:
                print('Y chose Black')

        #Print the board for Y player to see if X's light is on or off without modifying the remaining of x and y
            for_x_board = remaining(starting_x,starting_y,0,y)
            print(Fore.CYAN + "X's Board")
            print_board(for_x_board[0])
            print(Fore.CYAN + "Y's Board")
            print_board(for_x_board[1])

            print(Style.RESET_ALL+"Enter your x")
            x = int(input())
            while x > starting_x:
                print('Your number is out of range. Please enter again ')
                x = int(input())
            time.sleep(3)  # Give Player 1 a moment to read the input
            os.system('cls' if os.name == 'nt' else 'clear') 

            if x > 9:
                print('X chose White')
            else:
                print('X chose Black')

        starting_x, starting_y = remaining(starting_x,starting_y,x,y)
        x_win,y_win = bigger(x_win,y_win,x,y)
        print(f'X win is: {x_win},Y win is {y_win}')
        turn += 1

    #Print the last record
    starting_x, starting_y = remaining(starting_x,starting_y,x,y)
    print(Fore.CYAN+"X'board")
    print_board(starting_x)
    print(Fore.CYAN+"Y'board")
    print_board(starting_y)
    print(turn)
    print(f'X win is: {x_win},Y win is {y_win}')

    #Determine the winner
    if x_win > y_win:
        print('X won')
    else:
        print('Y won')
    
winner(0,0,99,99)