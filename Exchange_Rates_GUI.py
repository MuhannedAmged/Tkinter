import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def convert_currency():
    f_rom = from_currency_var.get().strip().upper()
    t_o = to_currency_var.get().strip().upper()
    lan_g = language_var.get().strip().lower()

    request = requests.get(f"https://www.xe.com/{lan_g}/currencyconverter/convert/?Amount=1&From={f_rom}&To={t_o}")
    src = request.content
    soup = BeautifulSoup(src, "lxml")
    price = soup.find_all("p", {"class": "result__BigRate-sc-1bsijpp-1 dPdXSB"})

    for i in range(len(price)):
        result_label.config(text=price[i].text)


app = tk.Tk()
app.title("محول العملات")
app.iconbitmap("C:\\Users\\LAPTOPS HOUSE\\Desktop\\Mohaned\\Python\\مشاريع\\dollar.ico")

from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
language_var = tk.StringVar()

from_currency_label = ttk.Label(app, text="ادخل رمز العملة الأولى:")
from_currency_label.grid(row=0, column=0, padx=10, pady=10)
from_currency_entry = ttk.Entry(app, textvariable=from_currency_var)
from_currency_entry.grid(row=0, column=1, padx=10, pady=10)

to_currency_label = ttk.Label(app, text="ادخل رمز العملة الثانية:")
to_currency_label.grid(row=1, column=0, padx=10, pady=10)
to_currency_entry = ttk.Entry(app, textvariable=to_currency_var)
to_currency_entry.grid(row=1, column=1, padx=10, pady=10)

language_label = ttk.Label(app, text="ادخل اللغة:")
language_label.grid(row=2, column=0, padx=10, pady=10)
language_entry = ttk.Entry(app, textvariable=language_var)
language_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(app, text="تحويل", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
