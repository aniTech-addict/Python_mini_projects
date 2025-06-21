import os

def get_user_file_name(user_id):
    return f"Storage/{user_id}.json"

def create_new_user():
    user_id =input("Enter Your Username: ")
    if user_exists(user_id):
        return "Sorry the username is already in use... Login insted ?"
    try:
        file = get_user_file_name(user_id)
        with open(f'{file}', 'w'):
            print('Created User Sucessfully')
            return file
            
    except IOError as e:
        print(f"Error creating file: {e}")
        return None


def login_as_user():
    user_id = input('Enter username :')
    if user_exists(user_id):
        return get_user_file_name(user_id)
    else:
        return None
    
    
        
def user_exists(user_id):
    
    username = get_user_file_name(user_id)
    storage_path = 'Storage'
    users = os.listdir(storage_path)
    
    return username in users
    
