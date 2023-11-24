import tkinter as tk
import ttkbootstrap as ttk

def convert():
    goofs_input = entry_int.get()
    gaffs_output = f"Goofs: {goofs_input}  Gaffs: {goofs_input * 1.78}"
    output_string.set(gaffs_output)
    entry_int.set("")

# window 
window = ttk.Window(themename = 'darkly')
window.title("Demo")
window.geometry('325x150')

# title
title_label = ttk.Label(master = window, 
                        text = "Goofs to Gaffs", 
                        font = 'Calibri 20')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, 
                  textvariable = entry_int)
button = ttk.Button(master = input_frame, 
                    text = "Convert", 
                    command = convert)
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady= 10)

# output 
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text = '0', 
                         font = 'Calibri 18 bold',
                         textvariable = output_string)
output_label.pack()


# run the window
window.mainloop()