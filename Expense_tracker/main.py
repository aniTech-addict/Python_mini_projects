import json
from unicodedata import category
import re

def main():
    print("\n~~ Expense Tracker ~~\n")
    
    amount = int(input("Enter Amount Spent:").replace(',',''))
    
    category = get_category()
    date = get_date()
    
    save_data(amount,category,date)



           
def get_category():
    while True:
        category = input("\nE: Education\n"
                        "F: Food\n"
                        "C: Clothes\n"
                        "En: Entertainment\n")
        
        if re.match('^[EFC]$', category) or category == 'En':
            return category
            
        else:
            print('Please enter the right category')
    
    
    
def get_date():
    print("\nEnter Slash seperated Date")
    while True:
        day = input("DD/MM/YY \r")
        if re.match(r'^\d{2}/\d{2}/\d{2}$', day):
            break
        else:
            print("Invalid date format. Please enter DD/MM/YY.")
    
    return day.split('/')   


def save_data(amount,category,date):
    with open('data.json','a+') as file:
        entry = {
        "month": date[1],
        "category": category,
        "amount": amount
    }
        
    with open('data.json', 'a') as file:
        file.write(json.dumps(entry) + '\n')
        
        
if __name__ == "__main__":
    main()

