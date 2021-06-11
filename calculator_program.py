from tkinter import *
import parser

root = Tk()
root.title = "Calculator"
root.geometry("300x300")

# entering_user_input_into_textbox

i = 0
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# adding_input_field

display = Entry(root, bg="white")
display.grid(row=1, columnspan=6, sticky=NSEW)

# adding_buttons

Button(root, text="1", command=lambda: get_variables(1), bg="light blue", padx=5, pady=5).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variables(2), bg="light blue", padx=5, pady=5).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variables(3), bg="light blue", padx=5, pady=5).grid(row=2, column=2)
Button(root, text="4", command=lambda: get_variables(4), bg="light blue", padx=5, pady=5).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variables(5), bg="light blue", padx=5, pady=5).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variables(6), bg="light blue", padx=5, pady=5).grid(row=3, column=2)
Button(root, text="7", command=lambda: get_variables(7), bg="light blue", padx=5, pady=5).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variables(8), bg="light blue", padx=5, pady=5).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variables(9), bg="light blue", padx=5, pady=5).grid(row=4, column=2)

# adding_another_button

Button(root, text="AC", command=lambda: clear_all(), bg="red", padx=5, pady=5).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variables(0), bg="light blue", padx=5, pady=5).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate(), bg="gold", padx=5, pady=5).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_operation("+"), bg="violet", padx=5, pady=5).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-"), bg="violet", padx=5, pady=5).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*"), bg="violet", padx=5, pady=5).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/"), bg="violet", padx=5, pady=5).grid(row=5, column=3)

# adding_additional_operations

Button(root, text="pi", command=lambda: get_operation("*3.14"), bg="violet", padx=5, pady=5).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operation("%"), bg="violet", padx=5, pady=5).grid(row=3, column=4)
Button(root, text="( ", command=lambda: get_operation("("), bg="violet", padx=5, pady=5).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operation("**"), bg="violet", padx=5, pady=5).grid(row=5, column=4)

Button(root, text="del", command=lambda: undo(), bg="red", padx=5, pady=5).grid(row=2, column=5)
Button(root, text="sqrt 2", command=lambda: get_operation("*1.414"), bg="violet", padx=5, pady=5).grid(row=3, column=5)
Button(root, text=" )", command=lambda: get_operation(")"), bg="violet", padx=5, pady=5).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_operation("**2"), bg="violet", padx=5, pady=5).grid(row=5, column=5)

root.mainloop()

