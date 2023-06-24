from tkinter import*
from tkinter import ttk,messagebox
           
class Course:
    def __init__(self,root):
        self.root=root
        self.root.title('Course Page')
        self.f=Frame(root,height=700,width=1300)
        self.f.propagate(0)
        self.f.pack()
        
        frame1=Frame(self.f,bg='white')
        frame1.place(x=20,y=40,width=1250,height=580)
        title=Label(self.f,text='Courses',font=('times new roman',20,'bold underline'),bg='white',fg='blue').place(x=530,y=5)
        
        c=Canvas(frame1, bg='white', height=1000, width=1250, cursor='pencil')
        c.pack()
        c.create_rectangle(20,20,1230,560,fill='white',width=4)
        c.create_rectangle(20,80,1230,80,fill='white',width=1)
        c.create_rectangle(20,140,1230,140,fill='white',width=1)
        c.create_rectangle(20,200,1230,200,fill='white',width=1)
        c.create_rectangle(20,260,1230,260,fill='white',width=1)
        c.create_rectangle(20,320,1230,320,fill='white',width=1)
        c.create_rectangle(20,380,1230,380,fill='white',width=1)
        c.create_rectangle(20,440,1230,440,fill='white',width=1)
        c.create_rectangle(20,500,1230,500,fill='white',width=1)
       
        fnt=('Times',15,'bold')
        c.create_text(100,50,text='Course',font=fnt,fill='black')
        c.create_text(550,50,text='Duration',font=fnt,fill='black')
        c.create_text(1000,50,text='Fees',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,110,text='B.Com',font=fnt,fill='black')
        c.create_text(550,110,text='3 years',font=fnt,fill='black')
        c.create_text(1000,110,text='150000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,170,text='M.Com',font=fnt,fill='black')
        c.create_text(550,170,text='2 years',font=fnt,fill='black')
        c.create_text(1000,170,text='200000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,230,text='BA',font=fnt,fill='black')
        c.create_text(550,230,text='3 years',font=fnt,fill='black')
        c.create_text(1000,230,text='170000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        fnt=('Times',15)
        c.create_text(100,290,text='BCA',font=fnt,fill='black')
        c.create_text(550,290,text='3 years',font=fnt,fill='black')
        c.create_text(1000,290,text='235000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,350,text='MCA',font=fnt,fill='black')
        c.create_text(550,350,text='2 years',font=fnt,fill='black')
        c.create_text(1000,350,text='400000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,410,text='B.Tech',font=fnt,fill='black')
        c.create_text(550,410,text='4 years',font=fnt,fill='black')
        c.create_text(1000,410,text='520000/-',font=fnt,fill='black')
        
        fnt=('Times',15)
        c.create_text(100,470,text='Bpt',font=fnt,fill='black')
        c.create_text(550,470,text='4.5 years',font=fnt,fill='black')
        c.create_text(1000,470,text='300000/-',font=fnt,fill='black')
        
        self.btn2=Button(frame1,text="Back",width=8,height=1,bg='white',fg='red',font=("times new roman",12,'bold'),command=self.back).place(x=40,y=510)

    def back(self):
        self.root.destroy()
        import register
        
root=Tk()
obj=Course(root)
root.mainloop()    
