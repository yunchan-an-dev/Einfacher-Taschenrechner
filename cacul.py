from tkinter import Tk, Label, Button, StringVar
from tkinter import ttk
from math import sqrt

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Einfacher Taschenrechner")
        self.window.geometry("300x200")

        self.display_text = StringVar()
        self.display_text.set("0")
        self.result = None

        self.create_widgets()

    def create_widgets(self):
        display = Label(
            self.window,
            textvariable=self.display_text,
            bg="grey",
            font=("Arial", 24),
            fg="black"
        )
        self.display = display
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttongrid = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("√", 5, 0), ("x^2", 5, 1), ("C", 5, 2), ("←", 5, 3)
        ]
        for (text, row, col) in buttongrid:
            if text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                command = lambda t=text: self.on_number_click(t)
            elif text in ["+", "-", "*", "/"]:
                command = lambda op=text: self.on_operator_click(op)
            elif text == "=":
                command = self.on_equals_click
            elif text == "√":
                command = self.on_sqrt_click
            elif text == "x^2":
                command = self.on_square_click
            elif text == "C":
                command = self.on_clear_click
            elif text == "←":
                command = self.on_backspace_click
            button = Button(
                self.window,
                text=text,
                width=5,
                height=2,
                command=command
            )      
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_number_click(self, value):
        if value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            self.display_text.set(self.display_text.get() + value)
            self.update_display()

    def on_operator_click(self, op):
        if op in ["+", "-", "*", "/"]:
            self.display_text.set(self.display_text.get() + f" {op} ")
            self.update_display()

    def on_equals_click(self):
        if self.display_text.get() == "":
            return
        try:
            expression = self.display_text.get()
            result = eval(expression)
            self.display_text.set(str(result))
        except Exception as e:
            self.display_text.set("Error")
        self.update_display()

    def on_sqrt_click(self):
        if self.display_text.get() == "":
            return
        try:
            current = float(self.display_text.get())
            result = sqrt(current)
            self.display_text.set(str(result))
            self.update_display()
        except Exception as e:
            self.display_text.set("Error")
        self.update_display()

    def on_square_click(self):
        if self.display_text.get() == "":
            return
        try:
            current = float(self.display_text.get())
            result = current ** 2
            self.display_text.set(str(result))
        except Exception as e:
            self.display_text.set("Error")
        self.update_display()

    def on_clear_click(self):
        self.display_text.set("0")
        self.update_display()

    def on_backspace_click(self):
        current = self.display_text.get()
        self.display_text.set(current[:-1])
        self.update_display()

    def update_display(self):
        self.display.config(text=self.display_text.get())

if __name__ == "__main__":
    calculator = Calculator()
    calculator.window.mainloop()