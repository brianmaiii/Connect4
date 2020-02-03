import connectfour
import math
import tkinter


class Game_TK:
    def __init__(self, col, row, state):
        """Constructor that sets up the screen."""
        self._state = state

        self._SQUARESIZE = 100
        width = col * self._SQUARESIZE
        height = row * self._SQUARESIZE

        self._window = tkinter.Tk()
        self._window.title('Connect Four')

        frame = tkinter.Frame(self._window, width=width, height=60)
        frame.bind("<Button-1>", self.callback)
        frame.bind("<Button-3>", self.callback2)
        frame.pack()
        self._canvas = tkinter.Canvas(self._window, width=width, height=height)
        self.draw_board(self._state)
        self._canvas.pack()
        self._window.mainloop()
        #self.rectangle

    def draw_board(self, state):
        """Draws the board onto the screen."""
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        for y in range(connectfour.BOARD_COLUMNS):
            x1 = y * 100
            y1 = 2
            x2 = x1 + 100
            y2 = y1 + 100
            for x in range(connectfour.BOARD_ROWS):
                if state[0][y][x] == 0:
                    self._canvas.create_oval(x1+4, y1+3, x2, y2,
                                             fill='black')
                if state[0][y][x] == 1:
                    self._canvas.create_oval(x1+4, y1+3, x2, y2,
                                             fill='green')
                if state[0][y][x] == 2:
                    self._canvas.create_oval(x1+4, y1+3, x2, y2,
                                             fill='orange')
                y1 += 100
                y2 += 100

    def callback(self, event):
        """Handels left button click for gui.(drop move)"""
        try:
            col = math.floor(event.x/self._SQUARESIZE)
            self._state = connectfour.drop(self._state, col)
            self.draw_board(self._state)
            self.check_winner()
        except (connectfour.InvalidMoveError, connectfour.GameOverError):
            print("INVALID MOVE")

    def callback2(self, event):
        """Handels right button click for gui.(pop move)"""
        try:
            col = math.floor(event.x/self._SQUARESIZE)
            self._state = connectfour.pop(self._state, col)
            self.draw_board(self._state)
            self.check_winner()
        except (connectfour.InvalidMoveError, connectfour.GameOverError):
            print("INVALID MOVE")

    def check_winner(self):
        """Checks if there is a winner and prints a winner message."""
        self.draw_board(self._state)
        if connectfour.winner(self._state) == 1:
            if connectfour.BOARD_COLUMNS >= 4:
                self._canvas.create_text((connectfour.BOARD_COLUMNS/2)*100, (connectfour.BOARD_ROWS/2)*100, fill="red", font=("Helvetica Bold", "40"),
                                         text="Player One Wins")
            else:
                self._canvas.create_text((connectfour.BOARD_COLUMNS/2)*100, (connectfour.BOARD_ROWS/2)*100, font=("Helvetica Bold", "13"), fill="red",
                                         text="P One Wins")

        if connectfour.winner(self._state) == 2:
            if connectfour.BOARD_COLUMNS >= 4:
                self._canvas.create_text((connectfour.BOARD_COLUMNS/2)*100, (connectfour.BOARD_ROWS/2)*100, font=("Helvetica Bold", "40"), fill="red",
                                         text="Player Two Wins")
            else:
                self._canvas.create_text((connectfour.BOARD_COLUMNS/2)*100, (connectfour.BOARD_ROWS/2)*100, font=("Helvetica Bold", "13"), fill="red",
                                         text="P Two Wins")
