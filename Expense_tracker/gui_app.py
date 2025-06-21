from operator import ne
from tkinter import *
from tkinter import ttk
import os

def main():
    window = Tk()
    
    WIDTH = 700
    HEIGHT = 500
    TITLE = "Expense Tracker"
    
    #Font Settings
    APP_FONT = ("Arial", 14)
    TITLE_FONT = ("Arial", 20, "bold")
    
    if icon_path := os.path.join("Images", "expense-tracker.png"):
        ICON = PhotoImage(file=icon_path)
        window.iconphoto(True, ICON)
    else:
        print(f"Warning: Icon not found at {icon_path}")
    
    #Window Settings
    window.title(TITLE)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(False, False) 
    
    notebook = ttk.Notebook(window)
    
    input_tab = Frame(notebook)
    report_tab = Frame(notebook)
    
    notebook.add(input_tab,text = "Input")
    notebook.add(report_tab,text = "Report")
    
    input_frame = Frame(input_tab)
    input_frame.pack(pady=10)
    
    notebook.pack(fill=BOTH)
    
    main_label = Label(input_tab,text = "Expense Tracker",font = TITLE_FONT)
    main_label.pack()
    
    
    amount_label = Label(input_frame,text="Amount :",font=APP_FONT)
    amount_label.grid(row = 1, column=0,padx=10,pady=10)
    amount_entry = Entry(input_frame,font=APP_FONT)
    amount_entry.grid(row=1,column = 1,padx=10,pady=10)
    get_amount(amount_entry)
    
    
    window.mainloop()
    
def get_amount(amount_entry):
    amount_entry.get().replace(',','')
    amount_entry.focus_set()

if __name__ == "__main__":
    main()