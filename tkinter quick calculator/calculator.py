from tkinter import * 

root = Tk()
root.title("Calculator")

#create input field
input = Entry(root, width=55, borderwidth=5)
#put input field onto the grid
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#define what happens when a number is pressed
def input_number(number):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))

#define clear function
def clear_input():
    input.delete(0, END)

#get operand and operator function
def get_fnum_and_operator(operation):
    global f_num
    f_num = int(input.get())
    input.delete(0, END)
    global operand
    operand = operation

#define equals function
def equals_function():
    s_num = int(input.get())
    input.delete(0,END)
    if operand == "+":
        total = f_num + s_num
    if operand == "-":
        total = f_num - s_num
    if operand == "*":
        total = f_num * s_num
    if operand == "/":
        total = f_num / s_num
    input.insert(0, total)


#create buttons 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: input_number(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: input_number(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: input_number(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: input_number(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: input_number(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: input_number(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: input_number(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: input_number(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: input_number(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: input_number(0))
add_button = Button(root, text="+", padx=37, pady=20, command=lambda: get_fnum_and_operator("+"))
sub_button = Button(root, text="-", padx=39, pady=20, command=lambda: get_fnum_and_operator("-"))
mult_button = Button(root, text="*", padx=39, pady=20, command=lambda: get_fnum_and_operator("*"))
divide_button = Button(root, text="/", padx=39, pady=20, command=lambda: get_fnum_and_operator("/"))
equals_button = Button(root, text="=", padx=39, pady=20, command=equals_function)
clear_button = Button(root, text="AC", padx=36, pady=20, command=clear_input)

#put buttons onto grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
equals_button.grid(row=4,column=1)
clear_button.grid(row=4, column=2)

add_button.grid(row=1, column=3)
sub_button.grid(row=2, column=3)
mult_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3)

root.mainloop()