from tkinter import *  
from PIL import ImageTk, Image
import customer_register as cr

def login_():

    ch = Tk()
    ch.title("choice")
    img =Image.open('waste.jpg')
    ch.configure(bg = 'dark olive green')

    ch.geometry("500x500+250+100")
    fnt = ("Courier",22,"bold")
    fnt1 = ("Ubuntu", 18, "bold","italic")
    fnt2 = ("Ubuntu", 15, "bold","italic")

    frame = Frame(ch,bg='light grey',width=250,height =500)
    frame.pack(side=LEFT)

    # heading
    h1 = Label(frame, text = "Household \n Waste \n Management \nSystem",font=fnt,bg='light grey',fg="dark olive green")
    h1.pack(pady=50)

    h2 = Label(frame, text = "Manage Your \nAccounts",font=fnt1, bg='light grey',fg='dark green')
    h2.pack(pady=50)

    frame.pack_propagate(False)

    cus_lbl= Label(ch, text= "Are you a customer?", font= fnt2,bg='dark olive green')
    cus_lbl.place(x=260,y=100)

    cusButton = Button(ch, text="Customer Login",font=fnt2,bg='gray1',fg='snow')
    cusButton.place(x=300, y=140)

    ca_lbl= Label(ch, text= "Are you a collection \nagent?", font= fnt2,bg='dark olive green')
    ca_lbl.place(x=260,y=230)

    caButton = Button(ch, text="CA Login",font=fnt2,bg='gray1',fg='snow')
    caButton.place(x=320, y=290)

    # Execute tkinter

    ch.resizable(True, True)
    ch.mainloop()

def register_():

    ch = Tk()
    ch.title("choice")
    img =Image.open('waste.jpg')
    ch.configure(bg = 'dark olive green')

    ch.geometry("500x500+250+100")

    fnt = ("Courier",22,"bold")
    fnt1 = ("Ubuntu", 18, "bold","italic")
    fnt2 = ("Ubuntu", 15, "bold","italic")

    frame = Frame(ch,bg='light grey',width=250,height =500)
    frame.pack(side=LEFT)

    # heading
    h1 = Label(frame, text = "Household \n Waste \n Management \nSystem",font=fnt,bg='light grey',fg="dark olive green")
    h1.pack(pady=50)

    h2 = Label(frame, text = "Manage Your \nAccounts",font=fnt1, bg='light grey',fg='dark green')
    h2.pack(pady=50)

    frame.pack_propagate(False)

    cus_lbl= Label(ch, text= "Are you a customer?", font= fnt2,bg='dark olive green')
    cus_lbl.place(x=260,y=100)

    cusButton = Button(ch, text="Customer Register",font=fnt2,bg='gray1',fg='snow',command=cr.register)
    cusButton.place(x=290, y=140)

    ca_lbl= Label(ch, text= "Are you a collection \nagent?", font= fnt2,bg='dark olive green')
    ca_lbl.place(x=260,y=230)

    caButton = Button(ch, text="CA Register",font=fnt2,bg='gray1',fg='snow')
    caButton.place(x=320, y=290)

    # Execute tkinter

    ch.resizable(True, True)
    ch.mainloop()


root = Tk()
root.configure(bg = 'cyan4')
root.title('waste management system')
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')

#font
fnt = ("Ubuntu", 35, "bold")
fnt1 = ("Ubuntu", 18, "bold")
fnt2 = ("Ubuntu", 18,"italic")
fnt3 = ("Ubuntu", 16,"bold","underline","italic")
fnt4 = ("Courier", 24,"italic","bold")

#frame
top_frame = Frame(root,bg='light grey',width= root.winfo_screenwidth(),height = 55)
top_frame.pack(side=TOP)

#home icon
image = Image.open('home.jpg')
rs_img = image.resize((40,40))
display = ImageTk.PhotoImage(rs_img)

img_label = Label(top_frame, image=display)
img_label.pack(side = LEFT,padx=10)

top_frame.pack_propagate(False)

#heading in menubar
h2 = Label(top_frame,text='HOME', font= fnt1,bg ='light grey', fg='GRAY1').pack(side=LEFT,padx=10) 

#heading
h1 = Label(root,text='Household Waste Management System', font= fnt, bg='cyan4',fg='gray1')
h1.pack(pady=20)

#image 
canvas = Canvas(root, width = 295, height = 315)  
canvas.pack(side = LEFT,padx=150,pady=10)
ig = Image.open("waste_throw.jpg") 
ig = ig.resize((295,315))
img = ImageTk.PhotoImage(ig)  
canvas.create_image(0, 0, anchor=NW, image=img) 

#quote
h2 = Label(root,text="Reuse The Past, Recycle The Present, \nSave The Future", font= fnt4, bg='cyan4',fg='ivory2')
h2.place(x=550,y=270)

#Button
login_lbl= Label(root, text= "Already a user?", font= fnt3,bg='cyan4')
login_lbl.place(x=615,y=395)

lc = Image.open('lock.png')
lc = lc.resize((30,30))
lck = ImageTk.PhotoImage(lc) 

loginButton = Button(root, text="Login",image=lck,compound="left",bg='gray1',fg='snow',font=fnt1,command=login_)
loginButton.place(x=800, y=385)

rg_lbl= Label(root, text= "New User?", font= fnt3,bg='cyan4')
rg_lbl.place(x=670,y=480)

RegisterButton = Button(root, text="Register",bg='gray1',fg='snow',font=fnt1,command=register_)
RegisterButton.place(x=800, y=470)

root.resizable(True, True)
root.mainloop()
