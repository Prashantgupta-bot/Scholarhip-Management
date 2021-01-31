from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Mainpage:
    def __init__(self,root):
        self.root=root
        self.root.title("Application Form for Student ")
        self.root.geometry("1350x800")

        #  Top Image

        self.top = ImageTk.PhotoImage(file="images/log.gif")
        left = Label(self.root, image=self.top, bg="white").place(x=0, y=0, width=1350, height=160)

        frame1 = Frame(self.root, bg="gray")
        frame1.place(x=0, y=160, width=1400, height=1000)

        frame2 = Frame(frame1, bg="red")
        frame2.place(x=0, y=0, width=1400, height=40)

        title = Label(frame2,text="Student Entry Details",font=("times in roman", 20, "bold"),
                      bg="red" ,fg="black").place(x=500,)
        # -----------first row
        f_name = Label(frame1, text="Full Name", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=50, y=50)
        self.txt_f_name = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_f_name.place(x=200, y=50, width=200)

        Age = Label(frame1, text="Age in Years", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=450, y=50)
        self.txt_Age = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_Age.place(x=600, y=50, width=200)

        #-----------2nd row

        father_name = Label(frame1, text="Father's Name", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=50, y=80)
        self.txt_father_name = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_father_name.place(x=200, y=80, width=200)

        mother_name = Label(frame1, text="Mother's Name", font=("times in roman", 15, "bold"), bg="gray",
                    fg="black").place(x=450, y=80)
        self.txt_mother = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_mother.place(x=600, y=80, width=200)

        frame3 = Frame(frame1, bg="red")
        frame3.place(x=0, y=115, width=1400, height=30)

        mobile = Label(frame1, text="Mobile Number", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=850, y=50)
        self.txt_mobile = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_mobile.place(x=1020, y=50, width=200)

        email = Label(frame1, text="Email", font=("times in roman", 15, "bold"), bg="gray",
                      fg="black").place(x=850, y=80)
        self.txt_email = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_email.place(x=1020, y=80, width=200)

        title = Label(frame3,text="Course Details - Presently Studying",font=("times in roman", 15, "bold"),
                      bg="red" ,fg="black").place(x=500,height=25)
         #--------------3rd row

        address= Label(frame1, text="Address", font=("times in roman", 15, "bold"), bg="gray",
                            fg="black").place(x=50, y=150)
        self.txt_address = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_address.place(x=200, y=155, width=200)

        pin = Label(frame1, text="Pin Code", font=("times in roman", 15, "bold"), bg="gray",
                            fg="black").place(x=450, y=155)
        self.txt_pin= Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_pin.place(x=600, y=155, width=200)

        #----------------4rt row

        country = Label(frame1, text="Country", font=("times in roman", 15, "bold"), bg="gray",
                         fg="black").place(x=50, y=190)
        self.cmb_Country = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_Country["values"] = ("Select", "India", "London", "USA", "UK", "UAE", "Other")
        self.cmb_Country.place(x=200, y=190, width=200)
        self.cmb_Country.current(0)

        Aadhar = Label(frame1, text="Aadhar Number", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=450, y=190)
        self.txt_Aadhar = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_Aadhar.place(x=600, y=190, width=200)

        Domicile = Label(frame1, text="Domicile/UT", font=("times in roman", 15, "bold"), bg="gray",
                         fg="black").place(x=50, y=225)
        self.cmb_Domicile = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_Domicile["values"] = ("Select", "Madhya Pradesh", "Uttar Pradesh", "Assam", "Bihar", "Gujarat", "Other")
        self.cmb_Domicile.place(x=200, y=225, width=200)
        self.cmb_Domicile.current(0)

        tution_fee = Label(frame1, text="Tution Fee", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=450, y=225)
        self.txt_tution_fee = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_tution_fee.place(x=600, y=225, width=200)

        frame4 = Frame(frame1, bg="red")
        frame4.place(x=0, y=260, width=1400, height=30)

        title = Label(frame4, text="Qualification Examination Passes",
                      font=("times in roman", 15, "bold"),
                      bg="red", fg="black").place(x=500, height=25)


        exam_passed = Label(frame1, text="Exam Passed", font=("times in roman", 15, "bold"), bg="gray",
                         fg="black").place(x=50, y=300)
        self.cmb_exam_passed = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_exam_passed["values"] = (
        "Select", "SSLC/X", "HSC/+2/Vocational", "Diploma", "UG Degree", "PG Degree", "Other")
        self.cmb_exam_passed.place(x=200, y=300, width=200)
        self.cmb_exam_passed.current(0)

        yop = Label(frame1, text="Passing Year", font=("times in roman", 15, "bold"), bg="gray",
                       fg="black").place(x=450, y=300)
        self.txt_yop = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_yop.place(x=600, y=300, width=200)




        frame5 = Frame(frame1, bg="red")
        frame5.place(x=0, y=340, width=1400, height=30)

        title = Label(frame5, text="Bank Details",
                      font=("times in roman", 15, "bold"),
                      bg="red", fg="black").place(x=600, height=25)

        institute_name = Label(frame1, text="Institute Name", font=("times in roman", 15, "bold"), bg="gray",
                               fg="black").place(x=850, y=155)
        self.cmb_institute_name = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_institute_name["values"] = (
            "Select", "TIT Main", "TIT SCIENCE", "TIT ADVANCE", "TIT EXCELLENCE", "Other")
        self.cmb_institute_name.place(x=1020, y=155, width=200)
        self.cmb_institute_name.current(0)

        course_name = Label(frame1, text="Course Name", font=("times in roman", 15, "bold"), bg="gray",
                               fg="black").place(x=850, y=190)
        self.cmb_course_name = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_course_name["values"] = (
            "Select", "B.Tech", "M.Tech", "MBA", "MSc", "Other")
        self.cmb_course_name.place(x=1020, y=190, width=200)
        self.cmb_course_name.current(0)

        roll = Label(frame1, text="Roll No", font=("times in roman", 15, "bold"), bg="gray",
                           fg="black").place(x=850, y=225)
        self.txt_roll = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_roll.place(x=1020, y=225, width=200)

        Acc_No = Label(frame1, text="Account No", font=("times in roman", 15, "bold"), bg="gray",
                     fg="black").place(x=50, y=370)
        self.txt_Acc_No = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_Acc_No.place(x=200, y=375, width=200)

        bank_name= Label(frame1, text="Bank Name", font=("times in roman", 15, "bold"), bg="gray",
                            fg="black").place(x=450, y=370)
        self.cmb_bank_name = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.cmb_bank_name["values"] = (
            "Select", "SBI", "UBI", "Axis Bank", "Paytm Payment Bank","Airtel Payment Bank", "Other")
        self.cmb_bank_name.place(x=600, y=375, width=200)
        self.cmb_bank_name.current(0)

        ifsc = Label(frame1, text="IFSC Code", font=("times in roman", 15, "bold"), bg="gray",
                      fg="black").place(x=850, y=370)
        self.txt_ifsc = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_ifsc.place(x=1020, y=370, width=200)


        marks  = Label(frame1, text="Marks in %", font=("times in roman", 15, "bold"), bg="gray",
                      fg="black").place(x=850, y=300)
        self.txt_marks = Entry(frame1, font=("times in roman", 15), bg="lightgray")
        self.txt_marks.place(x=1020, y=300, width=200)

        cast = Label(frame1, text="Category", font=("times in roman", 15, "bold"), bg="gray",
                         fg="black").place(x=50, y=410)
        self.txt_cast = ttk.Combobox(frame1, font=("times in roman", 13), state="readonly", justify=CENTER)
        self.txt_cast["values"] = ("Select", "ST", "SC", "OBC", "GEN", "Other")
        self.txt_cast.place(x=200, y=410, width=200)
        self.txt_cast.current(0)


        dob = Label(frame1, text="DOB(d/m/y)", font=("times in roman", 15, "bold"), bg="gray",
                      fg="black").place(x=450, y=410)
        self.txt_dob = Entry(frame1, font=("times in roman", 13), bg="lightgray")
        self.txt_dob.place(x=600, y=410, width=200)

        # save & next button
        self.btn_imgs = ImageTk.PhotoImage(file="images/save.png")
        btn_register = Button(frame1, image=self.btn_imgs, bd=0, cursor="hand2", command=self.register_data).place(x=1220,  y=420)

        self.btn_imgss = ImageTk.PhotoImage(file="images/home de.jpg")
        btn_register = Button(self.root, image=self.btn_imgss, bd=0, cursor="hand2", command=self.home_window).place(
            x=1220, y=50)



    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_Age.get() == "" or self.txt_marks.get() == "Select" or self.txt_ifsc.get() == "" or self.cmb_bank_name.get() == "" or self.txt_Acc_No.get()=="" or self.txt_roll.get()=="" or self.txt_dob.get()=="" or self.txt_cast.get()=="" or self.cmb_course_name.get()=="" or self.cmb_institute_name.get()=="" or self.txt_yop.get()=="" or self.cmb_exam_passed.get()=="" or self.txt_tution_fee.get()=="" or self.cmb_Domicile.get()=="" or self.txt_pin.get()=="" or self.txt_address.get()=="" or self.txt_Aadhar.get()=="" or self.cmb_Country.get()=="" or self.txt_email.get()=="" or self.txt_mobile.get()=="" or self.txt_father_name.get()=="" or self.txt_mother.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.txt_Age.get() < "18" and self.txt_Age.get() > "25" or  self.txt_cast.get()=="GEN":
            messagebox.showerror("Error", "You are not eligible for the scholarship due to age or cast", parent=self.root)

        else:
            try:
                db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345",
                        database="informations"
                )
                cur = db.cursor()

                s = "INSERT INTO pet  (name,age,mobile_no,father_name,mother_name,email,address,pin,institute,country,aadhar,course,domicile,tution_fee,roll_no,exam_passed,passing_year,marks_in_percentage,account_no,bank_name,ifsc_code,cast,dob)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";

                b1 = ( self.txt_f_name.get() ,
                       self.txt_Age.get() ,
                       self.txt_mobile.get(),
                       self.txt_father_name.get(),
                       self.txt_mother.get(),

                       self.txt_email.get(),
                       self.txt_address.get(),
                       self.txt_pin.get(),
                       self.cmb_institute_name.get(),
                       self.cmb_Country.get(),
                       self.txt_Aadhar.get(),
                       self.cmb_course_name.get(),
                       self.cmb_Domicile.get(),
                       self.txt_tution_fee.get(),
                       self.txt_roll.get(),
                       self.cmb_exam_passed.get(),
                       self.txt_yop.get(),
                       self.txt_marks.get(),
                       self.txt_Acc_No.get(),
                       self.cmb_bank_name.get(),
                       self.txt_ifsc.get() ,
                       self.txt_cast.get(),
                       self.txt_dob.get(),
                       );


                cur.execute(s, b1)
                db.commit();
                db.close();
                messagebox.showwarning("Conformation","once data will be saved you can not modify it, Do you want to proceed , if yes then click ok to move next", parent=self.root)
                messagebox.showinfo("Congratulations ",  f"{self.txt_f_name.get()} Application Has been received , your amount of  {self.txt_tution_fee.get()} rupees will be reflected  to your account provided by you ", parent=self.root)





            except Exception as es:
              messagebox.showerror("Error", f"Error due to;-  {str(es)}", parent=self.root)
    def home_window(self):
        self.root.destroy()
        import Mainpage

win = Tk()
obj=Mainpage(win)
win.mainloop()