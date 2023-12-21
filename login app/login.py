import tkinter as tk
import ttkbootstrap as ttk

# BUTTON FUNCTIONS

# LOGIN BUTTON 
def login():
    pass

def register():
    register_window = tk.Toplevel(login_window)
    register_window.title("Register")
    register_window.geometry("325x255")

    # title
    title_lable = ttk.Label(master = register_window,
                            text = "Register",
                            font = "Calibri 20",
                            padding=10)
    
    # place title in window
    title_lable.pack()
    
    # username frame
    username_frame = ttk.Frame(master = register_window)

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
    password_frame = ttk.Frame(master = register_window)

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

    # email frame
    email_frame = ttk.Frame(master = register_window)

    # email text 
    email_text = ttk.Label(master = email_frame,
                           text = "Email: ",
                           font = "Calibri 12",
                           width = 12,
                           padding = 5)
    
    # email input 
    email_input = ttk.Entry(master = email_frame,
                            width = 20)
    
    # pack email text and input into email fram e
    email_text.pack(side = "left")
    email_input.pack(side = "left")
    email_frame.pack()

    # button frame 
    button_frame = ttk.Frame(master = register_window)

    # submit button 
    submit_button = ttk.Button(master = button_frame,
                              text = "SUBMIT",
                              style = 'warning',
                              command=submit)
    
    # back button 
    back_button = ttk.Button(master = button_frame,
                             text = "BACK",
                             style = 'warning')
    
    # pack buttons into button frame
    submit_button.pack(side = 'left',
                      padx = 10,
                      pady = 10)
    back_button.pack(side = 'left',
                     padx = 10,
                     pady = 10)

    # pack button frame into window
    button_frame.pack(pady=10)

    login_window.state("withdrawn")

def submit():
    pass

# MAIN LOGIN WINDOW

def login_window():
    # window 
    global login_window
    login_window = ttk.Window(themename = "darkly")
    login_window.title("Log In")
    login_window.geometry("325x235")

    # title
    title_label = ttk.Label(master = login_window, 
                            text = "Welcome", 
                            font = "Calibri 20",
                            padding=10)
    
    # place title in window
    title_label.pack()

    # username frame
    username_frame = ttk.Frame(master = login_window)
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
    password_frame = ttk.Frame(master = login_window)

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
    button_frame = ttk.Frame(master = login_window)

    # login button 
    login_button = ttk.Button(master = button_frame,
                              text = "LOGIN",
                              style = 'warning',
                              command=login)
    
    # register button 
    register_button = ttk.Button(master = button_frame,
                             text = "REGISTER",
                             style = 'warning',
                             command=register)
    
    # pack buttons into button frame
    login_button.pack(side = 'left',
                      padx = 10,
                      pady = 10)
    register_button.pack(side = 'left',
                     padx = 10,
                     pady = 10)

    # pack button frame into window
    button_frame.pack(pady=10)


    # run
    login_window.mainloop()

# test
login_window()