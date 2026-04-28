from login_window import LoginWindow
from login_controller import LoginController
from database_class import DatabaseClass

if __name__ == "__main__":
    # 1. Initialize the Model (the Database class)
    database = DatabaseClass() 
    
    # 2. Initialize the View
    login_window = LoginWindow()
    
    # 3. Initialize the Controller (This "glues" them together)
    login_controller = LoginController(database, login_window)
    
    # 4. Start the app
    login_window.run()
