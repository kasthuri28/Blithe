import Customer_Dashboard as cs
import tkinter as tk 
from tkinter import*
from tkinter import messagebox

import psycopg2

def make_bill(c_id,ca_id):

    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM customer WHERE CUSTOMER_ID = %s",[c_id])
    res = cur.fetchone()

    cur.execute("SELECT * FROM collection_agency WHERE agency_id = %s",[ca_id])
    res1 = cur.fetchone()

    cur.execute("SELECT * FROM booking WHERE c_id = %s and agency_id = %s",(c_id,ca_id))
    res2 = cur.fetchone()

    root = Tk()
    root.configure(bg = 'dark olive green')
    root.title('waste management system')
    root.geometry(f'{root.winfo_screenwidth()-200}x{root.winfo_screenheight()-200}')

    #font
    fnt = ("Ubuntu", 35, "bold","underline","italic")
    fnt4 = ("Courier", 20,"italic","bold")

    #heading
    h1 = Label(root,text='BILL',font= fnt, bg='ivory2',fg='gray1',width=7)
    h1.pack(pady=20)

    #quote
    #retreiving customer name from customer table

    name = 'Name: '+res[2]
    hno = 'House Number: '+res[1]
    #sna = 'Street Name: '+res[3]
    city = 'City:  '+res[3]
    pno = 'Mobile Number: '+res[4]
    cna = 'Collection Agency Name: '+res1[1]
    wt = 'Type of Waste: '+res2[4]
    pr = res1[5]
    
    #print(pr,res2[7],res1[6])
    total_amt = (200//100)*pr + res1[6]
    ta = 'Total Amount: '+str(total_amt)

    cur.execute("update booking set total_amt = %s where c_id = %s and agency_id = %s",(total_amt,c_id,ca_id))
    conn.commit()

    h2 = Label(root,text=name, font= fnt4, bg='dark olive green',fg='ivory2')
    h2.place(x=root.winfo_screenwidth()//7,y=170)

    h3 = Label(root,text=hno, font= fnt4, bg='dark olive green',fg='ivory2')
    h3.place(x=root.winfo_screenwidth()//7,y=210)

   # h4 = Label(root,text="times new roman", font= fnt4, bg='dark olive green',fg='ivory2')
   # h4.place(x=root.winfo_screenwidth()//7,y=250)

    h5 = Label(root,text=city, font= fnt4, bg='dark olive green',fg='ivory2')
    h5.place(x=root.winfo_screenwidth()//7,y=290)

    h6 = Label(root,text=pno, font= fnt4, bg='dark olive green',fg='ivory2')
    h6.place(x=root.winfo_screenwidth()//7,y=330)

    h7 = Label(root,text=cna, font= fnt4, bg='dark olive green',fg='ivory2')
    h7.place(x=root.winfo_screenwidth()//7,y=370)

    h8 = Label(root,text=wt, font= fnt4, bg='dark olive green',fg='ivory2')
    h8.place(x=root.winfo_screenwidth()//7,y=410)

    h9 = Label(root,text=ta, font= fnt4, bg='dark olive green',fg='ivory2')
    h9.place(x=root.winfo_screenwidth()//7,y=450)
  
    root.resizable(True, True)
    root.mainloop()

make_bill("1","CA-b600c0")
