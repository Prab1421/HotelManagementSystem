from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class FeedbackPage:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1295x550+235+228')

        # Variables
        self.selection = StringVar()
        self.id = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.feedback_type = StringVar()
        self.feedback_text = StringVar()
        self.fid = StringVar()

        # Title Label
        lbltitle = Label(self.root, text='FEEDBACK PAGE', font=('times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)

        # Logo Image
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=5, y=55, width=1285, height=490)

        # Left Section (Customer/Employee Details)
        left_frame = LabelFrame(main_frame, text='Customer/Employee Details', font=('arial', 12, 'bold'), bd=2, relief=RIDGE)
        left_frame.place(x=5, y=5, width=400, height=480)

        lbl_selection = Label(left_frame, text='Select:', font=('arial', 12, 'bold'))
        lbl_selection.place(x=10, y=10)
        self.cmb_selection = ttk.Combobox(left_frame, textvariable=self.selection, font=('arial', 12), state='readonly')
        self.cmb_selection['values'] = ('Customer', 'Employee')
        self.cmb_selection.current(0)
        self.cmb_selection.place(x=150, y=10, width=200)
        self.cmb_selection.bind('<<ComboboxSelected>>', self.update_form)

        lbl_id = Label(left_frame, text='ID:', font=('arial', 12, 'bold'))
        lbl_id.place(x=10, y=50)
        self.txt_id = ttk.Entry(left_frame, textvariable=self.id, font=('arial', 12))
        self.txt_id.place(x=150, y=50, width=200)

        lbl_fname = Label(left_frame, text='First Name:', font=('arial', 12, 'bold'))
        lbl_fname.place(x=10, y=90)
        self.txt_fname = ttk.Entry(left_frame, textvariable=self.fname, font=('arial', 12))
        self.txt_fname.place(x=150, y=90, width=200)

        lbl_lname = Label(left_frame, text='Last Name:', font=('arial', 12, 'bold'))
        lbl_lname.place(x=10, y=130)
        self.txt_lname = ttk.Entry(left_frame, textvariable=self.lname, font=('arial', 12))
        self.txt_lname.place(x=150, y=130, width=200)

        lbl_mobile = Label(left_frame, text='Mobile:', font=('arial', 12, 'bold'))
        lbl_mobile.place(x=10, y=170)
        self.txt_mobile = ttk.Entry(left_frame, textvariable=self.mobile, font=('arial', 12))
        self.txt_mobile.place(x=150, y=170, width=200)

        lbl_email = Label(left_frame, text='Email:', font=('arial', 12, 'bold'))
        lbl_email.place(x=10, y=210)
        self.txt_email = ttk.Entry(left_frame, textvariable=self.email, font=('arial', 12))
        self.txt_email.place(x=150, y=210, width=200)

        lbl_fid = Label(left_frame, text='Feedback_id:', font=('arial', 12, 'bold'))
        lbl_fid.place(x=10, y=250)
        self.txt_fid = ttk.Entry(left_frame, textvariable=self.fid, font=('arial', 12))
        self.txt_fid.place(x=150, y=250, width=200)

        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=30, y=300, width=300, height=40)

        btnUpdate = Button(btn_frame, text='Update',command=self.update_data, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10, activebackground='red', foreground='gold')
        btnUpdate.grid(row=0, column=0, padx=1)

        btnDelete = Button(btn_frame,  text='Delete',command=self.delete_data, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10, activebackground='red', foreground='gold')
        btnDelete.grid(row=0, column=1, padx=1)

        btnReset = Button(btn_frame, text='Reset',command=self.reset_fields, font=('arial', 11, 'bold'), bg='black', fg='gold', width=10, activebackground='red', foreground='gold')
        btnReset.grid(row=0, column=2, padx=1)

        # Right Section (Feedback Management)
        right_frame = LabelFrame(main_frame, text='Feedback Management', font=('arial', 12, 'bold'), bd=2, relief=RIDGE)
        right_frame.place(x=410, y=5, width=865, height=480)

        # Upper Part of Right Section
        upper_frame = Frame(right_frame, bd=2, relief=RIDGE)
        upper_frame.place(x=5, y=5, width=855, height=225)

        lbl_feedback_type = Label(upper_frame, text='Feedback Type:', font=('arial', 12, 'bold'))
        lbl_feedback_type.place(x=10, y=10)
        self.cmb_feedback_type = ttk.Combobox(upper_frame, textvariable=self.feedback_type, font=('arial', 12), state='readonly')
        self.cmb_feedback_type['values'] = ('Complaint', 'Suggestion', 'Feedback', 'Other')
        self.cmb_feedback_type.current(0)
        self.cmb_feedback_type.place(x=150, y=10, width=200)

        lbl_feedback = Label(upper_frame, text='Feedback:', font=('arial', 12, 'bold'))
        lbl_feedback.place(x=10, y=50)
        self.txt_feedback = Text(upper_frame, font=('arial', 12), height=8, width=60)
        self.txt_feedback.place(x=10, y=80, height=130, width=800)



        btn_submit = Button(upper_frame, text='Submit Feedback', font=('arial', 12, 'bold'), command=self.submit_feedback, bg='blue', fg='white', activebackground='red', activeforeground='white')
        btn_submit.place(x=650, y=175, width=150)

        # Lower Part of Right Section (Feedback Display)
        lower_frame = Frame(right_frame, bd=2, relief=RIDGE)
        lower_frame.place(x=5, y=235, width=855, height=210)

        # Scrollbars
        scroll_x = Scrollbar(lower_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(lower_frame, orient=VERTICAL)

        self.feedback_table = ttk.Treeview(lower_frame, columns=( 'feedback_id', 'ID', 'First Name', 'Last Name', 'Mobile', 'Email', 'Feedback Type', 'Feedback'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.feedback_table.xview)
        scroll_y.config(command=self.feedback_table.yview)

        self.feedback_table.heading('feedback_id', text='Feedback_ID')
        self.feedback_table.heading('ID', text='ID')
        self.feedback_table.heading('First Name', text='First Name')
        self.feedback_table.heading('Last Name', text='Last Name')
        self.feedback_table.heading('Mobile', text='Mobile')
        self.feedback_table.heading('Email', text='Email')
        self.feedback_table.heading('Feedback Type', text='Feedback Type')
        self.feedback_table.heading('Feedback', text='Feedback')

        self.feedback_table['show'] = 'headings'

        # Set column width to 150 for all columns
        self.feedback_table.column('feedback_id', width=150)
        self.feedback_table.column('ID', width=150)
        self.feedback_table.column('First Name', width=150)
        self.feedback_table.column('Last Name', width=150)
        self.feedback_table.column('Mobile', width=150)
        self.feedback_table.column('Email', width=150)
        self.feedback_table.column('Feedback Type', width=150)
        self.feedback_table.column('Feedback', width=150)
        

        self.feedback_table.pack(fill=BOTH, expand=1)
        self.feedback_table.bind('<<TreeviewSelect>>', self.getcursor)
        self.fetch_feedback()

    def update_form(self, event):
        selection = self.selection.get()
        if selection == 'Customer':
            self.txt_fname.config(state=NORMAL)
            self.txt_lname.config(state=NORMAL)
        else:
            self.txt_fname.config(state=NORMAL)
            self.txt_lname.config(state=NORMAL)

    def submit_feedback(self):
        selection = self.selection.get()
        id = self.txt_id.get()
        fname = self.txt_fname.get()
        lname = self.txt_lname.get()
        mobile = self.txt_mobile.get()
        email = self.txt_email.get()
        feedback_type = self.cmb_feedback_type.get()
        feedback = self.txt_feedback.get("1.0", END).strip()
        fid = self.txt_fid.get()

        if not id or not fname or not lname or not mobile or not email:
            messagebox.showerror('Error', 'Please enter ID.', parent=self.root)
            return

        if not feedback:
            messagebox.showerror('Error', 'Feedback cannot be empty.', parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()

            if selection == 'Customer':
                cursor.execute("SELECT * FROM customer WHERE Reference = %s", (id,))
                customer = cursor.fetchone()
                if not customer:
                    messagebox.showerror('Error', 'Customer not found.', parent=self.root)
                    return
                cursor.execute('''
                    INSERT INTO feedback (id, first_name, last_name, mobile, email, feedback_type, feedback, feedback_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
                ''', (id, fname, lname, mobile, email, feedback_type, feedback, fid))
            elif selection == 'Employee':
                cursor.execute("SELECT * FROM register WHERE emplid = %s", (id,))
                employee = cursor.fetchone()
                if not employee:
                    messagebox.showerror('Error', 'Employee not found.', parent=self.root)
                    return
                cursor.execute('''
                    INSERT INTO feedback (id, first_name, last_name, mobile, email, feedback_type, feedback, feedback_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
                ''', (id, fname, lname, mobile, email, feedback_type, feedback, fid))

            conn.commit()
            messagebox.showinfo('Success', 'Feedback submitted successfully.', parent=self.root)
            self.fetch_feedback()
            self.reset_fields()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f"Error occurred: {e}", parent=self.root)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def reset_fields(self):
        """Reset all input fields."""
        self.cmb_selection.current(0)
        self.id.set('')
        self.fname.set('')
        self.lname.set('')
        self.mobile.set('')
        self.email.set('')
        self.feedback_type.set('')
        self.txt_feedback.delete("1.0", END)
        self.fid.set('')
        

    def fetch_feedback(self):
        for record in self.feedback_table.get_children():
            self.feedback_table.delete(record)

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM feedback")
            rows = cursor.fetchall()

            for row in rows:
                self.feedback_table.insert('', END, values=row)

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f"Error occurred: {e}", parent=self.root)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def getcursor(self, event=''):
        rowcursor = self.feedback_table.focus()
        content = self.feedback_table.item(rowcursor)
        row = content['values']
        
        if len(row) >= 8: 
            self.id.set(row[1])          
            self.fname.set(row[2])        
            self.lname.set(row[3])        
            self.email.set(row[5])       
            self.mobile.set(row[4])      
            self.feedback_type.set(row[6])
            self.txt_feedback.delete("1.0", END)
            self.txt_feedback.insert(END, row[7]) 
            self.fid.set(row[0])
        else:
            print("Selected row does not contain enough data.")

    def update_data(self):
        id = self.id.get()
        fname = self.fname.get()
        lname = self.lname.get()
        mobile = self.mobile.get()
        email = self.email.get()
        feedback_type = self.feedback_type.get()
        feedback_text = self.txt_feedback.get("1.0", END).strip()
        fid = self.fid.get()

        if not id:
            messagebox.showerror('Error', 'Please select a record to update.', parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()

            cursor.execute('''
                UPDATE feedback SET  feedback_id=%s, first_name=%s, last_name=%s, mobile=%s, email=%s, feedback_type=%s, feedback=%s 
                WHERE id=%s
            ''', (fid, fname, lname, mobile, email, feedback_type, feedback_text, id))

            conn.commit()
            messagebox.showinfo('Success', 'Feedback updated successfully.', parent=self.root)
            self.fetch_feedback()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f"Error occurred: {e}", parent=self.root)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_data(self):
        """Delete the selected record from the database."""
        id = self.id.get()

        if not id:
            messagebox.showerror('Error', 'Please select a record to delete.', parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM feedback WHERE id = %s", (id,))

            conn.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo('Error', 'Record not found or already deleted.', parent=self.root)
            else:
                messagebox.showinfo('Success', 'Record deleted successfully.', parent=self.root)

            self.fetch_feedback()
            self.reset_fields()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f"Error occurred: {e}", parent=self.root)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = FeedbackPage(root)
    root.mainloop()
