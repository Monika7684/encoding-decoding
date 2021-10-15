from tkinter import *
import base64
from tkinter import font
from typing import Collection

root= Tk()
root.title("Message Encript And Decript")
root.geometry("1200x700+0+0")
Top = Frame(root,width=1200,relief=SUNKEN)
Top.pack(side=TOP)

f1 = Frame(root,width=800,relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Top,font=('helvetica',50,'bold'),
            text="SECRET MESSAGING \n")
lblInfo.pack()
          
#Inisilizing variable

Msg = StringVar()
Key = StringVar()
mode = StringVar()
result = StringVar()

# lable For messaging 
lblmsg = Label(f1,font=('arial',16,'bold'),text="MESSAGE",bd=16,anchor='w')
lblmsg.grid(row=1,column=0)

txtMsg = Entry(f1,font=('arial',16,'bold'),textvariable=Msg,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtMsg.grid(row=1,column=1)
# lable For key
lblkey = Label(f1,font=('arial',16,'bold'),text="KEY (Only Integer)",bd=16,anchor='w')
lblkey.grid(row=2,column=0)

txtkey = Entry(f1,font=('arial',16,'bold'),textvariable=Key,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtkey.grid(row=2,column=1)

# lable For Mode

lblmode = Label(f1,font=('arial',16,'bold'),text="Mode (e for Encrypt,d for Decrypt)",bd=16,anchor='w')
lblmode.grid(row=3,column=0)

txtmode = Entry(f1,font=('arial',16,'bold'),textvariable=mode,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtmode.grid(row=3,column=1)
# lable For  result

lblresult = Label(f1,font=('arial',16,'bold'),text="The Result-",bd=16,anchor='w')
lblresult.grid(row=2,column=2)

txtresult = Entry(f1,font=('arial',16,'bold'),textvariable=result,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtresult.grid(row=2,column=3)

def encode(key,msg):
    enc = []

    for i in range(len(msg)):
        key_c =key[i%len(key)]
        enc_c = chr((ord(msg[i])+ord(key_c))%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key,msg):
    dec = []
    enc = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(enc)):
        key_c =key[i%len(key)]
        dec_c = chr((256+ord(enc[i])-ord(key_c))%256)
        
        dec.append(dec_c)
    
    return "".join(dec)
def resultFun():
    msg= Msg.get()
    k = Key.get()
    m = mode.get()

    if m == 'e':
        result.set(encode(k,msg))
    else:
        result.set(decode(k,msg))

def resetFun():
    Msg.set("")
    mode.set("")
    result.set("")
    Key.set("")
def exitFun():
    root.destroy()

# Button 
btnTotal = Button(f1,padx=16,pady=8,fg='black',
                    font=('arial',16,'bold'),width=10,
                    text="Show Message",bg='powder blue',command=resultFun).grid(row=6,column=1)
btnReset = Button(f1,padx=16,pady=8,fg='black',
                    font=('arial',16,'bold'),width=10,
                    text="Reset",bg='powder blue',command=resetFun).grid(row=6,column=2)
btnExit = Button(f1,padx=16,pady=8,fg='black',
                    font=('arial',16,'bold'),width=10,
                    text="Exit",bg='powder blue',command=exitFun).grid(row=6,column=3)



root.mainloop()