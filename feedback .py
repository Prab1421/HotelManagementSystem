from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime


class FeedbackPage:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1295x550+235+228')

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

        # Left Section
        left_frame = LabelFrame(main_frame, text='Customer/Employee Details', font=('arial', 12, 'bold'), bd=2, relief=RIDGE)
        left_frame.place(x=5, y=5, width=400, height=480)

        # Right Section
        right_frame = LabelFrame(main_frame, text='Feedback Management', font=('arial', 12, 'bold'), bd=2, relief=RIDGE)
        right_frame.place(x=410, y=5, width=865, height=480)

        # Upper Part of Right Section
        upper_frame = Frame(right_frame, bd=2, relief=RIDGE)
        upper_frame.place(x=5, y=5, width=855, height=225)

        lbl_customer_no = Label(left_frame, text='Customer No:', font=('arial', 12, 'bold'))
        lbl_customer_no.place(x=10, y=10)
        self.txt_customer_no = Entry(left_frame, font=('arial', 12))
        self.txt_customer_no.place(x=150, y=10, width=200)

        lbl_employee_id = Label(left_frame, text='Employee ID:', font=('arial', 12, 'bold'))
        lbl_employee_id.place(x=10, y=50)
        self.txt_employee_id = Entry(left_frame, font=('arial', 12))
        self.txt_employee_id.place(x=150, y=50, width=200)

        lbl_mobile_no = Label(left_frame, text='Mobile No:', font=('arial', 12, 'bold'))
        lbl_mobile_no.place(x=10, y=90)
        self.txt_mobile_no = Entry(left_frame, font=('arial', 12))
        self.txt_mobile_no.place(x=150, y=90, width=200)

        lbl_email = Label(left_frame, text='Email ID:', font=('arial', 12, 'bold'))
        lbl_email.place(x=10, y=130)
        self.txt_email = Entry(left_frame, font=('arial', 12))
        self.txt_email.place(x=150, y=130, width=200)

        lbl_feedback_type = Label(left_frame, text='Feedback Type:', font=('arial', 12, 'bold'))
        lbl_feedback_type.place(x=10, y=170)
        self.cmb_feedback_type = ttk.Combobox(left_frame, font=('arial', 12), state='readonly')
        self.cmb_feedback_type['values'] = ('Complaint', 'Appreciation', 'Suggestion', 'Other')
        self.cmb_feedback_type.place(x=150, y=170, width=200)

        lbl_feedback = Label(upper_frame, text='Feedback:', font=('arial', 12, 'bold'))
        lbl_feedback.place(x=10, y=10)
        self.txt_feedback = Text(upper_frame, font=('arial', 12), height=8, width=60)
        self.txt_feedback.place(x=10, y=40, height=130, width=500)

        btn_submit = Button(upper_frame, text='Submit Feedback', font=('arial', 12, 'bold'), command=self.submit_feedback)
        btn_submit.place(x=10, y=200)

        # Lower Part of Right Section
        lower_frame = Frame(right_frame, bd=2, relief=RIDGE)
        lower_frame.place(x=5, y=235, width=855, height=240)

        self.feedback_table = ttk.Treeview(lower_frame, columns=('ID', 'Mobile No', 'Email', 'Feedback'), show='headings')
        self.feedback_table.heading('ID', text='ID')
        self.feedback_table.heading('Mobile No', text='Mobile No')
        self.feedback_table.heading('Email', text='Email')
        self.feedback_table.heading('Feedback', text='Feedback')
        self.feedback_table.pack(fill=BOTH, expand=1)

        self.fetch_feedback()

    def submit_feedback(self):
        customer_no = self.txt_customer_no.get()
        employee_id = self.txt_employee_id.get()
        feedback = self.txt_feedback.get("1.0", END).strip()

        if not customer_no and not employee_id:
            messagebox.showerror('Error', 'Please enter either Customer No or Employee ID.', parent=self.root)
            return
        
        if not feedback:
            messagebox.showerror('Error', 'Feedback cannot be empty.', parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()

            if customer_no:
                cursor.execute('INSERT INTO feedback (customer_no, feedback) VALUES (%s, %s)', (customer_no, feedback))
            elif employee_id:
                cursor.execute('INSERT INTO feedback (employee_id, feedback) VALUES (%s, %s)', (employee_id, feedback))

            conn.commit()
            conn.close()
            messagebox.showinfo('Success', 'Feedback submitted successfully!', parent=self.root)
            self.fetch_feedback()
        except Exception as e:
            messagebox.showwarning('Error', f'Error: {str(e)}', parent=self.root)

    def fetch_feedback(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM feedback')
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.feedback_table.delete(*self.feedback_table.get_children())
                for row in rows:
                    self.feedback_table.insert('', END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showwarning('Error', f'Error: {str(e)}', parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = FeedbackPage(root)
    root.mainloop()
