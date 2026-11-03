import tkinter as tk
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("450x600")
        self.result_var = tk.StringVar(value="0")