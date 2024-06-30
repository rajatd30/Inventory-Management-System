from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import mysql.connector

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Product Categories")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ================================= Variables ===============================
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        # ================================= Title ===================================
        
        lbl_title=Label(self.root, text="Manage Product Category", font=("goudy old style",30), bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack( side=TOP, fill=X, padx=10, pady=20)
        
        # =================================== Label ===================================
        
        lbl_title=Label(self.root, text="Category Name", font=("goudy old style",30), bg="white")
        lbl_title.place(x=50, y=100)
        lbl_title=Entry(self.root, textvariable=self.var_name, font=("goudy old style",18), bg="lightyellow")
        lbl_title.place(x=50, y=170, width=300)
        
        # =================================== Buttons ===================================
        
        btn_add=Button(self.root, text="ADD",command=self.add, font=("goudy old style",15), bg="#4caf50", fg="white", cursor="hand2")
        btn_add.place(x=360, y=170, width=150, height=30)
        btn_delete=Button(self.root, text="DELETE",command=self.delete, font=("goudy old style",15), bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=520, y=170, width=150, height=30)
        
        # ====================================== Category Details ==========================
        cat_frame=Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)
        
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        
        self.category_table=ttk.Treeview(cat_frame, columns=("cid", "name"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid", text="Category ID")
        self.category_table.heading("name", text="Name")
        
        self.category_table["show"]="headings"

        self.category_table.column("cid", width=100)
        self.category_table.column("name", width=100)
        
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        
        # ==================================== Images =================================
        
        self.img1=Image.open("images/1.png") 
        self.img1=self.img1.resize((500,250), Image.LANCZOS)   
        self.img1=ImageTk.PhotoImage(self.img1)
        self.lbl_img1=Label(self.root, image=self.img1, bd=2, relief=RIDGE)  
        self.lbl_img1.place(x=50, y=220)
        
        self.img2=Image.open("images/3.png") 
        self.img2=self.img2.resize((500,250), Image.LANCZOS)   
        self.img2=ImageTk.PhotoImage(self.img2)
        self.lbl_img2=Label(self.root, image=self.img2, bd=2, relief=RIDGE)  
        self.lbl_img2.place(x=580, y=220)
        self.show()
        
    # =============================== Functions =================================
    
    def add(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name should be required")
            else:
                cur.execute(f"select * from category where name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already exist try a different one")
                else:
                    cur.execute(f"insert into category(name) values(%s)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully")
                    self.show()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=categoryClass(self.new_win)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")  
            
            
    def show(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('', END, values=row)
        
        except Exception as ex:        
            messagebox.showerror("Error",f"Error due to: {str(ex)}")  
            
            
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
        
    def delete(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select Category")
            else:
                cur.execute(f"select * from category where cid=%s",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error! Please Try Again")
                else:
                    self.new_win=Toplevel(self.root)
                    self.new_obj=categoryClass(self.new_win)
                    op=messagebox.askyesno("Confirm","Do you really want to delete this employee?")
                    if op==True:
                        cur.execute(f"delete from category where cid=%s",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully")
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
                        self.new_win=Toplevel(self.root)
                        self.new_obj=categoryClass(self.new_win)
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

        
        
if __name__=="__main__":  
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()