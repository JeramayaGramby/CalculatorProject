import os
import tkinter as tk
import math
import pathlib


calculator_color = "#4222ff"
label_color = "#000000"
button_background_color = "#583cff"
operator_button_color = "#5336ff"
top_screen_font = ("Helvetica", 16, "bold")
body_font = ("Akzidenz-Grotesk", 42, "bold")
button_font = ("Futura", 24, "bold")
operator_font = ("Akzidenz-Grotesk", 20, "bold")

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        icon_path = pathlib.Path('Calculator.ico')
        self.window.iconbitmap(icon_path)
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator V1")
        
        # Frame Creation
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        
        # Button Creation
        self.digits = {
            7:(3,1), 8:(3,2), 9:(3,3),
            4:(4,1), 5:(4,2), 6:(4,3),
            1:(5,1), 2:(5,2), 3:(5,3),
            0:(6,2), '.':(6,1)
        }

        self.operations = {
            '/': '\u00F7', '*': '\u00D7',
            '-': '-', '+': '+'
        }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        # This is a 4x6 calculator so columns go to range(1,5) and rows go to range(1,6)
        for x in range(1,6):
            self.buttons_frame.rowconfigure(x, weight=3)
        for x in range(1,5):
            self.buttons_frame.columnconfigure(x, weight=2)


        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.special_buttons()
            
    def special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_squared_button()
        self.create_sqrt_button()
        self.create_one_over_x_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_tan_button()
    
    # Creating and initializing label properties
    def create_display_labels(self):
        total_label= tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=calculator_color,
                              fg=label_color, padx=24, font=top_screen_font)

        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=calculator_color,
                               fg=label_color, padx=24, font=body_font)

        label.pack(expand=True, fill="both")

        return total_label,label

    # Creating the dimensions of the window
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=calculator_color)

    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_current_label()

    # Adding Buttons to the UI
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=button_background_color, fg=label_color,
                               font=button_font, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, columnspan=1)

    # Creating the clear button
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.clear)
        button.grid(row=1, column=4, sticky=tk.NSEW)
    
    # Creating "square" button
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}*{self.current_expression}"))
        self.update_total_label()

    def create_squared_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00B2", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.square)
        button.grid(row=2, column=2, sticky=tk.NSEW)
    
    # Creating "square root" button
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        if float(self.current_expression) < 0:
            self.current_expression = "Error"
            self.update_total_label()
        else:
            self.update_total_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221Ax", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.sqrt)
        button.grid(row=2, column=3, sticky=tk.NSEW)

    # Creating "1/x" button
    def one_over_x(self):
        try:
            self.current_expression = str(eval(f"1/{self.current_expression}"))
        except ZeroDivisionError:
            self.current_expression = "Error"
        finally:
            self.update_total_label()

    def create_one_over_x_button(self):
        button = tk.Button(self.buttons_frame, text="\u215Fx", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.one_over_x)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    # Creating "sin" button
    def sin(self):
        sin = math.sin(float(self.current_expression))
        self.current_expression = str(eval(f"{sin}"))
        self.update_total_label()

    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text="sin", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.sin)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    # Creating "cos" button
    def cos(self):
        cos = math.cos(float(self.current_expression))
        self.current_expression = str(eval(f"{cos}"))
        self.update_total_label()

    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text="cos", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.cos)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    # Creating "tan" button
    def tan(self):
        tan = math.tan(float(self.current_expression))
        self.current_expression = str(eval(f"{tan}"))
        self.update_total_label()

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text="tan", bg=operator_button_color, fg=label_color,
                           font=operator_font, borderwidth=0, command=self.tan)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_current_label()

    # Creating "equals" button
    def create_equals_button(self):
            button = tk.Button(self.buttons_frame, text="=", bg=operator_button_color, fg=label_color,
                               font=operator_font, borderwidth=0, command=self.evaluate)
            button.grid(row=6, column=3, columnspan=2, sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def create_operator_buttons(self):
        i = 2
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=operator_button_color, fg=label_color,
                               font=operator_font, borderwidth=0, command= lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    # Creating a window for the UI
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=self.total_expression)

    def update_current_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()


