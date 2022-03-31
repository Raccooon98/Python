from tkinter import*
from decimal import*
#key input fucnction
def click(key):
    if key == "=":
        result = str(eval(display.get()))
        display.insert(END, "="+result)
    elif key=="C":
        display.delete(0,END)
    elif key == ed1_pad_list[0]:
        display.insert(END, "3.141592654")
    elif key == ed1_pad_list[1]:
        display.insert(END,"300000000")
    elif key == ed1_pad_list[2]:
        display.insert(END, "330")
    elif key == ed1_pad_list[3]:
        display.insert(END, "149597887.5")
    elif key == ed2_pad_list[0]:
        factorial(display.get())
    
    else:
        display.insert(END,key)
def results(event):
    result = str(eval(display.get()))
    display.insert(END, "="+result)
def clear(event):
    display.delete(0,END)
def factorial(n):
    n=int(n)
    ans=n
    while n>1:
        ans=ans*(n-1)
        n=n-1
    return ans
###main
window=Tk()
window.title("MyCalcualaotor")
#top_row Frame generation
top_row = Frame(window)
top_row.grid(row=0,column=0,columnspan=2,sticky=N)

#
display=Entry(top_row,width=45,bg="light green")
display.grid()

num_pad=Frame(window)
num_pad.grid(row=1,column=0,sticky=W)
num_pad_list=[
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

r=0
c=0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c=c+1
    if c>2:
        c=0
        r=r+1

cal_pad=Frame(window)
cal_pad.grid(row=1,column=1,sticky=E)
cal_pad_list=[
    '*', '/',
    '+', '-',
    '(', ')',
    'C']
r=0
c=0
for btn_text in cal_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(cal_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c=c+1
    if c>1:
        c=0
        r=r+1
        
ed1_pad=Frame(window)
ed1_pad.grid(row=2,column=0,sticky=W)
ed1_pad_list=[
    "pi",
    "speed of light (m/s)",
    "speed of sound(m/s)",
    "average distance to Sun(km)"]
r=0
c=0
for btn_text in ed1_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(ed1_pad, text=btn_text, width=18, command=cmd).grid(row=r,column=c)
    c=c+1
    if c>0:
        c=0
        r=r+1

ed2_pad=Frame(window)
ed2_pad.grid(row=2,column=1,sticky=E)
ed2_pad_list=[
    "factorial(!)",
    "-> roman",
    "-> binary",
    "binary -> 10"]
r=0
c=0
for btn_text in ed2_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(ed2_pad, text=btn_text, width=12, command=cmd).grid(row=r,column=c)
    c=c+1
    if c>0:
        c=0
        r=r+1


window.bind('<Return>', results)
window.bind('<Escape>', clear)
window.mainloop()
