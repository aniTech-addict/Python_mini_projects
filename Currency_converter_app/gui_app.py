from tkinter import *
from tkinter import ttk, messagebox
from turtle import width
import currency_value_grabber as CV
import os
# Assuming your backend logic is in currency_value_grabber.py
# import currency_value_grabber as CV 

window = Tk()

WIDTH = 700
HEIGHT = 500
TITLE = "Currency Converter"

icon_path = os.path.join("Images", "Money-Bag-emoji.png")
if os.path.exists(icon_path):
    ICON = PhotoImage(file=icon_path)
    window.iconphoto(True, ICON)
    print(f"Warning: Icon not found at {icon_path}")

def show_help():
    messagebox.showinfo("Help", """Welcome to the Currency Converter!

        Here's how to get started:

        1.  **Enter Amount:**
            *   In the "Amount" field, type the numerical value of the currency you want to convert (e.g., 100, 50.75).

        2.  **Enter Base Country:**
            *   In the "Base Country Name" field, type the full name of the country whose currency you are converting FROM (e.g., United States, India, Japan).
            *   Ensure correct spelling for accurate results.

        3.  **Enter Foreign Country:**
            *   In the "Foreign Country Name" field, type the full name of the country whose currency you are converting TO (e.g., Canada, European Union, Australia).
            *   Again, spelling is important.

        4.  **Click "Convert":**
            *   Once all fields are filled, click the "Convert" button.

        5.  **View Result:**
            *   The converted amount will be displayed below the button.

        **Tips:**
        *   Country names are case-insensitive (e.g., "india" is the same as "INDIA").
        *   If you see an "Unsupported country" error, please double-check the spelling of the country names.
        *   An internet connection is required to fetch the latest exchange rates.

        Happy converting!""")
    
    
help_icon_path = os.path.join("Images", "help-icon.png")
HELP = PhotoImage(file=help_icon_path)
help_button = Button(window, text="Help", font=("Arial", 12), image=HELP,command=show_help)
help_button.pack(side="right", padx=10, pady=10)

window.title(f"""{TITLE}""")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False) # Optional: prevent resizing


# Define a consistent font
APP_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 20, "bold")

# --- Main Title ---
title_label = Label(window, text="Currency Converter", font=TITLE_FONT)
title_label.pack(pady=20)

# --- Frame for input fields ---
input_frame = Frame(window)
input_frame.pack(pady=10)

# --- Amount ---
amount_label = Label(input_frame, text="Amount:", font=APP_FONT)
amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
amount_entry = Entry(input_frame, font=APP_FONT, width=25)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# --- Base Country ---
base_country_label = Label(input_frame, text="Base Country Name:", font=APP_FONT)
base_country_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
base_country_entry = Entry(input_frame, font=APP_FONT, width=25)
base_country_entry.grid(row=1, column=1, padx=5, pady=5)

# --- Foreign Country ---
foreign_country_label = Label(input_frame, text="Foreign Country Name:", font=APP_FONT)
foreign_country_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
foreign_country_entry = Entry(input_frame, font=APP_FONT, width=25)
foreign_country_entry.grid(row=2, column=1, padx=5, pady=5)

# --- Convert Button ---
def perform_conversion():
    """
    Callback for the Convert button. Retrieves the values from the input fields, 
    performs the currency conversion and updates the result label.

    :raises ValueError: if the amount is not a valid number
    :raises Exception: if any other unexpected error occurs
    """
    try:
        amount_str = amount_entry.get().replace(',', '')
        if not amount_str:
            messagebox.showerror("Error", "Amount cannot be empty.")
            return
        amount = float(amount_str) # Use float for currency
        base_country = base_country_entry.get().strip()
        foreign_country = foreign_country_entry.get().strip()

        if not base_country or not foreign_country:
            messagebox.showerror("Error", "Country names cannot be empty.")
            return

        counter_currency_value = CV.currency_value(base_country,foreign_country)
        if counter_currency_value is None:
            messagebox.showerror("Error", "Unsupported country. Please recheck the spelling or Enter another Country Name")
            return
        converted_amount = amount * counter_currency_value
        result_var.set(f"Converted Amount: {converted_amount:.2f}")

        
        print(f"Amount: {amount}, Base: {base_country}, Foreign: {foreign_country}")
        result_var.set(f"Conversion for {amount} from {base_country} to {foreign_country} is {converted_amount:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a number.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

convert_button = Button(window, text="Convert",
                        font=(APP_FONT[0], APP_FONT[1], "bold"), # Make button font bold
                        bg="green", fg="white", command=perform_conversion)
convert_button.pack(pady=20)



# --- Result Display ---
result_var = StringVar()
result_label = Label(window, textvariable=result_var, font=APP_FONT, wraplength=WIDTH-40)
result_label.pack(pady=10)

window.mainloop()


