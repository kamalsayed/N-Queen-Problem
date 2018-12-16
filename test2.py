import tkinter as tk
import copy
class GameBoard(tk.Frame):
    def __init__(self,parent, rows=8, columns=8, size=32, color1="white", color2="black"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=4, pady=4)
        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)
    def addpiece(self, name, image, row=0, column=0):
            '''Add a piece to the playing board'''
            self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
            self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
            '''Place a piece at the given row/column'''
            self.pieces[name] = (row, column)
            x0 = (column * self.size) + int(self.size / 2)
            y0 = (row * self.size) + int(self.size / 2)
            self.canvas.coords(name, x0, y0)

    def refresh(self, event):
            '''Redraw the board, possibly in response to window being resized'''
            xsize = int((event.width - 1) / self.columns)
            ysize = int((event.height - 1) / self.rows)
            self.size = min(xsize, ysize)
            self.canvas.delete("square")
            color = self.color2
            for row in range(self.rows):
                color = self.color1 if color == self.color2 else self.color2
                for col in range(self.columns):
                    x1 = (col * self.size)
                    y1 = (row * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                    color = self.color1 if color == self.color2 else self.color2
            for name in self.pieces:
                self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
            self.canvas.tag_raise("piece")
            self.canvas.tag_lower("square")


if __name__ == "__main__":
    def take_input():
        """Accepts the size of the chess board"""
        while True:
            try:
                size = int(input('What is the size of the chessboard? n = \n'))

                if size <= 3:
                    print("Enter a value such that size>=4")
                    continue
                return size
            except ValueError:
                print("Invalid value entered. Enter again")


    def get_board(size):
        """Returns an n by n board"""
        board = [0] * size
        for ix in range(size):
            board[ix] = [0] * size
        return board

    #each time get a new column to check the safety of it's left side of the row and -              -
    def is_safe(board, row, col, size):                                             #  -          -
        """Check if it's safe to place a queen at board[x][y]"""                       # -  &&  -

        # check row on left side
        for iy in range(col):
            if board[row][iy] == 1:
                return False

        ix, iy = row, col
        #-
        #  -
        #    -
        while ix >= 0 and iy >= 0:
            if board[ix][iy] == 1:
                return False
            ix -= 1
            iy -= 1

        jx, jy = row, col
        while jx < size and jy >= 0:
            if board[jx][jy] == 1:
                return False
            jx += 1
            jy -= 1

        return True

    def solve(board, col, size):
        """Use backtracking to find all solutions"""
        # base case
        if col >= size:
            return

        for i in range(size):
            if is_safe(board, i, col, size):
                board[i][col] = 1
                if col == size - 1:
                    add_solution(board)
                    board[i][col] = 0 #to use it again
                    return
                solve(board, col + 1, size)
                # backtrack
                board[i][col] = 0 #to use it again

    def add_solution(board):
        """Saves the board state to the global variable 'solutions'"""
        global solutions
        saved_board = copy.deepcopy(board)
        solutions.append(saved_board)

    #smile icon code
    imagedata = '''
            R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
            ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
            R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
            P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
            fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
            Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
            e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
            nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
            ////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
            aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
            +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
            kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
            BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
            yxYYEAA7
        '''
    size = take_input()
    board = get_board(size)
    solutions = []
    solve(board, 0, size)
    s = size
    root = tk.Tk()
    b= GameBoard(root,rows=s,columns=s)
    b.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    Queen = tk.PhotoImage(data=imagedata)
    for _ in range(size):
        for x in range(size):
            if solutions[0][_][x] == 1:
                b.addpiece("Queen"+str(x),Queen ,_, x)

    print("Total solutions = {}".format(len(solutions)))

    root.mainloop()
