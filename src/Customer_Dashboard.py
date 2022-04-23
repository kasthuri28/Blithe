import view_status as ca
from tkinter import*
import Logout as ll
import psycopg2
import Booking

def Customer(c_id):  


    def view():
        ca.view_status(c_id)
        
    root=Tk()
    root.title("Welcome")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.configure(bg='light green')
    o=Booking.booking()
    fnt4 = ("Courier", 15,"italic","bold")

    label1=Label(root,text="Welcome!!",font=("Ubuntu",45,"bold"),fg='green',bg='light green').place(x=500.5,y=20.0)

    button1=Button(root,text="Book Now",bg="white",fg="green",font=("Mesquite Std",12,"bold"),command=lambda : [f() for f in [root.destroy,o.book]]).place(x=850,y=350)
    button2=Button(root,text="Log out",bg="white",fg="green",font=("Mesquite Std",12,"bold"),command=lambda : [f() for f in [root.destroy,ll.Logout]]).place(x=860,y=400)
    button3=Button(root,text="Track Booking_Status",bg="white",fg="green",font=("Mesquite Std",12,"bold"),command=view).place(x=800,y=290)

    Frame_welcome=Frame(root,bg="white")
    Frame_welcome.place(x=100,y=200,height=240,width=500)

    label1=Label(Frame_welcome,text="Customer Details",font=("Helvetica",20,"bold"),fg='black',bg='white').place(x=100.5,y=20.0,)
    
    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM customer WHERE CUSTOMER_ID = %s",[c_id])
    res = cur.fetchone()

    #retreiving customer details

    name = 'Name: '+res[2]
    hno = 'House Number: '+res[1]
    #sna = 'Street Name: '+res[3]
    city = 'City:  '+res[3]
    pno = 'Mobile Number: '+res[4]
   
    h2 = Label(Frame_welcome,text=name, font= fnt4, bg='dark olive green',fg='ivory2')
    h2.place(x=root.winfo_screenwidth()//12,y=60)

    h3 = Label(Frame_welcome,text=hno, font= fnt4, bg='dark olive green',fg='ivory2')
    h3.place(x=root.winfo_screenwidth()//12,y=95)

    #h4 = Label(Frame_welcome,text=sna, font= fnt4, bg='dark olive green',fg='ivory2')
    #h4.place(x=root.winfo_screenwidth()//12,y=130)

    h5 = Label(Frame_welcome,text=city, font= fnt4, bg='dark olive green',fg='ivory2')
    h5.place(x=root.winfo_screenwidth()//12,y=165)

    h6 = Label(Frame_welcome,text=pno, font= fnt4, bg='dark olive green',fg='ivory2')
    h6.place(x=root.winfo_screenwidth()//12,y=200)

    root.resizable(True, True)

    root.mainloop()   

