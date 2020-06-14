from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import DBConnect
from Listrequest import ListTicket
dbConnect=DBConnect()
root=Tk()
root.title("Ticket reservation")
root.configure(background="#B7D4FF")
#Style
style=ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background="#B7D4FF")
style.configure('TButton',background="#B7D4FF")
style.configure('TRadiobutton',background="#B7D4FF")

#full name
ttk.Label(root, text="Full name:").grid(row=0,column=0,padx=10,pady=10)
EntryFullname=ttk.Entry(root, width=30, font=('Arial',16))
EntryFullname.grid(row=0,column=1)
#gender
ttk.Label(root, text="Gender:").grid(row=1,column=0)
spangander=StringVar()
ttk.Radiobutton(root, text="Male", variable=spangander, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text="Female", variable=spangander, value="Female").grid(row=1, column=2)


#comment
ttk.Label(root, text="Comments:").grid(row=2, column=0)
txtcomment=Text(root, width=30, height=15, font=('Arial',16))
txtcomment.grid(row=2,column=1, columnspan=2)

#Buttons
busave=ttk.Button(root, text="Save")
busave.grid(row=3,column=3)
bulist=ttk.Button(root, text="List Res")
bulist.grid(row=3,column=2)


def BuSaveData():
    #print("Full Name:{}".format(EntryFullName.get()))
    #print("Gender:{}".format(spangander.get()))
    #print("Comments:{}".format(txtcomment.get(1.0,'end')))
    msg=dbConnect.Add(EntryFullname.get(),spangander.get(),txtcomment.get(1.0,'end'))
    messagebox.showinfo(title="Add Info",message=msg)
    EntryFullname.delete(0,'end')
    txtcomment.delete(1.0,'end')

def BuListData():
    #TODO: show orders
    #print('not mplemented yet')
    Listrequest=ListTicket()


busave.config(command=BuSaveData)
bulist.config(command=BuListData)

root.mainloop()






