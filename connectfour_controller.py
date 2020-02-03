import connectfour_view as cfmodel
import connectfour


def welcome_message() -> str:
    """Welcomes the user to the game. Provides instructions on how to play."""
    print()
    print("Welcome to Connect Four! We are excited to have you play!")
    dash = '-' * 80
    print(dash)
    print("""HOW TO PLAY:

DROP: Click the left button of your mouse to activate DROP.
      DROP allows you to drop ONE colored disc in the column of your choosing.
      Once you decide to drop in a column, it is the next players turn.
      In order to DROP it is important that you click ON TOP of the board.
      The disc will NOT DROP unless you click above the column indicated.
      
POP:  Click the right button of your mouse to activate POP.
      POP lets you REMOVE the FIRST colored disc in the indicated column.
      You can only use POP if you have already placed a disc in a column.
      You may not go twice. Once you use POP it is the next players turn.
      You may not POP another players colored disc.
      Mac Users: You may need to click with two fingers to use. """)
    print()
    print("Do you want a customized board or the default 6x7?")


if __name__ == '__main__':
    inputInvalid = False
    runTime = True
    initialBool = False
    responseInt = False
    welcome = welcome_message()
    # While loop that starts the game asking for settings and such.
    while not responseInt:
        try:
            response = int(input("Press 1 for default board or 2 to customize: "))
            if response < 3 and response > 0:
                responseInt = True
                break
            else:
                print("You entered invalid input.")
                print()
        except ValueError:
            print("You entered invalid input.")
            print()
    while not initialBool:
        if response == 1:
            initialBool = True
            state = connectfour.new_game()
            game1 = cfmodel.Game_TK(connectfour.BOARD_COLUMNS, connectfour.BOARD_ROWS, state)
        elif response == 2:
            try:
                print()
                print("How many rows would you like on your board?")
                rows = int(input("Please enter a valid number of rows (ex. 4): "))
                connectfour.BOARD_ROWS = rows
                print("How many columns would you like on your board?")
                cols = int(input("Please enter a valid number of columns (ex. 4): "))
                connectfour.BOARD_COLUMNS = cols
                if rows < 4 and cols < 4:
                    print()
                    print("Invalid Board. Custom board not possible")
                    print("Either Rows or Columns must be 4 or greater.")
                    print("Please try again.")
                    print()
                else:
                    initialBool = True
                    state = connectfour.new_game()
                    game1 = cfmodel.Game_TK(connectfour.BOARD_COLUMNS,
                                            connectfour.BOARD_ROWS, state)
            except ValueError:
                print("Invalid input.")
        else:
            print("Invalid Input.")
