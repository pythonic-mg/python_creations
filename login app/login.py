import tkinter as tk
import ttkbootstrap as ttk


# MAIN WINDOW 

def main_window():
    # window 
    window = ttk.Window(themename = 'darkly')
    window.title("Welcome")
    window.geometry('325x325')

    # title
    title_lable = ttk.Label(master = window,
                            text = "Welcome",
                            font = "Calibri 20")

    # run
    window.mainloop()

# LOGIN WINDOW

def login_window():
    # window 
    window = ttk.Window(themename = "darkly")
    window.title("Log In")
    window.geometry("325x235")

    # title
    title_label = ttk.Label(master = window, 
                            text = "Login", 
                            font = "Calibri 20",
                            padding=10)
    title_label.pack()

    # username frame
    username_frame = ttk.Frame(master = window)

    # username text
    username_text = ttk.Label(master = username_frame,
                              text = "Username: ",
                              font = "Calibri 12",
                              width = 12,
                              padding = 5)
    
    # username input field
    username_input = ttk.Entry(master = username_frame, 
                               width=20)

    # pack username text and input field into username frame 
    username_text.pack(side = "left")
    username_input.pack(side = "left")

    # pack username frame
    username_frame.pack()

    # password frame
    password_frame = ttk.Frame(master = window)

    # password text
    password_text = ttk.Label(master = password_frame,
                              text = "Password: ",
                              font = "Calibri 12",
                              width = 12,
                              padding = 5)
    
    # password input field 
    password_input = ttk.Entry(master = password_frame,
                               width = 20)

    # pack into password frame
    password_text.pack(side = "left")
    password_input.pack(side = "left")

    # pack password frame into window
    password_frame.pack()

    # button frame 
    button_frame = ttk.Frame(master = window)

    # login button 
    login_button = ttk.Button(master = button_frame,
                              text = "LOGIN",
                              style = 'warning')
    
    # back button 
    back_button = ttk.Button(master = button_frame,
                             text = "BACK",
                             style = 'warning')
    
    # pack buttons into button frame
    login_button.pack(side = 'left',
                      padx = 10,
                      pady = 10)
    back_button.pack(side = 'left',
                     padx = 10,
                     pady = 10)

    # pack button frame into window
    button_frame.pack(pady=10)


    # run
    window.mainloop()

# REGISTER WINDOW 

def register_window():
    # window
    window = ttk.Window(themename = 'darkly')
    window.title("Register")
    window.geometry("325x325")

    # title
    title_lable = ttk.Label(master = window,
                            text = "Register",
                            font = "Calibri 20")

    #run
    window.mainloop()

# test
login_window()