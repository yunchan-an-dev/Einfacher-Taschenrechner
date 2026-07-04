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
        button.pack()

    def on_number_click(self, value):
        if self.result is not None:
            self.display_text.set(value)
            self.result = None
        else:
            current = self.display_text.get()
            if current == "0":
                self.display_text.set(value)
            else:
                self.display_text.set(current + value)

    def on_operator_click(self, operator):
        if operator in ["+", "-", "*", "/"]:
            self.display_text += f" {operator} "
            self.update_display()

    def on_equals_click(self):
        if equals in ["="]:
            eval self.display_text.get()
            show result = eval(self.display_text.get())
            result = eval(self.display_text.get())

    def on_sqrt_click(self):
        if sqrt in ["√"]:
            result = sqrt(float(self.display_text.get()))
            self.display_text = str(result)
            self.update_display()

    def on_square_click(self):
        if "x^2" in ["x^2"]:
            result = float(self.display_text.get()) ** 2
            self.display_text = str(result)
            self.update_display()

    def on_clear_click(self):
        if "C" in ["C"]:
            self.display_text = ""
            self.update_display()

    def on_backspace_click(self):
        if "←" in ["←"]:
            current = self.display_text.get()
            self.display_text.set(current[:-1])
            self.update_display()

    def update_display(self):
        self.display.config(text=self.display_text.get())