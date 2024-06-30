from tkinter import *
from tkinter import messagebox
import mysql.connector
import time
import os
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+80+40")
        self.root.title("XYZ Shop | Developed By Abc")
        self.root.config(bg="white")
        
        
        # ============================== Title ============================================
        
        self.icon_title=PhotoImage(file="images/4.png")
        self.title=Label(self.root,text="XYZ Shop", image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"), bg="blue", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1,height=70)
    
        # ================================= Button Logout =================================
        
        self.btn_logout=Button(self.root,text="Log Out",command=self.logout, font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1350,y=10,height=50,width=150)
        
        # =================================== Clock ========================================
        
        self.lbl_clock=Label(self.root,text="Welcome User !!! \t\t\t  Date:DD-MM-YYYY \t\t\t  Time:HH:MM:SS",font=("times new roman",15), bg="green", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        # ================================ Left Menu ========================================
        
        LeftMenu=Label(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200, height=650)
        
        self.lbl_menu=Label(LeftMenu,text="MENU", font=("times new roman",20),bg="black", fg="white").pack(side=TOP, fill=X)
        
        self.btn_employee=Button(LeftMenu,text="Employees",command=self.employee, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        self.btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        self.btn_Product=Button(LeftMenu,text="Product",command=self.product, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        self.btn_category=Button(LeftMenu,text="Category",command=self.category, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        self.btn_sales=Button(LeftMenu,text="Invoices",command=self.sales, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        self.btn_employee=Button(LeftMenu,text="Exit",command=root.destroy, font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        
        #======================================== Contents ========================================================
        
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]", bd=5, relief=RIDGE,font=("calibri",20,"bold"), bg="#33bbf9", fg="white")
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]", bd=5, relief=RIDGE,font=("calibri",20,"bold"), bg="#ff5722", fg="white")
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        self.lbl_category=Label(self.root,text="Total Category\n[0]", bd=5, relief=RIDGE,font=("calibri",20,"bold"), bg="#009688", fg="white")
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        self.lbl_product=Label(self.root,text="Total Product\n[0]", bd=5, relief=RIDGE,font=("calibri",20,"bold"), bg="#607d8b", fg="white")
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        self.lbl_sales=Label(self.root,text="Total Sales\n[0]", bd=5, relief=RIDGE,font=("calibri",20,"bold"), bg="gold", fg="white")
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        
        #===================================== Footer =============================================================
        
        lbl_footer=Label(self.root, text="Shop Inventory Management System | Developed By Abc\nFor any issues Contact: 987XXXX210",font=("times new roman",15), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)
        
        self.update_content()
        
        
        #==========================================================================================================
        
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
        # ==================================== Content Numbers ==============================================================

    def update_content(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            cur.execute("select * from employee")
            empl=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(empl))} ]")
            
            cur.execute("select * from supplier")
            supp=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(supp))} ]")
            
            cur.execute("select * from category")
            cate=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(cate))} ]")
            
            cur.execute("select * from product")
            prod=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[{str(len(prod))}]")
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n[{str(bill)}]")
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Welcome !!! \t\t\t  Date: {str(date_)} \t\t\t  Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
         
        
if __name__=="__main__":  
    root=Tk()
    obj=IMS(root)
    root.mainloop()