import random
import smtplib
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from login import LoginWindow

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Register')
        self.root.geometry('1530x800+0+0')

        #------- Variables --------
        self.fname = StringVar()
        self.lname = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        self.securityQ = StringVar()
        self.securityA = StringVar()
        self.password = StringVar()
        self.confirmp = StringVar()
        self.checkbtn = IntVar()
        self.otp = StringVar()
        self.emplid = StringVar()  # Variable to store employee ID

        # Generate and set employee ID
        self.generate_emplid()

        #--------- Background Image -------------
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\taj.jpg")
        lblbg = Label(self.root, image=self.bg)
        lblbg.place(x=0, y=0, relwidth=1, relheight=1)

        # ------------ Left Image ----------
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\room2.jpg")
        leftbg = Label(self.root, image=self.bg1)
        leftbg.place(x=50, y=100, width=470, height=580)

        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=760, height=580)

        #----------- Labels ---------
        lblregister = Label(frame, text='REGISTER HERE', font=('arial', 20, 'bold'), bg='white', fg='Darkgreen')
        lblregister.place(x=20, y=20)

        lblemplid = Label(frame, text='Employee ID:', font=('arial', 15, 'bold'), bg='white')
        lblemplid.place(x=50, y=70)
        self.txtemplid = ttk.Entry(frame, textvariable=self.emplid, font=('arial', 15, 'bold'), state='readonly')
        self.txtemplid.place(x=50, y=100, width=250)

        lblfirstname = Label(frame, text='First Name:', font=('arial', 15, 'bold'), bg='white')
        lblfirstname.place(x=50, y=130)
        self.txtfname = ttk.Entry(frame, textvariable=self.fname, font=('arial', 15, 'bold'))
        self.txtfname.place(x=50, y=160, width=250)

        # --- Last Name ----
        lbllastname = Label(frame, text='Last Name:', font=('arial', 15, 'bold'), bg='white')
        lbllastname.place(x=390, y=130)
        self.txtlname = ttk.Entry(frame, textvariable=self.lname, font=('arial', 15, 'bold'))
        self.txtlname.place(x=390, y=160, width=250)

        #---- Contact -----
        lblcontact = Label(frame, text='Contact:', font=('arial', 15, 'bold'), bg='white')
        lblcontact.place(x=50, y=200)
        self.txtcontact = ttk.Entry(frame, textvariable=self.contact, font=('arial', 15, 'bold'))
        self.txtcontact.place(x=50, y=230, width=250)

        # --- Email ----
        lblemail = Label(frame, text='Email:', font=('arial', 15, 'bold'), bg='white')
        lblemail.place(x=390, y=200)
        self.txtemail = ttk.Entry(frame, textvariable=self.email, font=('arial', 15, 'bold'))
        self.txtemail.place(x=390, y=230, width=250)

        #---- Security Question -----
        lblsecurityQ = Label(frame, text='Security Question:', font=('arial', 15, 'bold'), bg='white')
        lblsecurityQ.place(x=50, y=290)
        self.combosecurity = ttk.Combobox(frame, textvariable=self.securityQ, font=('arial', 13, 'bold'))
        self.combosecurity['values'] = (
            "Select", "What was the name of your first pet?", "What is your mother's maiden name?",
            "What was the name of your first school?", "What is your favorite book?", "In what city were you born?",
            "What was your childhood nickname?", "What was the make and model of your first car?",
            "What is the name of the street you grew up on?", "What was the name of your first employer?",
            "What is your father's middle name?"
        )
        self.combosecurity.place(x=50, y=320, width=270)
        self.combosecurity.current(0)

        # --- Security Answer----
        lblsecans = Label(frame, text='Security Answer:', font=('arial', 15, 'bold'), bg='white')
        lblsecans.place(x=390, y=290)
        self.txtsecans = ttk.Entry(frame, textvariable=self.securityA, font=('arial', 15, 'bold'))
        self.txtsecans.place(x=390, y=320, width=250)

        #---- Password -----
        lblpassword = Label(frame, text='Password:', font=('arial', 15, 'bold'), bg='white')
        lblpassword.place(x=50, y=370)
        self.txtpassword = ttk.Entry(frame, textvariable=self.password, font=('arial', 15, 'bold'), show='*')
        self.txtpassword.place(x=50, y=400, width=250)

        # --- Confirm Password----
        lblconfirmP = Label(frame, text='Confirm Password:', font=('arial', 15, 'bold'), bg='white')
        lblconfirmP.place(x=390, y=370)
        self.txtconfirmP = ttk.Entry(frame, textvariable=self.confirmp, font=('arial', 15, 'bold'), show='*')
        self.txtconfirmP.place(x=390, y=400, width=250)

        # Check button ------
        Checkbtn = Checkbutton(frame, variable=self.checkbtn, text='I Agree The Terms & Conditions',
                               font=('arial', 12, 'bold'), bg='white', onvalue=1, offvalue=0)
        Checkbtn.place(x=50, y=460)

        # ----- Register Button -----
        img1 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\register-now-button1.jpg")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, command=self.registerdata, image=self.photoimg1, borderwidth=0, bg='white',
                    activebackground='white', cursor='hand2')
        b1.place(x=130, y=500, width=270)

        # ----- Login Button -----
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\loginpng.png")
        img2 = img2.resize((200, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(frame, command=self.login_page, image=self.photoimg2, borderwidth=0, bg='white',
                    activebackground='white', cursor='hand2')
        b2.place(x=360, y=510, width=250)

    def generate_emplid(self):
        # Generate a random 6-digit employee ID
        self.emplid.set(str(random.randint(100000, 999999)))

    def login_page(self):
        self.newwindow = Toplevel(self.root)
        self.app = LoginWindow(self.newwindow)

    # ----- Function to Register Data with OTP Verification ---------
    def registerdata(self):
        if self.fname.get() == '' or self.email.get() == '' or self.securityQ.get() == 'Select':
            messagebox.showerror('Error', 'All fields are required!!!')
        elif self.password.get() != self.confirmp.get():
            messagebox.showerror('Error', 'Password & Confirm Password must be the same!!!')
        elif self.checkbtn.get() == 0:
            messagebox.showerror('Error', 'Please Agree to Terms & Conditions')
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            my_cursor = conn.cursor()
            query = 'SELECT * FROM register WHERE email=%s'
            value = (self.email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is not None:
                messagebox.showerror('Error', 'User already exists!!!')
            else:
                otp = str(random.randint(100000, 999999)) 
                self.send_otp(otp)  
                self.prompt_otp_verification(otp)

    # ---- Function to Send OTP ---------
    def send_otp(self, otp):
        admin_email = 'prab3906@gmail.com'
        admin_password = 'glqi jiqn hcht hyhl'  
        
        try:
            # Email setup
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            from_email = admin_email
            to_email = admin_email

            # Create the email content
            subject = 'Your OTP Code'
            body = f'Your OTP code is: {otp}'

            # Create MIME message
            message = MIMEMultipart()
            message['From'] = from_email
            message['To'] = to_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Connect to the server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(admin_email, admin_password)
                server.send_message(message)

            print(f"OTP sent to admin email: {otp}")

        except Exception as e:
            print(f"Failed to send OTP: {e}")
            print(f"OTP sent to admin: {otp}")

    def prompt_otp_verification(self, correct_otp):
        otp_window = Toplevel(self.root)
        otp_window.title("OTP Verification")
        otp_window.geometry("300x150+600+300")

        otp_label = Label(otp_window, text="Enter OTP", font=('arial', 15, 'bold'))
        otp_label.pack(pady=10)

        otp_entry = Entry(otp_window, textvariable=self.otp, font=('arial', 15, 'bold'))
        otp_entry.pack(pady=10)

        verify_button = Button(otp_window, text="Verify",
                               command=lambda: self.verify_otp(correct_otp, otp_window),
                               font=('arial', 12, 'bold'))
        verify_button.pack(pady=10)

    def verify_otp(self, correct_otp, otp_window):
        entered_otp = self.otp.get()
        if entered_otp == correct_otp:
            otp_window.destroy()  
            self.save_to_db()  
        else:
            messagebox.showerror('Error', 'Invalid OTP! Please try again.')

    def save_to_db(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            my_cursor = conn.cursor()
            query = 'INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password, emplid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            value = (self.fname.get(), self.lname.get(), self.contact.get(), self.email.get(), self.securityQ.get(), self.securityA.get(), self.password.get(), self.emplid.get())
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', 'Registration successful!')
            self.reset_fields()  # Reset the fields after successful registration
        except Exception as e:
            messagebox.showerror('Error', f"Error due to: {str(e)}")


    def reset_fields(self):
        self.fname.set('')
        self.lname.set('')
        self.contact.set('')
        self.email.set('')
        self.securityQ.set('Select')
        self.securityA.set('')
        self.password.set('')
        self.confirmp.set('')
        self.checkbtn.set(0)
        self.generate_emplid()  


root = Tk()
obj = RegisterWindow(root)
root.mainloop()
