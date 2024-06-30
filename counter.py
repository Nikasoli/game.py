from tkinter import *
#با این پروژه ی شمارشگره که یه دکمه اضافه کردن داره یه دکمه کم کردن که اول تابعشو مینوسیم بعدم کامندشو به دکمه ها وصل میکنیم


#function
x=0
def increase():
    global x
    #از اونجایی که ایکس بیرون تابع هست نمیتونیم تغییرش بدیم برای همین از گلوبال استفاده میکنیم
    x+=1
    IblResult.config(text=x)
def decrease():
    global x
    x-=1
    IblResult.config(text=x)

#یکم نگاهش کنین خود به خود یاد میگیرین هیچی نداره
win = Tk()



#widget
IblResult= Label(text='0',  bg= 'lightgreen')
IblResult.place(x=10 , y=10 , width=180 , height=40)

btnIncrease= Button(text='Increase' , bg='yellow', command=increase)
btnIncrease.place(x=100 , y=60, width=90 , height=40)

btnDecrease= Button(text='Decrease' , bg='skyblue', command=decrease)
btnDecrease.place(x=10 , y=60, width=90 , height=40)



mainloop()

