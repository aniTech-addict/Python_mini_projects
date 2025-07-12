import json
import manage_users as user
from manage_entry import GetData,SaveData
#import re


"""
Actions to perform based on user selection 

    1. Login -> checks for username if exits, else returns already_exits error.
    2. Create new Users -> takes new username, create new json file using username as filename.
    3. Exit -> exit application

"""
def handle_logins():
    """Handles user login."""
    username = user.login_as_user()
    if not username:
        print("No user found... Try Again")
        return None
    return username

def handle_new_users():
    """Handles new user creation."""
    username = user.create_new_user()
    if username is None:
        print("Error creating user... Try Again")
        return None
    return username

def app_exit():
    """Exits the application."""
    print("Exiting Expense Tracker. Goodbye!")
    exit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~Actions END~~~~~~~~~~~~~~~~~~~~~~~~~#

class ExpenseTrackerApp:
    """Main application class for the Expense Tracker."""

    def __init__(self):
        self.current_user = None
        self.options = {
            1: self.handle_login_action,
            2: self.handle_create_user_action,
            3: app_exit
        }

    def handle_login_action(self):
        """Handles the login action from the menu."""
        self.current_user = handle_logins()
        if self.current_user:
            print(f"Logged in as {self.current_user}")
            self.run_user_session()

    def handle_create_user_action(self):
        """Handles the create new user action from the menu."""
        new_user = handle_new_users()
        if new_user:
            print(f"User {new_user} created successfully.")

    def run_menu(self):
        """Displays the main menu and handles user input."""
        print("\n~~ Expense Tracker ~~\n")
        while self.current_user is None:
            try:
                user_entry = int(input("1. Login\n2. Create New user\n3. Quit\nSelect an option: "))
                action = self.options.get(user_entry)
                if action:
                    action()
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


    def get_data(self):
        """Collects expense data from the user."""
        input_entry = GetData()
        input_entry.get_amount()
        input_entry.get_category()
        input_entry.get_date()
        return input_entry

    def run_user_session(self):
        """Runs the session for a logged-in user."""
        print(f"\nWelcome, {self.current_user}!")
        while self.current_user:
            try:
                print("\nUser Menu:")
                print("1. Add Expense")
                print("2. View Reports (Not implemented)")
                print("3. Logout")
                print("4. Quit")
                user_choice = int(input("Select an option: "))

                if user_choice == 1:
                    entry_data = self.get_data()
                    save_entry = SaveData(self.current_user)
                    save_entry.save_entry(entry_data)
                elif user_choice == 2:
                    print("Report functionality is not yet implemented.")
                    # TODO: Implement report generation
                elif user_choice == 3:
                    self.current_user = None
                    print("Logged out.")
                    self.run_menu() # Go back to the main menu
                elif user_choice == 4:
                    app_exit()
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


    def run(self):
        """Starts the main application loop."""
        self.run_menu()


def main():
    """Main function to start the Expense Tracker application."""
    app = ExpenseTrackerApp()
    app.run()

if __name__ == "__main__":
    main()
