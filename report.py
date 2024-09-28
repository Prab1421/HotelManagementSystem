from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk

class ReportPage:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL MANAGEMENT SYSTEM - REPORT PAGE')
        self.root.geometry('1295x550+235+228')

        #---- variables ---------
        self.roomno = StringVar()
        self.custname = StringVar()
        self.idproof = StringVar()
        self.checkin = StringVar()
        self.checkout = StringVar()
        self.meal = StringVar()
        self.roomtype = StringVar()
        self.noofdays = StringVar()
        self.mobile= StringVar()

        # Title
        lbltitle = Label(self.root, text='REPORT PAGE', font=('times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # Labelframe for Report Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Report Details', padx=2, font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=5, y=50, width=600, height=490)

        # Labels and Entries for Report Details
        # Room Number
        lblroomno = Label(labelframeleft, text='Room No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblroomno.grid(row=0, column=0, sticky=W)
        self.txtroomno = ttk.Entry(labelframeleft,textvariable=self.roomno, width=29, font=('arial', 13, 'bold'))
        self.txtroomno.grid(row=0, column=1)

        # Customer Name
        lblcustname = Label(labelframeleft, text='Customer Name:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcustname.grid(row=1, column=0, sticky=W)
        self.txtcustname = ttk.Entry(labelframeleft,textvariable=self.custname, width=29, font=('arial', 13, 'bold'))
        self.txtcustname.grid(row=1, column=1)

        # Duration of Stay
        lblduration = Label(labelframeleft, text='Duration of Stay:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblduration.grid(row=2, column=0, sticky=W)
        self.txtduration = ttk.Entry(labelframeleft,textvariable=self.noofdays, width=29, font=('arial', 13, 'bold'))
        self.txtduration.grid(row=2, column=1)

        # mobile
        lblmobile = Label(labelframeleft, text='Mobile No.:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblmobile.grid(row=3, column=0, sticky=W)
        self.txtmobile = ttk.Entry(labelframeleft,textvariable=self.mobile, width=29, font=('arial', 13, 'bold'))
        self.txtmobile.grid(row=3, column=1)


        # Check-In Date
        lblcheckin = Label(labelframeleft, text='Check-In Date:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcheckin.grid(row=4, column=0, sticky=W)
        self.txtcheckin = ttk.Entry(labelframeleft,textvariable=self.checkin, width=29, font=('arial', 13, 'bold'))
        self.txtcheckin.grid(row=4, column=1)

        # Check-Out Date
        lblcheckout = Label(labelframeleft, text='Check-Out Date:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblcheckout.grid(row=5, column=0, sticky=W)
        self.txtcheckout = ttk.Entry(labelframeleft,textvariable=self.checkout, width=29, font=('arial', 13, 'bold'))
        self.txtcheckout.grid(row=5, column=1)

        # Meal Type
        lblmeal = Label(labelframeleft, text='Meal Type:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblmeal.grid(row=6, column=0, sticky=W)
        self.meal = StringVar()
        meal_entry = ttk.Entry(labelframeleft,textvariable=self.meal, width=29, font=('arial', 13, 'bold'))
        meal_entry.grid(row=6, column=1)

        # Room Type
        lblroomtype = Label(labelframeleft, text='Room Type:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblroomtype.grid(row=7, column=0, sticky=W)
        self.roomtype = StringVar()
        roomtype_entry = ttk.Entry(labelframeleft, textvariable=self.roomtype, width=29, font=('arial', 13, 'bold'))
        roomtype_entry.grid(row=7, column=1)

        # Tax and Total Fields
        lbltax = Label(labelframeleft, text='Tax:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lbltax.grid(row=8, column=0, sticky=W)
        self.paidtax = StringVar()
        txttax = ttk.Entry(labelframeleft, textvariable=self.paidtax, width=29, font=('arial', 13, 'bold'))
        txttax.grid(row=8, column=1)

        lblsubtotal = Label(labelframeleft, text='Subtotal:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblsubtotal.grid(row=9, column=0, sticky=W)
        self.actualtotal = StringVar()
        txtsubtotal = ttk.Entry(labelframeleft, textvariable=self.actualtotal, width=29, font=('arial', 13, 'bold'))
        txtsubtotal.grid(row=9, column=1)

        # Charges
        lbltotal = Label(labelframeleft, text='Total:', font=('arial', 12, 'bold'), padx=2, pady=6)
        lbltotal.grid(row=10, column=0, sticky=W)
        self.total = StringVar()
        txttotal = ttk.Entry(labelframeleft, textvariable=self.total, width=29, font=('arial', 13, 'bold'))
        txttotal.grid(row=10, column=1)

        

        # Button Frame for Search, Reset, and Calculate
        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=410, width=590, height=40)

        # Search Button
        btnsearch = Button(btnframe, text='Search', command=self.search_data, font=('arial', 11, 'bold'), bg='black', fg='gold', width=20)
        btnsearch.grid(row=0, column=0, padx=1)

        # Reset Button
        btnreset = Button(btnframe, text='Reset', command=self.reset_fields, font=('arial', 11, 'bold'), bg='black', fg='gold', width=20)
        btnreset.grid(row=0, column=1, padx=1)

        # Calculate Button
        btncalculate = Button(btnframe, text='Calculate', command=self.totally, font=('arial', 11, 'bold'), bg='black', fg='gold', width=20)
        btncalculate.grid(row=0, column=2, padx=1)

        # Table Frame for Displaying Data
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details', padx=2, font=('times new roman', 12, 'bold'))
        tableframe.place(x=610, y=50, width=675, height=490)

        # Scrollbars for the Table
        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.report_table = ttk.Treeview(tableframe, columns=('Room No', 'Customer Name', 'Duration', 'Check-In', 'Check-Out', 'Meal Type', 'Room Type', 'Mobile'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.report_table.xview)

        scroll_y.config(command=self.report_table.yview)

    # Define Column Headings
        self.report_table.heading('Room No', text='Room No')
        self.report_table.heading('Customer Name', text='Customer Name')
        self.report_table.heading('Duration', text='Duration')
        self.report_table.heading('Check-In', text='Check-In Date')
        self.report_table.heading('Check-Out', text='Check-Out Date')
        self.report_table.heading('Meal Type', text='Meal Type')
        self.report_table.heading('Room Type', text='Room Type')
        self.report_table.heading('Mobile', text='Mobile No.')

        self.report_table['show'] = 'headings'

        # Define Column Widths
        self.report_table.column('Room No', width=150)
        self.report_table.column('Customer Name', width=150)
        self.report_table.column('Duration', width=100)
        self.report_table.column('Check-In', width=150)
        self.report_table.column('Check-Out', width=150)
        self.report_table.column('Meal Type', width=150)
        self.report_table.column('Room Type', width=150)
        self.report_table.column('Mobile', width=150)

        self.report_table.pack(fill=BOTH, expand=1)

        # Populate Data
        self.report_table.bind('<ButtonRelease-1>', self.getcursor)
        self.fetch_data()

    def getcursor(self, event=''):
        rowcursor = self.report_table.focus()
        content = self.report_table.item(rowcursor)
        row= content['values']
        self.roomno.set(row[0]),
        self.custname.set(row[1]), 
        self.noofdays.set(row[2]),
        self.checkin.set(row[3]),
        self.checkout.set(row[4]),
        self.meal.set(row[5]),
        self.roomtype.set(row[6]),
        self.mobile.set(row[7])
        
        

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="mydata"
            )
            cursor = conn.cursor()

            # SQL query to join customer and room tables based on contact information
            query = '''
            SELECT 
                r.roomavailable AS 'Room No', 
                c.Name AS 'Customer Name', 
                r.noofdays AS 'Duration',  
                r.checkin AS 'Check-In Date', 
                r.checkout AS 'Check-Out Date', 
                r.Meal AS 'Meal Type', 
                r.roomtype AS 'Room Type', 
                c.Mobile AS 'Mobile no.'
            FROM 
                customer c
            JOIN 
                room r ON c.Mobile = r.contact
            '''
            
            cursor.execute(query)
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.report_table.delete(*self.report_table.get_children())
                for row in rows:
                    self.report_table.insert('', END, values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def search_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="mydata"
            )
            cursor = conn.cursor()

            search_query = '''
            SELECT 
                r.roomavailable AS 'Room No', 
                c.Name AS 'Customer Name', 
                r.noofdays AS 'Duration',  
                r.checkin AS 'Check-In Date', 
                r.checkout AS 'Check-Out Date',
                r.Meal AS 'Meal Type', 
                r.roomtype AS 'Room Type',
                c.Mobile AS 'Mobile no.'
            FROM 
                customer c
            JOIN 
                room r ON c.Mobile = r.contact
            WHERE 1=1
            '''

            if self.txtroomno.get():
                search_query += f" AND r.roomavailable LIKE '%{self.txtroomno.get()}%'"
            if self.txtcustname.get():
                search_query += f" AND c.Name LIKE '%{self.txtcustname.get()}%'"
            if self.txtcheckin.get() and self.txtcheckout.get():
                search_query += f" AND r.checkin >= '{self.txtcheckin.get()}' AND r.checkout <= '{self.txtcheckout.get()}'"

            cursor.execute(search_query)
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.report_table.delete(*self.report_table.get_children())
                for row in rows:
                    self.report_table.insert('', END, values=row)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found.")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def reset_fields(self):
        self.txtroomno.delete(0, END)
        self.txtcustname.delete(0, END)
        self.txtduration.delete(0, END)
        self.txtmobile.delete(0, END)
        self.txtcheckin.delete(0, END)
        self.txtcheckout.delete(0, END)
        self.meal.set('')
        self.roomtype.set('')
        self.paidtax.set('')
        self.actualtotal.set('')
        self.total.set('')
        self.fetch_data()

    def totally(self):
        try:
            inDate = self.txtcheckin.get()
            outDate = self.txtcheckout.get()
            inDate = datetime.strptime(inDate, "%Y/%m/%d")
            outDate = datetime.strptime(outDate, "%Y/%m/%d")
            if outDate < inDate:
                self.txtduration.delete(0, END)  
            else:
                self.txtduration.delete(0, END)
                self.txtduration.insert(0, (outDate - inDate).days)
        except ValueError:
            self.txtduration.delete(0, END)
        
        room_cost = {
            'Single': 500,
            'Double': 1000,
            'Air-Conditioned Single': 1500,
            'Air-Conditioned Double': 2000,
            'Luxury': 3000
        }

        meal_cost = {
            'Breakfast': 300,
            'Lunch': 500,
            'Dinner': 700
        }
        
        selected_meal = self.meal.get()
        selected_roomtype = self.roomtype.get()
        q1 = float(meal_cost.get(selected_meal, 0))
        q2 = float(room_cost.get(selected_roomtype, 0))
        q3 = float(self.txtduration.get())
        q4 = float(q1 + q2)  
        q5 = float(q3 * q4) 
        Tax = 'Rs.' + str('%.2f' % (q5 * 0.05))
        subtotal = 'Rs.' + str('%.2f' % q5)
        total = 'Rs.' + str('%.2f' % (q5 + (q5 * 0.05)))
        self.paidtax.set(Tax)
        self.actualtotal.set(subtotal)
        self.total.set(total)


if __name__ == "__main__":
    root = Tk()
    obj = ReportPage(root)
    root.mainloop()
