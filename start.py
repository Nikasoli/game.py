#با استفاده از پروژه ی استارت یه پنجره باز میشه که شما هر اسمی توش وارد میکنین بعد یه فایل میسازه که اون اسمو تو اون فایل مینویسه
#بعد که اوکی رو میزنین پروژه ی سنگ کاغذ قیچی باز میشه و به اون اسمی که دادین بهش سلام میکنه و متیونین بازی کنین
from tkinter import *
import os 
os.system('cls')

def show_rps():
    name = username.get()
    #متود گت کلا دریافت میکنه تو پروژه ی فایل کرییت هم بود که دیتای سایت پایتون رو دریافت میکرد
    print(f'Hello {name}')
    win1.destroy()
    #متود دیستروی اون پنجره ای که ساختیمو میبنده یعنی خب وقتی اوکیو ردیم که نمیخوایم اون بغل بمونه تا ابد این اون پنجررو میبنده و وارد فایل سنگ کاغذ قیپی میشه 
    f = open('info.txt' , 'w')
    f.write(name)
    #با استفاده از دوتا خط بالا توی فایل تکست اینفو که میتونین هر اسمی براش بذارین مینویسه
    f.close()
    os.system('py rpsgraphical.py')
    #و با کد بالا وارد پروژه ی سنگ کاغذ قیچی میشه


win1=Tk()

username = Entry()
btn =  Button(text = 'Start', command = show_rps)
username.pack(padx=10, pady=10)
btn.pack()



win1.mainloop()