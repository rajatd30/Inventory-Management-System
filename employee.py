from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Employee Information")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ============================= All Variables ==========================
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
        
        # ================================= Title =============================================================
       
        title=Label(self.root,text="Employee Details", font=("goudy old style", 17), bg="#0f4d7d", fg="white" )
        title.place(x=50,y=20, width=1000)
        
        # =========================== Search Frame =============================
        
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("times new roman",12,"bold"), bd=2, relief=RIDGE)        
        SearchFrame.place(x=250, y=60, width=600, height=70)
        
        #============================ Combobox =================================
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select", "Email", "Name", "Contact"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15), bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=410,y=10,width=150,height=30)
        
        
        
        # ================================== Content ==========================================================
        
        # ======== Row1 ====================
        lbl_empid=Label(self.root,text="Emp ID", font=("goudy old style", 15), bg="white")
        lbl_empid.place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender", font=("goudy old style", 15), bg="white")
        lbl_gender.place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=750,y=150)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id, font=("goudy old style", 15), bg="lightyellow")
        txt_empid.place(x=150,y=150, width=180)
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=850,y=150, width=180)
        
        
        # ================ Row 2 ==============
        lbl_name=Label(self.root,text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B", font=("goudy old style", 15), bg="white")
        lbl_dob.place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J", font=("goudy old style", 15), bg="white")
        lbl_doj.place(x=750,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=150,y=190, width=180)
        
        txt_dob=Entry(self.root,textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow")
        txt_dob.place(x=500,y=190, width=180)
        
        txt_doj=Entry(self.root,textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow")
        txt_doj.place(x=850,y=190, width=180)
        
        # ================ Row 3 ==============
        lbl_email=Label(self.root,text="Email", font=("goudy old style", 15), bg="white")
        lbl_email.place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password", font=("goudy old style", 15), bg="white")
        lbl_pass.place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type", font=("goudy old style", 15), bg="white")
        lbl_utype.place(x=750,y=230)
        
        txt_email=Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow")
        txt_email.place(x=150,y=230, width=180)
        
        txt_pass=Entry(self.root,textvariable=self.var_pass, font=("goudy old style", 15), bg="lightyellow")
        txt_pass.place(x=500,y=230, width=180)
        
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select", "Admin", "Employee"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)
        
        # ================ Row 4 ==============
        lbl_address=Label(self.root,text="Address", font=("goudy old style", 15), bg="white")
        lbl_address.place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary", font=("goudy old style", 15), bg="white")
        lbl_salary.place(x=350,y=270)
        
        txt_address=Entry(self.root,textvariable=self.var_address, font=("goudy old style", 15), bg="lightyellow")
        txt_address.place(x=150,y=270, width=180, height=60)
        
        txt_salary=Entry(self.root,textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow")
        txt_salary.place(x=500,y=270, width=180)
        
        # ================================= Button ================================================
        
        btn_add=Button(self.root,text="Add",command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=860,y=305,width=110,height=28)

        # ================================ Employee Details =======================================
        
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)

        self.employee_table.heading("eid", text="Emp ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact", text="Contact")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("pass", text="Password")
        self.employee_table.heading("utype", text="User Type")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("salary", text="Salary")
        
        self.employee_table["show"]="headings"
        
        self.employee_table.column("eid", width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("pass", width=100)
        self.employee_table.column("utype", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("salary", width=100)

        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()


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
                    cur.execute(f"insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                       
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.var_address.get(),
                                self.var_salary.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=employeeClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
                    
    
    def show(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
        
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}") 
            
            
    def get_data(self,ev):
        f=self.employee_table.focus()
        content=(self.employee_table.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_address.set(row[9]),
        self.var_salary.set(row[10])
        
                
    def update(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Please Enter Employee ID")
            else:
                cur.execute(f"select * from employee where eid=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID")
                else:
                    cur.execute(f"update employee set  name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, pass=%s, utype=%s, address=%s, salary=%s where eid=%s",(
                       
                                
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.var_address.get(),
                                self.var_salary.get(),
                                self.var_emp_id.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=employeeClass(self.new_win)
                    
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
            
    def delete(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Please Enter Employee ID")
            else:
                cur.execute(f"select * from employee where eid=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID")
                else:
                    self.new_win=Toplevel(self.root)
                    self.new_obj=employeeClass(self.new_win)
                    op=messagebox.askyesno("Confirm","Do you really want to delete this employee?")
                    if op==True:
                        cur.execute(f"delete from employee where eid=%s",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully")
                        self.show()
                        self.new_win=Toplevel(self.root)
                        self.new_obj=employeeClass(self.new_win)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")        


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.var_address.set("")
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        
        self.show()
        
        
    def search(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search Type")
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input must be required")     
            else:           
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found!!!")
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

        

if __name__=="__main__":  
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()