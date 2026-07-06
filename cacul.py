from tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Einfacher Taschenrechner")
        self.window.geometry("300x200")

        self.display_text = tk.StringVar()
        self.display_text.set("0")
        self.result = None

        self.create_widgets()

    def create_widgets(self):
        display = tk.Label(
            self.window,
            text=self.display_text,
            bg="grey",
            font=("Arial", 24),
            fg="black"
        )
        self.display = display
        self.display.pack(pady=10)

        buttongrid = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("√", 5, 0), ("x^2", 5, 1), ("C", 5, 2), ("←", 5, 3)
        ]

        for (text, row, col) in buttongrid:
            button = tk.Button(
                self.window,
                text=text,
                width=5,
                height=2,
                command=lambda t=text: self.on_number_click(t)
        )
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_number_click(value):
        if value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            self.display_text.set(self.display_text.get() + value)
            
        else:
            self.display_text.set(value)
          

    def on_operator_click(op):
        if op in ["+", "-", "*", "/"]:
            self.display_text.set(self.display_text.get() + f" {op} ")
            self.update_display()

    def on_equals_click(equals):
        if equals in ["="]:
            try:
                expression = self.display_text.get()
                result = eval(expression)
                self.display_text.set(str(result))
            except Exception as e:
                self.display_text.set("Error")
            
    def on_sqrt_click(sqrt):
        if sqrt in ["√"]:
            result = sqrt(float(self.display_text.get()))
            sqrt.display_text.set(str(result))
            sqrt.update_display()

    def on_square_click(square):
        if square in ["x^2"]:
            result = float(square.display_text.get()) ** 2
            square.display_text.set(str(result))
            square.update_display()

    def on_clear_click(c):
        if c in ["C"]:
            self.display_text.set("")
            self.update_display()

    def on_backspace_click(back):
        if back in ["←"]:
            current = back.display_text.get()
            back.display_text.set(current[:-1])
            back.update_display()

    def update_display(self):
        self.display.config(text=self.display_text.get())

#----------------main
if __name__ == "__main__":
    calculator = Calculator()
    calculator.window.mainloop()