from tkinter import *
root = Tk()
root.title("Calculator")

# ---------Functioning--------
val = ""

def btn_1():
    global val
    val = val + "%"
    data.set(val)

def btn_C():
    global val
    val = ""
    data.set(val)

def btn_backspace():
    global val
    val = val[:-1]
    data.set(val)

def btn_4():
    global val
    val = val + "/"
    data.set(val)
    
def btn_5():
    global val
    val = val + "7"
    data.set(val)

def btn_6():
    global val
    val = val + "8"
    data.set(val)

def btn_7():
    global val
    val = val + "9"
    data.set(val)

def btn_8():
    global val
    val = val + "*"
    data.set(val)

def btn_9():
    global val
    val = val + "4"
    data.set(val)

def btn_10():
    global val
    val = val + "5"
    data.set(val)

def btn_11():
    global val
    val = val + "6"
    data.set(val)

def btn_12():
    global val
    val = val + "-"
    data.set(val)

def btn_13():
    global val
    val = val + "1"
    data.set(val)

def btn_14():
    global val
    val = val + "2"
    data.set(val)

def btn_15():
    global val
    val = val + "3"
    data.set(val)

def btn_16():
    global val
    val = val + "+"
    data.set(val)

def btn_17():
    global val
    val = val + "00"
    data.set(val)

def btn_18():
    global val
    val = val + "0"
    data.set(val)

def btn_19():
    global val
    val = val + "."
    data.set(val)

def btn_result():
    global val
    try:
        r = eval(val)
        data.set(r)
        val = str(r)
    except:
        data.set("ERROR")
        val=""

root.geometry("450x600")
root.resizable(0,0)

data = StringVar()

output_screen = Label(root,fg="#469ee6", bg="#646d82",padx=6,pady=18,font="Verdana 25",anchor="se",textvariable=data)
output_screen.pack(expand=True,fill="both")

btnrow1 = Frame(root)


btn1 = Button(btnrow1,text="%",font="Verdana 13",relief=GROOVE, border=0,command=btn_1,bg="#273342",fg="#e81963")
btn1.pack(expand=True,fill="both",side=LEFT)
# btn1.bind("<Button-1>",click)

btn2 = Button(btnrow1,text="c",font="Verdana 14",relief=GROOVE, border=0,command=btn_C,bg="#273342",fg="#e81963")
btn2.pack(expand=True,fill="both",side=LEFT)

btn3 = Button(btnrow1,text="<-",font="Verdana 13",relief=GROOVE, border=0,command=btn_backspace,bg="#273342",fg="#e81963")
btn3.pack(expand=True,fill="both",side=LEFT)

btn4 = Button(btnrow1,text="/",font="Verdana 13",relief=GROOVE, border=0,command=btn_4,bg="#273342",fg="#e81963")
btn4.pack(expand=True,fill="both",side=LEFT)


btnrow1.pack(expand=True,fill="both")




btnrow2 = Frame(root)


btn5 = Button(btnrow2,text="7",font="Verdana 13",relief=GROOVE, border=0,command=btn_5,bg="#273342",fg="#469ee6")
btn5.pack(expand=True,fill="both",side=LEFT)
# btn5.bind("<Button-1>",click)

btn6 = Button(btnrow2,text="8",font="Verdana 13",relief=GROOVE, border=0,command=btn_6,bg="#273342",fg="#469ee6")
btn6.pack(expand=True,fill="both",side=LEFT)

btn7 = Button(btnrow2,text="9",font="Verdana 13",relief=GROOVE, border=0,command=btn_7,bg="#273342",fg="#469ee6")
btn7.pack(expand=True,fill="both",side=LEFT)

btn8 = Button(btnrow2,text="*",font="Verdana 13",relief=GROOVE, border=0,command=btn_8,bg="#273342",fg="#e81963")
btn8.pack(expand=True,fill="both",side=LEFT)


btnrow2.pack(expand=True,fill="both")




btnrow3 = Frame(root)


btn9 = Button(btnrow3,text="4",font="Verdana 13",relief=GROOVE, border=0,command=btn_9,bg="#273342",fg="#469ee6")
btn9.pack(expand=True,fill="both",side=LEFT)

btn10 = Button(btnrow3,text="5",font="Verdana 13",relief=GROOVE, border=0,command=btn_10,bg="#273342",fg="#469ee6")
btn10.pack(expand=True,fill="both",side=LEFT)

btn11 = Button(btnrow3,text="6",font="Verdana 13",relief=GROOVE, border=0,command=btn_11,bg="#273342",fg="#469ee6")
btn11.pack(expand=True,fill="both",side=LEFT)

btn12 = Button(btnrow3,text="-",font="Verdana 13",relief=GROOVE, border=0,command=btn_12,bg="#273342",fg="#e81963")
btn12.pack(expand=True,fill="both",side=LEFT)


btnrow3.pack(expand=True,fill="both")




btnrow4 = Frame(root)


btn13 = Button(btnrow4,text="1",font="Verdana 13",relief=GROOVE, border=0,command=btn_13,bg="#273342",fg="#469ee6")
btn13.pack(expand=True,fill="both",side=LEFT)

btn14 = Button(btnrow4,text="2",font="Verdana 13",relief=GROOVE, border=0,command=btn_14,bg="#273342",fg="#469ee6")
btn14.pack(expand=True,fill="both",side=LEFT)

btn15 = Button(btnrow4,text="3",font="Verdana 13",relief=GROOVE, border=0,command=btn_15,bg="#273342",fg="#469ee6")
btn15.pack(expand=True,fill="both",side=LEFT)

btn16 = Button(btnrow4,text="+",font="Verdana 12",relief=GROOVE, border=0,command=btn_16,bg="#273342",fg="#e81963")
btn16.pack(expand=True,fill="both",side=LEFT)


btnrow4.pack(expand=True,fill="both")




btnrow5 = Frame(root)


btn17 = Button(btnrow5,text="00",font="Verdana 11",relief=GROOVE, border=0,command=btn_17,bg="#273342",fg="#469ee6")
btn17.pack(expand=True,fill="both",side=LEFT)

btn18 = Button(btnrow5,text="0",font="Verdana 14",relief=GROOVE, border=0,command=btn_18,bg="#273342",fg="#469ee6")
btn18.pack(expand=True,fill="both",side=LEFT)

btn19 = Button(btnrow5,text=".",font="Verdana 17",relief=GROOVE, border=0,command=btn_19,bg="#273342",fg="#469ee6")
btn19.pack(expand=True,fill="both",side=LEFT)

btn20 = Button(btnrow5,text="=",font="Verdana 13",relief=GROOVE, border=0,command=btn_result,fg="#000000",bg="#646d82")
btn20.pack(expand=True,fill="both",side=LEFT)


btnrow5.pack(expand=True,fill="both")







root.mainloop()