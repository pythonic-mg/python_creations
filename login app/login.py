import tkinter as tk
import ttkbootstrap as ttk
import os


## MAIN WINDOW ## 

def m_window():
    # window 
    global main_window
    main_window = ttk.Window(themename = "darkly")
    main_window.title(" ")
    main_window.geometry("325x235")

    # title
    title_label = ttk.Label(master = main_window, 
                            text = "Welcome", 
                            font = "Calibri 20",
                            padding=10)
    
    # place title in window
    title_label.pack()

    # button frame 
    button_frame = ttk.Frame(master = main_window)

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
    main_window.mainloop()

## LOGIN WINDOW ##
    
def login():
    login_window = tk.Toplevel(main_window)
    login_window.title(" ")
    login_window.geometry('325x235')

    global username_login, password_login
    username_login = tk.StringVar()
    password_login = tk.StringVar()

    # title
    title_label = ttk.Label(master = login_window, 
                            text = "Log In", 
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
                               width=20,
                               textvariable=username_login)

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
                               width = 20,
                               textvariable=password_login)

    # pack into password frame
    password_text.pack(side = "left")
    password_input.pack(side = "left")

    # pack password frame into window
    password_frame.pack()

    # button frame 
    button_frame = ttk.Frame(master = login_window)

    # login button 
    login_button = ttk.Button(master = button_frame,
                              text = "LOG IN",
                              style = 'warning',
                              command=log_in)
    
    # register button 
    register_button = ttk.Button(master = button_frame,
                             text = "BACK",
                             style = 'warning',
                             command=back)
    
    # pack buttons into button frame
    login_button.pack(side = 'left',
                      padx = 10,
                      pady = 10)
    register_button.pack(side = 'left',
                     padx = 10,
                     pady = 10)

    # pack button frame into window
    button_frame.pack(pady=10)


## REGISTER WINDOW ## 

def register():
    register_window = tk.Toplevel(main_window)
    register_window.title("Register")
    register_window.geometry("325x255")

    global username_register, password_register, email_register
    username_register = tk.StringVar()
    password_register = tk.StringVar()
    email_register = tk.StringVar()

    global register_username_input, register_password_input, register_email_input

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
    register_username_input = ttk.Entry(master = username_frame, 
                               width=20,
                               textvariable=username_register)

    # pack username text and input field into username frame 
    username_text.pack(side = "left")
    register_username_input.pack(side = "left")

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
    register_password_input = ttk.Entry(master = password_frame,
                               width = 20,
                               textvariable=password_register)

    # pack into password frame
    password_text.pack(side = "left")
    register_password_input.pack(side = "left")

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
    register_email_input = ttk.Entry(master = email_frame,
                            width = 20,
                            textvariable=email_register)
    
    # pack email text and input into email fram e
    email_text.pack(side = "left")
    register_email_input.pack(side = "left")
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
                             style = 'warning',
                             command=back)
    
    # pack buttons into button frame
    submit_button.pack(side = 'left',
                      padx = 10,
                      pady = 10)
    back_button.pack(side = 'left',
                     padx = 10,
                     pady = 10)

    # pack button frame into window
    button_frame.pack(pady=10)


# login screen button

def log_in():
    username = username_login.get()
    password = password_login.get()

# register screen button

def submit():
    registered = False
    username = register_username_input.get()
    password = register_password_input.get()
    email = register_email_input.get()

    file = open("credentials.txt", "a")
    for line in open("credentials.txt", "r").readlines():
        login_info = line.split()
        if username == login_info[1]:
            registered = True
    if registered:
        file.close()
        register_username_input.delete(0, 'end')
        register_password_input.delete(0, 'end')
        register_email_input.delete(0, 'end')
    else:
        file.write(f"Username: {username} Password: {password} Email: {email}\n")
        file.close()
        register_username_input.delete(0, 'end')
        register_password_input.delete(0, 'end')
        register_email_input.delete(0, 'end')

    

    
        

## RETURN TO MAIN WINDOW ## 

def back():
    main_window1 = tk.Toplevel(main_window)
    main_window1.title(" ")
    main_window1.geometry("325x235")

    # title
    title_label = ttk.Label(master = main_window1, 
                            text = "Welcome", 
                            font = "Calibri 20",
                            padding=10)
    
    # place title in window
    title_label.pack()

    # button frame 
    button_frame = ttk.Frame(master = main_window1)

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

# test
m_window()