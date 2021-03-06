from os import scandir
from tkinter import *
from tkinter import messagebox
from tkinter.tix import Balloon
from turtle import width
from PIL import Image,ImageTk
import psycopg2
import uuid



class CA_reg:
    def ca_reg(self):
        sc=Tk()
        self.sc=sc
        self.sc.title("Register Here")
        self.sc.geometry("2550x1000")
        self.bgi =Image.open("bg1.jpg")
        self.bgi_res= self.bgi.resize((2550,1000))
        self.bg=ImageTk.PhotoImage(self.bgi_res)
        bg=Label(image=self.bg).place(x=-100,y=150)
        #bg.image=self.bg
        #bg.pack()
        self.sc.config(bg="white")

        self.bgr=ImageTk.PhotoImage(file="bgr.png")
        bgr=Label(self.sc,image=self.bgr).place(x=200,y=80,height=400)

        frame1=Frame(self.sc,bg="light green")
        frame1.place(x=680,y=80,width=1000,height=400)

        h1 = Label(text = "Collection Agency Registration",font=("times new roman",15,"bold"),bg='light grey',fg="dark olive green")
        h1.pack(pady=50)
        h1.place(x=810,y=40)


        image = Image.open('home.png')
        rs_img = image.resize((40,40))
        
        self.but_home = ImageTk.PhotoImage(rs_img)
        btn_r=Button(image=self.but_home,bg="light green",bd=0,cursor="hand2",command= self.home_p).place(x=10,y=10)


        
        f_name= Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=50,y=10)
        self.f_name_e =Entry(frame1,font=("times new roman",15))
        self.f_name_e.place(x=50,y=50)
      
        l_name= Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=350,y=10)
        self.l_name_e =Entry(frame1,font=("times new roman",15))
        self.l_name_e.place(x=350,y=50)

        city= Label(frame1,text="City",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=50,y=100)
        self.city_e =Entry(frame1,font=("times new roman",15))
        self.city_e.place(x=50,y=140)
      
        
        user_id= Label(frame1,text="User_Id",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=350,y=100)
        self.user_id_e =Entry(frame1,font=("times new roman",15))
        self.user_id_e.place(x=350,y=140)

        ph_no= Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=50,y=200)
        self.ph_no_e =Entry(frame1,font=("times new roman",15))
        self.ph_no_e.place(x=50,y=240)
      
    

        W_type= Label(frame1,text="Waste Type",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=350,y=200)
        self.W_type_e =Entry(frame1,font=("times new roman",15))
        self.W_type_e.place(x=350,y=240)


        

        psw= Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=50,y=300)
        self.psw_e =Entry(frame1,font=("times new roman",15),show="*")
        self.psw_e.place(x=50,y=340)

        v1=IntVar(value=0)

        def showp():
            if(v1.get()==1):
                self.psw_e.config(show="")
            else:
                self.psw_e.config(show="*")

        cp=Checkbutton(self.sc,text="Show Password",variable=v1,onvalue=1,offvalue=0,command=showp)
        cp.place(x=750,y=460)
      
        con_psw= Label(frame1,text="Conform Password",font=("times new roman",15,"bold"),bg="light green",fg="gray").place(x=350,y=300)
        self.con_psw_e =Entry(frame1,font=("times new roman",15))
        self.con_psw_e.place(x=350,y=340)

        self.but_regimg = ImageTk.PhotoImage(file="reg_btn.png")
        btn_r=Button(frame1,image=self.but_regimg,bg="light green",bd=0,cursor="hand2",command= self.register_ca).place(x=700,y=310)

        btn_L=Button(self.sc,text="Sign In",font=("times new roman",20),bd=0,bg="light green").place(x=1000,y=500,width=180)
        
        t1= Label(self.sc,text="Already Registered ? ",bd=0,fg="black",borderwidth=0,highlightthickness=0,font=("times new roman",15,"bold")).place(x=800,y=520)

    def home_p(self):
        self.sc.destroy()
        import home

   
        
    def register_ca(self):
        Sym=['@','#','$','%','&','*','!']
        if self.f_name_e.get() == "" or self.l_name_e.get() == "" or self.city_e.get() == "" or self.user_id_e.get() == "" or self.ph_no_e.get() =="" or self.W_type_e.get()=="" or self.psw_e.get() =="" or self.con_psw_e.get() =="" :
            messagebox.showerror("Error","All fields are required", parent=self.sc)
            print(self.f_name_e.get(),self.l_name_e.get(),self.city_e.get(),self.user_id_e.get() ,self.ph_no_e.get() ,self.W_type_e.get(),self.psw_e.get() ,self.con_psw_e.get() )
        elif len(self.psw_e.get())<4:
            messagebox.showerror("Error","Length of Password must be more than 5")
        elif not any(c.isdigit()for c in self.psw_e.get()):
            messagebox.showerror("Error","Atleast one numeral required",parent=self.sc)
        elif not any(c.isupper()for c in self.psw_e.get()):
            messagebox.showerror("Error","Atleast one uppercase letter required",parent=self.sc)
        elif not any(c.islower()for c in self.psw_e.get()):
            messagebox.showerror("Error","Atleast one lowercase letter required",parent=self.sc)
        elif not any(c in Sym for c in self.psw_e.get()):
            messagebox.showerror("Error","Atleast one special character required",parent=self.sc)
        elif self.psw_e.get()!= self.con_psw_e.get():
            messagebox.showerror("Error","Both Passwords must be same",parent=self.sc)
        else:
            try:
                
                ca_id= "CA-" + str(uuid.uuid1())[:6]
                conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
                cur = conn.cursor()
                cur.execute("insert into collection_agency values(%s,%s,%s,%s,%s)",
                (ca_id,
                 
                 self.f_name_e.get() + " " + self.l_name_e.get(),
                 self.city_e.get(),
                 self.ph_no_e.get(),
                 self.W_type_e.get()
                )
                )

                cur.execute("insert into ca_login values (%s,%s,%s)",
                (ca_id,
                 self.user_id_e.get(),
                 self.psw_e.get()

                ))
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Success","Your registration is completed",parent=self.sc)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.sc)


            
            

#o1=CA_reg(sc)
#sc.mainloop()





