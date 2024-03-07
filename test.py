import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create a rectangle
rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Add text to the rectangle
text = canvas.create_text(100, 100, text="Hello", fill="white", font=("Arial", 12))

root.mainloop()