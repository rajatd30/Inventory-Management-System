from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Supplier Information")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ============================= All Variables ==========================
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_desc=StringVar()        
        
                
        #============================ Search Frame =================================
        
        lbl_search=Label(self.root,text="Invoice No.", font=("goudy old style",15))
        lbl_search.place(x=700, y=80)
        
        txt_search=Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style",15), bg="lightyellow").place(x=800,y=80, width=160)
        btn_search=Button(self.root,text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=980,y=79,width=100,height=28)
        
        # ================================= Title =============================================================
       
        title=Label(self.root,text="Supplier Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white" )
        title.place(x=50,y=10, width=1000)
        
        # ================================== Content ==========================================================
        
        # ======== Row1 ====================
        lbl_supplier_invoice=Label(self.root,text="Invoice No.", font=("goudy old style", 15), bg="white")
        lbl_supplier_invoice.place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow")
        txt_supplier_invoice.place(x=180,y=80, width=180)
        
        
        
        
        # ================ Row 2 ==============
        lbl_name=Label(self.root,text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=180,y=120, width=180)
        
        
        
        # ================ Row 3 ==============
        lbl_contact=Label(self.root,text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=180,y=160, width=180)
        
        
        
        # ================ Row 4 ==============
        lbl_desc=Label(self.root,text="Description", font=("goudy old style", 15), bg="white")
        lbl_desc.place(x=50,y=200)
        
        
        text_desc=Entry(self.root,textvariable=self.var_desc, font=("goudy old style", 15), bg="lightyellow")
        text_desc.place(x=180,y=200, width=470, height=90)
        
       
        
        # ================================= Button ================================================
        
        btn_add=Button(self.root,text="Add",command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=180,y=370,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=300,y=370,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=420,y=370,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=540,y=370,width=110,height=28)

        # ================================ Employee Details =======================================
        
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)
        
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        
        self.supplier_table=ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)

        self.supplier_table.heading("invoice", text="Invoice")
        self.supplier_table.heading("name", text="Name")
        self.supplier_table.heading("contact", text="Contact")
        self.supplier_table.heading("desc", text="Description")

        
        self.supplier_table["show"]="headings"
        
        self.supplier_table.column("invoice", width=100)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("contact", width=100)
        self.supplier_table.column("desc", width=100)

        
        self.supplier_table.pack(fill=BOTH,expand=1)
        self.supplier_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()


# =============================== Database Connect =========================================

    def add(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice is required")
            else:
                cur.execute(f"select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. is already exist try a different one")
                else:
                    cur.execute(f"insert into supplier values(%s,%s,%s,%s)",(
                       
                                self.var_sup_invoice.get(),
                                self.var_name.get(),                            
                                self.var_contact.get(),                                
                                self.var_desc.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=supplierClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
                    
    def show(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert('', END, values=row)
        
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}") 
            
            
    def get_data(self,ev):
        f=self.supplier_table.focus()
        content=(self.supplier_table.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_desc.set(row[3])
        
        
                
    def update(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Number must be required")
            else:
                cur.execute(f"select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice Number")
                else:
                    cur.execute(f"update supplier set  name=%s, contact=%s, description=%s where invoice=%s",(
                       
                                
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.var_desc.get(),
                                self.var_sup_invoice.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=supplierClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
            
    def delete(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Please Enter Invoice Number")
            else:
                cur.execute(f"select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice Number")
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete this employee?")
                    if op==True:
                        cur.execute(f"delete from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully")
                        self.show()
                        self.new_win=Toplevel(self.root)
                        self.new_obj=supplierClass(self.new_win)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")        


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("") 
        self.var_desc.set("")
        self.var_searchtxt.set("")
        self.show()
        
        
    def search(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input must be required")     
            else:           
                cur.execute(f"select * from supplier where invoice=%s ",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    self.supplier_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found!!!")
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

        

if __name__=="__main__":  
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()