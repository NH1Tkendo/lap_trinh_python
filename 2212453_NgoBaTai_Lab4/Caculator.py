from tkinter import Tk, W, E, StringVar
from tkinter.ttk import Frame, Style, Button, Entry


class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.expression = ""
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5), font="serif 10")

        for i in range(4):
            self.columnconfigure(i, pad=3)

        for i in range(5):
            self.rowconfigure(i, pad=3)

        self.equation = StringVar()
        entry = Entry(self, textvariable=self.equation)
        entry.grid(row=0, columnspan=4, sticky=W + E)

        # Hàng 1: Cls, Back, (trống), Close
        Button(self, text="Cls", command=self.clear).grid(row=1, column=0)
        Button(self, text="Back", command=self.backspace).grid(row=1, column=1)
        Button(self).grid(row=1, column=2)  # Nút trống
        Button(self, text="Close", command=self.parent.quit).grid(row=1, column=3)

        # Các nút số và toán tử
        buttons = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
        ]

        for text, row, col in buttons:
            Button(self, text=text, command=lambda t=text: self.press(t)).grid(
                row=row, column=col
            )

        self.pack()

    def press(self, num):
        self.expression += str(num)
        self.equation.set(self.expression)

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = result  # Lưu kết quả để tiếp tục tính toán
        except:
            self.equation.set("Error")
            self.expression = ""


root = Tk()
app = Calculator(root)
root.mainloop()
