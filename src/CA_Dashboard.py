from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import psycopg2
from tkinter import messagebox
#import view_prog as vvp
#import home as h
#import view_hist as vvh

def CA():
    root = Tk()
    root.title('Collection Agency Dashboard')
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    def login():
        name="pending"
        sql = "select C_Id , Status from Booking where Status=%s"
        cur.execute(sql,([name]))
        results = cur.fetchall()

        return results

        #return results
    # Open the Image File
    '''
    bg = ImageTk.PhotoImage(file="waste.jpg")
    canvas = Canvas(root, width=700, height=3500)  #700 3500
    canvas.pack(fill=BOTH, expand=True)

        # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg) #, anchor='nw')
    '''

        # Function to resize the window
    def resize_image(e):
        global image, resized, image2
                # open image to resize it
        image = Image.open("waste.jpg")
                # resize the image with width and height of root
        resized = image.resize((width, height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

        # Bind the function to configure the parent window
    root.bind("<Configure>", resize_image)

    tb = Frame(root)

    tb.pack()

    image = Image.open('home.jpg')
    rs_img = image.resize((40,40))
            
    but_home = ImageTk.PhotoImage(rs_img)
    btn_r=Button(image=but_home,bg="light green",bd=0,cursor="hand2").place(x=10,y=10)

    lbl=Label(root, text="Welcome",font=("Times new roman",35,"bold"),fg="#d77334",bg="White").place(x=500, y=70)

    Button(root,text = 'View Pending',font=("Ravie", 13,"bold"), height = 1, width = 15, bd = '5',fg="white",bg="#d77337",pady = 10).place(x=60,y=140)

    Button(root,text = 'View Completed',font=("Ravie", 13,"bold"), height = 1, width = 15, bd = '5',fg="white",bg="#d77337",pady = 10).place(x=60,y=270)

    res=login()
    

    tree = ttk.Treeview(tb, height= len(res))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Ravie', 20),background="white")
    style.configure("Treeview", background="white", foreground="black",font=('Ravie', 17),rowheight=50, fieldbackground="silver")

    tb.place(x = 450, y = 370)
    tree['columns']=("Customer_Id", "Status")
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Customer_Id")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Status")
    but=Button(root,text = 'Login')

    

    def rem_many():
        x=tree.selection()
        values = tree.item(x,'values')
        
        print(values)
        for i in x:
            try:

                name= values[0]
                print(name)
                stat="In Progress"
                sql = "update booking SET status=%s where c_id=%s"
                cur.execute(sql,(stat,name))
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
           
            tree.delete(i)
        

    remove_many=Button(root,text = 'Accept',font=("Ravie", 13,"bold"), bd = '5',fg="white",bg="#d77337", height = 1, width = 10, command=lambda : [f() for f in [rem_many]]).place(x=700,y=780)


    # Insert the data in Treeview widget
    for i in range(len(res)):
        tree.insert( '', 'end', text=i+1,values=(res[i][0],res[i][1]))

    for i in range(len(res)):
        pass
    tree.pack()

    def Compute():
        try:
      
            name= values[0]
            print(name)
            stat="In Progress"
            sql = "update booking SET status=%s where c_id=%s"
            #cur.execute(sql,(stat,name))
            cur.execute("select * from booking where c_id=%s",(name))
            
            results = cur.fetchall()
            print(results)


        
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    root.mainloop()
#CA()