from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime





class Details:
    def __init__(self, root):
        self.root=root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1295x550+235+228')

        #------- variables: ------------

        self.vfloor = StringVar()
        self.vroomno = StringVar()
        self.vroomtype = StringVar()

        #------------Title-------------
        lbltitle= Label(self.root, text='ROOM BOOKING DETAILS', font=('times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)

        #---------Logo -----------
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        #-------- Label Frame ----------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='New RoomBooking', padx=2, font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width= 540, height= 350)

        #------ Label and Entry -----
        # 1. ---- Floor:-- ----

        lblfloor = Label(labelframeleft, text='Floor:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblfloor.grid(row=0, column=0, sticky=W)
        txtfloor = ttk.Entry(labelframeleft,textvariable=self.vfloor, width=20, font=('arial', 13, 'bold'))
        txtfloor.grid(row=0 , column= 1, sticky=W)

        # 2. ---- Room No.:-- ----

        lblroomNo = Label(labelframeleft, text='Room No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblroomNo.grid(row=1, column=0, sticky=W)
        txtroomNo = ttk.Entry(labelframeleft,textvariable=self.vroomno, width=20, font=('arial', 13, 'bold'))
        txtroomNo.grid(row=1 , column= 1, sticky=W)

        # 2. ---- Room Type:-- ----

        lblroomtype = Label(labelframeleft, text='Room Type:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblroomtype.grid(row=2, column=0, sticky=W)
        txtroomtype = ttk.Entry(labelframeleft,textvariable=self.vroomtype, width=20, font=('arial', 13, 'bold'))
        txtroomtype.grid(row=2 , column= 1, sticky=W)

        #------- Button Frame --------

        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=200, width=412, height=40)

        #---------- 1. Add Button --------

        btnAdd = Button(btnframe, text='Add', command=self.addData, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        #---------- 2. Update Button --------

        btnUpdate = Button(btnframe, text='Update',command=self.update, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        #---------- 3. Delete Button --------

        btndelete = Button(btnframe, text='Delete',command=self.idelete,  font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btndelete.grid(row=0, column=2, padx=1)

        #---------- 4. Reset Button --------

        btnreset = Button(btnframe, text='Reset',command=self.ireset, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnreset.grid(row=0, column=3, padx=1)

        #----------- Table Frame and Search System ----------

        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Roomdetails', padx=2, font=('times new roman', 12, 'bold'))
        tableframe.place(x=600, y=55, width= 600, height= 350)

        #---------- Scroll bar for table -------

        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)
        self.roomtable = ttk.Treeview(tableframe, columns=('floor', 'roomno', 'roomtype'), xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.roomtable.xview)
        scroll_y.config(command=self.roomtable.yview)

        self.roomtable.heading('floor', text= 'Floor')
        self.roomtable.heading('roomno', text= 'RoomNo.')
        self.roomtable.heading('roomtype', text= 'RoomType')

        self.roomtable['show'] = 'headings'

        self.roomtable.column('floor', width=100)
        self.roomtable.column('roomno', width=100)
        self.roomtable.column('roomtype', width=100)

        self.roomtable.pack(fill=BOTH, expand=1)
        self.roomtable.bind('<ButtonRelease-1>', self.getcursor)
        self.fetchdata()


        # Add Room Data into Database:--------

    def addData(self):
        if self.vfloor.get()=='' or self.vroomtype.get()== '':
            messagebox.showerror('Error', 'All fields are required', parent= self.root)
        else:
            try:
                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                m_cursor.execute('insert into roomdetails values(%s,%s,%s)', (
                                                                                            self.vfloor.get(),
                                                                                            self.vroomno.get(),
                                                                                            self.vroomtype.get(),
                                                                                        ))
                
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Success', 'Room Booked!!!', parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong:{str(es)}!!', parent=self.root)

    # ----- Working on Fetching the data into columns -------

    def fetchdata(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute('select * from roomdetails')
        rows = m_cursor.fetchall()
        if len(rows)!= 0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert('', END, values=i)
        conn.commit()
        conn.close()



    #-------- Get cursor -------
    def getcursor(self, event=''):
        rowcursor = self.roomtable.focus()
        content = self.roomtable.item(rowcursor)
        row= content['values']
        self.vfloor.set(row[0]),
        self.vroomno.set(row[1]),
        self.vroomtype.set(row[2])

    #---- Update Table ------
    def update(self):
        if self.vroomno.get()=='':
            messagebox.showerror('Error', 'Please Enter Valid Room Number!!', parent=self.root)
        else:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            m_cursor.execute('update roomdetails set floor=%s, roomtype=%s where roomno=%s', (                           
                                                                                                                                            self.vfloor.get(),
                                                                                                                                            self.vroomtype.get(),
                                                                                                                                            self.vroomno.get(),

                                                                                                                                            ))
            
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo('Update', 'Room Details has been updated successfully!!', parent=self.root)

    
    # --------- Delete Button Functionality ---------

    def idelete(self):
        idelete = messagebox.askyesno('HOTEL MANAGEMENT SYSTEM', 'Do you want to delete this room records??', parent= self.root)
        if idelete>0:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            query = 'delete from roomdetails where roomno=%s'
            value=(self.vroomno.get(),)
            m_cursor.execute(query, value)
        else:
            if not idelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    #----------- Reset Button Functionality --------

    def ireset(self):
        self.vfloor.set(''),
        self.vroomno.set(''),
        self.vroomtype.set('')









if __name__ == "__main__":
    root = Tk()
    obj= Details(root)
    root.mainloop()