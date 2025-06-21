import json
import Manage_users as user
from manage_entry import GetData,SaveData
import re

def main():
    print("\n~~ Expense Tracker ~~\n")
    
    while True: 
        
        #---------------- User Entry ---------------- 
        user_entry = int((input("1.Login\n"
                                "2.Create New user\n"
                                "3.Quit\n")))
        if user_entry == 1:
            username = user.login_as_user()
            if username == None:
                print("Login Failed... Try Again")
                input()
                main()
            
        elif user_entry == 2:
            username = user.create_new_user()
        
        elif user_entry == 3:
            exit()
            
        else:
            print("Invalid Entry... Try Again")
            input()
            main()
        #---------------- User Entry END----------------
            
        # Data Entry
        input_entry = GetData()
        input_entry.get_amount()
        input_entry.get_category()
        input_entry.get_date()
        
        
        save_entry = SaveData(username)
        save_entry.save_entry(input_entry)
                

        
if __name__ == "__main__":
    main()
