from tkinter import*
from tkinter import ttk,messagebox
           
class Terms:
    def __init__(self,root):
        self.root=root
        self.root.title('Terms Page')
        self.f=Frame(root,height=700,width=1300)
        self.f.propagate(0)
        self.f.pack()
        
        frame1=Frame(self.f,bg='white')
        frame1.place(x=30,y=60,width=1200,height=580)
        title=Label(self.f,text='Terms & Conditions',font=('times new roman',20,'bold underline'),bg='white',fg='blue').place(x=530,y=5)
    
        
        text=Text(frame1,wrap=WORD,font=('Times',15))
        text.insert(INSERT,"1)   Scholarship/ Financial Aid and different phases of Fee/ Scholarship are applicable for Indian Applicants only.2) Grant of Scholarship/ Financial Aid in different phases is subject to prevalence of scheme at the time of receipt of application and is further subject to verification and authentication of the information, certificates and other documents as required by the University.3) Applicants, who have scored 10 CGPA in 10th or 10+2 (12th) class of any board, will be considered for scholarship equivalent to that of Bracket-I scholarship (on the basis of eligibility qualification).4) Scholarship/ Financial Aid will be offered at the time of Admission only. It may be offered on different basis like Scholarship on the basis of Sports, on the basis of cultural performance or on the basis of marks in qualifying exam etc. Applicant can claim the Scholarship/ Financial Aid on any one basis and the claim must be made at the time of filing Application for Admissions or before the date prescribed by the University subject to the last date of Admission with Scholarship/ Financial Aid for the concerned Programme. In case applicant has opted Scholarship/ Financial Aid of one type (i.e. on one basis) or has not opted for it, then any change in the Scholarship (type/ bracket/ amount) so claimed will not be allowed at later stage.5) Scholarship/ Financial Aid will be awarded to the candidate only after the verification of original documents. In case candidate is not able to provide the documents within the stipulated time as prescribed by the university, subject to maximum of 6 months from the last date of admission, then scholarship/ financial aid will not be awarded or may be canceled, if already awarded. 7) In case, an applicant is eligible for Scholarship/ Financial Aid as well as for any other monetary benefit under any other scheme or policy of University, then the applicant will have to opt for only one scheme of his/her choice.6) A candidate being admitted under Post Matric Scholarship or any other Govt. Scholarship for full programme fee waiver can either avail scholarship offered by Govt. agency or Scholarship/ Financial Aid offered by the University.7) If a candidate earlier admitted in a programme during one phase, later on applies for programme transfer; then he will be entitled for the fee/ scholarship/ financial aid benefit applicable in that phase in which he initially took admission in, subject to last date of admission and availability of seats in the concerned programme and other conditions prescribed for that specific phase. However, no separate schedule of NEST will be available for such candidates.Example: Case 1) Applicant initially admitted in Phase-I in BFA with 50% scholarship, if later on in Phase IV seeks transfer to B.A., then for B.A. also he will get the same scholarship bracket as for BFA in Phase I (50% Scholarship). Case 2) Applicant initially admitted in Phase I in B.Tech. with 50% Scholarship after qualifying NEST, if later on in Phase IV seeks transfer to B.A., then for B.A. also, he/she will get the benefit of Phase I Scholarship.")
        text.pack()
        
        self.btn1=Button(frame1,text="Back",width=8,height=1,bg='white',fg='red',font=("times new roman",12,'bold'),command=self.Back).place(x=40,y=510)

    def Back(self):
        self.root.destroy()
        import register
        
root=Tk()        
obj=Terms(root)
root.mainloop()    
