import tkinter as tk
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("450x600")
        self.result_var = tk.StringVar(value="0")
        
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 36), justify="right", bd=10, relief="sunken", bg="black", fg="white")
        display.pack(fill="both", padx=20, pady=20, ipady=15)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
                
     # اصلاح گرید: دکمه 0 در ستون 0 با colspan=2 و دکمه نقطه در ستون 2
     buttons = [
         ("C", 0, 0, self.clear), ("<-", 0, 1, self.backspace), ("+/-", 0, 2, self.negate), ("/", 0, 3, lambda: self.add_op("/")),
         ("7", 1, 0, lambda: self.add_num(7)), ("8", 1, 1, lambda: self.add_num(8)), ("9", 1, 2, lambda: self.add_num(9)), ("*", 1, 3, lambda: self.add_op("*")),
         ("4", 2, 0, lambda: self.add_num(4)), ("5", 2, 1, lambda: self.add_num(5)), ("6", 2, 2, lambda: self.add_num(6)), ("-", 2, 3, lambda: self.add_op("-")),
         ("1", 3, 0, lambda: self.add_num(1)), ("2", 3, 1, lambda: self.add_num(2)), ("3", 3, 2, lambda: self.add_num(3)), ("+", 3, 3, lambda: self.add_op("+")),
         ("0", 4, 0, lambda: self.add_num(0), 2), (".", 4, 2, lambda: self.add_num(".")), ("=", 4, 3, self.calculate),
     ]
    
    for btn in buttons:
                 if len(btn) == 4:
                     text, row, col, cmd = btn
                     colspan = 1
                 else:
                     text, row, col, cmd, colspan = btn
                     color = "red" if text == "C" else "orange" if text == "=" else "gray" if text in ["/", "*", "-", "+"] else "lightgray"