from tkinter import*
import csv
from time import*

list_times=['13.00-14.00','14.00-15.00','15.00-16.00',
            '16.00-17.00','17.00-18.00','18.00-19.00',
            '19.00-20.00','20.00-21.00','21.00-22.00',
            '22.00-23.00','23.00-00.00']
list_name_usetimes=[]
win=Tk()
win.configure(bg='gold')
win.minsize(550,400)
win.title('Football field reservation program')


#ฟังก์ชั่นสำหรับหน้าแรก
def firstpage():
    win.minsize(550,400)
    title1.grid(row=0,column=1)
    title2.grid(row=1,column=1)
    nextfirst.grid(row=5,column=2,pady=50)
    tur.grid(row=5,column=1,pady=50)
    close.grid(row=5,column=0,pady=50)


#ฟังก์ชั่นสำหรับหน้าสอง
def secondpage():
    win.minsize(550,500)
    title1.grid_forget()
    title2.grid_forget()
    nextfirst.grid_forget()
    tur.grid_forget()
    close.grid_forget()
    head.grid(row=0,column=1,columnspan=3)
    en.grid(row=1,column=0)
    inp.grid(row=1,column=1,columnspan=3)
    inp.focus()
    et.grid(row=2,column=0)
    et1.grid(row=6,column=0)
    et2.grid(row=7,column=0)
    et3.grid(row=2,column=1,columnspan=5)
    time1.grid(row=3,column=0)
    time2.grid(row=3,column=1)
    time3.grid(row=3,column=2)
    time4.grid(row=3,column=3)
    time5.grid(row=3,column=4)
    time6.grid(row=4,column=0)
    time7.grid(row=4,column=1)
    time8.grid(row=4,column=2)
    time9.grid(row=4,column=3)
    time10.grid(row=4,column=4)
    time11.grid(row=5,column=0)
    nextsecond.grid(row=8,column=4,pady=10)
    choose.grid(row=8,column=2,pady=10)
    back.grid(row=8,column=0,pady=10)


#ฟังก์ชั่นสำหรับหน้าสาม
def thridpage():
    win.minsize(550,400)
    en.grid_forget()
    inp.grid_forget()
    et1.grid_forget()
    et2.grid_forget()
    et3.grid_forget()
    time1.grid_forget()
    time2.grid_forget()
    time3.grid_forget()
    time4.grid_forget()
    time5.grid_forget()
    time6.grid_forget()
    time7.grid_forget()
    time8.grid_forget()
    time9.grid_forget()
    time10.grid_forget()
    time11.grid_forget()
    nextsecond.grid_forget()
    choose.grid_forget()
    back.grid_forget()
    price1.grid(row=1,column=0)
    price1_1.grid(row=1,column=1)
    price2.grid(row=2,column=0)
    price2_1.grid(row=2,column=1)
    price3.grid(row=3,column=0)
    price3_1.grid(row=3,column=1)
    close.grid(row=5,column=0,pady=50)
    use_time=time.get()
    price2_1.config(text=time_config)
    use_name=inp.get()
    price1_1.config(text=use_name)
    prices=('{} THB'.format(price))
    price3_1.config(text=prices)
    fillpath=strftime('%d'+' '+'%b'+' '+'%Y'+'.csv')
    
    
#ฟังก์ชั่นสำหรับปุ่มย้อนกลับไปหน้าแรก
def backsecondpage():
    win.minsize(550,400)
    head.grid_forget()
    en.grid_forget()
    inp.grid_forget()
    et.grid_forget()
    et1.grid_forget()
    et2.grid_forget()
    et3.grid_forget()
    time1.grid_forget()
    time2.grid_forget()
    time3.grid_forget()
    time4.grid_forget()
    time5.grid_forget()
    time6.grid_forget()
    time7.grid_forget()
    time8.grid_forget()
    time9.grid_forget()
    time10.grid_forget()
    time11.grid_forget()
    nextsecond.grid_forget()
    choose.grid_forget()
    back.grid_forget()
    title1.grid(row=0,column=1)
    title2.grid(row=1,column=1)
    nextfirst.grid(row=5,column=2,pady=50)
    tur.grid(row=5,column=1,pady=50)
    close.grid(row=5,column=0,pady=50)


#ฟังก์ชั่นคำนวณ
price=0
keeptimes=''
time_config=''
def choosetimes():
    name=inp.get()
    keeptimes=time.get()
    list_name_usetimes=('{},{},{}'.format(name,keeptimes,500)).split(',')
    global time_config
    global price
    try:
        fillpath=strftime('%d'+' '+'%b'+' '+'%Y'+'.csv')
        with open(fillpath,'r',encoding='utf-8')as NP:
            read_file=csv.reader(NP)
            add_list=list(read_file)
    except Exception:
        with open(fillpath,'w',encoding='utf-8')as NP:
            writer=csv.writer(NP,lineterminator='\n')
            writer.writerow(list_name_usetimes)
            time_config+=keeptimes+'\n'
            et2.config(text=time_config)
        price+=500
    else:
        a_time=[]
        for i in add_list:
            a_time.append(i[1])
        if keeptimes not in a_time:
            with open(fillpath,'a',encoding='utf-8')as NP:
                writer=csv.writer(NP,lineterminator='\n')
                writer.writerow(list_name_usetimes)
                time_config+=keeptimes+'\n'
                et2.config(text=time_config)
            price+=500
        else:
            win2=Toplevel(win)
            win2.config(bg='lightpink')
            Label(win2,text='This time has been booked\n Please select a new time.'
                  ,font='Tahoma 60 bold',bg='lightpink').grid(pady=20)
            Button(win2,text='CLOSE',command=win2.destroy,width=10,bg='firebrick'
                 ,fg='black',bd=10,font='Tahoma 9 bold').grid()


#ฟังก์ชั่นเรียกดูข้อมูลที่จองเวลาไปแล้ว        
def turnovers():
    price_total=0
    name_all=''
    time_all=''
    price_all=''
    fillpath=strftime('%d'+' '+'%b'+' '+'%Y'+'.csv')
    try:
        with open(fillpath,'r',encoding='utf-8')as NP:
            read_file=csv.reader(NP)
            add_list=list(read_file)
    except Exception:
        win3=Toplevel(win)
        win3.config(bg='lightpink')
        Label(win3,text='File not found',font='Tahoma 60 bold',bg='lightpink').grid()
        Button(win3,text='CLOSE',command=win3.destroy,width=10,bg='firebrick'
                 ,fg='black',bd=10,font='Tahoma 9 bold').grid()
    else:
        for i in add_list:
            name_all+=i[0]+'\n'
            time_all+=i[1]+'\n'
            price_all+=i[2]+'\n'
            price_total+=500
        price_total_n=('Price Total {} THB'.format(price_total))
        win3=Toplevel(win)
        win3.config(bg='lightpink')
        lb1=Label(win3,text='Name',font='Tahoma 24 bold',bg='lightpink')
        lb2=Label(win3,text='Time',font='Tahoma 24 bold',bg='lightpink')
        lb3=Label(win3,text='Price',font='Tahoma 24 bold',bg='lightpink')
        
        lb1.grid(row=1,column=0)
        lb2.grid(row=1,column=1)
        lb3.grid(row=1,column=2)
        
        lb1_1=Label(win3,text=' ',font='Tahoma 12 bold',bg='lightpink')
        lb2_1=Label(win3,text=' ',font='Tahoma 12 bold',bg='lightpink')
        lb3_1=Label(win3,text=' ',font='Tahoma 12 bold',bg='lightpink')
        lb4_1=Label(win3,text=' ',font='Tahoma 12 bold',bg='lightpink',fg='blue')
        lb1_1.grid(row=2,column=0)
        lb2_1.grid(row=2,column=1)
        lb3_1.grid(row=2,column=2)
        lb4_1.grid(row=3,column=2)
        lb1_1.config(text=name_all)
        lb2_1.config(text=time_all)
        lb3_1.config(text=price_all)
        lb4_1.config(text=price_total_n)
        Button(win3,text='CLOSE',command=win3.destroy,width=10,bg='firebrick'
                 ,fg='black',bd=10,font='Tahoma 9 bold').grid(padx=20)


#หน้าต่างแรก
title1=Label(win,text='NP',font='Tahoma 60 bold',bg='gold',height=1)
title2=Label(win,text='Club Stadium',font='Tahoma 48 bold',bg='gold',height=2)
nextfirst=Button(win,text='NEXT',width=10,bg='cyan',fg='black',bd=10,
                font='Tahoma 9 bold',command=secondpage)
tur=Button(win,text='TURNOVER',width=10,bg='lightgreen',fg='black',bd=10,
                font='Tahoma 9 bold',command=turnovers)
close=Button(win,text='CLOSE',command=win.destroy,width=10,bg='firebrick'
                 ,fg='black',bd=10,font='Tahoma 9 bold')


#หน้าต่างสอง
head=Label(win,text='NP Club',font='Tahoma 36 bold',bg='gold')
myint=StringVar()
myinput=myint.get()
en=Label(win,text='Enter Name',font='Tahoma 12 bold',height=4
         ,bg='gold')
inp=Entry(win,textvariable=myint.get(),width=30)
et=Label(win,text='Enter Time',font='Tahoma 12 bold',height=4
         ,bg='gold')
et1=Label(win,text='You choose',font='Tahoma 12 bold',width=10
         ,bg='gold',fg='red')
et2=Label(win,text=' ',font='Tahoma 12 bold'
         ,bg='gold',fg='red',height=13)
et3=Label(win,text='**Select the time and press the |Choose Time| button\n'
          'You can choose from multiple times**',font='Tahoma 9 bold'
          ,height=4,bg='gold')
time=StringVar()
time.set('0')
time1=Radiobutton(win,text=list_times[0],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[0],variable=time)
time2=Radiobutton(win,text=list_times[1],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[1],variable=time)
time3=Radiobutton(win,text=list_times[2],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[2],variable=time)
time4=Radiobutton(win,text=list_times[3],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[3],variable=time)
time5=Radiobutton(win,text=list_times[4],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[4],variable=time)
time6=Radiobutton(win,text=list_times[5],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[5],variable=time)
time7=Radiobutton(win,text=list_times[6],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[6],variable=time)
time8=Radiobutton(win,text=list_times[7],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[7],variable=time)
time9=Radiobutton(win,text=list_times[8],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[8],variable=time)
time10=Radiobutton(win,text=list_times[9],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[9],variable=time)
time11=Radiobutton(win,text=list_times[10],font='Tahoma 9 bold',bg='gold'
                  ,value=list_times[10],variable=time)
nextsecond=Button(win,text='NEXT',width=10,bg='cyan',fg='black',bd=10,
                    font='Tahoma 9 bold',command=thridpage)
choose=Button(win,text='Choose Time',width=10,bg='lightgreen',fg='black',bd=10,
                    font='Tahoma 9 bold',command=choosetimes)
back=Button(win,text='BACK',width=10,bg='firebrick'
                    ,fg='black',bd=10,font='Tahoma 9 bold',command=backsecondpage)


#หน้าต่างสาม
head=Label(win,text='NP Club',font='Tahoma 36 bold',bg='gold')
price1=Label(win,text='Name',font='Tahoma 14 bold',width=10,height=4
             ,bg='gold')
price1_1=Label(win,text=' ',font='Tahoma 14 bold',width=10,height=4
             ,bg='gold')
price2=Label(win,text='Time',font='Tahoma 14 bold',width=10,height=4
             ,bg='gold')
price2_1=Label(win,text=' ',font='Tahoma 14 bold',width=10
             ,bg='gold',height=13)
price3=Label(win,text='You must pay',font='Tahoma 14 bold',height=4
             ,bg='gold',fg='red')
price3_1=Label(win,text=' ',font='Tahoma 14 bold',height=4
             ,bg='gold',fg='red')
close=Button(win,text='CLOSE',command=win.destroy,width=10,bg='firebrick'
                 ,fg='black',bd=10,font='Tahoma 9 bold')


firstpage()
mainloop()
