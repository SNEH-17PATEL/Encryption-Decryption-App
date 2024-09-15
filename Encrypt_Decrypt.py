# import modules

from tkinter import *
from tkinter import messagebox
import base64
import os

# def functions
def reset():
    code.set("")
    text1.delete(1.0,END)


def decrypt():
    password=code.get()
    if password == "1234":
            screen2=Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.resizable(0,0)
            screen2.configure(bg="#00bd56")

            message = text1.get(1.0,END)
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
            text2 = Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD)
            text2.place(x=10,y=40,width=380,height=150)
            text2.insert(END,decrypt)

    elif password == "":
         messagebox.showerror("Decryption","Input Password")
    elif password != "1234":
         messagebox.showerror("Decryption","Invalid Password")
         


def encrypt():
    password=code.get()
    if password == "1234":
            screen1=Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("400x200")
            screen1.resizable(0,0)
            screen1.configure(bg="#ed3833")

            message = text1.get(1.0,END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")

            Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
            text2 = Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD)
            text2.place(x=10,y=40,width=380,height=150)
            text2.insert(END,encrypt)
    elif password == "":
         messagebox.showerror("Encryption","Input Password")
    elif password != "1234":
         messagebox.showerror("Encryption","Invalid Password")
 
         
# main screen

screen = Tk()
screen.geometry("375x398")
screen.resizable(0,0)
screen.title("Encryp_Decryp App")

# label and text box for messsage to be encrypted or decrypted
Label(text="Enter text for Encryption and Decryption",fg="black",font="calbri 13").place(x=10,y=10)
text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=10,y=50,width=355,height=100)

# label and entry box for entering password
Label(text="Enter secret key for Encryption and Decryption",fg="black",font="calbri 13").place(x=10,y=170)

code=StringVar()
Entry(textvariable=code,width=19,font="arial 25",show="*").place(x=10,y=200)


# buttons 

Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",command=encrypt).place(x=10,y=250)
Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",command=decrypt).place(x=200,y=250)
Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",command=reset).place(x=10,y=300)
Button(text="QUIT",height="2",width=50,bg="#e28743",fg="white",command=screen.destroy).place(x=10,y=350)


screen.mainloop()


