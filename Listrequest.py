from tkinter import *
from tkinter import ttk
from database import DBConnect
dbConnect=DBConnect()
class ListTicket:

    def __init__(self):
        self._root=Tk()
        self._dbconnect=DBConnect()
        tv=ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0',text='ID')
        tv.configure(column=('Name','Gender','Comment'))
        tv.heading('Name',text='Name')
        tv.heading('Gender',text='Gender')
        tv.heading('Comment',text='Comment')
        cursor=self._dbconnect.Listrequest()
        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'Gender',row['Gender'])
            tv.set('#{}'.format(row['ID']),'Comment',row['Comment'])

        self._root.mainloop()
root=Tk()




root.mainloop()
