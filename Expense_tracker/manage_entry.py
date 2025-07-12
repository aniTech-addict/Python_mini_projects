import json
import re

class GetData:
    
    def __init__(self):
        self.date  = None
        self.category = None
        self.amount = None
        
    
    def get_amount(self):
        while True:
            try:
                self.amount = int(input('Enter Amount: '))
                break
            except ValueError:
                print('Invalid amount. Please enter a number')
                
        
    def get_category(self):
        while True:
            category = input("\nE: Education\n"
                            "F: Food\n"
                            "C: Clothes\n"
                            "En: Entertainment\n")
            
            if re.match('^[EFC]$', category) or category == 'En':
                self.category = category
                break
                
            else:
                print('Please enter the right category')
                
    
    def get_date(self):
        print("\nEnter Slash seperated Date")
        while True:
            day = input("DD/MM/YY \r")
            if re.match(r'^\d{2}/\d{2}/\d{2}$', day):
                self.date = day.split('/')
                break
            else:
                print("Invalid date format. Please enter DD/MM/YY.")  
                
                
    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }
        
class SaveData:
    def __init__(self,file_name):
        self.file_name = file_name
        
    def save_entry(self,entry_data):
        try:
            with open(f'{self.file_name}','a+') as file:
                file.write(json.dumps(entry_data.to_dict()))
                file.write('\n')
                print('Entry saved successfully')
                
        except IOError as e:
            print(f"Error saving entry: {e}")

def main():
    print("Function not to be called directly.")

if __name__ == '__main__':
    main()