from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+80+40")
        self.root.config(bg="#99ccff")
        
         
        self.username=StringVar()
        self.password=StringVar()
        # =================================== Login Frame ===========================================

        login_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        login_frame.place(x=250, y=50, width=800, height=480)
        
        title=Label(login_frame,text="LOGIN",font=("elephant",30,"bold"),fg="blue", bg="#9999ff")
        title.place(x=0,y=30,relwidth=1)
        
        lbl_username=Label(login_frame,text="USERNAME", font=("goudy old style",20), bg="white")
        lbl_username.place(x=50,y=150)
        txt_username=Entry(login_frame,textvariable=self.username, font=("Comic sans ms",20),bg="lightyellow")
        txt_username.place(x=280,y=150,width=400)
        
        lbl_pswd=Label(login_frame,text="PASSWORD", font=("goudy old style",20), bg="white")
        lbl_pswd.place(x=50,y=220)
        txt_pswd=Entry(login_frame, textvariable=self.password,show="*",font=("Times new roman",20),bg="lightyellow")
        txt_pswd.place(x=280,y=220,width=400)
        
        btn_login=Button(login_frame,text="Log In",command=self.userlogin, font=("Times new roman",20),bg="#00b0f0",cursor="hand2", activebackground="#00b0f0")
        btn_login.place(x=280,y=300,width=250,height=50)
        
        hr=Label(login_frame,bg="lightgrey").place(x=50,y=390,width=690,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgrey",font=("Times new roman",20)).place(x=380,y=370)
        
        btn_forget=Button(login_frame,text="Forgot Password?", command=self.forget_window,font=("Times new roman",15),bd=0,bg="white", fg="#00759E",cursor="hand2", activebackground="white", activeforeground="#00759e")
        btn_forget.place(x=320,y=420)
        
        # ================================ Register Frame ==============================
        
        reg_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        reg_frame.place(x=250, y=550, width=800, height=80)
        
        lbl_reg=Label(reg_frame, text="Don't have an account? ",font=("Times new roman",15),bg="white").place(x=250,y=20)
        btn_signup=Button(reg_frame,text="Sign Up",command=self.signup,font=("Times new roman",15),bd=0,bg="white", fg="#00b0f0",cursor="hand2", activebackground="white", activeforeground="#00759e")
        btn_signup.place(x=440,y=17)
        
    
    def userlogin(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        try:
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                cur.execute(f"select utype from employee where eid=%s and pass=%s",(self.username.get(), self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid username or password")
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")            
                    
                
    def forget_window(self):
        con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
        cur=con.cursor()
        
        try:
            if self.username.get()=="":
                messagebox.showerror("Error","Username must be required")
            else:
                cur.execute(f"select email from employee where eid=%s",(self.username.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid username , Please try again")
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    chk=self.send_email(email[0])
                    if chk!="f":
                        messagebox.showerror("Error","Connection Error, Try Again")
                    else:
                        self.forget_window=Toplevel(self.root)
                        self.forget_window.title("Reset Password")
                        self.forget_window.geometry("500x400+500+100")
                        self.forget_window.focus_force()
                        
                        title=Label(self.forget_window,text="RESET PASSWORD", font=("Goudy old style",25,"bold","underline")).place(x=0,y=0,relwidth=1)
                        lbl_reset=Label(self.forget_window,text="Enter OTP", font=("Goudy old style",15,"bold")).place(x=10,y=50)
                        txt_reset=Entry(self.forget_window,textvariable=self.var_otp, font=("Times new roman",17)).place(x=10,y=90,height=40)
                        self.btn_reset=Button(self.forget_window,text="Submit",command=self.validate_otp, font=("Goudy old style",13),bg="orange").place(x=250,y=90, width=100, height=40)
                        
                        lbl_new_pass=Label(self.forget_window,text="Enter New Password", font=("Goudy old style",15,"bold")).place(x=10,y=180)
                        lbl_new_txt=Entry(self.forget_window,textvariable=self.var_new_pass, font=("Goudy old style",17)).place(x=10,y=220)

                        lbl_new_pass2=Label(self.forget_window,text="Confirm Password", font=("Goudy old style",15,"bold")).place(x=10,y=260)
                        lbl_new_txt2=Entry(self.forget_window,textvariable=self.var_conf_pass, font=("Goudy old style",17)).place(x=10,y=300)
                        self.btn_update=Button(self.forget_window,text="Login",command=self.update_pass,font=("Goudy old style",13),bg="lightgreen")
                        self.btn_update.place(x=10,y=350,width=100)
                    
        except Exception as exc:
            messagebox.showerror("Error",f"Error due to:{str(exc)}")
    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            pass
        else:
            messagebox.showerror("Error","Invalid OTP, Try Again")
            
    def update_pass(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showinfo("Information","Please Enter Password")
        elif self.var_new_pass.get()==self.var_conf_pass.get():
            messagebox.showerror("Information","Password must be same")
        else:
            con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
            cur=con.cursor()
            try:
                cur.execute(f"update employee set pass=%s where eid=%s",(self.var_new_pass.get(),self.username.get()))
                con.commit()
                messagebox.showinfo("Information","Password Updated Successfully")
                self.forget_window.destroy()
            except Exception as exc:
                messagebox.showerror("Error",f"Error due to:{str(exc)}")             
    
        
    def signup(self):
        self.root.destroy()
        os.system("python signup.py")
            
root=Tk()
obj=Login(root)
root.mainloop()
    