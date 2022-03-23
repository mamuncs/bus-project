from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from tkinter import messagebox
import mysql.connector
from time import strftime
import calendar



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
        self.title=Label(self.f1,text="MMS BUS TICKET BOOKING SYSTEM",font=("arial 16 bold"),fg="black",bg='#ddd')
        self.title.place(x=180,y=5)
        Button(self.f1,text="HOME",bg='green',fg='white',font=('arial 9 bold'),command=self.home,width=14).place(x=10,y=50)
        Button(self.f1,text="SERVICE AREA",bg='green',fg='white',font=('arial 9 bold'),command=self.service_area,width=16).place(x=117,y=50)
        Label(self.f1,text="Please Registration First to Get Our Services",font=("arial 12 bold"),bg='green',fg='white').place(x=250,y=50)
       
            
        #fram2
        self.f2=Frame(self.root,height=450,width=700)
        self.f2.place(x=0,y=80)
        self.login_frame=Frame(self.f2,height=450,width=150,bg='#ddd')#margin left column
        self.imges_frame=Frame(self.f2,height=450,width=550,highlightbackground="green",highlightcolor="green",highlightthickness=1)#Right all content frame
        self.login_frame.place(x=0,y=0)
        self.imges_frame.place(x=150,y=0)
        ###########
        Label(self.login_frame,text="Bellow",font=('arial 9 bold')).place(x=20,y=90)
        Label(self.login_frame,text="Login or Registration",font=('arial 9 bold')).place(x=7,y=110)
        Button(self.login_frame,text="LOGIN",width=12,font=("arial 8 bold"),fg='white',bg='green',command=self.login_window).place(x=10,y=150)
        Button(self.login_frame,text="REGISTRATION",width=12,font=("arial 8 bold"),fg='white',bg='green',command=self.register_window).place(x=10,y=200)
        Button(self.login_frame,text="Forgot password",bg="#ddd",bd=None,command=self.forgotpass_window).place(x=10,y=250)
        
    
        #fram3
        self.f3=Frame(self.root,height=70,width=700,background='gray')
        self.f3.place(x=0,y=530)
        #footer Area
        Label(self.f3,text="All right reserved MMS Bus Services Copyright @ Mamun",font=("arial 10 bold"),fg='white',bg='green').place(x=6,y=8)
        Button(self.f3,text="CONTACT US",font=("arial 9 bold"),bg='green',fg="white",width=14,command=self.contactus).place(x=400,y=7)
        Button(self.f3,text="PRIVACY POLICY",font=("arial 9 bold"),bg='green',fg="white",width=16,command=self.Privacy_poly).place(x=508,y=7)
        Button(self.f3,text="EXIT",font=("arial 9 bold"),bg='green',fg="white",width=9,command=self.stop).place(x=630,y=7)
        



    
    

    #fucntion section
    def clear(self):
        for item in self.imges_frame.winfo_children():
            item.destroy()

    def stop(self):
        sys.exit()


    def home(self):
        self.clear()
        gmail=ImageTk.PhotoImage(Image.open("1.jpg"))
        self.lab=Label(self.imges_frame,image=gmail)
        self.lab.photo=gmail
        self.lab.place(x=0,y=0) 
        Label(self.imges_frame,text="We are Highly Promise to Services our Coustomer").place(x=10,y=400)
        Label(self.imges_frame,text="Help Line 24 Hours: 2474252",font=('arial 8 bold')).place(x=10,y=420)
      
####working procsssss.................
    def forgotpass_window(self):
        self.upmail=StringVar()
        self.uppass=StringVar()
        self.clear()
        Label(self.imges_frame,text="Enter your Email",font=("arial 10 bold")).place(x=20,y=40)
        Entry(self.imges_frame,textvariable=self.upmail,width=40,bd=4).place(x=20,y=70)
        Label(self.imges_frame,text="Enter your New password",font=("arial 10 bold")).place(x=20,y=100)
        Entry(self.imges_frame,textvariable=self.uppass,width=40,bd=4).place(x=20,y=140)
        Button(self.imges_frame,text="Change password",bg='black',fg='white',font=('arial 12 bold'),command=self.forgotpass).place(x=115,y=180)
    
    def forgotpass(self):
        #self.clear()
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        q="select * from user where email=%s"
        val=(self.upmail.get(),)
        mycursor.execute(q,val)
        result=mycursor.fetchone()
        if result!=None:
            q="UPDATE user SET usr_pwd = %s,con_usr_pwd=%s WHERE email = %s"
            val=(self.uppass.get(),self.uppass.get(),result[3])
            mycursor.execute(q,val)
            mydb.commit()
            messagebox.showinfo("Success","Your passwrod hasbeen Reset.")
            self.login_window()
        else:
            messagebox.showerror("Error","Your email is incorrect!!")


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
            data=row[3]
            f=open("password.txt","w")
            f.write(data)
            f.close()
            messagebox.showinfo("success","your are login!!")
            #### we have to import login page
            self.root.destroy()
            import login
            
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
            q="select * from user where email=%s"
            val=(self.email.get(),)
            mycursor.execute(q,val)
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
        
        Label(self.imges_frame,text="Our Service is Open 7 days and 24 Hours",font=('arial 10 bold')).place(x=40,y=10)
        tv = ttk.Treeview(self.imges_frame,height=21)
        tv['columns']=('start', 'end', 'distance','cost','busname','time','startjourneytime')
        tv.column('#0', width=0, stretch=NO)
        tv.column('start', anchor=CENTER, width=70)
        tv.column('end', anchor=CENTER, width=70)
        tv.column('distance', anchor=CENTER, width=90)
        tv.column('cost', anchor=CENTER, width=80)
        tv.column('busname', anchor=CENTER, width=80)
        tv.column('time', anchor=CENTER, width=70)
        tv.column('startjourneytime', anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('start', text='From', anchor=CENTER)
        tv.heading('end', text='To', anchor=CENTER)
        tv.heading('distance', text='Distance', anchor=CENTER)
        tv.heading('cost', text='Cost', anchor=CENTER)
        tv.heading('busname', text='Busname', anchor=CENTER)
        tv.heading('time', text='Reach time', anchor=CENTER)
        tv.heading('startjourneytime', text='Journey Time', anchor=CENTER)
        tv.place(x=0,y=50)
        for dt in showresult: 
            tv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))



    # End service area treeView 

    ###### ticket system
    def ticketwindow(self):
        self.clear()
        self.printmail=StringVar()
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
       
        Label(self.imges_frame,text="Your Email",font=("arial 12 bold")).place(x=20,y=150)
        self.e1=Entry(self.imges_frame,width=30,bd=4,textvariable=self.printmail)
        self.e1.place(x=25,y=190)
        self.ebtn=Button(self.imges_frame,text="Submit buy ticket",font=("arial 10 bold"),bg='black',fg='white',command=self.buyticket)
        self.ebtn.place(x=230,y=190)
        


    def buyticket(self):
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        if self.choice1.get()=="" or self.choice2.get()=="" or self.printmail.get()=="":
            messagebox.showerror("Error","Your Field is empty!!!")

        elif self.choice1.get()==self.choice2.get():
            messagebox.showerror("Error","Please Valid input!!")
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Khulna":
            q="select * from area_info where busname='Sohag'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            e=self.printmail.get()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid").place(x=40,y=350)
            #Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
            Button(self.imges_frame,text="Confrim Ticket").place(x=100,y=360)


        elif self.choice1.get()=="Khulna" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Sohag'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
####dhaka to Narail
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Narail":
            q="select * from area_info where busname='Digonto'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            e=self.printmail.get()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)

        elif self.choice1.get()=="Narail" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Digonto'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            e=self.printmail.get()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
##Dhaka to BArisal
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Barisal":
            q="select * from area_info where busname='BM poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            e=self.printmail.get()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)

        elif self.choice1.get()=="Barisal" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='BM poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            e=self.printmail.get()
            mycursor.execute("select * from user where email=%s or varify='%s'",(self.printmail.get(),None))
            user=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
#dhaka to rangpur  
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Rangpur":
            q="select * from area_info where busname='Ran poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
            Label(self.imges_frame,text="MMS Bus Service Ticket",font=("arial 14 bold")).place(x=150,y=20)
            Label(self.imges_frame,font=("arial 10"),text="cost:"+str(result[4])).place(x=10,y=50)   
        elif self.choice1.get()=="Rangpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Ran poribohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
            Label(self.imges_frame,text="MMS Bus Service Ticket",font=("arial 14 bold")).place(x=150,y=20)
            Label(self.imges_frame,font=("arial 10"),text="cost:"+str(result[4])).place(x=10,y=50)  
#Dhaka to chottogram
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Chottogram":
            q="select * from area_info where busname='Snigdha'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
        elif self.choice1.get()=="Chottogram" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Snigdha'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)

#dhaka to dintaj pur
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Dinajpur":
            q="select * from area_info where busname='Korotoa'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
        elif self.choice1.get()=="Dinajpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Korotoa'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
#dhaka to cummilla
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Cummilla":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
        elif self.choice1.get()=="Dinajpur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Km spiceal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)

#dhaka to shylet
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Shylet":
            q="select * from area_info where busname='Shajalal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
        elif self.choice1.get()=="Shylet" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Shajalal'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380) 
#dhaka to gazipur
        elif self.choice1.get()=="Dhaka" and self.choice2.get()=="Gazipur":
            q="select * from area_info where busname='Gazipur Bohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)
        elif self.choice1.get()=="Gazipur" and self.choice2.get()=="Dhaka":
            q="select * from area_info where busname='Gazipur Bohon'"
            mycursor.execute(q)
            result=mycursor.fetchone()
            self.clear()
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
            Label(self.imges_frame,font=("arial 10 bold"),text="Ticket Day:  ").place(x=40,y=350)
            Label(self.imges_frame,font=("arial 10 bold"),text="Status:  Unpaid ").place(x=40,y=380)


        else:
            messagebox.showerror("Error","You have worng input!!")
            
        
        



        
    def Privacy_poly(self):
        self.clear()
  
        Label(self.imges_frame,text="Privacy Policy",font=('arial 11')).place(x=10,y=10)
        Label(self.imges_frame,text="This privacy policy has been compiled to better serve those who are concerned \nwith how their ‘Personally identifiable information’ (PII) is being used\n online. PII, as used in US privacy law and information\n security, is information that can be used on its own or with\n other information to identify, contact, or locate a \nsingle person, or to identify an individual in context",font=('arial 11')).place(x=10,y=30)

        Label(self.imges_frame,text="When ordering or registering on our site, as appropriate,you may be asked to enter \nyour name, email address, mailing address, phone number, credit card information,\n or other details to help you with your experience.",font=('arial 11')).place(x=10,y=160)
       

    def time(self):
        t=strftime('%H:%M:%S %p')
        label=Label(self.login_frame,text=t,font=('arial 10 bold'),bg='black',fg='cyan').place(x=15,y=300)
        

        
    


root=Tk()      

obj=Myapp(root)
#my app start..
obj.home()
obj.time()





###My ap end
root.mainloop()