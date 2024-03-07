import tkinter as tk

class Chessboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chessboard")
        self.geometry("400x400")
        self.pieces = {
            "00": "♖", "01": "♘", "02": "♗", "03": "♕", "04": "♔", "05": "♗", "06": "♘", "07": "♖",
            "10": "♙", "11": "♙", "12": "♙", "13": "♙", "14": "♙", "15": "♙", "16": "♙", "17": "♙",
            "70": "♜", "71": "♞", "72": "♝", "73": "♛", "74": "♚", "75": "♝", "76": "♞", "77": "♜",
            "60": "♟", "61": "♟", "62": "♟", "63": "♟", "64": "♟", "65": "♟", "66": "♟", "67": "♟"
        }
        self.create_board()

    def create_board(self):
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        colors = ["white", "black"]
        self.squares = {}
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                square_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.squares[square_id] = (row, col)
                self.canvas.tag_bind(square_id, "<Button-1>", self.on_square_clicked)
                if row < 2 or row > 5: 
                    text_id = self.create_piece(row,col,x1,y1)

    
    def create_piece(self,row,col,x,y):
        piece = self.pieces.get(str(row)+str(col))
        piece_color = "blue" 
        if row < 2: piece_color = "red"
        return self.canvas.create_text(x+25, y+25, text=piece, fill=piece_color, font=("Arial", 24))

    def on_square_clicked(self, event):
        square_id = event.widget.find_closest(event.x, event.y)[0]
        row, col = self.squares[square_id]
        print("Square clicked:", row, col)


if __name__ == "__main__":
    app = Chessboard()
    app.mainloop()
