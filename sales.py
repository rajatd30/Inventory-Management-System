from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Invoices")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ============================== Variables ================================
        
        self.var_invoice=StringVar()
        self.bill_list=[]
        
        # =================================== Title ===================================
        
        lbl_title=Label(self.root, text="View Invoices", font=("goudy old style",30), bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack( side=TOP, fill=X, padx=10, pady=20)

        lbl_invoice=Label(self.root,text="Invoice No.", font=("times new roman", 15), bg="white")
        lbl_invoice.place(x=50,y=100)
        
        txt_invoice=Entry(self.root, textvariable=self.var_invoice,font=("times new roman", 15), bg="lightyellow")
        txt_invoice.place(x=160,y=100, width=180, height=28)
        
        btn_search=Button(self.root, text="Search",command=self.search,font=("times new roman", 15,"bold"),cursor="hand2", bg="#2196f3", fg="white")
        btn_search.place(x=360,y=100, width=120, height=28)
        btn_clear=Button(self.root, text="Clear", command=self.clear,font=("times new roman", 15,"bold"),cursor="hand2", bg="lightgrey")
        btn_clear.place(x=490,y=100, width=120, height=28)
        
        # ============================ Sales Frame ===================================
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,height=330,width=200)
        
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        # ========================= Show Frame ===================================

        show_frame=Frame(self.root,bd=3,relief=RIDGE)
        show_frame.place(x=280,y=140,height=330,width=410)
        
        lbl_title=Label(show_frame, text="Customer Bill Area", font=("goudy old style",20), bg="orange", fg="white")
        lbl_title.pack( side=TOP, fill=X)
        
        scrolly2=Scrollbar(show_frame,orient=VERTICAL)
        self.bill_area=Text(show_frame,font=("goudy old style",15),bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)
        
        # ======================== Image ====================================
        
        self.bill_photo=Image.open("images/2.png") 
        self.bill_photo=self.bill_photo.resize((450,300), Image.LANCZOS)   
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        self.lbl_bill_photo=Label(self.root, image=self.bill_photo, bd=0, relief=RIDGE)  
        self.lbl_bill_photo.place(x=700, y=110)
        
        self.show()
        
        
        # ======================= Other Functions ====================================

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=="txt":
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
        
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required")
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice Number")
                
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
        self.var_invoice.set("")

                
                
if __name__=="__main__":  
    root=Tk()
    obj=salesClass(root)
    root.mainloop()