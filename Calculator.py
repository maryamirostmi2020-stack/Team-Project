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