from tkinter import*
from tkinter import ttk,messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Registration Form')
        self.f=Frame(root,height=700,width=1300,bg="violet")
        self.f.propagate(0)
        self.f.pack()

        frame1=Frame(self.f,bg='white')
        frame1.place(x=150,y=80,width=1000,height=550)
        title=Label(self.f,text='Sign Up',font=('times new roman',20,'bold underline'),bg='white',fg='blue').place(x=500,y=30)
    
        f_name=Label(self.f,text='First Name',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=200,y=100)
        self.txt_fname=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_fname.place(x=50,y=60,width=250)
        
        l_name=Label(self.f,text='Last Name',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=500,y=100)
        self.txt_lname=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_lname.place(x=350,y=60,width=250)
        
        self.contact=Label(self.f,text='Contact',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=200,y=190)
        self.txt_contact=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_contact.place(x=50,y=150,width=250)
        
        email=Label(self.f,text='Email',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=500,y=190)
        self.txt_email=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_email.place(x=350,y=150,width=250)
        
        dob=Label(self.f,text='DOB',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=200,y=280)
        self.txt_dob=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_dob.place(x=50,y=240,width=250)
        
        country=Label(self.f,text='Country',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=500,y=280)
        self.cmb_coun=ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER)
        self.cmb_coun['values']=("Select","Germany","Argentina","China","India","Egypt","Russia","Australia")
        self.cmb_coun.place(x=350,y=240,width=250)
        self.cmb_coun.current(0)
    
        gender=Label(self.f,text='Gender',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=200,y=370)
        self.var_gen=IntVar()
        fnt=('courier',15,'bold')
        self.r=Radiobutton(frame1,bg='light gray',font=fnt,variable=self.var_gen,value=1,text='MALE')
        self.r1=Radiobutton(frame1,bg='light gray',font=fnt,variable=self.var_gen,value=2,text='FEMALE')
        self.r.place(x=50,y=330)
        self.r1.place(x=170,y=330)
        
        course=Label(self.f,text='Course',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=500,y=370)
        self.cmb_cour=ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER)
        self.cmb_cour['values']=("Select","B.Com","M.Com","BA","BCA","MCA","B.Tech","Bpt")
        self.cmb_cour.place(x=350,y=330,width=250)
        self.cmb_cour.current(0)
        
        password=Label(self.f,text='Password',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=200,y=460)
        self.txt_pass=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_pass.place(x=50,y=420,width=250)
        
        con_pass=Label(self.f,text='Confirm Password',font=('times new roman',20,'bold'),bg='white',fg='black').place(x=500,y=460)
        self.txt_confpass=Entry(frame1,font=('times new roman',15),bg='lightgray')
        self.txt_confpass.place(x=350,y=420,width=250)
        
        self.var_c=IntVar()
        c=Checkbutton(frame1,text='I Agree to the Terms and Conditions',variable=self.var_c,onvalue=1,offvalue=0,bg="white",font=('times new roman',12,'bold')).place(x=50,y=460)
        
        self.btn1=Button(frame1,text="Register",width=12,height=1,cursor="hand2",bg='light green',font=("times new roman",15,'bold'),command=self.register_data).place(x=750,y=400)
        
        self.btn3=Button(frame1,text="Exit",width=12,height=1,cursor="hand2",bg='white',fg='red',font=("times new roman",15,'bold'),command=self.iExit).place(x=750,y=460)

        self.btn4=Button(frame1,text="Reset",width=12,height=1,cursor="hand2",bg='light blue',font=("times new roman",15,'bold'),command=self.clear).place(x=750,y=340)
        
        self.btn2=Button(frame1,text="T & R",width=8,height=1,cursor="hand2",bg='white',fg='black',font=("times new roman",12,'bold'),command=self.Terms).place(x=50,y=500)

        self.btn5=Button(frame1,text="Course details",width=12,height=1,cursor="hand2",bg='white',fg='black',font=("times new roman",12,'bold'),command=self.Course).place(x=150,y=500)
    
    def iExit(self):
        iExit=messagebox.askyesno("Registration form","Do you Really want to Exit")
        if iExit > 0:
            root.destroy()
            return
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.txt_dob.get()=="" or self.cmb_coun.get()=="Select" or self.cmb_cour.get()=="Select" or self.txt_pass.get()=="" or self.txt_confpass.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_pass.get() != self.txt_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_gen.get()==0:
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.var_c.get()==0:
             messagebox.showerror("Error","Please Agree the Terms and Conditions",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',password='Raj@12345',user='root',database='userInfo')
                mycursor = conn.cursor()
            except:
                messagebox.showerror("Error","Database connectivity issues...")


            query = 'insert into data(first_name,last_name,email,contact,dob,country,course,passwd) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            val = (self.txt_fname.get(),self.txt_lname.get(),self.txt_email.get(),self.txt_contact.get()
                   ,self.txt_dob.get(),self.cmb_coun.get(),self.cmb_cour.get(),self.txt_pass.get())

            mycursor.execute(query,val)
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Registration Successfull')
            self.clear()
            
        
        
    def Terms(self):
        self.root.destroy()
        import terms

    def Course(self):
        self.root.destroy()
        import course

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_dob.delete(0,END)
        self.txt_confpass.delete(0,END)
        self.cmb_coun.current(0)
        self.cmb_cour.current(0) 
        
root=Tk()
obj=Register(root)
root.mainloop()
