from distutils.cmd import Command
from logging import root
from tkinter import *
import tkinter  
from PIL import Image,ImageTk
import datetime
import psycopg2
import uuid
from tkinter import messagebox
from datetime import datetime
import Booking

def Submit_Request_page():
        ch = Tk()
        ch.title("Submit Request")
  
        ch.configure(bg = 'dark olive green')

        ch.geometry("800x500+250+100")
        fnt = ("Courier",22,"bold")
        fnt1 = ("Ubuntu", 18, "bold","italic")
        fnt2 = ("Ubuntu", 15, "bold","italic")

        frame = Frame(ch,bg='light grey',width=500,height =800)
        frame.pack(side=LEFT)

    # heading
        h1 = Label(frame, text = "Choose the collection agency",font=fnt,bg='light grey',fg="dark olive green")
        h1.pack(pady=50)



        frame.pack_propagate(False)

        list={}
        ca_l=[]
        conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
       

        postgreSQL_select_Query = "select agency_id,agency_name,waste_type,city from collection_agency"

        cur.execute(postgreSQL_select_Query)
        
        l = cur.fetchall()
        #print(l)
        for row in l:
            choice = Booking.booking.printcalist()
            
            if(choice==row[2]):
                list[row[0]]=row[1]
              
               
        for i in list:
            ca_l.append((i, list[i]))
        py=0
        for i in range(len(ca_l)):
                for j in range(2):
                    e=Entry(frame,width=20,fg='blue',font=('Arial',16,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END,ca_l[i][j])
                req_button = tkinter.Button(ch, text='Submit request',command=submit_booking(i))
                req_button.pack()
                req_button.place(x=500,y=230+py)
                py=py+40

def submit_booking(i):
            try:
                
                B_id= "B-" + str(uuid.uuid1())[:6]
                conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
                cur = conn.cursor()
                date= datetime.date(datetime.now())
                time=datetime.time(datetime.now())
                c_id="1"
                status ="pending"
                w_a= 200
                total_amt=700
                w_t="Plastic"

                cur.execute("insert into booking values(%s,%s,%s,%s,%s,%s,%s)",
                (B_id,
                 date,
                 time,
                 Submit_Request_page.ca_l[i][0],
                 c_id,
                 status,
                 w_t,
                 w_a,
                 total_amt

                 ))

                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your request is sent",parent=Submit_Request_page.ch)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=Submit_Request_page.ch.root)
        