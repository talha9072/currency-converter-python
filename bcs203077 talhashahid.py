import requests
import tkinter as tk
from tkinter import ttk

# create the Tkinter window
root = tk.Tk()
root.title(" bcs203077 Currency Converter")

# set the window size and background color
root.geometry("600x400")
root.configure(bg="#add8e6")

# create the style
style = ttk.Style()
style.theme_create("my_style", parent="alt", settings={
    "TLabel": {
        "configure": {"foreground": "#f2f2f2", "background": "#282828", "font": ("Arial", 14)}
    },
    "TEntry": {
        "configure": {"foreground": "#444444", "background": "#f2f2f2", "font": ("Arial", 14)}
    },
    "TCombobox": {
        "configure": {"foreground": "#444444", "background": "#f2f2f2", "font": ("Arial", 14)}
    },
    "TButton": {
        "configure": {"foreground": "#f2f2f2", "background": "#444444", "font": ("Arial", 14)}
    }
})
style.theme_use("my_style")

# get the currency exchange rates from the internet
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
rates = response.json()['rates']

# create the available currencies list
available_currencies = list(rates.keys())

# create the input widgets
amount_label = ttk.Label(root, text="Enter Amount:", style="TLabel")
amount_label.pack(pady=20)
amount_entry = ttk.Entry(root)
amount_entry.pack()

from_label = ttk.Label(root, text="From:", style="TLabel")
from_label.pack(pady=10)
from_menu = ttk.Combobox(root, values=available_currencies, state="readonly")
from_menu.pack()

to_label = ttk.Label(root, text="To:", style="TLabel")
to_label.pack(pady=10)
to_menu = ttk.Combobox(root, values=available_currencies, state="readonly")
to_menu.pack()

result_label = ttk.Label(root, text="", style="TLabel")
result_label.pack(pady=20)

# create the conversion function
def convert_currency():
    try:
        # get the input values
        amount = float(amount_entry.get())
        currency_from = from_menu.get()
        currency_to = to_menu.get()

        # convert the currency
        result = amount * rates[currency_to] / rates[currency_from]

        # update the result label
        result_label.configure(text=f"{amount:.2f} {currency_from} is equal to {result:.2f} {currency_to}")
    except ValueError:
        result_label.configure(text="Invalid input")

# create the reset function
def reset_values():
    amount_entry.delete(0, tk.END)
    from_menu.current(0)
    to_menu.current(0)
    result_label.configure(text="")

# create the conversion and reset buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)
convert_button = ttk.Button(button_frame, text="Convert", command=convert_currency, style="TButton")
convert_button.pack(side=tk.LEFT, padx=10)
reset_button = ttk.Button(button_frame, text="Reset", command=reset_values, style="TButton")
reset_button.pack(side=tk.LEFT, padx=10)

# run the Tkinter event loop
root.mainloop()
