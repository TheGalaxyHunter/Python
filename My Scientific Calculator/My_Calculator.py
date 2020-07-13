import math
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Integration_Differentiation import calculus

solution = 0


class Calculator:  # *-*-* CALCULATOR *-*-*
    calc_value = 0.0  # Stores the current value to display in the entry
    operator = ""  # Stores the operator(+, -, *, /)
    equal = False
    string = ""

    def __init__(self, root):  # ----- __init__ -----
        # Will hold the changing value stored in the entry
        self.value = StringVar(root, value="")
        self.value1 = StringVar(root, value="")

        # Title of the Application
        root.title("Scientific Calculator")

        # root.config(bg="grey")

        # Width and Height of the Application
        root.geometry("304x256")

        # Setting application resizable false
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        width=6,
                        padding=1)

        style.configure("TEntry",
                        font="Arial",
                        padding=5)

        # Create Label Box to show the previous entry ----- 0th Row -----
        self.l1 = ttk.Label(root, textvariable=self.value1, width=26, font="Arial", anchor=E)
        # self.l1 = Text(root1, width=26, height=20, font="Arial")
        self.l1.grid(row=0, columnspan=4)

        # Create Text Entry box ----- 1st Row -----
        self.e2 = ttk.Entry(root, textvariable=self.value1, justify=RIGHT, width=26, font="Arial")
        self.e2.grid(row=1, columnspan=4)
        self.e1 = ttk.Entry(root, textvariable=self.value, justify=RIGHT, width=26, font="Arial")
        self.e1.grid(row=1, columnspan=4)
        # self.e1.configure(editable=False)

        # ----- 2nd Row -----
        self.b17 = ttk.Button(root, text="AC", command=lambda: self.clear())
        self.r1 = Radiobutton(root, indicatoron=0, value=1, text="ON", font="Serif 12 bold", command=lambda: self.on())
        self.r2 = Radiobutton(root, indicatoron=0, value=2, text="OFF", font="Serif 12 bold", command=lambda: self.off())
        self.b18 = ttk.Button(root, text="<<", command=lambda: self.backspace())
        self.b17.grid(row=2, column=0)
        self.r1.grid(row=2, column=1)
        self.r2.grid(row=2, column=2)
        self.b18.grid(row=2, column=3)

        # ----- 3rd Row -----
        self.b1 = ttk.Button(root, text="7", command=lambda: self.b_press("7"))
        self.b2 = ttk.Button(root, text="8", command=lambda: self.b_press("8"))
        self.b3 = ttk.Button(root, text="9", command=lambda: self.b_press("9"))
        self.b4 = ttk.Button(root, text="÷", command=lambda: self.o_b_press("/"))
        self.b1.grid(row=3, column=0)
        self.b2.grid(row=3, column=1)
        self.b3.grid(row=3, column=2)
        self.b4.grid(row=3, column=3)

        # ----- 4rd Row -----
        self.b5 = ttk.Button(root, text="4", command=lambda: self.b_press("4"))
        self.b6 = ttk.Button(root, text="5", command=lambda: self.b_press("5"))
        self.b7 = ttk.Button(root, text="6", command=lambda: self.b_press("6"))
        self.b8 = ttk.Button(root, text="*", command=lambda: self.o_b_press("*"))
        self.b5.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.b7.grid(row=4, column=2)
        self.b8.grid(row=4, column=3)

        # ----- 5th Row -----
        self.b9 = ttk.Button(root, text="1", command=lambda: self.b_press("1"))
        self.b10 = ttk.Button(root, text="2", command=lambda: self.b_press("2"))
        self.b11 = ttk.Button(root, text="3", command=lambda: self.b_press("3"))
        self.b12 = ttk.Button(root, text="+", command=lambda: self.o_b_press("+"))
        self.b9.grid(row=5, column=0)
        self.b10.grid(row=5, column=1)
        self.b11.grid(row=5, column=2)
        self.b12.grid(row=5, column=3)

        # ----- 6th Row -----
        self.b13 = ttk.Button(root, text="0", command=lambda: self.b_press("0"))
        self.b14 = ttk.Button(root, text=".", command=lambda: self.b_press("."))
        self.b15 = ttk.Button(root, text="=", command=lambda: self.equals())
        self.b16 = ttk.Button(root, text="-", command=lambda: self.o_b_press("-"))
        self.b13.grid(row=6, column=0)
        self.b14.grid(row=6, column=1)
        self.b15.grid(row=6, column=2)
        self.b16.grid(row=6, column=3)

        # ----- 7th Row -----
        img = Image.open('down_arrow.png')
        self.img1 = ImageTk.PhotoImage(img)
        img2 = Image.open('right_arrow.png')
        self.img3 = ImageTk.PhotoImage(img2)
        self.b19 = ttk.Button(root, image=self.img1, command=lambda: self.down(root), width=8)
        self.bInv = Button(root, text="Inv", font="Serif 11 bold", command=lambda: self.inv(), relief="raised", width=5)
        self.b19.grid(row=7, column=1, columnspan=2)

        # ----- 8th Row -----
        self.b20 = ttk.Button(root, text="sin", command=lambda: self.scientific("sin"))
        self.b21 = ttk.Button(root, text="cos", command=lambda: self.scientific("cos"))
        self.b22 = ttk.Button(root, text="tan", command=lambda: self.scientific("tan"))
        self.b23 = ttk.Button(root, text="log", command=lambda: self.scientific("log"))
        self.b20.grid(row=8, column=0)
        self.b21.grid(row=8, column=1)
        self.b22.grid(row=8, column=2)
        self.b23.grid(row=8, column=3)

        # ----- 9th Row -----
        self.b24 = ttk.Button(root, text="cosec", command=lambda: self.scientific("cosec"))
        self.b25 = ttk.Button(root, text="sec", command=lambda: self.scientific("sec"))
        self.b26 = ttk.Button(root, text="cot", command=lambda: self.scientific("cot"))
        self.b27 = ttk.Button(root, text="ln", command=lambda: self.scientific("ln"))
        self.b24.grid(row=9, column=0)
        self.b25.grid(row=9, column=1)
        self.b26.grid(row=9, column=2)
        self.b27.grid(row=9, column=3)

        # ----- 10th Row -----
        self.b28 = ttk.Button(root, text="sinh", command=lambda: self.scientific("sinh"))
        self.b29 = ttk.Button(root, text="cosh", command=lambda: self.scientific("cosh"))
        self.b30 = ttk.Button(root, text="tanh", command=lambda: self.scientific("tanh"))
        self.b31 = ttk.Button(root, text="π", command=lambda: self.b_press("π"))
        self.b28.grid(row=10, column=0)
        self.b29.grid(row=10, column=1)
        self.b30.grid(row=10, column=2)
        self.b31.grid(row=10, column=3)

        # ----- 11th Row -----
        self.b32 = ttk.Button(root, text="x²", command=lambda: self.scientific("x²"))
        self.b33 = ttk.Button(root, text="x³", command=lambda: self.scientific("x³"))
        # self.b34 = ttk.Button(root1, text="xʸ", command=lambda: self.scientific("xʸ"))  # find a way
        self.b34 = ttk.Button(root, text="1/x", command=lambda: self.scientific("1/x"))
        self.b35 = ttk.Button(root, text="e", command=lambda: self.b_press("e"))
        self.b32.grid(row=11, column=0)
        self.b33.grid(row=11, column=1)
        self.b34.grid(row=11, column=2)
        self.b35.grid(row=11, column=3)

        # ----- 12th Row -----
        self.b36 = ttk.Button(root, text="√", command=lambda: self.scientific("√"))
        self.b37 = ttk.Button(root, text="³√", command=lambda: self.scientific("³√"))
        # self.b38 = ttk.Button(root1, text="ʸ√", command=lambda: self.scientific("ʸ√"))  # find a way
        self.b38 = Button(root, text="Calculus", font="Serif 11 bold", relief=RAISED,
                          command=lambda: self.calculus_frame(), width=5)
        self.b36.grid(row=12, column=0)
        self.b37.grid(row=12, column=1)
        self.b38.grid(row=12, column=2, columnspan=2)
        self.b38.config(width=15)

        # ----- Binding Keyboard Keys -----
        root.bind(0, lambda event: self.b_press("0"))
        root.bind(1, lambda event: self.b_press("1"))
        root.bind(2, lambda event: self.b_press("2"))
        root.bind(3, lambda event: self.b_press("3"))
        root.bind(4, lambda event: self.b_press("4"))
        root.bind(5, lambda event: self.b_press("5"))
        root.bind(6, lambda event: self.b_press("6"))
        root.bind(7, lambda event: self.b_press("7"))
        root.bind(8, lambda event: self.b_press("8"))
        root.bind(9, lambda event: self.b_press("9"))
        root.bind(".", lambda event: self.b_press("."))
        root.bind("+", lambda event: self.o_b_press("+"))
        root.bind("-", lambda event: self.o_b_press("-"))
        root.bind("*", lambda event: self.o_b_press("*"))
        root.bind("/", lambda event: self.o_b_press("/"))
        root.bind("=", lambda event: self.equals())
        root.bind("<Return>", lambda event: self.equals())
        root.bind("<BackSpace>", lambda event: self.backspace())
        root.bind("pi", lambda event: self.b_press("π"))
        root.bind("e", lambda event: self.b_press("e"))

    def b_press(self, var):  # ----- B_PRESS -----
        if self.equal:
            # Clear the entry box
            self.e1.delete(0, "end")
            self.equal = False
        # Get the current value in the entry
        value = self.e1.get()
        if var != "e" and var != "π":
            if var == "." and "." not in value or var != ".":
                if value == "" and var == ".":
                    value += "0"
                # Put the new value to the right of it
                # If it was 1 and 2 is pressed it is now 12
                # Otherwise the new number goes on the left
                value += var
                # self.string += value

                # Clear the entry box
                self.e1.delete(0, "end")
                # self.e2.delete(0, "end")

                # Insert the new value going from left to right
                self.e1.insert(0, value)
                # self.e2.insert(0, self.string)

        elif var == "e" or var == "π":
            if value == "":
                value += var

                # Clear the entry box
                self.e1.delete(0, "end")

                # Insert the new value going from left to right
                self.e1.insert(0, value)

    def o_b_press(self, var):  # ----- O_B_PRESS -----
        global solution
        if self.calc_value == 0:  # if no previous calculations are pending
            # Get the value out of the entry box for the calculation

            if self.e1.get() == "π":
                self.calc_value = math.pi

            elif self.value.get() == "e":
                self.calc_value = math.e

            else:
                self.calc_value = float(self.value.get())

            # Set the operator button click so when equals is clicked
            # that function knows what calculation to use
            if var == "/":
                print("\n" + "/ Pressed")
                self.operator = "/"

            elif var == "*":
                print("\n" + "* Pressed")
                self.operator = "*"

            elif var == "+":
                print("\n" + "+ Pressed")
                self.operator = "+"

            elif var == "-":
                print("\n" + "- Pressed")
                self.operator = "-"

            # Clear the entry box
            self.e1.delete(0, "end")
            self.e2.delete(0, "end")

            # Update the label box
            self.string = "{0} {1}".format(self.calc_value, self.operator)
            self.e2.insert(0, self.string)

        else:
            # do the previous calculations which is pending

            if self.value.get() == "π":
                x = math.pi

            elif self.value.get() == "e":
                x = math.e

            else:
                x = float(self.value.get())

            y = self.calc_value

            if self.operator == "/":
                solution = y / x

            elif self.operator == "*":
                solution = y * x

            elif self.operator == "+":
                solution = y + x

            elif self.operator == "-":
                solution = y - x

            print(y, " ", self.operator, " ", x, " ", solution)
            self.calc_value = solution

            # Set the operator button click so when equals is clicked
            # that function knows what calculation to use
            if var == "/":
                print("\n" + "/ Pressed")
                self.operator = "/"

            elif var == "*":
                print("\n" + "* Pressed")
                self.operator = "*"

            elif var == "+":
                print("\n" + "+ Pressed")
                self.operator = "+"

            elif var == "-":
                print("\n" + "- Pressed")
                self.operator = "-"

            # Clear the entry box
            self.e1.delete(0, "end")
            self.e2.delete(0, "end")

            # Update the label box
            self.string = "{0} {1}".format(solution, self.operator)
            self.e2.insert(0, self.string)

    def scientific(self, var):  # ----- SCIENTIFIC -----
        global solution
        # Get the value out of the entry box for the calculation

        if self.value.get() == "π":
            x = math.pi

        elif self.value.get() == "e":
            x = math.e

        else:
            x = float(self.value.get())

        # Set the operator button click so when equals is clicked
        # that function knows what calculation to use
        if var == "sin":
            print("\n" + "sine function")
            solution = math.sin(x)  # sine function
            self.trig(var, x)
            print("sin(" + str(x) + ") ", solution)

        elif var == "cos":
            print("\n" + "cosine function")
            solution = math.cos(x)  # cosine function
            self.trig(var, x)
            print("cos(" + str(x) + ") ", solution)

        elif var == "tan":
            print("\n" + "tangent function")
            solution = math.tan(x)  # tangent function
            self.trig(var, x)
            print("tan(" + str(x) + ") ", solution)

        elif var == "cosec":
            print("\n" + "cosecant function")
            solution = 1 / math.sin(x)  # cosecant function
            self.trig(var, x)
            print("cosec(" + str(x) + ") ", solution)

        elif var == "sec":
            print("\n" + "secant function")
            solution = 1 / math.cos(x)  # secant function
            self.trig(var, x)
            print("sec(" + str(x) + ") ", solution)

        elif var == "cot":
            print("\n" + "cotangent function")
            solution = 1 / math.tan(x)  # cotangent function
            self.trig(var, x)
            print("cot(" + str(x) + ") ", solution)

        elif var == "sinh":
            print("\n" + "hyperbolic sine function")
            solution = math.sinh(x)  # hyperbolic sine function
            self.trig(var, x)
            print("sinh(" + str(x) + ") ", solution)

        elif var == "cosh":
            print("\n" + "hyperbolic cosine function")
            solution = math.cosh(x)  # hyperbolic cosine function
            self.trig(var, x)
            print("cosh(" + str(x) + ") ", solution)

        elif var == "tanh":
            print("\n" + "hyperbolic tangent function")
            solution = math.tanh(x)  # hyperbolic tangent function
            self.trig(var, x)
            print("tanh(" + str(x) + ") ", solution)

        elif var == "sin⁻¹":
            print("\n" + "sine inverse function")
            if -1 <= x <= 1:  # sine inverse function
                solution = math.asin(x)
                self.trig(var, x)
                print("sin⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "cos⁻¹":
            print("\n" + "cosine inverse function")
            if -1 <= x <= 1:  # cosine inverse function
                solution = math.acos(x)
                self.trig(var, x)
                print("cos⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "tan⁻¹":
            print("\n" + "tangent inverse function")
            solution = math.atan(x)  # tangent inverse function
            self.trig(var, x)
            print("tan⁻¹(" + str(x) + ") ", solution)

        elif var == "cosec⁻¹":
            print("\n" + "cosecant inverse function")
            if -1 >= x >= 1:  # cosecant inverse function
                solution = math.asin(1 / x)
                self.trig(var, x)
                print("cosec⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "sec⁻¹":
            print("\n" + "secant inverse function")
            if -1 >= x >= 1:  # secant inverse function
                solution = math.acos(1 / x)
                self.trig(var, x)
                print("sec⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "cot⁻¹":
            print("\n" + "cotangent inverse function")
            solution = 1 / math.atan(1 / x)  # cotangent inverse function
            self.trig(var, x)
            print("cot(" + str(x) + ") ", solution)

        elif var == "sinh⁻¹":
            print("\n" + "hyperbolic sine inverse function")
            solution = math.asinh(x)  # hyperbolic sine inverse function
            self.trig(var, x)
            print("sinh⁻¹(" + str(x) + ") ", solution)

        elif var == "cosh⁻¹":
            print("\n" + "hyperbolic cosine inverse function")
            if x >= 1:
                solution = math.acosh(x)  # hyperbolic cosine inverse function
                self.trig(var, x)
                print("cosh⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "tanh⁻¹":
            print("\n" + "hyperbolic tangent inverse function")
            if -1 < x < 1:
                solution = math.atanh(x)  # hyperbolic tangent inverse function
                self.trig(var, x)
                print("tanh⁻¹(" + str(x) + ") ", solution)
            else:
                print("Invalid input")
                solution = ""

        elif var == "10ⁿ":
            print("\n" + "nth power of 10")
            solution = 10 ** x  # nth power of 10
            self.string = "10^{}".format(x)
            self.label_text(self.string)
            print(str(x) + "th power of 10 ", solution)

        elif var == "eⁿ":
            print("\n" + "nth power of e")
            solution = math.e ** x  # nth power of e
            self.string = "e^{}".format(x)
            self.label_text(self.string)
            print(str(x) + "th power of e ", solution)

        elif var == "x²":
            print("\n" + "square")
            solution = x ** 2  # square
            self.string = "{}²".format(x)
            self.label_text(self.string)
            print("(" + str(x) + ")² ", solution)

        elif var == "x³":
            print("\n" + "cube")
            solution = x ** 3  # cube
            self.string = "{}³".format(x)
            self.label_text(self.string)
            print("(" + str(x) + ")³ ", solution)

        # elif var == "xʸ":
        #     print("\n" + "x to the power y")
        #     solution = x**y                                       # x to the power y
        #     print("("+str(x)+")ʸ ", solution)

        elif var == "√":
            print("\n" + "square root1")
            solution = math.sqrt(x)  # square root1
            self.string = "√({})".format(x)
            self.label_text(self.string)
            print("√({}) ".format(x), solution)

        elif var == "1/x":
            print("\n" + "reciprocal")
            solution = 1 / x  # reciprocal
            self.string = "1/{}".format(x)
            self.label_text(self.string)
            print("1/{} ".format(x), solution)

        elif var == "log":
            print("\n" + "logarithm function")
            solution = math.log10(x)  # logarithm function
            self.string = "log₁₀({})".format(x)
            self.label_text(self.string)
            print("log₁₀({}) ".format(x), solution)

        # elif var == "ʸ√":
        #     print("\n" + "yth root1")
        #     solution = x**(1/y)                                   # yth root1
        #     print("ʸ√("+str(x)+") ", solution)

        elif var == "³√":
            print("\n" + "cube root1")
            solution = x ** (1 / 3)  # cube root1
            self.string = "³√({})".format(x)
            self.label_text(self.string)
            print("³√({}) ".format(x), solution)

        elif var == "ln":
            print("\n" + "natural logarithm function")
            solution = math.log(x)  # natural logarithm function
            print("ln(" + str(x) + ") ", solution)

        self.equal = True

        # Clear the entry box
        self.e1.delete(0, "end")

        # Insert the new value going from left to right
        self.e1.insert(0, solution)

    def trig(self, var, x1):
        self.string = "{0}({1})".format(var, x1)
        self.e2.delete(0, "end")
        self.e2.insert(0, self.string)

    def label_text(self, var):
        self.e2.delete(0, "end")
        self.e2.insert(0, var)

    def equals(self):  # ----- EQUALS -----
        # Make sure a operator button was clicked
        global solution
        if self.operator != "":

            if self.value.get() == "π":
                x = math.pi

            elif self.value.get() == "e":
                x = math.e

            else:
                x = float(self.e1.get())

            y = self.calc_value

            if self.operator == "/":  # Divide
                solution = y / x

            elif self.operator == "*":  # Multiplication
                solution = y * x

            elif self.operator == "+":  # Addition
                solution = y + x

            elif self.operator == "-":  # Subtraction
                solution = y - x

            print(y, " ", self.operator, " ", x, " ", "=", " ", solution)
            self.string = "{0} {1} {2}".format(y, self.operator, x)
            # Clear the variables
            self.calc_value = 0.0
            self.operator = ""
            self.equal = True

            # Clear the entry box
            self.e1.delete(0, "end")
            self.e2.delete(0, "end")

            # Insert the result
            self.e1.insert(0, solution)
            self.e2.insert(0, self.string)

    def clear(self):  # ----- CLEAR -----
        # Clear the variables
        self.calc_value = 0.0
        self.operator = ""

        # Clear the entry box
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def backspace(self):  # ----- BACKSPACE -----
        # Get the current value in the entry
        value = self.e1.get()
        length = len(value)
        if value == "π":
            text = value[:length - 2]
        else:
            text = value[:length - 1]
        # Clear the entry box
        self.e1.delete(0, "end")

        # Insert the new value going from left to right
        self.e1.insert(0, text)

    def up(self, root):  # ----- UP -----
        img = Image.open('down_arrow.png')
        self.img1 = ImageTk.PhotoImage(img)
        root.geometry("304x256")
        self.b19.config(image=self.img1, command=lambda: self.down(root))
        self.bInv.grid_forget()

    def down(self, root):  # ----- DOWN -----
        img = Image.open('up_arrow.png')
        self.img1 = ImageTk.PhotoImage(img)
        root.geometry("304x426")
        self.b19.config(image=self.img1, command=lambda: self.up(root))
        self.bInv.grid(row=7, column=3, sticky=W)

    def inv(self):  # ----- INV -----
        self.bInv.config(relief=SUNKEN, command=lambda: self.inverse())
        self.b20.config(text="sin⁻¹", command=lambda: self.scientific("sin⁻¹"))
        self.b21.config(text="cos⁻¹", command=lambda: self.scientific("cos⁻¹"))
        self.b22.config(text="tan⁻¹", command=lambda: self.scientific("tan⁻¹"))
        self.b23.config(text="10ⁿ", command=lambda: self.scientific("10ⁿ"))
        self.b24.config(text="cosec⁻¹", command=lambda: self.scientific("cosec⁻¹"))
        self.b25.config(text="sec⁻¹", command=lambda: self.scientific("sec⁻¹"))
        self.b26.config(text="cot⁻¹", command=lambda: self.scientific("cot⁻¹"))
        self.b27.config(text="eⁿ", command=lambda: self.scientific("eⁿ"))
        self.b28.config(text="sinh⁻¹", command=lambda: self.scientific("sinh⁻¹"))
        self.b29.config(text="cosh⁻¹", command=lambda: self.scientific("cosh⁻¹"))
        self.b30.config(text="tanh⁻¹", command=lambda: self.scientific("tanh⁻¹"))

    def inverse(self):  # ----- INVERSE -----
        self.bInv.config(relief=RAISED, command=lambda: self.inv())
        self.b20.config(text="sin", command=lambda: self.scientific("sin"))
        self.b21.config(text="cos", command=lambda: self.scientific("cos"))
        self.b22.config(text="tan", command=lambda: self.scientific("tan"))
        self.b23.config(text="log", command=lambda: self.scientific("log"))
        self.b24.config(text="cosec", command=lambda: self.scientific("cosec"))
        self.b25.config(text="sec", command=lambda: self.scientific("sec"))
        self.b26.config(text="cot", command=lambda: self.scientific("cot"))
        self.b27.config(text="ln", command=lambda: self.scientific("ln"))
        self.b28.config(text="sinh", command=lambda: self.scientific("sinh"))
        self.b29.config(text="cosh", command=lambda: self.scientific("cosh"))
        self.b30.config(text="tanh", command=lambda: self.scientific("tanh"))

    def on(self):  # ----- ON -----
        # Select ON radio button
        self.r1.select()

        # Enable the text box and the buttons
        self.e1.config(state=NORMAL)
        self.e2.config(state=NORMAL)
        self.l1.config(state=NORMAL)
        self.b1.config(state=NORMAL)
        self.b2.config(state=NORMAL)
        self.b3.config(state=NORMAL)
        self.b4.config(state=NORMAL)
        self.b5.config(state=NORMAL)
        self.b6.config(state=NORMAL)
        self.b7.config(state=NORMAL)
        self.b8.config(state=NORMAL)
        self.b9.config(state=NORMAL)
        self.b10.config(state=NORMAL)
        self.b11.config(state=NORMAL)
        self.b12.config(state=NORMAL)
        self.b13.config(state=NORMAL)
        self.b14.config(state=NORMAL)
        self.b15.config(state=NORMAL)
        self.b16.config(state=NORMAL)
        self.b17.config(state=NORMAL)
        self.b18.config(state=NORMAL)
        self.b19.config(state=NORMAL)
        self.b20.config(state=NORMAL)
        self.b21.config(state=NORMAL)
        self.b22.config(state=NORMAL)
        self.b23.config(state=NORMAL)
        self.b24.config(state=NORMAL)
        self.b25.config(state=NORMAL)
        self.b26.config(state=NORMAL)
        self.b27.config(state=NORMAL)
        self.b28.config(state=NORMAL)
        self.b29.config(state=NORMAL)
        self.b30.config(state=NORMAL)
        self.b31.config(state=NORMAL)
        self.b32.config(state=NORMAL)
        self.b33.config(state=NORMAL)
        self.b34.config(state=NORMAL)
        self.b35.config(state=NORMAL)
        self.b36.config(state=NORMAL)
        self.b37.config(state=NORMAL)
        self.b38.config(state=NORMAL)
        # self.b39.config(state=NORMAL)
        self.bInv.config(state=NORMAL)

    def off(self):  # ----- OFF -----
        # Select OFF radio button
        self.r2.select()

        # Disable the text box and the buttons
        self.e1.config(state=DISABLED)
        self.e2.config(state=DISABLED)
        self.l1.config(state=DISABLED)
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)
        self.b10.config(state=DISABLED)
        self.b11.config(state=DISABLED)
        self.b12.config(state=DISABLED)
        self.b13.config(state=DISABLED)
        self.b14.config(state=DISABLED)
        self.b15.config(state=DISABLED)
        self.b16.config(state=DISABLED)
        self.b17.config(state=DISABLED)
        self.b18.config(state=DISABLED)
        self.b19.config(state=DISABLED)
        self.b20.config(state=DISABLED)
        self.b21.config(state=DISABLED)
        self.b22.config(state=DISABLED)
        self.b23.config(state=DISABLED)
        self.b24.config(state=DISABLED)
        self.b25.config(state=DISABLED)
        self.b26.config(state=DISABLED)
        self.b27.config(state=DISABLED)
        self.b28.config(state=DISABLED)
        self.b29.config(state=DISABLED)
        self.b30.config(state=DISABLED)
        self.b31.config(state=DISABLED)
        self.b32.config(state=DISABLED)
        self.b33.config(state=DISABLED)
        self.b34.config(state=DISABLED)
        self.b35.config(state=DISABLED)
        self.b36.config(state=DISABLED)
        self.b37.config(state=DISABLED)
        # self.b38.config(state=DISABLED)
        # self.b39.config(state=DISABLED)
        self.bInv.config(state=DISABLED)

    def calculus_frame(self):
        self.off()
        # self.b38.config(relief=SUNKEN)
        calculus()


def main():
    global solution
    # Get the root1 window object
    top = Tk()
    top.focus()

    # Create the calculator
    calc = Calculator(top)
    solution = 0
    calc.r1.invoke()

    # Run the app until exited
    top.mainloop()


main()
