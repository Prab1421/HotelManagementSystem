from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime

class RoomBooking:
    def __init__(self, root):
        self.root=root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1295x550+235+228')
        #------ Variables ------------
        self.varcontact = StringVar()
        self.checkin = StringVar()
        self.checkout = StringVar()
        self.roomtype = StringVar()
        self.roomavailable = StringVar()
        self.meal = StringVar()
        self.noofdays = StringVar()
        self.paidtax = StringVar()
        self.actualtotal = StringVar()
        self.total = StringVar()

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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='RoomBooking Details', padx=2, font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width= 425, height= 490)

        #------ Label and Entry -----
        # 1. customer reference:---

        lblcustmorcontact = Label(labelframeleft, text='Customer Contact:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcustmorcontact.grid(row=0, column=0, sticky=W)
        txtcontact = ttk.Entry(labelframeleft, textvariable=self.varcontact, width=20, font=('arial', 13, 'bold'))
        txtcontact.grid(row=0, column=1, sticky=W)

        # 0 a. FetchData Button
        btnfetch = Button(labelframeleft, command=self.fetchcontact, text='Fetch', font=('arial', 8, 'bold'), bg='black', fg='gold', width=5)
        btnfetch.place(x=350, y=4)

        # 2. Check-in details
        checkin = Label(labelframeleft, text='Check-in Date:', font=('arial', 12, 'bold'), padx=2, pady=6)
        checkin.grid(row=1, column=0, sticky=W)
        txtcheckin = ttk.Entry(labelframeleft, textvariable=self.checkin, width=27, font=('arial', 13, 'bold'))
        txtcheckin.grid(row=1, column=1)

        # 3. Check-out details
        lblcheckout = Label(labelframeleft, text='Check-out Date:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcheckout.grid(row=2, column=0, sticky=W)
        txtcheckout = ttk.Entry(labelframeleft, textvariable=self.checkout, width=27, font=('arial', 13, 'bold'))
        txtcheckout.grid(row=2, column=1)

        # 4. Room Type
        lblroomT = Label(labelframeleft, text='Room Type:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblroomT.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor = conn.cursor()
        m_cursor.execute('select distinct roomtype from roomdetails')
        rows1 = [row[0] for row in m_cursor.fetchall()]
        conn.close()

        comboroom = ttk.Combobox(labelframeleft, textvariable=self.roomtype, font=('arial', 13, 'bold'), width=25, state='readonly')
        comboroom['values'] = rows1
        comboroom.current(0)
        comboroom.grid(row=3, column=1)

        # Bind the room type combobox to update available rooms
        comboroom.bind("<<ComboboxSelected>>", self.update_available_rooms)

        # 5. Available Room
        lblavailroom = Label(labelframeleft, text='Available Room', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblavailroom.grid(row=4, column=0, sticky=W)

        self.comboroomno = ttk.Combobox(labelframeleft, textvariable=self.roomavailable, font=('arial', 13, 'bold'), width=25, state='readonly')
        self.comboroomno.grid(row=4, column=1)

        # Bind room type selection to update available rooms
        comboroom.bind("<<ComboboxSelected>>", self.update_available_rooms)
        # Populate room types initially
        self.update_available_rooms()

        # 6. Meal (Text Entry)
        lblmeal = Label(labelframeleft, text='Meal(s):', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblmeal.grid(row=5, column=0, sticky=W)
        txtmeal = ttk.Entry(labelframeleft, textvariable=self.meal, width=27, font=('arial', 13, 'bold'))
        txtmeal.grid(row=5, column=1)

        # 7. Date count
        lblnoofdays = Label(labelframeleft, text='No. of Days:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblnoofdays.grid(row=6, column=0, sticky=W)
        txtnoofdays = ttk.Entry(labelframeleft, textvariable=self.noofdays, width=27, font=('arial', 13, 'bold'))
        txtnoofdays.grid(row=6, column=1)

        # 8. Payment
        lblpaidtax = Label(labelframeleft, text='Paid Tax:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0, sticky=W)
        txtpaidtax = ttk.Entry(labelframeleft, textvariable=self.paidtax, width=27, font=('arial', 13, 'bold'))
        txtpaidtax.grid(row=7, column=1)

        # 9. Subtotal
        lblsubtotal = Label(labelframeleft, text='Subtotal', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblsubtotal.grid(row=8, column=0, sticky=W)
        txtsubtotal = ttk.Entry(labelframeleft, textvariable=self.actualtotal, width=27, font=('arial', 13, 'bold'))
        txtsubtotal.grid(row=8, column=1)

        # 10. Total Cost
        lbltotalpayment = Label(labelframeleft, text='Total Cost:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lbltotalpayment.grid(row=9, column=0, sticky=W)
        txttotalpayment = ttk.Entry(labelframeleft, textvariable=self.total, width=27, font=('arial', 13, 'bold'))
        txttotalpayment.grid(row=9, column=1)

        # -------- Bill Button ---------
        btnBill = Button(labelframeleft,command=self.totally, text='Bill', font=('arial', 9, 'bold'), bg='black', fg='gold', width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        #------- Button Frame --------
        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        #---------- 1. Add Button --------

        btnAdd = Button(btnframe,command=self.addData, text='Add', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        #---------- 2. Update Button --------

        btnUpdate = Button(btnframe,command=self.update, text='Update', font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        #---------- 3. Delete Button --------

        btndelete = Button(btnframe, text='Delete', command=self.idelete, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btndelete.grid(row=0, column=2, padx=1)

        #---------- 4. Reset Button --------

        btnreset = Button(btnframe, text='Reset',command=self.ireset, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10)
        btnreset.grid(row=0, column=3, padx=1)

    def update_available_rooms(self, event=None):
        # Fetch the selected room type
        selected_roomtype = self.roomtype.get()

        # Query the database for available rooms based on the selected room type
        conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor = conn.cursor()
        query = 'SELECT roomno FROM roomdetails WHERE roomtype = %s'
        m_cursor.execute(query, (selected_roomtype,))
        rooms = [row[0] for row in m_cursor.fetchall()]
        conn.close()

        # Update the available rooms combobox
        self.comboroomno['values'] = rooms
        if rooms:
            self.comboroomno.current(0)

        

        # --------- Right Side Image ---------------

        img3 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\bed.jpg")
        img3 = img3.resize((515, 262), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.place(x=760, y=55, width=515, height=262)


        #----------- Table Frame and Search System ----------

        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details and Search System', padx=2, font=('times new roman', 12, 'bold'))
        tableframe.place(x=435, y=280, width= 840, height= 260)



        # 1. Label Search By: -------

        lblsearchby = Label(tableframe, text='Search By:', font=('arial', 13, 'bold'), bg='Red', fg='white')
        lblsearchby.grid(row=0, column=0, sticky=W, padx= 2)

        self.searchvar = StringVar()

        combosearchby = ttk.Combobox(tableframe,  textvariable=self.searchvar, font=('arial', 13, 'bold'), state='readonly', width=24)
        combosearchby['values'] = ('Contact', 'Room')
        combosearchby.current(0)
        combosearchby.grid(row=0, column=1,padx= 2)

        self.txtsearch = StringVar()
        txtsearch = ttk.Entry(tableframe,textvariable=self.txtsearch, width=24, font=('arial', 13, 'bold'))
        txtsearch.grid(row=0, column= 2, padx= 2)

        #---------- 1. Search Button --------

        btnsearch = Button(tableframe,command=self.search, text='Search', font=('arial', 9, 'bold'), bg='black', fg='gold', width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        #---------- 2. showall Button --------

        btnshowall = Button(tableframe, text='Show All',command=self.fetchdata, font=('arial', 9, 'bold'), bg='black', fg='gold', width=10)
        btnshowall.grid(row=0, column=4, padx=1)


        #----------- Show Data Table ----------

        detailstable = Frame(tableframe, bd=2, relief=RIDGE)
        detailstable.place(x=0, y=50, width=820, height=180)

        #---------- Scroll bar for table -------

        scroll_x = ttk.Scrollbar(detailstable, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailstable, orient=VERTICAL)

        self.roomtable = ttk.Treeview(detailstable, columns=('contact', 'checkindate', 'checkoutdate','roomtype', 'roomavailable', 'Meal', 'noofdays'), xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.roomtable.xview)
        scroll_y.config(command=self.roomtable.yview)

        self.roomtable.heading('contact', text= 'ContactNo.')
        self.roomtable.heading('checkindate', text= 'CheckinDate')
        self.roomtable.heading('checkoutdate', text= 'CheckoutDate')
        self.roomtable.heading('roomtype', text= 'RoomType')
        self.roomtable.heading('roomavailable', text= 'RoomAvailable')
        self.roomtable.heading('Meal', text= 'Meal')
        self.roomtable.heading('noofdays', text= 'No.ofDays')

        self.roomtable['show'] = 'headings'

        self.roomtable.column('contact', width=100)
        self.roomtable.column('checkindate', width=100)
        self.roomtable.column('checkoutdate', width=100)
        self.roomtable.column('roomtype', width=100)
        self.roomtable.column('roomavailable', width=100)
        self.roomtable.column('Meal', width=100)
        self.roomtable.column('noofdays', width=100)

        self.roomtable.pack(fill=BOTH, expand=1)
        self.roomtable.bind('<ButtonRelease-1>', self.getcursor)
        self.fetchdata()


    # Add Room Data into Database:--------

    def addData(self):
        if self.varcontact.get() == '' or self.checkin.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor = conn.cursor()
                m_cursor.execute('INSERT INTO room (contact, checkin, checkout, roomtype, roomavailable, meal, noofdays) VALUES (%s, %s, %s, %s, %s, %s, %s)', (
                    self.varcontact.get(),
                    self.checkin.get(),
                    self.checkout.get(),
                    self.roomtype.get(),
                    self.roomavailable.get(),
                    self.meal.get(),
                    self.noofdays.get()
                ))
                
                conn.commit()
                self.fetchdata() 
                conn.close()
                messagebox.showinfo('Success', 'Room Booked!!!', parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning', f'Something went wrong: {str(es)}!!', parent=self.root)


    # ----- Working on Fetching the data into columns -------

    def fetchdata(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute('select * from room')
        rows = m_cursor.fetchall()
        if len(rows)!= 0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert('', END, values=i)
        conn.commit()
        conn.close()

    # ----------- Working on update table --------

    def getcursor(self, event=''):
        rowcursor = self.roomtable.focus()
        content = self.roomtable.item(rowcursor)
        row= content['values']
        self.varcontact.set(row[0]),
        self.checkin.set(row[1]),
        self.checkout.set(row[2]),
        self.roomtype.set(row[3]),
        self.roomavailable.set(row[4]),
        self.meal.set(row[5]),
        self.noofdays.set(row[6])


    def update(self):
        if self.varcontact.get()=='':
            messagebox.showerror('Error', 'Please Enter Valid Contact Number!!', parent=self.root)
        else:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            m_cursor.execute('update room set checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, Meal=%s, noofdays=%s where contact=%s', (                           
                                                                                                                                            self.checkin.get(),
                                                                                                                                            self.checkout.get(),
                                                                                                                                            self.roomtype.get(),
                                                                                                                                            self.roomavailable.get(),
                                                                                                                                            self.meal.get(),
                                                                                                                                            self.noofdays.get(),
                                                                                                                                            self.varcontact.get()

                                                                                                                                            ))
            
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo('Update', 'Room Details has been updated successfully!!', parent=self.root)


    # --------- Delete Button Functionality ---------

    def idelete(self):
        idelete = messagebox.askyesno('HOTEL MANAGEMENT SYSTEM', 'Do you want to delete this customer??', parent= self.root)
        if idelete>0:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            query = 'delete from room where contact=%s'
            value=(self.varcontact.get(),)
            m_cursor.execute(query, value)
        else:
            if not idelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()

    #----------- Reset Button Functionality --------

    def ireset(self):
        self.varcontact.set(''),
        self.checkin.set(''),
        self.checkout.set(''),
        self.roomtype.set(''),
        self.roomavailable.set(''),
        self.meal.set(''),
        self.noofdays.set('')
        self.paidtax.set('')
        self.actualtotal.set(''),
        self.total.set('')
    
    def search(self):
        search_value = self.txtsearch.get()
        if not search_value:
            messagebox.showerror("Error", "Please enter a value to search.")
            return

        conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
        m_cursor = conn.cursor()
        
        # Construct the query to search in both 'contact' and 'roomavailable' columns
        query = f"SELECT * FROM room WHERE contact LIKE %s OR roomavailable LIKE %s"
        m_cursor.execute(query, (f'%{search_value}%', f'%{search_value}%'))
        rows = m_cursor.fetchall()

        if rows:
            self.roomtable.delete(*self.roomtable.get_children())
            for row in rows:
                self.roomtable.insert('', END, values=row)
        else:
            messagebox.showinfo("Information", "Record Not Found")

        conn.close()
    # All Data Fetch-----

    def fetchcontact(self):
        if self.varcontact.get()=='':
            messagebox.showerror('Error', 'Please enter contact number!!', parent= self.root)
        else:
            conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor= conn.cursor()
            query = ('select Name from customer where Mobile=%s')
            value = (self.varcontact.get(),)
            m_cursor.execute(query, value)
            row= m_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'ContactNumber not found!!', parent= self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=445, y= 55, width=290, height=180)

                #--------Name:----------

                lblName = Label(showDataframe, text='Name: ', font=('arial', 12, 'bold'))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl.place(x=90, y=0)

                #--------Fetch Gender:------------

                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                query = ('select Gender from customer where Mobile=%s')
                value = (self.varcontact.get(),)
                m_cursor.execute(query, value)
                row= m_cursor.fetchone()

                lblName = Label(showDataframe, text='Gender: ', font=('arial', 12, 'bold'))
                lblName.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl2.place(x=90, y=30)

                #------------- Fetch Email ------------

                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                query = ('select Email from customer where Mobile=%s')
                value = (self.varcontact.get(),)
                m_cursor.execute(query, value)
                row= m_cursor.fetchone()

                lblEmail = Label(showDataframe, text='Email: ', font=('arial', 12, 'bold'))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl3.place(x=90, y=60)

                #-------------- Fetch Nationality -----------

                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                query = ('select Nationality from customer where Mobile=%s')
                value = (self.varcontact.get(),)
                m_cursor.execute(query, value)
                row= m_cursor.fetchone()

                lblNationality = Label(showDataframe, text='Nationality: ', font=('arial', 12, 'bold'))
                lblNationality.place(x=0, y=90)

                lbl3 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl3.place(x=90, y=90)

                #---------------- Address ---------
                conn= mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
                m_cursor= conn.cursor()
                query = ('select Address from customer where Mobile=%s')
                value = (self.varcontact.get(),)
                m_cursor.execute(query, value)
                row= m_cursor.fetchone()

                lblAddress = Label(showDataframe, text='Address: ', font=('arial', 12, 'bold'))
                lblAddress.place(x=0, y=120)

                lbl4 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl4.place(x=90, y=120)

    def totally(self):
        try:
            inDate = self.checkin.get()
            outDate = self.checkout.get()
            inDate = datetime.strptime(inDate, "%Y/%m/%d")
            outDate = datetime.strptime(outDate, "%Y/%m/%d")
            if outDate < inDate:
                self.noofdays.set(0)
            else:
                self.noofdays.set((outDate - inDate).days)

            room_cost = {
                'Single': 200,
                'Double': 600,
                'Air-Conditioned Single': 500,
                'Air-Conditioned Double': 800,
                'Luxury': 1500
            }
            
            # Meal cost based on user input (comma-separated)
            meal_prices = {
                'Breakfast': 100,
                'Lunch': 250,
                'Dinner': 250
            }

            #-------- Select meal/meals according to your choice ------
            selected_meals = self.meal.get().split(',')

            # Calculate total meal cost based on selected meals
            total_meal_cost = sum(meal_prices.get(meal.strip(), 0) for meal in selected_meals)

            # Fetch selected room type and corresponding cost
            selected_roomtype = self.roomtype.get()
            room_cost_amount = float(room_cost.get(selected_roomtype, 0))

            # Calculate total number of days
            days = float(self.noofdays.get())

            # Calculate subtotal, tax, and total cost
            subtotal = (total_meal_cost + room_cost_amount) * days
            tax = subtotal * 0.05  # Assuming 5% tax

            # Format the calculated values for display
            Tax = '₹' + str('%.2f' % tax)
            subtotal_str = '₹' + str('%.2f' % subtotal)
            total = '₹' + str('%.2f' % (subtotal + tax))

            # Set the calculated values to the respective fields
            self.paidtax.set(Tax)
            self.actualtotal.set(subtotal_str)
            self.total.set(total)

        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {ex}")

if __name__ == "__main__":
    root = Tk()
    obj= RoomBooking(root)
    root.mainloop()