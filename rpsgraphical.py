#این اصلی ترین پروژس که سنگ کاغذ قیچیه با خود کامپیوتر 
#سه تا گزینه دارین که هرکدومو بزنین همون لحظه خود برنامه رندوم یه گزینرو در جواب به شما میده و بهتون میگه خودش برنده شده یا شما یا مساوی شدین
#خام این پروژه تو فولدر 
#rps_without_answer هست

from tkinter import *
from random import *
from tkinter import messagebox
#مسج باکس ماژولیه که پیشفرض تو خود پایتون هست
#کارش اینه که تو خود برنامه میتونین تب جدید بیارین مقلا پیغام هشدار یا ارور یا تایید و... که اینجا دو سه باری ازش استفاده کردیم
import os
os.system('cls')

#Variable
lst = ['rock' , 'paper' , 'scissor']
c_score = 0
u_score = 0
#اینجا اول متغیر هامونو تعیین میکنیم
#یو اسکور امتیاز یوزر یا خود شماست
#سی اسکور امتیاز کامپیوتره که جفتشون تو حالت اول خب صفرن دیگه مگه اینکه نژادپرست باشید خیخیخیخیصهخثهعصذثبتصبصترینصلزصثغلیهعثصلاصثعاصهعثیثسقاعه9غنیقلهخ08عفیقلا

#Function
def rock():
    global c_score
    global u_score
    #متغیرمون چون خارج از تابعه با استفاده از گلوبال میتونیم تغییرش بدیم وگرنه تغییر نمیکنه
    #با استفاده از رندوم اینجا برای هر سه حالت سنگ کاغذ و قیچی تعیین کردیم که اگه مثلا من سنگو زدم کامپیوتر قیچیو کی میبره و کی چه امتیازی میگیره
    c = choice(lst)
    print(c)
    if c == 'rock':
        lblResult.config(text = 'DRAW!')
        #مثلا اینجا داریم برای تابع سنگ یا راک تعیین میکنیم اگه کامپیوتر رندوم سنگ آورد مساوی میشیم
    elif c == 'paper':
        c_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. Computer Won!')
        #یا اینجا اگه شما سنگ بیاری کامپیوتر کاغذ کامپیوتر میبره
        #تعیین کردیم سی اسکور یدونه بهش اضافه میشه
        #و با اف استرینگ امتیازارو داخل متنمون نشون میدیم
    else:
        u_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. You Won!')
        #اینم همینه اگه شما سنگ بیاری و کامپیوتر قیچی شما میبری و یه امتیاز بهت اضافه میشه و نشون میده
        #برای بقیه حالت ها هم توابعشونو به همین شکل مینویسیم که نیازی نبود همرو کپی پیست کردیم فقط جاهاشونو عوض کردیم
def paper():
    global c_score
    global u_score
    c = choice(lst)
    print(c)
    if c == 'rock':
        u_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. You Won!')
    elif c == 'paper':
        lblResult.config(text = 'DRAW!')
    else:
        c_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. Computer Won!')
def scissor():
    global c_score
    global u_score
    c = choice(lst)
    print(c)
    if c == 'rock':
        c_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. Computer Won!')
    elif c == 'paper':
        lblResult.config(text = 'DRAW!')
    else:
        u_score+=1
        lblResult.config(text = f'Computer ={c_score} & User = {u_score}. You Won!')

#×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××        
def msg():
    #یا استفاده از مسج باکس یه پنجره میسازیم که وقتی یوزرمون رو دکمش که کد تیکینتر پایینه کلیک میکنه بهش برنده ی نحاییو با توجه به مقدار امتیاز میگه
    #باز هم از گلوبال استفاده میکنیم
    global c_score
    global u_score
    if u_score > c_score:
        messagebox.showinfo('FATALITY', 'User is the WINNER!')
        #دات شو اینفو نوع اون پنجره ایه که باز میشه مدلای مختلف داره باز که یکی دیگشو پایین تر استفاده میکنیم و تو اینترنت ببینید بزا مدلاشو دیگه
        #اگه امتیاز یوزر بیشتر بود نشون میده یوزر برندس
    elif u_score == c_score:
        messagebox.showinfo('FATALITY', 'There is no winner\nDRAWwWwW')
        #اگه امتیازا برابر بود مساوی    
    else:
        messagebox.showinfo('FATALITY', 'Computer is the WINNER!')
        #و در غیر این صورت کامپیوتر برندس
#××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
def reset():
    #اینم با استفاده از مسج باکس یه پنجره باز میشه که میگه مطمعنی میخوای نتایجو ریست کنیم اگه بزنی یس ریست میشه نتایج و اگه بزنی نو ریست نمیشه
    msg = messagebox.askyesnocancel('WARNING!','Are You Sure')
    #دات اسک یس نو کنسل هم پنجره ای باز میکنه که به راحتی میپرسه آره یا نه
    #و اگه ایفمون ترو باشه یعنی مخاطب یس رو بزته نتایج ریست میشه
    #if msg==True
    #کد بالا همون کد پایینه
    if msg:
        global c_score
        global u_score
        c_score = 0
        u_score = 0
        lblResult.config(text='')
#××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
#تابع پایین مربوط میشه به پروژه ی 
#file_create.py
#و 
#start.py
#که با ایمپورت کردن او اس میتونیم ازش استفاده کنیم
#ما تو فایل استارت یه پنجره باز کردیم که شما یه اسم داخلش وارد میکنی اوکیو که میزنی میاد این پروژرو باز میکنه یعنی اصلا ما برای اجرا کردن این برنامه خودشو اجرا نمیکنیم اول پروژه ی استارتو بزا میکنیم و اون مارو به اینجا هدایت میکنه
#تو پروژه ی استارت وقتی اسمتو وارد میکنی یه فایل تکست درست میشه به اسم اینفو تو خود فولدر پروژه هم درست میشه
#که اسمی که شما داخل پنجره وارد کردین تو اون فایل تکست نوشته شده
#بعد وقتی اونجا اوکی رو میزنین وارد این پروژه میشه که اولش میگه
#hello (esmi ke vared kardin)
#و به ادامه ی استفاده از این برنامه میتونین ادامه بدین
def  user():
    f = open('info.txt', 'r')
    data = f.read()
    #با استفاده از دوتا خط بالا هم فایل اینفو رو میخونه
    lblUser.config(text=f'Hello {data}')
    #یا استفاده از خط بالا و اف استرینگ میگه هلو *اسمی که وارد کردین*      
    

win = Tk()
win.geometry('500x400+400+100')
win.iconbitmap('icon.ico')
win.title('Rock , Peper , scissor Game')
win.config(bg = 'Skyblue')

#widget-----------------------------------------

#Label Caption
lblCaption = Label(text='ROCK PAPER SCISSORS ' , font = ('arial' , 16) , bg = 'teal' , fg='Yellow')
lblCaption.place(width = 500 , height = 50)

#Rock
imgRock = PhotoImage(file ='rock.png')
btnRock = Button(image=imgRock , command = rock)
btnRock.place(x =30 , y = 80 ,  width = 120 , height = 120)

#paper
imgPaper = PhotoImage(file ='paper.png')
btnPaper = Button(image=imgPaper , command = paper)
btnPaper.place(x =190 , y = 80 ,  width = 120 , height = 120)

#Scissor
imgscissor = PhotoImage(file ='scissor.png')
btnscissor = Button(image=imgscissor , command = scissor)
btnscissor.place(x =350 , y = 80 ,  width = 120 , height = 120)

#ButtonResult
#دکمه ی اعلام نتایج که با کامند به تابع ام ای جی وصلش کردیم
btnResult = Button(text = 'Winner!' , font = ('arial' , 14) , bg = 'lightgreen' , fg= 'green', command=msg)
btnResult.place(x=30 , y=210 , width=200 , height=40)

#Label User
lblUser = Label(text='------------------------', font = ('arial' , 14) , bg = 'skyblue')
lblUser.place(x =0 , y = 250 ,  width =500 , height = 50 )

#Label
lblResult = Label(text='', font = ('arial' , 14) , bg = 'pink' , fg='black')
lblResult.place(x =0 , y = 300 ,  width =500 , height = 50)

#ButtonReset
#دکمه ی ریست که با کامند به تابع ریست وصل شده
btnReset = Button(text = 'RESET GAME RESULTS' , font = ('arial' , 14) , bg = 'red' , fg= 'white', command=reset)
btnReset.place(x=250 , y=210 , width=230 , height=40)

#آقا این خیلی مهمه حقیقتا خودم درست نفهمیدمش غایب بودم ولی اینو نذارین کلا کار نمیکنه
user()
mainloop()