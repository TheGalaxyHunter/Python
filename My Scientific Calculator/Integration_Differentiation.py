from tkinter import *
from tkinter import ttk
from sympy import *


class Calculus:
    def __init__(self, root1):  # ----- __init__ -----
        # Will hold the changing value stored in the entry
        self.value = StringVar(root1, value="")
        self.value1 = StringVar(root1, value="")
        self.value2 = StringVar(root1, value="")
        self.value3 = StringVar(root1, value="")

        # Title of the Application
        root1.title("Calculus")

        # Width and Height of the Application
        root1.geometry("408x290")

        # Setting application resizable false
        root1.resizable(width=False, height=False)

        def opButtons(frame, entry):
            self.bClear = Button(frame, text='CLR', font="Serif 10", command=lambda: entry.delete(0, END), width=3)
            self.b1 = Button(frame, text='+', font="Serif 12", command=lambda: self.bpress('+', entry), width=2)
            self.b2 = Button(frame, text='-', font="Serif 12", command=lambda: self.bpress('-', entry), width=2)
            self.b3 = Button(frame, text='*', font="Serif 12", command=lambda: self.bpress('*', entry), width=2)
            self.b4 = Button(frame, text='/', font="Serif 12", command=lambda: self.bpress('/', entry), width=2)
            self.b5 = Button(frame, text='^', font="Serif 12", command=lambda: self.bpress('^', entry), width=2)
            self.b6 = Button(frame, text='√', font="Serif 12", command=lambda: self.bpress('√', entry), width=2)
            self.b7 = Button(frame, text='(', font="Serif 12", command=lambda: self.bpress('(', entry), width=2)
            self.b8 = Button(frame, text=')', font="Serif 12", command=lambda: self.bpress(')', entry), width=2)
            self.bClear.grid(row=2, column=1, columnspan=1, padx=1, pady=0)
            self.b1.grid(row=2, column=2, columnspan=1, padx=1, pady=0)
            self.b2.grid(row=2, column=3, columnspan=1, padx=1, pady=0)
            self.b3.grid(row=2, column=4, columnspan=1, padx=1, pady=0)
            self.b4.grid(row=2, column=5, columnspan=1, padx=1, pady=0)
            self.b5.grid(row=2, column=6, columnspan=1, padx=1, pady=0)
            self.b6.grid(row=2, column=7, columnspan=1, padx=1, pady=0)
            self.b7.grid(row=2, column=8, columnspan=1, padx=1, pady=0)
            self.b8.grid(row=2, column=9, columnspan=1, padx=1, pady=0)

        # ----- 1st Row -----
        self.r1 = Radiobutton(root1, indicatoron=0, value=1, text="INTEGRATION", font="Algerian 15",
                              command=lambda: self.differentiation(), width=14)
        self.r2 = Radiobutton(root1, indicatoron=0, value=2, text="DIFFERENTIATION", font="Algerian 15",
                              command=lambda: self.integration(), width=14)
        self.r1.grid(row=0, column=0, padx=10, pady=20)
        self.r2.grid(row=0, column=1, padx=10, pady=20)

        # ---- 1st Frame ----
        #       ----** Row 1 **----
        self.f1 = ttk.Frame(root1)
        self.f1.grid(row=1, columnspan=10, pady=10)
        ttk.Label(self.f1, text="f(x) =", font="Serif 15", width=5).grid(row=1, column=0, padx=5)
        self.e1 = ttk.Entry(self.f1, textvariable=self.value, justify=LEFT, width=26, font="Serif")
        self.e1.grid(row=1, column=1, columnspan=9, padx=5)

        #       ----** Row 2 **----
        opButtons(self.f1, self.e1)

        #       ----** Row 3 **----
        self.int = Button(self.f1, text="Integrate", font="Serif 15", command=lambda: self.integrate(), width=10)
        self.int.grid(row=3, columnspan=10, pady=15)

        #       ----** Row 4 **----
        ttk.Label(self.f1, text="∫f(x)dx =", font="Arial 14", width=8).grid(row=4, column=0, padx=5, pady=10)
        self.e2 = ttk.Entry(self.f1, textvariable=self.value1, justify=LEFT, width=26, font="Arial")
        self.e2.grid(row=4, column=1, columnspan=9, padx=5, pady=10)

        # ---- 2nd Frame ----
        #       ----** Row 1 **----
        self.f2 = ttk.Frame(root1)
        self.f2.grid(row=1, columnspan=10, pady=10)
        ttk.Label(self.f2, text="f(x) =", font="Arial 15", width=5).grid(row=1, column=0, padx=5)
        self.e3 = ttk.Entry(self.f2, textvariable=self.value2, justify=LEFT, width=26, font="Serif")
        self.e3.grid(row=1, column=1, columnspan=9, padx=5)

        #       ----** Row 2 **----
        opButtons(self.f2, self.e3)

        #       ----** Row 3 **----
        self.int = Button(self.f2, text="Differentiate", font="Serif 15", command=lambda: self.differentiate(), width=10)
        self.int.grid(row=3, columnspan=10, pady=15)

        #       ----** Row 4 **----
        ttk.Label(self.f2, text="d/dx(f(x)) =", font="Arial 14", width=8).grid(row=4, column=0, padx=5, pady=10)
        self.e4 = ttk.Entry(self.f2, textvariable=self.value3, justify=LEFT, width=26, font="Arial")
        self.e4.grid(row=4, column=1, columnspan=9, padx=5, pady=10)

    @staticmethod
    def bpress(op, entry):
        value = entry.get()

        if value != '':
            if op == '+':
                value = "{} + ".format(value)

            elif op == '*':
                value = "{} * ".format(value)

            elif op == '/':
                value = "{} / ".format(value)

            elif op == '^':
                value = "{}^".format(value)

            elif op == ')':
                value = "{})".format(value)

        if op == '-':
            value = "{}-".format(value)

        if op == '(':
            value = "{}(".format(value)

        if op == '√':
            value = "{} √".format(value)

        entry.delete(0, END)
        entry.insert(0, value)

    def differentiation(self):
        # Adjust Frames
        self.f2.grid_forget()
        self.f1.grid(row=1, columnspan=3)
        self.f1.focus()
        self.e1.focus()
        print("\nDifferentiation")

    def differentiate(self):
        # Operation
        input = self.e3.get()
        query = input.split()
        str_expr = ''.join(query)
        str_expr = "diff({}, x)".format(str_expr)
        expr = sympify(str_expr)
        expr = str(expr).replace('**', '^')
        self.value3 = expr

        # Update Entry 2
        self.e4.delete(0, END)
        self.e4.insert(0, self.value3)

        # Print the answer
        print("The answer is", expr)

    def integration(self):
        # Adjust Frames
        self.f1.grid_forget()
        self.f2.grid(row=1, columnspan=3)
        self.f2.focus()
        self.e3.focus()
        print("\nIntegration")

    def integrate(self):
        print("Integration")
        input = self.e1.get()
        query = input.split()
        str_expr = ''.join(query)
        str_expr = "integrate({}, x)".format(str_expr)
        expr = sympify(str_expr)
        expr = str(expr).replace('**', '^')
        self.value1 = expr

        # Update Entry 4
        self.e2.delete(0, END)
        self.e2.insert(0, self.value1)

        print("The answer is", expr)


def calculus():
    # Get the root1 window object
    # top = Toplevel()
    top = Tk()

    # Create the calculator
    calc = Calculus(top)
    # calc.r1.invoke()
    calc.f1.grid_forget()
    calc.f2.grid_forget()

    # Run the app until exited
    top.focus_force()
    top.mainloop()


# calculus()
