from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from tkinter import messagebox
import mysql.connector
import datetime
from time import strftime


class Myapp:
    def __init__(self,root):
        self.root=root
        self.root.title("MMS Bus ticket System")
        
        #self.root.iconbitmap('1.jpg')
        self.root.geometry("700x600+400+10")
        self.root.minsize(700, 600)
        self.root.maxsize(700, 600)
        pic=ImageTk.PhotoImage(Image.open("bac.jpg"))
        self.lab=Label(self.root,image=pic)
        self.lab.photo=pic
        self.lab.place(x=0,y=0)
        ##fram1
        self.f1=Frame(self.root,height=80,width=700,background='gray')
        self.f1.place(x=0,y=0)
        self.title=Label(self.f1,text="MMS BUS TICKET BOOKING SYSTEM",font=("arial 14 bold"),fg="black",bg='#ddd')
        self.title.place(x=180,y=5)
        
        Button(self.f1,text="HOME",font=("arial 10 bold"),bg='green',fg="white",command=self.home,width=14).place(x=53,y=40)
        Button(self.f1,text="OUR SERVICE AREA",font=("arial 10 bold"),bg='green',fg="white",command=self.service_area,width=16).place(x=174,y=40)
        Button(self.f1,text="FIND BUS",font=("arial 10 bold"),bg='green',fg="white",width=14,command=self.findbus_widow).place(x=311,y=40)
        Button(self.f1,text="BUY TICKET",font=("arial 10 bold"),bg='green',fg="white",command=self.ticketwindow,width=14).place(x=432,y=40)
        Button(self.f1,text="PROFILE",font=("arial 10 bold"),bg='green',fg="white",width=13,command=self.profile).place(x=553,y=40)
        #Button(self.f1,text="Edit Profile",font=("arial 10 bold"),bg='green',fg="white",width=11).place(x=524,y=40)

       
            
        #fram2
        self.f2=Frame(self.root,height=450,width=700)
        self.f2.place(x=0,y=80)
        self.login_frame=Frame(self.f2,height=450,width=150,bg='#ddd')#margin left column
        self.imges_frame=Frame(self.f2,height=450,width=550,highlightbackground="green",highlightcolor="green",highlightthickness=1)#Right all content frame
        self.login_frame.place(x=0,y=0)
        self.imges_frame.place(x=150,y=0)
        ###########
        Label(self.login_frame,text="Bellow",font=('arial 9 bold')).place(x=20,y=90)
        Label(self.login_frame,text="Logout here",font=('arial 9 bold')).place(x=7,y=110)
        Button(self.login_frame,text="LOGOUT",width=10,font=("arial 9 bold"),fg='white',bg='green',command=self.logout).place(x=10,y=150)
        #Button(self.login_frame,text="Registration",width=10,font=("arial 10 bold"),fg='white',bg='green',command=self.register_window).place(x=10,y=200)
      



        #fram3
        self.f3=Frame(self.root,height=70,width=700,background='gray')
        self.f3.place(x=0,y=530)
        #footer Area
        Label(self.f3,text="All right reserved MMS Bus Services Copyright @ Mamun",font=("arial 10 bold"),fg='white',bg='green').place(x=6,y=8)
        Button(self.f3,text="CONTACT US",font=("arial 9 bold"),bg='green',fg="white",width=12,command=self.contactus).place(x=416,y=7)
        Button(self.f3,text="PRIVACY POLICY",font=("arial 9 bold"),bg='green',fg="white",width=16,command=self.Privacy_poly).place(x=509,y=7)
        Button(self.f3,text="EXIT",font=("arial 9 bold"),bg='green',fg="white",width=7,command=self.stop).place(x=630,y=7)
        



    
    

    #fucntion section
    def clear(self):
        for item in self.imges_frame.winfo_children():
            item.destroy()

    def stop(self):
        sys.exit()
    def logout(self):
        self.root.destroy()
        import main

### working process...............................
    def home(self):
        self.clear()
        gmail=ImageTk.PhotoImage(Image.open("1.jpg"))
        self.lab=Label(self.imges_frame,image=gmail)
        self.lab.photo=gmail
        self.lab.place(x=0,y=0) 
        Label(self.imges_frame,text="We are Highly Promise to Services our Coustomer").place(x=10,y=400)
        Label(self.imges_frame,text="Help Line 24 Hours: 2474252",font=('arial 8 bold')).place(x=10,y=420)
      
    def contactus(self):
        self.clear()
        Label(self.imges_frame,text="MMS BUS Service",font=('Arial 14 bold')).place(x=20,y=10)
        Label(self.imges_frame,text="Main Office :Gazipur-Joydepur",font=('Arial 11')).place(x=20,y=40)
        Label(self.imges_frame,text="Gmail :contact.mms@gmail.com",font=('Arial 11')).place(x=20,y=60)
        Label(self.imges_frame,text="Customar Care : 2474252",font=('Arial 11')).place(x=20,y=100)

    def login_window(self):
        self.clear()
        self.e=StringVar()
        self.p=StringVar()
        
        Label(self.imges_frame,text="Login Here",font=('Arial 14 bold')).place(x=80,y=40)
        Label(self.imges_frame,text="Email:",font=('Arial 10 bold')).place(x=40,y=90)
        self.login_email=Entry(self.imges_frame,textvariable=self.e,bd=4,width=40).place(x=130,y=90)
        Label(self.imges_frame,text="Password:",font=('Arial 10 bold')).place(x=40,y=140)
        self.login_pass=Entry(self.imges_frame,textvariable=self.p,bd=4,width=40).place(x=130,y=140)
        self.login_btn=Button(self.imges_frame,text="Login",font=('arial 12 bold'),bg='green',fg='white',command=self.login)
        self.login_btn.place(x=270,y=180)

    
    def login(self):
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        mycursor.execute("select * from user where email=%s and usr_pwd=%s",(self.e.get(),self.p.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showinfo("success","your are login!!")
            self.clear()
            #### we have to import login page
            Label(self.imges_frame,text="your profile page import").place(x=22,y=20)
        else:
            messagebox.showerror("Error","Your email or password is wrong!!!")
        
        

 ############################### Wroking processs.............
    def register_window(self):
        self.clear()
        self.gender=StringVar()
        
        self.fname=StringVar()
        self.lname=StringVar()
        self.email=StringVar()
        self.password=StringVar()
        self.conpassword=StringVar()
        
        self.phone=StringVar()
        Label(self.imges_frame,text="Register Here",font=('Arial 14 bold')).place(x=190,y=30)
        Label(self.imges_frame,text="First name ",font=('Arial 10 bold')).place(x=20,y=70)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.fname).place(x=20,y=90)
        Label(self.imges_frame,text="Last name ",font=('Arial 10 bold')).place(x=250,y=70)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.lname).place(x=250,y=90)
        Label(self.imges_frame,text="Email ",font=('Arial 10 bold')).place(x=20,y=130)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.email).place(x=20,y=150)
        Label(self.imges_frame,text="Phone number ",font=('Arial 10 bold')).place(x=250,y=130)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.phone).place(x=250,y=150)
        Label(self.imges_frame,text="Gender ",font=('Arial 10 bold')).place(x=20,y=180)
        #Radiobutton(self.imges_frame,text="Male",value="Male",variable=self.male).place(x=20,y=200)
        self.radiobtn1=Radiobutton(self.imges_frame,text="Male",value="Male",variable=self.gender,).place(x=20,y=200)
        self.radiobtn2=Radiobutton(self.imges_frame,text="FeMale",value="FeMale",variable=self.gender,).place(x=100,y=200)
        
        #Radiobutton(self.imges_frame,text="FeMale",value="FeMale",variable=self.female).place(x=100,y=200)
        Label(self.imges_frame,text="Password ",font=('Arial 10 bold')).place(x=20,y=230)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.password).place(x=20,y=270)
        Label(self.imges_frame,text="Confrim password ",font=('Arial 10 bold')).place(x=250,y=230)
        Entry(self.imges_frame,width=30,bd=3,textvariable=self.conpassword).place(x=250,y=270)
        self.regbtn=Button(self.imges_frame,text="Register",font=('Arial 11 bold'),fg='white',bg='green',command=self.registration)
        self.regbtn.place(x=290,y=320)
        


    ######### Registration code
    def registration(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.email.get()=="" or self.phone.get()=="" or self.gender.get()=="" or self.password.get()=="" or self.conpassword=="":
            messagebox.showerror("Error","Please Fill up All Field. !!")
        elif self.password.get()!=self.conpassword.get():
            messagebox.showerror("Error","Your Password doesn't match!!")
        else:
            mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
            mycursor=mydb.cursor()
            mycursor.execute("select * from user where email=%s or phone=%s",(self.email.get(),self.phone.get()))
            row=mycursor.fetchone()
            #print(row)
            if row==None:
                query="INSERT INTO user (fname,lname,email,phone,gender,usr_pwd,con_usr_pwd) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                value=(self.fname.get(),self.lname.get(),self.email.get(),self.phone.get(),self.gender.get(),self.password.get(),self.conpassword.get())
                mycursor.execute(query,value)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Welcome","Your registration is successfull.")
                self.login_window()
            else:
                messagebox.showerror("Error","Account already exit!!")
                     
    def service_area(self):
        self.clear()
        mydb= mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        query="SELECT * FROM area_info;"
        mycursor.execute(query)
        showresult=mycursor.fetchall()
        

        tv = ttk.Treeview(self.imges_frame,height=21)
        tv['columns']=('start', 'end', 'distance','busname')
        tv.column('#0', width=0, stretch=NO)
        tv.column('start', anchor=CENTER, width=130)
        tv.column('end', anchor=CENTER, width=150)
        tv.column('distance', anchor=CENTER, width=100)
        tv.column('busname', anchor=CENTER, width=200)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('start', text='From', anchor=CENTER)
        tv.heading('end', text='To', anchor=CENTER)
        tv.heading('distance', text='Distance', anchor=CENTER)
        tv.heading('busname', text='Busname', anchor=CENTER)

        tv.place(x=0,y=0)
        for dt in showresult: 
            tv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[1],dt[2],dt[3],dt[5]))

    # End service area treeView 


    #Find bus
    def findbus_widow(self):
        self.clear()
        self.busname=StringVar()
        Entry(self.imges_frame,bd=2,width=30,bg='#ddd',textvariable=self.busname).place(x=10,y=10)
        Button(self.imges_frame,text="Search",bg='black',fg='white',font=('arial 8 bold'),command=self.findbus).place(x=200,y=7)





    def findbus(self):
        mydb= mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        query="SELECT * FROM area_info WHERE busname LIKE '%"+self.busname.get()+"%'"
        mycursor.execute(query)
        showresult=mycursor.fetchall()
        

        tv = ttk.Treeview(self.imges_frame,height=21)
        tv['columns']=('start', 'end', 'distance','cost','busname','time',"starjourneytime")
        tv.column('#0', width=0, stretch=NO)
        tv.column('start', anchor=CENTER, width=80)
        tv.column('end', anchor=CENTER, width=80)
        tv.column('distance', anchor=CENTER, width=70)
        tv.column('cost', anchor=CENTER, width=70)
        tv.column('busname', anchor=CENTER, width=80)
        tv.column('time', anchor=CENTER, width=80)
        tv.column('starjourneytime', anchor=CENTER, width=80)
        

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('start', text='From', anchor=CENTER)
        tv.heading('end', text='To', anchor=CENTER)
        tv.heading('distance', text='Distance', anchor=CENTER)
        tv.heading('cost', text='Cost', anchor=CENTER)
        tv.heading('busname', text='Busname', anchor=CENTER)
        tv.heading('time', text='Reach time', anchor=CENTER)
        tv.heading('starjourneytime', text='Journey time', anchor=CENTER)
        tv.place(x=0,y=40)
        for dt in showresult: 
            tv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))


    ###### ticket system
    def ticketwindow(self):
        self.clear()
        #self.printmail=StringVar()
        Label(self.imges_frame,text="Welcome to MMS Bus Service",font=("Arial 14 bold")).place(x=70,y=20)
        self.startjourney=["Dhaka","Khulna","Narail","Barisal","Rangpur","Chottogram","Dinajpur","Cummilla","Shylet","Gazipur"]
        self.choice1=StringVar(self.imges_frame)
        self.choice1.set("Select")
        Label(self.imges_frame,text="Select your Start Journey",font=("arial 12 bold")).place(x=10,y=80)
        self.menu=OptionMenu(self.imges_frame,self.choice1,*self.startjourney,)
        self.menu.place(x=20,y=110)
        Label(self.imges_frame,text="Select your End Journey",font=("arial 12 bold")).place(x=250,y=80)
        self.endjourney=["Dhaka","Khulna","Narail","Barisal","Rangpur","Chottogram","Dinajpur","Cummilla","Shylet","Gazipur"]
        self.choice2=StringVar(self.imges_frame)
        self.choice2.set("Select")
        OptionMenu(self.imges_frame,self.choice2,*self.endjourney).place(x=250,y=110)
       
        #Label(self.imges_frame,text="Your Email",font=("arial 12 bold")).place(x=20,y=150)
        #self.e1=Entry(self.imges_frame,width=30,bd=4,textvariable=self.printmail)
        #self.e1.place(x=25,y=190)
        self.ebtn=Button(self.imges_frame,text="SUBMIT",font=("arial 10 bold"),bg='green',fg='white',command=self.buyticket)
        self.ebtn.place(x=335,y=260)
        self.year=IntVar(self.imges_frame)
        
        Label(self.imges_frame,text="Please Input valid Journey Date and Time",font=('arial 10 bold')).place(x=10,y=160)
        
        Label(self.imges_frame,text="Input Valid Journey Date",font=('arial 9 bold')).place(x=10,y=190)
        Label(self.imges_frame,text="Input Valid Journey Time",font=('arial 9 bold')).place(x=240,y=190)
        self.yearlist=[2022]
        self.year.set("Year")
        OptionMenu(self.imges_frame,self.year,*self.yearlist).place(x=10,y=220)
        self.month=IntVar(self.imges_frame)
        self.monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]
        OptionMenu(self.imges_frame,self.month,*self.monthlist).place(x=90,y=220)
        self.month.set("Month")
        self.day=IntVar(self.imges_frame)
        self.daylist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        OptionMenu(self.imges_frame,self.day,*self.daylist).place(x=170,y=220)
        self.day.set("Day")
        self.hour=IntVar()
        self.hourlist=[1,2,3,4,5,6,7,8,9,10,11,12]
        OptionMenu(self.imges_frame,self.hour,*self.hourlist).place(x=240,y=220)
        self.hour.set("Hour")
        self.minit=IntVar(self.imges_frame)
        self.minitlist=[00,5,10,15,20,25,30,35,40,45,50,55]
        OptionMenu(self.imges_frame,self.minit,*self.minitlist).place(x=320,y=220)
        self.minit.set("Minute")
        Label(self.imges_frame,text="If you forgot bus journey time then show bellow",font=("arial 8 bold"),fg='red').place(x=10,y=320)
        self.bustime=StringVar()
        self.buslist=["Sohag","Digonto","BM poribohon","Ran poribohon","Snigdha","Korotoa","Km spiceal","Shajalal","Gazipur Bohon"]
        OptionMenu(self.imges_frame,self.bustime,*self.buslist).place(x=10,y=340)
        self.bustime.set("Select")
        Button(self.imges_frame,text="Show",command=self.journeytime,width=9).place(x=12,y=370)
#### bus option time selection section
    def journeytime(self):
        if self.bustime.get()=="Sohag":
            Label(self.imges_frame,text="Journey time: 5:15 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Khulna",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 5:15 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Khulna-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Digonto":
            Label(self.imges_frame,text="Journey time: 3:10 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Narail",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 3:10 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Narail-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="BM poribohon":
            Label(self.imges_frame,text="Journey time: 1:45 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Barisal",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 1:45 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Barisal-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Ran poribohon":
            Label(self.imges_frame,text="Journey time: 2:50 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Rangpur",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 2:50 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Rangpur-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Snigdha":
            Label(self.imges_frame,text="Journey time: 4:15 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Chottogram",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 4:15 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Chottogram-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Korotoa":
            Label(self.imges_frame,text="Journey time: 7:45 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Dinajpur",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 7:45 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Dinajpur-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Km spiceal":
            Label(self.imges_frame,text="Journey time: 8:15 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-comilla",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 8:15 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="comilla-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Shajalal":
            Label(self.imges_frame,text="Journey time: 9:45 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Shylet",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 9:45 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Shylet-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
        elif self.bustime.get()=="Gazipur Bohon":
            Label(self.imges_frame,text="Journey time: 1:15 PM",font=('arial 8 bold')).place(x=10,y=400)
            Label(self.imges_frame,text="Dhaka-Gazipur",font=('arial 8 bold')).place(x=10,y=420)
            Label(self.imges_frame,text="Journey time: 1:15 PM",font=('arial 8 bold')).place(x=160,y=400)
            Label(self.imges_frame,text="Gazipur-Dhaka",font=('arial 8 bold')).place(x=160,y=420)
    def buyticket(self):
        y=str(self.year.get())
        m=str(self.month.get())
        d=str(self.day.get())
        
        f=open("password.txt","r")
        n=f.read()
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        mycursor.execute("select * from user where email=%s",(n,))
        user=mycursor.fetchone()
        #datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
        if self.choice1.get()=="" or self.choice2.get()=="":
            messagebox.showerror("Error","Your Field is empty!!!")
        #elif user==None:
            #messagebox.showerror("Error","Your Email is Wrong!!1")

        elif self.choice1.get()==self.choice2.get():
            messagebox.showerror("Error","Please Valid input!!")
        #elif y=="" or m=="" or d=="":
            #messagebox.showerror("Error","Your Datetime is wrong!!!")

        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Khulna":
            q="select * from area_info where busname='Sohag'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            #e=self.printmail.get()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="5" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())

            self.clear()
            cheak=self.total("Sohag",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                #runing working area

            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()


        elif self.choice1.get()=="Khulna" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Sohag'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="5" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Sohag",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
####dhaka to Narail
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Narail":
            q="select * from area_info where busname='Digonto'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="3" or Min!="10":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Digonto",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=400)
            else:
                messagebox.showerror("Ticket info","This bus no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Narail" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Digonto'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="3" or Min!="10":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Digonto",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=400)
            else:
                messagebox.showerror("ticket info","This bus has no ticket")
                self.ticketwindow()
##Dhaka to BArisal
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Barisal":
            q="select * from area_info where busname='BM poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="1" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("BM poribohon",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Staus : Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Barisal" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='BM poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="1" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("BM poribohon",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                # Label(self.imges_frame,font=("arial 10 bold"),text="Status :  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
#dhaka to rangpur  
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Rangpur":
            q="select * from area_info where busname='Ran poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()

            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="2" or Min!="50":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Ran poribohon",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status : Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Rangpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Ran poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="2" or Min!="50":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Ran poribohon",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
#Dhaka to chottogram
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Chottogram":
            q="select * from area_info where busname='Snigdha'"
            mycursor.execute(q)
            result=mycursor.fetchone()
 
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="4" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Snigdha",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status : Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d

                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Chottogram" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Snigdha'"
            mycursor.execute(q)
            result=mycursor.fetchone()
   
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="4" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Snigdha",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status : Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("ticket info","This bus has no ticket ")
                self.ticketwindow()
#dhaka to dintaj pur
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Dinajpur":
            q="select * from area_info where busname='Korotoa'"
            mycursor.execute(q)
            result=mycursor.fetchone()

            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="7" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Korotoa",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                # Label(self.imges_frame,font=("arial 10 bold"),text="Status: Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("ticket info","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Dinajpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Korotoa'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="7" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Korotoa",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status: Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()
#dhaka to cummilla
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Cummilla":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="8" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Km spiceal",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status : Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=400)
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
        elif self.choice1.get()=="Cummilla" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="8" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Km spiceal",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status : Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=400)
            else:
                messagebox.showerror("ticket info","This bus has no ticket")    
                self.ticketwindow()
### Dhaka to Dinajpur
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Dinajpur":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()

            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()

            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="7" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Korotoa",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)

                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Error","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Dinajpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()

            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()

            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="7" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Korotoa",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=60)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=90)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=120)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=150)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=180)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=210)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=240)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=270)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=300)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=330)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=390)
            else:
                messagebox.showerror("ticket info","This bus has no ticket")
                self.ticketwindow()
#dhaka to shylet
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Shylet":
            q="select * from area_info where busname='Shajalal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="9" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Shajalal",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Erro","This bus has no ticket")
                self.ticketwindow()
        elif self.choice1.get()=="Shylet" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Shajalal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="9" or Min!="45":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            self.clear()
            cheak=self.total("Shajalal",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status: Unpaid ").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d 
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
            else:
                messagebox.showerror("Error","This bus has no ticket")
                self.ticketwindow()    
#dhaka to gazipur
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Gazipur":
            q="select * from area_info where busname='Gazipur Bohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="1" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
            d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Gazipur Bohon",d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[1])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[2])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(d)).place(x=40,y=350)
                
                
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=d
            else:
                messagebox.showerror("ticket info","This bus has no ticket")
                self.ticketwindow()
## cheak ticket testing working...................................................
        elif self.choice1.get()=="Gazipur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Gazipur Bohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s",(n,))
            user=mycursor.fetchone()
            y=str(self.year.get())
            m=str(self.month.get())
            d=str(self.day.get())
            H=str(self.hour.get())
            Min=str(self.minit.get())
            if H !="1" or Min!="15":
                messagebox.showerror("Error","Input valid journey time!!")
                self.ticketwindow()
### Wroking ticket information
            self.d=datetime.datetime(self.year.get(),self.month.get(),self.day.get(),self.hour.get(),self.minit.get())
            self.clear()
            cheak=self.total("Gazipur Bohon",self.d)
            if cheak!=3:
                Label(self.imges_frame,text="TICKET INFORMATION",font=("arial 14 bold")).place(x=150,y=10)
                Label(self.imges_frame,font=("arial 10 bold"),text="Name:  "+str(user[1])+" "+str(user[2])).place(x=40,y=50)
                Label(self.imges_frame,font=("arial 10 bold"),text="Phone number:  "+str(user[4])).place(x=40,y=80)
                Label(self.imges_frame,font=("arial 10 bold"),text="Email: "+str(user[3])).place(x=40,y=110)
                Label(self.imges_frame,font=("arial 10 bold"),text="Gender:  "+str(user[5])).place(x=40,y=140)
                Label(self.imges_frame,font=("arial 10 bold"),text="Start Journey:  "+str(result[2])).place(x=40,y=170)
                Label(self.imges_frame,font=("arial 10 bold"),text="End journey:  "+str(result[1])).place(x=40,y=200)
                Label(self.imges_frame,font=("arial 10 bold"),text="Busname:  "+str(result[5])).place(x=40,y=230)
                Label(self.imges_frame,font=("arial 10 bold"),text="Distance:  "+str(result[3])).place(x=40,y=260)
                Label(self.imges_frame,font=("arial 10 bold"),text="Cost:  "+str(result[4])).place(x=40,y=290)
                Label(self.imges_frame,font=("arial 10 bold"),text="Duration Time:  "+str(result[6])).place(x=40,y=320)
                #Label(self.imges_frame,font=("arial 10 bold"),text="Status :  Unpaid").place(x=40,y=350)
                Label(self.imges_frame,font=("arial 10 bold"),text="Journey Date:  "+str(self.d)).place(x=40,y=350)
                Button(self.imges_frame,text="Payment",bg='green',fg='white',font=('arial 9 bold'),command=self.payment_window).place(x=40,y=410)
                self.firstname=user[1]
                self.lastname=user[2]
                self.phonenumber=user[4]
                self.emailnumber=user[3]
                self.sex=user[5]
                self.start=result[1]
                self.end=result[2]
                self.bus=result[5]
                self.dis=result[3]
                self.Cost=result[4]
                self.Duration=result[6]
                self.ticketday=self.d
            else:
                messagebox.showerror("Ticket info","This bus has no ticket")
                self.ticketwindow()

        else:
            messagebox.showerror("Error","This Service is Not Available Now")
    ###payment function
    def payment_window(self):
        self.clear()
        Label(self.imges_frame,text="Select payment method",font=("arial 10 bold")).place(x=20,y=20)
        self.paylist=["Bkash"]
        self.pay=StringVar(self.imges_frame)
        OptionMenu(self.imges_frame,self.pay,*self.paylist).place(x=20,y=50)
        #self.pay.set("Select")
        Button(self.imges_frame,text="Enter",command=self.paymenttest,bg="#ddd").place(x=105,y=53)
    
    def paymenttest(self):
        if self.pay.get()=="Bkash":
            self.bnumber=StringVar()
            self.bpin=StringVar()
            Label(self.imges_frame,text="Bkash number").place(x=20,y=90)
            Entry(self.imges_frame,textvariable=self.bnumber,bd=4).place(x=20,y=120)
            Label(self.imges_frame,text="Pin number").place(x=20,y=150)
            Entry(self.imges_frame,textvariable=self.bpin,bd=4).place(x=20,y=180)    
            Button(self.imges_frame,text="confrim payment",command=self.paymentconfrim,font=("arial 8 bold"),bg='green',fg='white').place(x=35,y=210)

    def paymentconfrim(self):
        if self.bnumber.get()=="" or self.bpin.get()=="":
            messagebox.showerror("Error","Your account_number or pin is empty")
        else:
            self.confrim()
        

    ###########ticket confrim
    def confrim(self):
        self.clear()
        
        messagebox.showinfo("Welcome","Completed payment Your ticket is Successfully purchase")
        self.ticketwindow()
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        q="insert into ticketinfo( fname, lname, phone, email, gender, start, end, busname, distance, cost, time,ticketday) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self.firstname,self.lastname,self.phonenumber,self.emailnumber,self.sex,self.start,self.end,self.bus,self.dis,self.Cost,self.Duration,self.ticketday)
        mycursor.execute(q,val)
        mydb.commit()
        import ticket
        mydb.close()


    def Privacy_poly(self):
        self.clear()
        Label(self.imges_frame,text="Privacy Policy",font=('arial 11')).place(x=10,y=10)
        Label(self.imges_frame,text="This privacy policy has been compiled to better serve those who are concerned \nwith how their ‘Personally identifiable information’ (PII) is being used\n online. PII, as used in US privacy law and information\n security, is information that can be used on its own or with\n other information to identify, contact, or locate a \nsingle person, or to identify an individual in context",font=('arial 11')).place(x=10,y=30)

        Label(self.imges_frame,text="When ordering or registering on our site, as appropriate,you may be asked to enter \nyour name, email address, mailing address, phone number, credit card information,\n or other details to help you with your experience.",font=('arial 11')).place(x=10,y=160)

# Profile and Edit Section 



    
    def profile(self):
        self.clear()
        f=open("password.txt","r")
        n=f.read()
        
        #print(n)
        #f.close()
        
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        q="select * from user where email=%s"
        val=(n,)
        mycursor.execute(q,val)
        result=mycursor.fetchone()
       
        
        self.fn=result[1]
        self.ln=result[2]
        self.en=result[3]
        self.pn=result[4]
        self.passn=result[6]
        Label(self.imges_frame,text="Your Account information",font=('arial 14 bold')).place(x=20,y=20)
        Label(self.imges_frame,text="Frist name : "+str(result[1]),font=('arial 9 bold')).place(x=20,y=80)
        Label(self.imges_frame,text="Last name : "+str(result[2]),font=('arial 9 bold')).place(x=20,y=110)
        Label(self.imges_frame,text="Email : "+str(result[3]),font=('arial 9 bold')).place(x=20,y=150)
        Label(self.imges_frame,text="Phone Number : "+str(result[4]),font=('arial 9 bold')).place(x=20,y=180)
        Label(self.imges_frame,text="Password : "+str(result[6]),font=('arial 9 bold')).place(x=20,y=210)
        Button(self.imges_frame,text="Edit",font=('arial 10 bold'),bg='black',fg='white',width=8,command=self.edit_window).place(x=20,y=260)
        Button(self.imges_frame,text="Delete Account",font=('arial 10 bold'),bg='black',fg='white',command=self.delete).place(x=100,y=260)

    def edit_window(self):
        self.clear()
        #Assign value in database
        self.efn=StringVar()
        self.eln=StringVar()
        self.een=StringVar()
        self.epn=StringVar()
        self.editpass=StringVar()

        Label(self.imges_frame,text="First name ",font=('arial 9 bold')).place(x=10,y=30)
        Entry(self.imges_frame,textvariable=self.efn).place(x=100,y=30)
        self.efn.set(self.fn)
        Label(self.imges_frame,text="Last name ",font=('arial 9 bold')).place(x=10,y=60)
        Entry(self.imges_frame,textvariable=self.eln).place(x=100,y=60)
        self.eln.set(self.ln)
        Label(self.imges_frame,text="Phone ",font=('arial 9 bold')).place(x=10,y=90)
        Entry(self.imges_frame,textvariable=self.epn).place(x=100,y=90)
        self.epn.set(self.pn)
        Label(self.imges_frame,text="Password  ",font=('arial 9 bold')).place(x=10,y=120)
        Entry(self.imges_frame,textvariable=self.editpass).place(x=100,y=120)
        self.editpass.set(self.passn)

        Button(self.imges_frame,text="Update",bg='black',fg='white',command=self.edit).place(x=140,y=160)

        

# Edit profile 
    def edit(self):
        f=open("password.txt","r")
        n=f.read()

        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        q="UPDATE user SET fname = %s, lname = %s, phone = %s, usr_pwd = %s,con_usr_pwd= %s WHERE user.email = %s"
        val=(self.efn.get(),self.eln.get(),self.epn.get(),self.editpass.get(),self.editpass.get(),n)
        mycursor.execute(q,val)
        mydb.commit()
        mycursor.close()
        messagebox.showinfo("Success","Your profile hasbeen updated!!")
        self.profile()

#delete profile
    def delete(self):
        f=open("password.txt","r")
        n=f.read()
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        ch=messagebox.askyesno("press yes or no ","Are you want to delete")
        if ch==True:
            q="delete from user where email=%s"
            val=(n,)
            mycursor.execute(q,val)
            mydb.commit()
            messagebox.showinfo("Account delete","Your account hasbeen deleted!!")
            self.stop()
        else:
            self.profile()
        

### bus ticket cheak section
    def total(self,n,k):
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()

        q="select busname= %sfrom ticketinfo where ticketday=%s"
        val=(n,k)
        mycursor.execute(q,val)
        cheak=mycursor.fetchall()
        count=0
        for i in cheak:
            count=count+1
        
        return count






root=Tk()
obj=Myapp(root)
#my app start..
obj.home()

#obj.total("Gazipur Bohon")


###My ap end
root.mainloop()