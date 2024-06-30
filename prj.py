from tkinter import *
from tkinter import ttk
import sqlite3
import pandas as pd
con=sqlite3.connect('data.db')
pk=con.cursor()
pk.execute('create table if not exists std(name text, level text, grade integer)')
def save():
    n=name.get()
    l=level.get()
    g=grade.get()
    full=[n,l,g]
    pk.execute('insert into std(name,level,grade) values(?,?,?)',full)
    con.commit()
    clear()
def clear():
    name.delete(0,'end')
    level.delete(0,'end')
    grade.delete(0,'end')
    name.focus()
def export():
    lst1=[]
    lst2=[]
    result1=pk.execute('select name from std')
    for i in result1:
        lst1.append(*i)
    result2=pk.execute('select grade from std')
    for i in result2:
        lst2.append(*i)
    lst3=list(zip(lst1,lst2))
    df=pd.DataFrame(lst3)
    df.to_excel('std.xlsx')
    df.to_html('std.html')
    df.to_json('std.json')
    df.to_csv('std.csv')
def search():
    name.delete(0,'end')
    level.delete(0,'end')
    n=name.get()
    result=pk.execute('select * from std where name=?',(n,))
    result=list(result)
    grade.insert(0,result[0],[2])
    grade.insert(0,result[0],[1])
win=Tk()
win.config(bg='purple')
win.geometry('300x400+300+500')
name=Entry(justify='center',font=('tahoma',12),bg='skyblue')
name.place(x=50,y=10,width=200,height=40)
level=ttk.Combobox(values=['هفتم','هشتم','نهم'])
level.place(x=50,y=65,width=200,height=40)
grade=Entry(justify='center',font=('tahoma',12),bg='skyblue')
grade.place(x=50,y=120,width=200,height=40)
bt1=Button(justify='center',font=('tahoma',14),bg='pink',text='save',command=save)
bt1.place(x=50,y=220,width=200,height=40)
bt2=Button(justify='center',font=('tahoma',14),bg='pink',text='search',command=search)
bt2.place(x=50,y=275,width=200,height=40)
bt3=Button(justify='center',font=('tahoma',14),bg='pink',text='export',command=export)
bt3.place(x=50,y=330,width=200,height=40)
mainloop()