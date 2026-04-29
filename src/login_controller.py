class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.login_button.config(command=self.on_login_click) # actions when the login button is clicked
        self.view.cancel_button.config(command=self.view.login_window.destroy) # actions when the cancel button is clicked
        self.view.login_window.bind('<Return>', lambda event: self.on_login_click()) # Bind the Enter key to trigger the login button click event

    def on_login_click(self):
        # Get email address and password from user input in view
        email = self.view.email_text.get()
        password = self.view.password_text.get()
        
        # Controller asks the Model (Database class) to check credentials
        student = self.model.find_student(email,password)
        if student:
            self.view.update_message("Login Successful!", color="green") # Update the message in the view to show success
            self.view.login_window.after(1000, self.complete_login)
        else:
            self.view.update_message("Incorrect email or password format.", color="red") # Update the message in the view to show failure

    def complete_login(self):
        self.view.login_window.destroy() # Close the login window
        self.open_enrolment_system() # Call a function to open the enrolment system window
