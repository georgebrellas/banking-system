#Bank Transaction System v2.2.1
from Bank import *
from tkinter import *

main = Tk()
numberText = Label(main,text="Number")
numberText.grid(row=0,column = 0)


numberInput = Entry(main)
numberInput.grid(row=1, column = 0)

pinText = Label(main,text="PIN")
pinText.grid(row=2, column = 0)

pinInput = Entry(main,show="*", width=4,state="disabled")
pinInput.grid(row=3, column = 0)
#Numbers


b1 = Button(main,text="1")
b2 = Button(main,text="2")
b3 = Button(main,text="3")



submit = Button(main,text="Login")
submit.grid(row=6)

main.mainloop()
