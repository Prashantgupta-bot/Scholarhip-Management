from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Registration Window")
        self.root.geometry("1350x700+0+0")

        # BG Image
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # LEFT Image
        self.left = ImageTk.PhotoImage(file="images/side.png.png")
        left = Label(self.root, image=self.left,bg="blue").place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="STAFF REGISTRATION", font=("times in roman", 20, "bold"),
                      bg="white", fg="green").place(x=50, y=30)

        f_name = Label(frame1, text="Full Name", font=("times in roman", 15, "bold"), bg="white",
                       fg="gray").place(x=50, y=100)
        self.txt_f_name = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_f_name.place(x=50, y=130, width=250)

        gender = Label(frame1, text="Select Your Gender", font=("times in roman", 15, "bold"), bg="white",
                       fg="gray").place(x=370, y=100)
        self.cmb_questss= ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_questss["values"] = ("Select", "Male", "Female", "Trans Gender", "Other")
        self.cmb_questss.place(x=370, y=130, width=250)
        self.cmb_questss.current(0)

        #---------------------------------Row 2

        contact = Label(frame1, text="Contact No.", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ---------------------------------Row 3

        question = Label(frame1, text="Choose Your Category", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times in roman", 13),state="readonly", justify=CENTER)
        self.cmb_quest["values"]=("Select","ST","SC","OBC","GEN","Other")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)


        answer = Label(frame1, text="Age", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        #------------------row 4

        password = Label(frame1, text="Password", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times in roman", 15), bg="lightgray",show="*")
        self.txt_password.place(x=50, y=340, width=250)


        c_password = Label(frame1, text="Conform Password", font=("times in roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=310)
        self.txt_c_password = Entry(frame1, font=("times in roman", 15), bg="lightgray",show="*")
        self.txt_c_password.place(x=370, y=340, width=250)

        #------------row 5 checkbox terms
        self.var_chk = IntVar()
        check = Checkbutton(frame1, text='I Agree The Terms and Conditions',variable=self.var_chk, onvalue=1, offvalue=0,bg="white",font=('times in roman',12)).place(x=50,y=380)

        #register button
        self.btn_img = ImageTk.PhotoImage(file="images/register.png")
        btn_register = Button(frame1,image=self.btn_img, bd=0, cursor="hand2",command=self.register_data).place(x=50, y=420)

        # login button
        self.btn_imgs = ImageTk.PhotoImage(file="images/llllll.jpg")
        btn_login = Button(self.root, image=self.btn_imgs, bd=0, cursor="hand2",command=self.login_window).place(x=210, y=550)

        #home button

        self.btn_imgss = ImageTk.PhotoImage(file="images/home.jpg")
        btn_login = Button(frame1, image=self.btn_imgss, bd=0, cursor="hand2", command=self.home_window).place(x=600,
                                                                                                                  y=400)
    def login_window(self):
        self.root.destroy()
        import staff_login

    def home_window(self):
        self.root.destroy()
        import Mainpage

    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_contact.get() == "":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_c_password.get():
            messagebox.showerror("Error", "Password and Conform Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Agree with our terms and conditions", parent=self.root)
        else:
            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="informations"
                )
                cur = db.cursor()

                s = "INSERT INTO details(Full_Name,Gender,Contact_no,Email,Cast,Age,Passwords) VALUES (%s, %s, %s, %s,%s,%s,%s)"

                b1 = (self.txt_f_name.get(),
                          self.cmb_questss.get(),
                          self.txt_contact.get(),
                          self.txt_email.get(),
                          self.cmb_quest.get(),
                          self.txt_answer.get(),
                          self.txt_password.get());

                cur.execute(s, b1)
                db.commit();
                db.close();
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)





            except Exception as es:
                messagebox.showerror("Error", f"Error due to;-  {str(es)}", parent=self.root)


win = Tk()
obj = Register(win)
win.mainloop()