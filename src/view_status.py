import tkinter as tk 
from tkinter import*
import psycopg2
from  tkinter import ttk

def view(c_id,ca_id):
    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM customer WHERE customer_id = %s",[c_id])
    res = cur.fetchone()

    cur.execute("SELECT * FROM collection_agency WHERE agency_id = %s",[ca_id])
    res1 = cur.fetchone()

    cur.execute("SELECT * FROM booking WHERE c_id = %s and agency_id = %s",(c_id,ca_id))
    res2 = cur.fetchone()

    root = Tk()
    root.configure(bg = 'sky blue')
    root.title('view bill')
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
   # sna = 'Street Name: '+res[3]
    city = 'City:  '+res[3]
    pno = 'Mobile Number: '+res[4]
    cna = 'Collection Agency Name: '+res1[1]
    wt = 'Type of Waste: '+res2[4]
    total_amt = res2[8]
    ta = 'Total Amount: '+str(total_amt)


    

    h2 = Label(root,text=name, font= fnt4, bg='green',fg='ivory2')
    h2.place(x=root.winfo_screenwidth()//7,y=170)

    h3 = Label(root,text=hno, font= fnt4, bg='green',fg='ivory2')
    h3.place(x=root.winfo_screenwidth()//7,y=210)

   # h4 = Label(root,text=sna, font= fnt4, bg='green',fg='ivory2')
    #h4.place(x=root.winfo_screenwidth()//7,y=250)

    h5 = Label(root,text=city, font= fnt4, bg='green',fg='ivory2')
    h5.place(x=root.winfo_screenwidth()//7,y=290)

    h6 = Label(root,text=pno, font= fnt4, bg='green',fg='ivory2')
    h6.place(x=root.winfo_screenwidth()//7,y=330)

    h7 = Label(root,text=cna, font= fnt4, bg='green',fg='ivory2')
    h7.place(x=root.winfo_screenwidth()//7,y=370)

    h8 = Label(root,text=wt, font= fnt4, bg='green',fg='ivory2')
    h8.place(x=root.winfo_screenwidth()//7,y=410)

    h9 = Label(root,text=ta, font= fnt4, bg='green',fg='ivory2')
    h9.place(x=root.winfo_screenwidth()//7,y=450)
  
    root.resizable(True, True)
    root.mainloop()

def view_status(c_id):

    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM booking WHERE c_id = %s and status = %s",(c_id,"In Progress"))
    res = cur.fetchall()


    root = Tk()
    root.configure(bg = 'light blue')
    root.title('waste management system')
    root.geometry(f'{root.winfo_screenwidth()-200}x{root.winfo_screenheight()-200}')


    tb = Frame(root)
    tb.pack()

    tree = ttk.Treeview(tb, height= len(res))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Ravie', 20),background="white")
    style.configure("Treeview", background="white", foreground="black",font=('Ravie', 17),rowheight=50, fieldbackground="ivory2")

    tb.place(x = root.winfo_screenwidth()//7, y =150)

    tree['columns']=("Collection Agency ID", "Status")
    tree.column("# 1", anchor=CENTER,width=300)
    tree.heading("# 1", text="Collection_Agency_Id")
    tree.column("# 2", anchor=CENTER,width=300)
    tree.heading("# 2", text="Status")
    
    def viewing():
        x=tree.selection()
        values = tree.item(x,'values')
        view(c_id,values[0])

    remove_many=Button(root,text = 'View Bill',font=("Ravie", 13,"bold"), bd = '5',fg="white",bg="#d77337", height = 1, width = 10, command=viewing).place(x=root.winfo_screenwidth()//2,y=425)

    # Insert the data in Treeview widget
    for i in range(len(res)):
        tree.insert( '', 'end', text=i+1,values=(res[i][3],res[i][5]))

    for i in range(len(res)):
        pass
    tree.pack()
    root.resizable(True, True)
    root.mainloop()

#view_status('1')
