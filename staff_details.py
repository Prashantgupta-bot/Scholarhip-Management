from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Mainpage:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Basic details for staff ")
        self.root.geometry("1350x800")

        # home button

        self.btn_imgss = ImageTk.PhotoImage(file="images/home.jpg")
        btn_login = Button(root, image=self.btn_imgss, bd=0, cursor="hand2", command=self.home_window).place(x=600,
                                                                                                               y=400)

        self.top = ImageTk.PhotoImage(file="images/log.gif")
        left = Label(self.root, image=self.top, bg="gray").place(x=0, y=500, width=1350, height=160)
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="informations"
            )
            cur = db.cursor()

            cur.execute("SELECT *  FROM pet limit 0,100")
            i = 0
            for pet in cur:
                for j in range(len(pet)):
                    e = Entry(root, width=10)
                    e.grid(row=i, column=j, sticky="w")
                    e.insert(END, pet[j])
                i = i + 1
                print()
            s = cur.execute("SELECT COUNT(mobile_no) FROM pet")

            messagebox.showinfo("Success", "Scholarship Awarded to all student and details of student are mentioned above", parent=self.root)






        except Exception as es:
            messagebox.showerror("Error", f"Error due to;-  {str(es)}", parent=self.root)

    def home_window(self):
        self.root.destroy()
        import Mainpage


win = Tk()
obj=Mainpage(win)
win.mainloop()