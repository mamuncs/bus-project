from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from tkinter import messagebox
import mysql.connector
import datetime





root=Tk()

class myclass(Tk):
    def __init__(self):
        self.root=root
        self.root.title("MMS Bus Servic Ticket Information")
        self.root.geometry("400x500+740+120")
        Label(self.root,text="MMS Bus Service Ticket",font=('arial 12 bold')).place(x=110,y=20)

    
    def tic(self):
        f=open("password.txt","r")
        mail=f.read()
        mydb=mysql.connector.connect(host='localhost',user='mamun',password='mamun1234',database='info')
        mycursor=mydb.cursor()
        q="select * from ticketinfo where email=%s"
        val=(mail,)
        mycursor.execute(q,val)
        result=mycursor.fetchone()
        #print(result)
        Label(self.root,font=("arial 10 bold"),text="Name : "+str(result[1])+" "+str(result[2])).place(x=20,y=60)
        Label(self.root,font=("arial 10 bold"),text="Phone number : "+str(result[3])).place(x=20,y=90)
        Label(self.root,font=("arial 10 bold"),text="Email : "+str(result[4])).place(x=20,y=120)
        Label(self.root,font=("arial 10 bold"),text="Gender : "+str(result[5])).place(x=20,y=150)
        Label(self.root,font=("arial 10 bold"),text="Start Journey : "+str(result[6])).place(x=20,y=180)
        Label(self.root,font=("arial 10 bold"),text="End journey:  "+str(result[7])).place(x=20,y=210)
        Label(self.root,font=("arial 10 bold"),text="Busname : "+str(result[8])).place(x=20,y=240)
        Label(self.root,font=("arial 10 bold"),text="Distance : "+str(result[9])).place(x=20,y=270)
        Label(self.root,font=("arial 10 bold"),text="Cost : "+str(result[10])).place(x=20,y=300)
        Label(self.root,font=("arial 10 bold"),text="Duration Time:  "+str(result[11])).place(x=20,y=330)
        Label(self.root,font=("arial 10 bold"),text="Ticket Day :  "+str(result[14])).place(x=20,y=360)
        Label(self.root,font=("arial 10 bold"),text="Status : "+str(result[12])).place(x=20,y=390)
        Label(self.root,font=("arial 10 bold"),text="Booking Day-Time : "+str(result[13])).place(x=20,y=420)
        Button(self.root,text="Print",font=('arial 9 bold'),bg='green',fg='white',command=self.download).place(x=150,y=460)
        self.fname=result[1]
        self.lname=result[2]
        self.phone=result[3]
        self.email=result[4]
        self.gender=result[5]
        self.start=result[6]
        self.end=result[7]
        self.busname=result[8]
        self.distance=result[9]
        self.cost=result[10]
        self.duration=result[11]
        self.ticday=result[14]
        self.status=result[12]
        self.bookingtime=result[13]
    

    def download(self):
        file=open("ticket/"+self.email+".txt","w")
        file.write("MMS Bus Ticket\n")
        file.write("______________\n")
        file.write("\nName: "+self.fname+" "+self.lname)
        file.write("\nPhone number: "+self.phone)
        file.write("\nEmail: "+self.email)
        file.write("\nGender: "+self.gender)
        file.write("\nStart journey: "+self.start)
        file.write("\nEnd journey: "+self.end)
        file.write("\nBusname: "+self.busname)
        file.write("\nDistance: "+self.distance)
        file.write("\nCost: "+self.cost)
        file.write("\nDuration time: "+self.duration)
        file.write("\nTicket day: "+self.ticday)
        file.write("\nstatus: "+self.status)
        file.write("\nBooking day: "+str(self.bookingtime))
        file.close()
        messagebox.showinfo("Successful","Your ticket is printed in txt file on your drive")






ob=myclass()
ob.tic()



root.mainloop()

