from cgitb import grey
from tkinter import *
from subprocess import call
from tkinter import messagebox
import psycopg2
from PIL import Image, ImageTk, ImageFilter
import CA_Dashboard as cad

def login():
    conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    uname = e1.get()
    passw = e2.get()

    sql = "select * from ca_login where ca_user_name = %s and ca_pass_word = %s"
    cur.execute(sql,[(uname),(passw)])
    results = cur.fetchall()

    if results:
        messagebox.showinfo("","Login Success")
        cad.CA()
        return True

    else:
        messagebox.showinfo("","Incorrect")
        return False



def LoginPage():

    

    

    root = Tk()
    root.title('Collection Agency Login')
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

  

   
    
    # Open the Image File
    bg = ImageTk.PhotoImage(file="home_bgr.jpg")

    canvas = Canvas(root, width=1000, height=3500)  #700 3500
    canvas.pack(fill=BOTH, expand=True)

    # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg) #, anchor='nw')
    
    def home_p():
        root.destroy()
        import home

    image = Image.open('home.png')
    rs_img = image.resize((40,40))
        
    but_home = ImageTk.PhotoImage(rs_img)
    btn_r=Button(image=but_home,bg="light green",bd=0,cursor="hand2",command= home_p).place(x=10,y=10)

    # Function to resize the window
    def resize_image(e):
        global image, resized, image2
        # open image to resize it
        image = Image.open("home_bgr.jpg")
        # resize the image with width and height of root
        resized = image.resize((width, height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    # Bind the function to configure the parent window
    root.bind("<Configure>", resize_image)

    F_login = Frame(root,bg="seashell2").place(x=600,y=300,height=550,width=700)


    label = Label(F_login, text="LOGIN!", font=("Ravie",35,"bold"),fg="#d77337",bg="seashell2").place(x=670,y=300)
    #label1 = Label(F_login, text="Login Area", font=("Impact",35,"bold"),fg="#d77337",bg="seashell2").place(x=660,y=250)
    
    global e1,e2
    l1=Label(root, text="Username",font=("Ravie", 18,"bold"),bg="seashell2",fg="black").place(x=700,y=400)
    l2=Label(root,text="Password",font=("Ravie", 18,"bold"),bg="seashell2",fg="black").place(x=700,y=500)

    
    e1 = Entry(F_login,font=("Goudy old style",12,"bold"), fg="black", bg="PeachPuff2")
    e1.place(x=700,y=440)

    e2 = Entry(F_login,font=("Goudy old style",12,"bold"), fg="black", bg="PeachPuff2",show='*')
    e2.place(x=700,y=540)

    if len(e2.get()) <= 6:
        warn = "NO"
     

    def my_show():
        if(e2.cget('show')=='*'):
            e2.config(show='')
        else:
            e2.config(show='*')

    c1 = Checkbutton(F_login,text='Show Password',command=my_show).place(x=700,y=580)

    Button(root,text = 'Login',font=("Ravie", 13,"bold"), height = 1, width = 10, bd = '5',fg="white",bg="#d77337",activeforeground = "green",activebackground = "pink",pady = 10, command=login).place(x=700,y=680)

    root.mainloop()

        
#LoginPage()
