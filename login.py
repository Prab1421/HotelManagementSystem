import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import mysql.connector
from hotel import HotelManagement
from customer import CustomerWindow
from room1 import RoomBooking
from details import Details
from report import ReportPage
from feedback import FeedbackPage

def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__ (self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")

        lblbg = Label(self.root, image=self.bg)
        lblbg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg='black')
        frame.place(x= 590, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\LoginIconAppl.png")
        img1= img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg='black', borderwidth=0)
        lblimg1.place(x=710, y=175, width=100, height=100)

        getstart = Label(frame, text='Get Started', font=('arial', 20, 'bold'), bg='black', fg='white')
        getstart.place(x=95, y=105)

        #----------- Labels ---------

        lblusername = Label(frame, text='Username',font=('arial', 15, 'bold'), bg='black', fg='white')
        lblusername.place(x=70, y= 155)

        self.textuser = ttk.Entry(frame, font=('arial', 15, 'bold'))
        self.textuser.place(x=40, y=183, width=270)

        lblpassword = Label(frame, text='Password',font=('arial', 15, 'bold'), bg='black', fg='white')
        lblpassword.place(x=70, y= 225)

        self.textpassword = ttk.Entry(frame, font=('arial', 15, 'bold'), show='*')
        self.textpassword.place(x=40, y=250, width=270)

        #------------- icon images ----------

        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\LoginIconAppl.png")
        img2= img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg='black', borderwidth=0)
        lblimg2.place(x=630, y=325, width=25, height=25)

        img3 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\lock-512.png")
        img3= img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3, bg='black', borderwidth=0)
        lblimg3.place(x=630, y=393, width=25, height=25)


        #login btn
        loginbtn = Button(frame,command=self.loginfunc, text= 'Login',font=('arial', 15, 'bold'), bd= 3, relief= RIDGE, fg='white', bg='red', activeforeground='white', activebackground='red')
        loginbtn.place(x=110, y=300, width=120, height=35)


        # registerbutton-----
        registerbtn = Button(frame, text= 'New User',command=self.regiswindow, font=('arial', 12, 'bold'), bd= 3, borderwidth=0 , fg='white', bg='black', activeforeground='white', activebackground='black')
        registerbtn.place(x=20, y=400, width=130)

        # forgetbutton------
        forgetbtn = Button(frame, text='Forget Password', command=self.forgotpasswordwindow, font=('arial', 12, 'bold'), bd=3, borderwidth=0, fg='white', bg='black', activeforeground='white', activebackground='black')
        forgetbtn.place(x=170, y=400, width=150)

    def regiswindow(self):
        #opening a newwindow when click on new user----
        self.newwindow = Toplevel(self.root)
        self.app = RegisterWindow(self.newwindow)

    def loginfunc(self):
        if self.textuser.get() == '' or self.textpassword.get() == '':
            messagebox.showerror('Error', 'Username or Password Required')
        elif self.textuser.get() == 'kapu' and self.textpassword.get() == 'ashu':
            messagebox.showinfo('Success', 'Welcome!!!')
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor = conn.cursor()
            m_cursor.execute('select * from register where email= %s and password=%s', (
                self.textuser.get(),
                self.textpassword.get()
            ))
            row = m_cursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Invalid username & password', parent=self.root)
            else:
                open_main = messagebox.askyesno('Yes/No', 'Access only Admin')
                if open_main > 0:
                    self.newwindow = Toplevel(self.root)
                    self.app = HotelManagement(self.newwindow)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()


    # For Reset Button in forgotpasswordwindow -------
    def freset(self):
        if self.combosecurity.get()=='Select':
            messagebox.showerror('Error', 'Please Select a security question.!!!', parent = self.root2)
        elif self.txtsecans.get()=='':
            messagebox.showerror('Error', 'Please enter the security answer.!!!', parent = self.root2)
        elif self.txtnewpass.get()=='':
            messagebox.showerror('Error', 'Please enter a new password to reset!!!', parent = self.root2)
        elif self.txtcnewpass.get()=='':
            messagebox.showerror('Error', 'Please enter a confirm new password to reset!!!', parent = self.root2)
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor = conn.cursor()
            query = ('select * from register where email= %s and securityQ=%s and securityA=%s')
            value = (self.textuser.get(), self.combosecurity.get(), self.txtsecans.get(),)
            m_cursor.execute(query, value)
            row = m_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Please enter the correct question or answer!!', parent = self.root2)
            else:
                query1 = ('update register set password=%s where email=%s')
                value1 = (self.txtnewpass.get(), self.textuser.get(),)
                m_cursor.execute(query1, value1)

                conn.commit()
                conn.close()
                messagebox.showinfo('Information', 'Your password has been reset!!!', parent = self.root2)
                self.root2.destroy()


    #---- Function for forget password ---------
    def forgotpasswordwindow(self):
        if self.textuser.get()=='':
            messagebox.showerror('Error', 'Please enter Username!!! to reset password')
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='Mydata')
            m_cursor = conn.cursor()
            query = ('select* from register where email = %s')
            value = (self.textuser.get(),)
            m_cursor.execute(query, value)
            row = m_cursor.fetchone()
            if row== None:
                messagebox.showerror('Error', 'Please enter a valid username!!')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('340x450+610+170')

                l = Label(self.root2 , text='Forget Password', font=('arial', 20, 'bold'), fg='red', bg='white')
                l.place(x=0, y=10, relwidth=1)

                #---- Security Question -----
                lblsecurityQ = Label(self.root2, text='Security Question:',font=('arial', 15, 'bold'),bg='white')
                lblsecurityQ.place(x=50, y= 80)
                self.combosecurity = ttk.Combobox(self.root2, font=('arial', 13, 'bold'))
                self.combosecurity['values'] = ("Select","What was the name of your first pet?", "What is your mother's maiden name?", "What was the name of your first school?", "What is your favorite book?", "In what city were you born?", "What was your childhood nickname?", "What was the make and model of your first car?", "What is the name of the street you grew up on?", "What was the name of your first employer?", "What is your father's middle name?")
                self.combosecurity.place(x=50, y=110, width=270)
                self.combosecurity.current(0)


                # --- Security Answer----
                lblsecans = Label(self.root2, text='Security Answer:',font=('arial', 15, 'bold'),bg='white')
                lblsecans.place(x=50, y= 150)
                self.txtsecans = ttk.Entry(self.root2, font=('arial', 15, 'bold'))
                self.txtsecans.place(x=50, y=180, width=250)

                # ------ New Password -----
                lblnewpass = Label(self.root2, text='New Password:',font=('arial', 15, 'bold'),bg='white')
                lblnewpass.place(x=50, y= 220)
                self.txtnewpass = ttk.Entry(self.root2, font=('arial', 15, 'bold'), show='*')
                self.txtnewpass.place(x=50, y=250, width=250)

                # ------ New Password -----
                lblcnewpass = Label(self.root2, text='Confirm New Password:',font=('arial', 15, 'bold'),bg='white')
                lblcnewpass.place(x=50, y= 290)
                self.txtcnewpass = ttk.Entry(self.root2, font=('arial', 15, 'bold'), show='*')
                self.txtcnewpass.place(x=50, y=320, width=250)

                forgotbtn = Button(self.root2,command=self.freset, text='Reset', font=('arial', 15, 'bold'), fg='white', bg='Darkgreen')
                forgotbtn.place(x=120, y=390)

        
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


class HotelManagement:
    def __init__(self, root):
        self.root=root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1550x800+0+0')

        #Top Most Image for first-----
        img1 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\hotel1.png")
        img1= img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        #---------Logo -----------
        img2 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        #------------Title-------------
        lbltitle= Label(self.root, text='HOTEL MANAGEMENT SYSTEM', font=('times new roman', 40, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=140, width=1550, height=50)

        #---------- Main Frame -----------
        mainframe = Frame(self.root, bd=4, relief=RIDGE)
        mainframe.place(x=0, y=190, width=1550, height=620)

        #----------- menu -----------
        lblmenu = Label(mainframe, text='Menu', font=('times new roman', 28, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lblmenu.place(x=0, y=0, width=230)

        #---------- Button Frame -----------
        btnframe = Frame(mainframe, bd=4, relief=RIDGE)
        btnframe.place(x=0, y=50, width=228, height=250)

        #---------- Customer Button -------
        custbtn = Button(btnframe, command=self.customerdetails, text='CUSTOMER',width=20, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        custbtn.grid(row=0, column=0, pady=1)

        roombtn = Button(btnframe, text='ROOM', command=self.roomdetails, width=20, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        roombtn.grid(row=1, column=0, pady=1)

        detailsbtn = Button(btnframe, text='DETAILS',width=20,command=self.detailsofroom, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        detailsbtn.grid(row=2, column=0, pady=1)

        reportbtn = Button(btnframe, text='REPORT',width=20,command=self.report, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        reportbtn.grid(row=3, column=0, pady=1)

        logoutbtn = Button(btnframe, text='LOGOUT',command=self.logout, width=20, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        logoutbtn.grid(row=4, column=0, pady=1)

        feedbackbtn = Button(btnframe, text='FEEDBACK',command=self.feedback, width=20, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, anchor='center', cursor='hand2')
        feedbackbtn.grid(row=5, column=0, pady=1)

        # ---------- Right Side image -------------
        img3 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(mainframe, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=228, y=0, width=1310, height=590)

        #-------- Down Images -----------

        img4 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\myh.jpg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(mainframe, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=270, width=230, height=210)

        img5 = Image.open(r"C:\Users\HP\Downloads\1633410403702hotel-images\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(mainframe, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=450, width=230, height=190)

    def customerdetails(self):
        self.newwindow = Toplevel(self.root)
        self.app = CustomerWindow(self.newwindow)

    def roomdetails(self):
        self.newwindow = Toplevel(self.root)
        self.app = RoomBooking(self.newwindow)

    def detailsofroom(self):
        self.newwindow = Toplevel(self.root)
        self.app = Details(self.newwindow)

    def logout(self):
        self.root.destroy()

    def report(self):
        self.newwindow = Toplevel(self.root)
        self.app = ReportPage(self.newwindow)

    def feedback(self):
        self.newwindow = Toplevel(self.root)
        self.app = FeedbackPage(self.newwindow)


if __name__ == '__main__':
    main()


    