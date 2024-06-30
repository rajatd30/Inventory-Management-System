from tkinter import *
from tkinter import ttk, messagebox
import os
import mysql.connector

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+80+40")
        self.root.title("Sign Up")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ============================= All Variables ==========================
        

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_address=StringVar()
        
        # ================================= Title =============================================================
       
        title=Label(self.root,text="Sign Up", font=("goudy old style", 25), bg="#0f4d7d", fg="white" )
        title.place(x=50,y=50, width=1250, height=50)
        
        
        # ================================== Content ==========================================================
        
        # ======== Row1 ====================
        lbl_empid=Label(self.root,text="Emp ID", font=("goudy old style", 15), bg="white")
        lbl_empid.place(x=50,y=140)
        lbl_gender=Label(self.root,text="Gender", font=("goudy old style", 15), bg="white")
        lbl_gender.place(x=500,y=140)
        lbl_contact=Label(self.root,text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=950,y=140)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id, font=("goudy old style", 15), bg="lightyellow")
        txt_empid.place(x=150,y=140, width=180)
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_gender.place(x=600, y=140, width=180)
        cmb_gender.current(0)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=1050,y=140, width=180)
        
        
        # ================ Row 2 ==============
        lbl_name=Label(self.root,text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=50,y=210)
        lbl_dob=Label(self.root,text="D.O.B", font=("goudy old style", 15), bg="white")
        lbl_dob.place(x=500,y=210)
        lbl_doj=Label(self.root,text="D.O.J", font=("goudy old style", 15), bg="white")
        lbl_doj.place(x=950,y=210)
        
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=150,y=210, width=180)
        
        txt_dob=Entry(self.root,textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow")
        txt_dob.place(x=600,y=210, width=180)
        
        txt_doj=Entry(self.root,textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow")
        txt_doj.place(x=1050,y=210, width=180)
        
        # ================ Row 3 ==============
        lbl_email=Label(self.root,text="Email", font=("goudy old style", 15), bg="white")
        lbl_email.place(x=50,y=280)
        lbl_pass=Label(self.root,text="Password", font=("goudy old style", 15), bg="white")
        lbl_pass.place(x=500,y=280)
        
        txt_email=Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow")
        txt_email.place(x=150,y=280, width=180)
        
        txt_pass=Entry(self.root,textvariable=self.var_pass, font=("goudy old style", 15), bg="lightyellow")
        txt_pass.place(x=600,y=280, width=180)
        
        # ================ Row 4 ==============
        lbl_address=Label(self.root,text="Address", font=("goudy old style", 15), bg="white")
        lbl_address.place(x=950,y=280)
        
        txt_address=Entry(self.root,textvariable=self.var_address, font=("goudy old style", 15), bg="lightyellow")
        txt_address.place(x=1050,y=280, width=180, height=60)
        
        
        # ================================= Button ================================================
        
        btn_add=Button(self.root,text="Sign Up",command=self.add, font=("goudy old style", 20), bg="#2196f3", fg="white", cursor="hand2").place(x=570,y=500,width=200,height=50)
        


    # =============================== Database Connect =========================================

    def add(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID is mandatory")
            else:
                cur.execute(f"select * from employee where eid=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already exist try a different one")
                else:
                    cur.execute(f"insert into employee(eid, name , email, gender, contact, dob, doj, pass, address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                       
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_address.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","SignUp Successful")
                  
                    self.root.destroy()
                    os.system("python login.py")
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
                    
    

            
if __name__=="__main__":  
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()