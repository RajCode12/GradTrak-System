from tkinter import*
from tkinter import ttk,messagebox
           
class Main:
    def __init__(self,root):
        self.root=root
        self.root.title('Main page')
        self.f=Frame(root,height=700,width=1300)
        self.f.propagate(0)
        self.f.pack()
        
        frame1=Frame(self.f,bg='white')
        frame1.place(x=40,y=50,width=1200,height=580)
        title=Label(self.f,text='Welcome to UMS',font=('times new roman',20,'bold underline'),bg='white',fg='blue').place(x=500,y=10)
        
       
        self.btn1=Button(frame1,text="Profile",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=10,y=10)
        
        self.btn2=Button(frame1,text="Message",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=10,y=120)
        
        self.btn3=Button(frame1,text="Meeting",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=10,y=220)
            
        self.btn4=Button(frame1,text="Fee Details",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=10,y=320)
        
        self.btn5=Button(frame1,text="Exit",width=12,height=1,cursor="hand2",bg='white',fg='red',font=("times new roman",15,'bold'),command=self.iExit).place(x=10,y=540)
        
        self.btn6=Button(frame1,text="Exam",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=140,y=10)
        
        self.btn7=Button(frame1,text="Result",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=260,y=10)
        
        self.btn8=Button(frame1,text="Query",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=380,y=10)
        
        self.btn9=Button(frame1,text="Contact",width=10,height=4,cursor="hand2",bg='pink',font=("times new roman",15,'bold')).place(x=500,y=10)
        
        
    def iExit(self):
        iExit=messagebox.askyesno("Registration form","Do you Really want to Exit")
        if iExit > 0:
            root.destroy()        
                
root=Tk()
obj1=Main(root)
root.mainloop()
