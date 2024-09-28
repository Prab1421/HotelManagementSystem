from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox




class CustomerWindow:
    def __init__(self, root):
        self.root=root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1295x550+235+228')

        #---------- Variables ----------
        self.varref = StringVar()
        x= random.randint(1000, 9999)
        self.varref.set(str(x))

        self.custname = StringVar()
        self.mothername = StringVar()
        self.gender= StringVar()
        self.post = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.nationality = StringVar()
        self.idproof = StringVar()
        self.idnumber = StringVar()
        self.address = StringVar()


        #------------Title-------------
        lbltitle= Label(self.root, text='ADD CUSTOMER DETAILS', font=('times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)

        #---------Logo -----------
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        #-------- Label Frame ----------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Customer Details', padx=2, font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width= 425, height= 490)

        #------ Label and Entry -----
        # 1. customer reference:---

        lblcustmorref = Label(labelframeleft, text='Customer Ref.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcustmorref.grid(row=0, column=0, sticky=W)
        txtref = ttk.Entry(labelframeleft,textvariable=self.varref, width=29, font=('arial', 13, 'bold'), state='readonly')
        txtref.grid(row=0 , column= 1)

        # 2. customer name: -------

        cname = Label(labelframeleft, text='Customer Name:', font=('arial', 12, 'bold'), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.custname, width=29, font=('arial', 13, 'bold'))
        txtcname.grid(row=1 , column= 1)

        # 3. mother name: --------

        lblmname = Label(labelframeleft, text='Mother Name:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.mothername, width=29, font=('arial', 13, 'bold'))
        txtmname.grid(row=2 , column= 1)

        # 4. Gender: ------

        lblgender = Label(labelframeleft, text='Gender:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblgender.grid(row=3, column=0, sticky=W)
        combogender = ttk.Combobox(labelframeleft,textvariable=self.gender, font=('arial', 13, 'bold'), state='readonly',width=27)
        combogender['values'] = ('Male', 'Female', 'Other')
        combogender.current(0)
        combogender.grid(row=3, column=1)


        # 5. Postcode:-----

        lblpincode = Label(labelframeleft, text='Pincode:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblpincode.grid(row=4, column=0, sticky=W)
        txtpin = ttk.Entry(labelframeleft,textvariable=self.post, width=29, font=('arial', 13, 'bold'))
        txtpin.grid(row=4 , column= 1)


        # 6. Mobileno:------

        lblmobileno = Label(labelframeleft, text='Mobile No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblmobileno.grid(row=5, column=0, sticky=W)
        txtmobile = ttk.Entry(labelframeleft,textvariable=self.mobile, width=29, font=('arial', 13, 'bold'))
        txtmobile.grid(row=5 , column= 1)

        # 7. Email:-------

        lblemail = Label(labelframeleft, text='Email:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)
        txtemail = ttk.Entry(labelframeleft,textvariable=self.email, width=29, font=('arial', 13, 'bold'))
        txtemail.grid(row=6 , column= 1)


        # 8. Nationality: -------

        lblnationality = Label(labelframeleft, text='Nationality:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblnationality.grid(row=7, column=0, sticky=W)
        combonation = ttk.Combobox(labelframeleft,textvariable=self.nationality, font=('arial', 13, 'bold'), state='readonly',width=27)
        combonation['values'] = ('American', 'British', 'Canadian', 'Chinese', 'German', 'French', 'Italian', 'Japanese', 'Mexican', 'Indian', 'Brazilian', 'Australian', 'Russian', 'South Korean', 'Spanish', 'Dutch', 'Swedish', 'Norwegian', 'Danish', 'Finnish', 'Greek', 'Turkish', 'Portuguese', 'Irish', 'Egyptian', 'South African', 'New Zealander', 'Polish', 'Argentinian', 'Chilean', 'Singaporean')
        combonation.current(0)
        combonation.grid(row=7, column=1)

        # 9. Id Proof Combobox: --------

        lblidproof = Label(labelframeleft, text='Id Proof No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblidproof.grid(row=8, column=0, sticky=W)
        comboid = ttk.Combobox(labelframeleft,textvariable=self.idproof, font=('arial', 13, 'bold'), state='readonly',width=27)
        comboid['values'] = ('Passport', 'Driver\'s License', 'National ID Card', 'Voter ID', 'Social Security Card', 'Birth Certificate', 'Military ID', 'Residency Permit', 'Student ID', 'Health Insurance Card')
        comboid.current(0)
        comboid.grid(row=8, column=1)


        # 10. Id Number: ---------

        lblidno = Label(labelframeleft, text='Id No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblidno.grid(row=9, column=0, sticky=W)
        txtidno = ttk.Entry(labelframeleft,textvariable=self.idnumber, width=29, font=('arial', 13, 'bold'))
        txtidno.grid(row=9 , column= 1)



        # 11. Address: -------

        lbladdress = Label(labelframeleft, text='Address:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)
        txtaddress = ttk.Entry(labelframeleft,textvariable=self.address, width=29, font=('arial', 13, 'bold'))
        txtaddress.grid(row=10 , column= 1)

        #------- Button Frame --------

        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        #---------- 1. Add Button --------

        btnAdd = Button(btnframe, text='Add',command=self.addData, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        #---------- 2. Update Button --------

        btnUpdate = Button(btnframe, text='Update', command=self.update, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        #---------- 3. Delete Button --------

        btndelete = Button(btnframe, text='Delete',command= self.idelete, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btndelete.grid(row=0, column=2, padx=1)

        #---------- 4. Reset Button --------

        btnreset = Button(btnframe, text='Reset',command=self.ireset, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnreset.grid(row=0, column=3, padx=1)

        #----------- Table Frame and Search System ----------

        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details and Search System', padx=2, font=('times new roman', 12, 'bold'))
        tableframe.place(x=435, y=50, width= 840, height= 490)



        # 1. Label Search By: -------

        lblsearchby = Label(tableframe, text='Search By:', font=('arial', 12, 'bold'), bg='Red', fg='white')
        lblsearchby.grid(row=0, column=0, sticky=W, padx= 2)

        self.searchvar = StringVar()

        combosearchby = ttk.Combobox(tableframe,  textvariable=self.searchvar, font=('arial', 11, 'bold'), state='readonly', width=24)
        combosearchby['values'] = ('MobileNo.', 'Reference')
        combosearchby.current(0)
        combosearchby.grid(row=0, column=1,padx= 2)

        self.txtsearch = StringVar()
        txtsearch = ttk.Entry(tableframe,textvariable=self.txtsearch, width=24, font=('arial', 12, 'bold'))
        txtsearch.grid(row=0, column= 2, padx= 2)

        #---------- 1. Search Button --------

        btnsearch = Button(tableframe, text='Search', command=self.search, font=('arial', 10, 'bold'), bg='black', fg='gold', width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        #---------- 2. showall Button --------

        btnshowall = Button(tableframe, text='Show All',command=self.fetchdata, font=('arial', 10, 'bold'), bg='black', fg='gold', width=10)
        btnshowall.grid(row=0, column=4, padx=1)

        #----------- Show Data Table ----------

        detailstable = Frame(tableframe, bd=2, relief=RIDGE)
        detailstable.place(x=0, y=50, width=820, height=350)

        #---------- Scroll bar for table -------

        scroll_x = ttk.Scrollbar(detailstable, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailstable, orient=VERTICAL)

        self.customer_table = ttk.Treeview(detailstable, columns=('Reference', 'Name', 'Mother Name','Gender', 'Post', 'Mobile', 'Email', 'Nationality', 'Id Proof', 'Id Number', 'Address'), xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading('Reference', text= 'Reference No.')
        self.customer_table.heading('Name', text= 'Customer Name')
        self.customer_table.heading('Mother Name', text= 'Mother Name')
        self.customer_table.heading('Gender', text= 'Gender')
        self.customer_table.heading('Post', text= 'Post')
        self.customer_table.heading('Mobile', text= 'Mobile')
        self.customer_table.heading('Email', text= 'Email')
        self.customer_table.heading('Nationality', text= 'Nationality')
        self.customer_table.heading('Id Proof', text= 'Id Proof')
        self.customer_table.heading('Id Number', text= 'Id No.')
        self.customer_table.heading('Address', text= 'Address')

        self.customer_table['show'] = 'headings'

        self.customer_table.column('Reference', width=100)
        self.customer_table.column('Name', width=100)
        self.customer_table.column('Mother Name', width=100)
        self.customer_table.column('Gender', width=100)
        self.customer_table.column('Post', width=100)
        self.customer_table.column('Mobile', width=100)
        self.customer_table.column('Email', width=100)
        self.customer_table.column('Nationality', width=100)
        self.customer_table.column('Id Proof', width=100)
        self.customer_table.column('Id Number', width=100)
        self.customer_table.column('Address', width=100)

        self.customer_table.pack(fill=BOTH, expand=1)
        self.customer_table.bind('<ButtonRelease-1>', self.getcursor)
        self.fetchdata()

    def addData(self):
        if self.mobile.get()=='' or self.mothername.get()== '':
            messagebox.showerror('Error', 'All fields are required', parent= self.root)
        else:
            try:
                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                m_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                            self.varref.get(),
                                                                                            self.custname.get(),
                                                                                            self.mothername.get(),
                                                                                            self.gender.get(),
                                                                                            self.post.get(),
                                                                                            self.mobile.get(),
                                                                                            self.email.get(),
                                                                                            self.nationality.get(),
                                                                                            self.idproof.get(),
                                                                                            self.idnumber.get(),
                                                                                            self.address.get()

                                                                                        ))
                
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo('Success', 'Customer has been added!!', parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong:{str(es)}!!', parent=self.root)
                

    def fetchdata(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute('select * from customer')
        rows = m_cursor.fetchall()
        if len(rows)!= 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for i in rows:
                self.customer_table.insert('', END, values=i)
        conn.commit()
        conn.close()

    def getcursor(self, event=''):
        rowcursor = self.customer_table.focus()
        content = self.customer_table.item(rowcursor)
        row= content['values']
        self.varref.set(row[0]),
        self.custname.set(row[1]),
        self.mothername.set(row[2]),
        self.gender.set(row[3]),
        self.post.set(row[4]),
        self.mobile.set(row[5]),
        self.email.set(row[6])
        self.nationality.set(row[7]),
        self.idproof.set(row[8]),
        self.idnumber.set(row[9]),
        self.address.set(row[10])


    def update(self):
        if self.mobile.get()=='':
            messagebox.showerror('Error', 'Please Enter Mobile Number!!', parent=self.root)
        else:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            m_cursor.execute('update customer set Name=%s, MotherName=%s, Gender=%s, Post=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s where Reference=%s', (
                                                                                                                                                                                
                                                                                                                                                                                self.custname.get(),
                                                                                                                                                                                self.mothername.get(),
                                                                                                                                                                                self.gender.get(),
                                                                                                                                                                                self.post.get(),
                                                                                                                                                                                self.mobile.get(),
                                                                                                                                                                                self.email.get(),
                                                                                                                                                                                self.nationality.get(),
                                                                                                                                                                                self.idproof.get(),
                                                                                                                                                                                self.idnumber.get(),
                                                                                                                                                                                self.address.get(),
                                                                                                                                                                                self.varref.get()

                                                                                                                                                                                ))
            
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo('Update', 'Customer Details has been updated successfully!!', parent=self.root)

    def idelete(self):
        idelete = messagebox.askyesno('HOTEL MANAGEMENT SYSTEM', 'Do you want to delete this customer??', parent= self.root)
        if idelete>0:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            query = 'delete from customer where Reference=%s'
            value=(self.varref.get(),)
            m_cursor.execute(query, value)
        else:
            if not idelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    def ireset(self):
        #self.varref.set(''),
        self.custname.set(''),
        self.mothername.set(''),
        #self.gender.set(''),
        self.post.set(''),
        self.mobile.set(''),
        self.email.set('')
        #self.nationality.set(''),
        #self.idproof.set(''),
        self.idnumber.set(''),
        self.address.set('')

        x= random.randint(1000, 9999)
        self.varref.set(str(x))

    def search(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute(f"SELECT * FROM customer WHERE {self.searchvar.get()} LIKE %s", (f'%{self.txtsearch.get()}%',))
        rows= m_cursor.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for i in rows:
                self.customer_table.insert('',END, values=i)
            conn.commit()
        conn.close()








if __name__ == "__main__":
    root = Tk()
    obj= CustomerWindow(root)
    root.mainloop()