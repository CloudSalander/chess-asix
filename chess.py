import tkinter as tk

class ChessboardGUI:
    def __init__(self, master, size=8, square_size=50):
        self.master = master
        self.size = size
        self.square_size = square_size
        self.canvas = tk.Canvas(master, width=size * square_size, height=size * square_size)
        self.canvas.pack()

        self.draw_chessboard()
        self.place_chess_pieces()

    def draw_chessboard(self):
        colors = ["cyan", "yellow"]
        for row in range(self.size):
            for col in range(self.size):
                color = colors[(row + col) % 2]
                x0, y0 = col * self.square_size, row * self.square_size
                x1, y1 = x0 + self.square_size, y0 + self.square_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def place_chess_pieces(self):
        piece_positions = {
            (0, 0): "♜", (0, 7): "♜",
            (7, 0): "♖", (7, 7): "♖",
            (0, 1): "♞", (0, 6): "♞",
            (7, 1): "♘", (7, 6): "♘",
            (0, 2): "♝", (0, 5): "♝",
            (7, 2): "♗", (7, 5): "♗",
            (0, 3): "♛", (7, 3): "♕",
            (0, 4): "♚", (7, 4): "♔"
        }
       
        for i in range(8):
            piece_positions[(1,i)] = "\u265F"
            piece_positions[(6,i)] = "\u2659"
    
        for position, piece in piece_positions.items():
            x, y = position
            x_center = (x + 0.5) * self.square_size
            y_center = (y + 0.5) * self.square_size
            self.canvas.create_text(x_center, y_center, text=piece, font=("Arial", 20))
   

if __name__ == "__main__":
    tablero = tk.Tk()
    tablero.title("Ajedrez 2.0")
    chessboard_gui = ChessboardGUI(tablero)
    tablero.mainloop()
