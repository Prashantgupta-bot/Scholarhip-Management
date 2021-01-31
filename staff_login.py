from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Login:

    def __init__(self,root):
        self.root = root
        self.root.title("Staff Login Window")
        self.root.geometry("1350x700+0+0")

        # LEFT Image
        self.left = ImageTk.PhotoImage(file="images/logi.jpg")
        bg = Label(self.root, image=self.left).place(x=0, y=160, width=600, height=600)

        #  Top Image
        self.top = ImageTk.PhotoImage(file="images/log.gif")
        left = Label(self.root, image=self.top, bg="gray").place(x=0, y=0, width=1350, height=160)

        # Login Frame
        frame1 = Frame(self.root, bg="red")
        frame1.place(x=500, y=160, width=1000, height=800)

        title = Label(frame1, text="STAFF LOGIN ", font=("times in roman", 20, "bold"), bg="red", fg="black").place(
            x=50, y=30,width=800)

        username = Label(frame1, text="Username", font=("times in roman", 15, "bold"), bg="red", fg="black").place(x=100,
                                                                                                              y=100)
        self.txt_username = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_username.place(x=290, y=100, width=500)

        password = Label(frame1, text="Password", font=("times in roman", 15, "bold"), bg="red", fg="black").place(
            x=100, y=150)
        self.txt_password = Entry(frame1, font=("times in roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=290, y=150, width=500)

        self.btn = Button(frame1, text="Login",command=self.login_data,cursor="hand2", font=("title in roman", 20,"bold"), bg="red", fg="black").place(x=290,y=350,width=200)


        self.btn_newregistration = Button(frame1,cursor="hand2",command=self.register_window ,text="New Registration ?", font=("title in roman", 20, "bold"), bg="red", fg="black").place(x=510,
                                                                                                            y=350,
                                                                                                            width=280)


        question = Label(frame1, text="Security Question", font=("times in roman", 15, "bold"), bg="red",
                         fg="black").place(x=100, y=200)
        self.cmb_quests = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_quests["values"] = ("Select", "Your First Pet Name ?", "Your Birth Place ?", "Your Best Friend Name ?")
        self.cmb_quests.place(x=290, y=200, width=500)
        self.cmb_quests.current(0)

        answers = Label(frame1, text="Answer", font=("times in roman", 15, "bold"), bg="red", fg="black").place(x=100,
                                                                                                                y=250)
        self.txt_answers = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_answers.place(x=290, y=250, width=500)

        # home button

        self.btn_imgss = ImageTk.PhotoImage(file="images/home.jpg")
        btn_login = Button(root, image=self.btn_imgss, bd=0, cursor="hand2", command=self.home_window).place(x=1220,y=50)

    def register_window(self):
        self.root.destroy()
        import staff_registration

    def home_window(self):
        self.root.destroy()
        import Mainpage


    def login_data(self):
            if self.txt_username.get()=="" or self.txt_password.get()=="" or self.cmb_quests.get()=="" or self.txt_answers.get()=="":
                messagebox.showerror("Error Occured", "All fields are required",parent=self.root)
            else:
                try:
                    db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345",
                        database="informations"
                    )
                    cur = db.cursor()


                    s = "SELECT * FROM details  WHERE Email=%s AND Passwords=%s "
                    b1 = (self.txt_username.get(), self.txt_password.get())
                    cur.execute(s, b1)
                    row = cur.fetchone()

                    if row ==None:
                        messagebox.showerror("Error Occured", "Invalid Username or Password", parent=self.root)

                    else:
                        messagebox.showinfo("Congratulations", "Login Successful, click ok to see details And Application of Applied student", parent=self.root)
                        self.root.destroy()
                        import staff_details
                    cur.close()



                except Exception as es:

                    messagebox.showerror("Error", f"Error due to;-  {str(es)}", parent=self.root)



win = Tk()
obj=Login(win)
win.mainloop()
