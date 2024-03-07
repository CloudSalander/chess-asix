import tkinter as tk

class ChessBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess")
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.setup_pieces()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "white"
                else:
                    color = "gray"
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def setup_pieces(self):
        pieces = {
            "wr1": "♖", "wn1": "♘", "wb1": "♗", "wq": "♕", "wk": "♔", "wb2": "♗", "wn2": "♘", "wr2": "♖",
            "wp1": "♙", "wp2": "♙", "wp3": "♙", "wp4": "♙", "wp5": "♙", "wp6": "♙", "wp7": "♙", "wp8": "♙",
            "br1": "♜", "bn1": "♞", "bb1": "♝", "bq": "♛", "bk": "♚", "bb2": "♝", "bn2": "♞", "br2": "♜",
            "bp1": "♟", "bp2": "♟", "bp3": "♟", "bp4": "♟", "bp5": "♟", "bp6": "♟", "bp7": "♟", "bp8": "♟"
        }
        for piece, symbol in pieces.items():
            row, col = self.get_position(piece)
            x, y = col * 50 + 25, row * 50 + 25
            self.canvas.create_text(x, y, text=symbol, font=("Arial", 24))

    def get_position(self, square):
        letters = "abcdefgh"
        numbers = "87654321"
        col = letters.index(square[1])
        row = numbers.index(square[2])
        return row, col

def main():
    root = tk.Tk()
    chess_board = ChessBoard(root)
    root.mainloop()

if __name__ == "__main__":
    main()

