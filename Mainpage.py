from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Mainpage:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry("1350x700+0+0")

        #  Top Image

        self.top = ImageTk.PhotoImage(file="images/log.gif")
        left = Label(self.root, image=self.top, bg="white").place(x=0, y=0, width=1350, height=160)

        #Top left

        self.top_left = ImageTk.PhotoImage(file="images/content_scholarships.png")
        left = Label(self.root, image=self.top_left, bg="white").place(x=0, y=160, width=500, height=500)

        self.bottom_left = ImageTk.PhotoImage(file="images/lll.png")
        left = Label(self.root, image=self.bottom_left, bg="white").place(x=0, y=550, width=500, height=150)

        # Login Frame
        frame1 = Frame(self.root, bg="gray")
        frame1.place(x=500, y=160, width=1000, height=800)


        self.frame_left = ImageTk.PhotoImage(file="images/staff first.jpg")
        left = Label(frame1, image=self.frame_left, bg="white").place(x=50, y=50, width=225, height=225)

        self.frame_right = ImageTk.PhotoImage(file="images/sssss.jpg")
        left = Label(frame1, image=self.frame_right, bg="white").place(x=50, y=290, width=225, height=255)

        self.btn_staff = ImageTk.PhotoImage(file="images/pppp.jpg")
        btn_register = Button(frame1, image=self.btn_staff, bd=0, cursor="hand2", command=self.register_window).place(x=350,
                                                                                                                  y=150)

        # login button
        self.btn_staffs = ImageTk.PhotoImage(file="images/llllll.jpg")
        btn_login = Button(frame1, image=self.btn_staffs, bd=0, cursor="hand2", command=self.login_window).place(x=600,
                                                                                                                  y=150)

        self.btn_student = ImageTk.PhotoImage(file="images/pppp.jpg")
        btn_register = Button(frame1, image=self.btn_student, bd=0, cursor="hand2", command=self.register_windows).place(
            x=350,
            y=400)

        # login button
        self.btn_students = ImageTk.PhotoImage(file="images/llllll.jpg")
        btn_login = Button(frame1, image=self.btn_students, bd=0, cursor="hand2", command=self.login_windows).place(x=600,
                                                                                                               y=400)
    def login_window(self):
        self.root.destroy()
        import staff_login

    def register_window(self):
        self.root.destroy()
        import staff_registration

    def login_windows(self):
        self.root.destroy()
        import staff_login

    def register_windows(self):
        self.root.destroy()
        import student_registration


win = Tk()
obj = Mainpage(win)
win.mainloop()