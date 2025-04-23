from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()

window=tk.Tk()
window.geometry("500x360")


def clicked():
    amnt=int(e1.get())
    fr=e2.get().upper()
    t=e3.get().upper()
    data=amnt,fr,'in',t,'is',round(a.convert(amnt,fr,t),4) # a.convert(500,'INR','USD'))[Amount:500,Base-Currency:'INR',Target-Currency:'USA'] 
    l5=tk.Label(window,text=data,font="times 14 bold").place(x=230,y=230)


l1=tk.Label(window,text="Currency Converter",font="Times 25 bold").place(x=100, y=0)
l2=tk.Label(window,text="Enter amount:", font="times 18 bold ").place(x=50, y=60)
l3=tk.Label(window,text="From:",font="times 18 bold").place(x=50,y=100)
l4=tk.Label(window,text="To:",font="times 18 bold").place(x=50,y=140)
e1=tk.Entry(window)
e2=tk.Entry(window)
e3=tk.Entry(window)


b1=tk.Button(window,text="Enter",command=clicked).place(x=245,y=185)
b2=tk.Button(window,text="Exit",command=window.destroy).place(x=300,y=185)


e1.place(x=300,y=65)
e2.place(x=300,y=105)
e3.place(x=300,y=145)


window.mainloop()


