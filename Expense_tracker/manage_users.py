import os

def get_user_file_name(user_id):
    return f"Storage/{user_id}.json"

def create_new_user():
    user_id =input("Enter Your Username: ")
    if user_exists(user_id):
        return None
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
        return False
     
        
def user_exists(user_id):
    
    file_name = f'{user_id}.json'
    users = os.listdir('Storage')
    if file_name in users:
        return True
    
    return False
    
