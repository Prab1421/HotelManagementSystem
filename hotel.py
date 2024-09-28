from tkinter import*
from PIL import Image, ImageTk   #pip install pillow
from customer import CustomerWindow
from room import RoomBooking
from details import Details
from report import ReportPage
from feedback import FeedbackPage



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


if __name__ == "__main__":
    root = Tk()
    obj= HotelManagement(root)
    root.mainloop()


