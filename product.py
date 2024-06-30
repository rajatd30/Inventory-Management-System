from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Products Details")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # =============================== Variables ==========================

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()        
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.var_pid=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.fetch_cat_sup()
        
        # =============================== Frame ===============================
       
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10, height=450, width=480)
        
        # ================================= Label ===============================
        
        title=Label(product_frame,text="Manage Products", font=("goudy old style", 18), bg="#0f4d7d", fg="white")
        title.pack(side=TOP,fill=X)
        
        lbl_category=Label(product_frame,text="Category", font=("goudy old style", 18), bg="white")
        lbl_category.place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier", font=("goudy old style", 18), bg="white")
        lbl_supplier.place(x=30,y=110)
        lbl_product=Label(product_frame,text="Product Name", font=("goudy old style", 18), bg="white")
        lbl_product.place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price", font=("goudy old style", 18), bg="white")
        lbl_price.place(x=30,y=210)
        lbl_quantity=Label(product_frame,text="Quantity", font=("goudy old style", 18), bg="white")
        lbl_quantity.place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status", font=("goudy old style", 18), bg="white")
        lbl_status.place(x=30,y=310)
        
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list, state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_cat.place(x=200,y=60, width=200)
        cmb_cat.current(0)
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list, state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_sup.place(x=200,y=110, width=200)
        cmb_sup.current(0)
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",15), bg="lightyellow")
        txt_name.place(x=200,y=160, width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15), bg="lightyellow")
        txt_price.place(x=200,y=210, width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("goudy old style",15), bg="lightyellow")
        txt_qty.place(x=200,y=260, width=200)
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_status.place(x=200,y=310, width=200)
        cmb_status.current(0)
        
        # ================================= Button ================================================
        
        btn_add=Button(product_frame,text="Add",command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=340,y=400,width=100,height=40)
        
        # =========================== Search Frame =============================
        
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("times new roman",12,"bold"), bd=2, relief=RIDGE)        
        SearchFrame.place(x=500, y=10, width=580, height=80)
        
        #============================ Combobox =================================
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"), state="readonly", justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15), bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=410,y=10,width=150,height=30)
        
         # ================================ Product Details =======================================
        
        p_frame=Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=500,y=100,width=580,height=360)
        
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        
        self.product_table=ttk.Treeview(p_frame, columns=("pid", "Category","Supplier", "name", "price", "qty", "status"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Product ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")
        
        
        self.product_table["show"]="headings"
        
        self.product_table.column("pid", width=100)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

    # =============================== Database Connect / Functions =========================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
            
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
        
        
        
    def add(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_name.get()=="" or self.var_sup.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            else:
                cur.execute(f"select * from product where name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already exist try a different one")
                else:
                    cur.execute(f"insert into product(Category,Supplier,name,price,qty,status) values(%s,%s,%s,%s,%s,%s)",(
                       
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                self.var_status.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=productClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
                    
    def show(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}") 
            
            
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        print(row)
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])

        
                
    def update(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product")
            else:
                cur.execute(f"select * from product where pid=%s",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product")
                else:
                    cur.execute(f"update product set  Category=%s, Supplier=%s, name=%s, price=%s, qty=%s, status=%s where pid=%s",(
                       
                                
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                self.var_status.get(),
                                self.var_pid.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=productClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
            
    def delete(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Enter Product ID")
            else:
                cur.execute(f"select * from product where pid=%s",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product")
                else:
                    self.new_win=Toplevel(self.root)
                    self.new_obj=productClass(self.new_win)
                    op=messagebox.askyesno("Confirm","Do you really want to delete this product?")
                    if op==True:
                        cur.execute(f"delete from product where pid=%s",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully")
                        self.show()
                        self.new_win=Toplevel(self.root)
                        self.new_obj=productClass(self.new_win)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")        
                        


    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active")
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
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found!!!")
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}")


if __name__=="__main__":  
    root=Tk()
    obj=productClass(root)
    root.mainloop()