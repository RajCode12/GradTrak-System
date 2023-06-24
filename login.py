from tkinter import*
from tkinter import ttk,messagebox
import mysql.connector

class Login():
    def __init__(self,root):
        self.root=root
        self.root.title('Login Form')
        self.f=Frame(root,height=700,width=1300,bg="violet")
        self.f.propagate(0)
        self.f.pack()
        
        frame1=Frame(self.f,bg='white')
        frame1.place(x=250,y=100,width=800,height=500)
        title=Label(self.f,text="Login",font=('times new roman',20,'bold underline'),bg='white',fg='blue').place(x=600,y=30)
        
        email_id=Label(self.f,text='Email Id',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=430,y=200)
        self.txt_email_id=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_email_id.place(x=350,y=110,width=250)
        
        password=Label(self.f,text='Password',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=430,y=300)
        self.txt_password=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_password.place(x=350,y=210,width=250)
        
        self.btn1=Button(frame1,text="Login",width=12,height=1,cursor="hand2",bg='light green',font=("times new roman",15,'bold'),command=self.login_data).place(x=350,y=310)
        
        self.btn2=Button(frame1,text="Register",width=12,height=1,cursor="hand2",bg='light blue',font=("times new roman",15,'bold'),command=self.Register).place(x=350,y=370)
        
        self.btn3=Button(frame1,text="Exit",width=12,height=1,cursor="hand2",bg='white',fg='red',font=("times new roman",15,'bold'),command=self.iExit).place(x=20,y=450)
        
    def iExit(self):
        iExit=messagebox.askyesno("Registration form","Do you Really want to Exit")
        if iExit > 0:
            root.destroy()
            return
        
    def login_data(self):
        if self.txt_email_id.get()=="": 
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()=="": 
            messagebox.showinfo("Error","Please Enter Your Pasword",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',password='Raj@12345',user='root',database='userInfo')
                mycursor = conn.cursor()
            except:
                messagebox.showerror("Error","Database connectivity issues...")
                return 

            query = 'select * from data where email=%s and passwd=%s'
            mycursor.execute(query,(self.txt_email_id.get(),self.txt_password.get()))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.root.destroy()
                import main

            
    def Register(self):
        self.root.destroy()
        import register

root=Tk()
objobj=Login(root)
root.mainloop()
