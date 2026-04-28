import tkinter as tk

class LoginWindow:
    def __init__(self):
        self.login_window = tk.Tk() # Create / instantiate an instance of the login window
        self.login_window.title("GUIUniApp - Login") # Set window title (title bar at the top)
        
        # Calculate position coordinates
        LOGIN_WINDOW_WIDTH = 450
        LOGIN_WINDOW_HEIGHT = 300
        x = (self.login_window.winfo_screenwidth() // 2) - (LOGIN_WINDOW_WIDTH // 2)
        y = (self.login_window.winfo_screenheight() // 2) - (LOGIN_WINDOW_HEIGHT // 2)
        
        self.login_window.geometry(f'{LOGIN_WINDOW_WIDTH}x{LOGIN_WINDOW_HEIGHT}+{x}+{y}') # Set the geometry (width x height + x_offset + y_offset)
        
        # self.login_window.geometry("300x200") # Set window size
        self.login_window.config(background="white") # Set window background color
        self.login_window.resizable(False, False) # Window is not resizable

        # Welcome text at the upper part of the window
        welcome_label = tk.Label(self.login_window, text="Welcome to GUIUniApp", bg="white", fg="black", font="Helvetica 12 bold")
        welcome_label.place(relx=0.5, rely=0.1, anchor="n")

        # label frame to contain email and password fields
        login_label_frame = tk.LabelFrame(self.login_window, text="Log in with your school email address", bg="white", fg="black", font="Helvetica 10 bold")
        login_label_frame.columnconfigure(0, weight=1)
        login_label_frame.columnconfigure(1, weight=3)
        login_label_frame.place(relx=0.5, rely=0.5, relwidth=0.57, anchor="center")

        # the text "email" on the left
        email_label = tk.Label(login_label_frame, text="Email:", justify="left", bg="white", fg="black", font="Helvetica 10 bold")
        email_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        # the text "password" on the left
        password_label = tk.Label(login_label_frame, text="Password:", justify="left", bg="white", fg="black", font="Helvetica 10 bold")
        password_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        # input for email
        self.email_text = tk.StringVar()
        self.email_field = tk.Entry(login_label_frame, textvariable=self.email_text)
        self.email_field.grid(column=1, row=0, padx=5, pady=5)
        self.email_field.focus()

        # input for password
        self.password_text = tk.StringVar()
        self.password_field = tk.Entry(login_label_frame, textvariable=self.password_text, show="*")
        self.password_field.grid(column=1, row=1, padx=5, pady=5)        

        # login button at the lower part of the window
        self.login_button = tk.Button(login_label_frame, text="Login")
        self.login_button.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)

        # cancel button at the lower part of the window
        self.cancel_button = tk.Button(login_label_frame, text="Cancel",command=self.login_window.destroy) # command invokes a function to close root window when clicked
        self.cancel_button.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)

        # Create a StringVar to hold the message of login status (success / failure)
        self.status_message = tk.StringVar()
        self.status_message.set("") # Start empty

        # Create the label and link it to the StringVar
        self.message_label = tk.Label(self.login_window, textvariable=self.status_message, fg="black", bg="white")
        self.message_label.place(relx=0.5, rely=0.85, anchor="center")

    # Add a method for LoginController to call
    def update_message(self, text, color="red"):
        self.status_message.set(text)
        self.message_label.config(fg=color)

    def run(self):
        self.login_window.mainloop()

# Start the GUI event loop
if __name__ == "__main__":
    app = LoginWindow()
    app.run()
