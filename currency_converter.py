from tkinter import Tk,ttk
from tkinter import *

from PIL import Image,ImageTk
import requests
import json

#colors
cor0 = "#FFFFFF" #WHITE
cor1 = "#333333" #BLACK
cor2 = "#EB5D51" #RED


window=Tk() #create a window
window.geometry('500x500') #size of window
window.title('Converter') #text at top
window.configure(bg=cor0) #Backgorund color of window
window.resizable(height=FALSE,width=FALSE) #increase height and width

#frames Are used to hold the widgets as a container
top = Frame(window,width=500,height=60,bg=cor2)
top.grid(row=0,column=0)

main = Frame(window,width=300,height=400,bg=cor0)
main.grid(row=2,column=0)

def convert():

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == 'USD':
        symbol = '$ '
    elif currency_2 == 'CAD':
        symbol = 'CAD '
    elif currency_2 == 'TRY':
        symbol = '₺ '
    elif currency_2 == 'EUR':
        symbol = '€ '
    elif currency_2 == 'INR':
        symbol = '₹ '
    elif currency_2 == 'PKR':
        symbol = '₨ '
    elif currency_2 == 'CNY':
        symbol = '¥ '
    elif currency_2 == 'GBP':
        symbol = '£ '
    elif currency_2 == 'SAR':
        symbol = 'SR '
    elif currency_2 == 'AUD':
        symbol = 'AUD '
    elif currency_2 == 'HKD':
        symbol = 'HK $ '
    elif currency_2 == 'AED':
        symbol = ' د.إ '
    elif currency_2 == 'IQD':
        symbol = ' ع.د '
    elif currency_2 == 'IRR':
        symbol = ' ﷼ '
    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + "{:.2f}".format(converted_amount)
    result['text'] = formatted
    print(converted_amount, formatted)


icon = Image.open('12.png')
icon = icon.resize((50,50))
icon = ImageTk.PhotoImage(icon)
app_name= Label(top,image=icon,compound=LEFT,text="Currency Converter",height=5,padx=46,pady=30,anchor=CENTER,font=('Arial 18 bold'),bg=cor2,fg=cor0)
app_name.place(x=0, y=0)

#mainframe
result = Label(main, text=" ", width=20, height=2, pady=4, relief=SOLID, anchor=CENTER, font= ('Ivy 16 bold'), bg=cor0, fg=cor1)
result.place(x=23, y=10)
#currency list
currency = ['CAD','PKR','EUR','INR','USD','TRY','CNY','GBP','SAR','AUD','HKD','AED','IRR','IQD']

from_label = Label(main,text="From",width=16,height=2,pady=0,padx=0,relief="flat",anchor=NW,font=('Ivy 12 bold'),bg=cor0,fg=cor1)
from_label.place(x=38, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['state'] = 'readonly'
combo1['values'] = (currency)
combo1.place(x=18,y=125)

to_label = Label(main,text= "To" ,width=20,height=2,pady=0,padx=0,relief="flat",anchor=NW,font=('Ivy 12 bold'),bg=cor0,fg=cor1)
to_label.place(x=218, y=90)

combo2 = ttk.Combobox(main, width=8,justify=CENTER, font=("Ivy 12 bold"))
combo2['state'] = 'readonly'
combo2['values'] = (currency)
combo2.place(x=186,y=125)

tex = Label(main,text="Integers Only",width=22,justify=CENTER,font=("Ivy 16 bold"),fg=cor2,bg=cor0)
tex.place(x=20,y=170)

value = Entry(main,text=" ",width=22, justify=CENTER,font=('Ivy 14 bold'),relief=SOLID)
value.place(x=35,y=205)

button = Button(main,text="Converter",width=22,padx=5,height=1,bg=cor2,fg=cor0,font=('Ivy 14 bold'),relief=SOLID,command=convert)
button.place(x=13,y=250)

window.mainloop()
