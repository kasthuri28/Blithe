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
import sub_req
#import Customer_reg
global vw

class booking:
    

    def book(self):
        #self.B_id=b_id
        #self.B_date=datetime.date.today()
        #self.B_time=datetime.time.strftime()

        self.root=Tk()
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        
        self.root.title("BOOKING")
        #self.root.geometry("500x500+250+100")

        #Background image
        self.bgi =Image.open("bg1.jpg")
        self.bgi_res= self.bgi.resize((2550,1000))
        self.bg=ImageTk.PhotoImage(self.bgi_res)
        bg=Label(image=self.bg).place(x=-100,y=150)

        self.bgi =Image.open("bg1.jpg")
        self.bgi_res= self.bgi.resize((2550,1000))
        self.bg=ImageTk.PhotoImage(self.bgi_res)
        bg=Label(image=self.bg).place(x=-100,y=150)
        #bg.image=self.bg
        #bg.pack()
        self.root.config(bg="white")
      
    
        #home button

        image = Image.open('home.png')
        rs_img = image.resize((40,40))
        
        self.but_home = ImageTk.PhotoImage(rs_img)
        btn_r=Button(image=self.but_home,bg="light green",bd=0,cursor="hand2",command= self.home_p).place(x=10,y=10)


        #1st heading        
        
        h1 = Label(self.root,text = "Book your Collection Agency Here",font=("times new roman",22,"bold"),bg='white',fg="dark olive green")
        h1.pack(pady=50)
        h1.place(x=690,y=40)

        #2nd heading


        h2 = Label(self.root,text = "Choose your criterias",font=("times new roman",22,"bold"),bg='white',fg="dark olive green")
        h2.pack(pady=50)
        h2.place(x=690,y=250)

        

        h3 = Label(text = "Hi",font=("times new roman",22,"bold"),bg='white',fg="dark olive green")
        h3.pack(pady=50)
        h3.place(x=690,y=200)

        #Options menu for waste type and amount
        lw=["Plastic","Biodegradable","Metals","Glasses"]
        self.vw=tkinter.StringVar(self.root)
        self.vw.set("Select waste type")
        
        qw=tkinter.OptionMenu(self.root,self.vw,*lw)
        qw.config(width=50,height=3)
        qw.pack()
        qw.place(x=690,y=350)

        la=["100g","200g","300kg","400kg","500kg","600kg","700kg","800kg","900kg","1Kg"]
        va=tkinter.StringVar(self.root)
        va.set("Select approx amount")

        qw=tkinter.OptionMenu(self.root,va,*la)
        qw.config(width=50,height=3)
        qw.pack()
        qw.place(x=690,y=440)

        #submit button
        submit_button = tkinter.Button(self.root, text='Submit',command=self.printcalist)
        submit_button.pack()
        submit_button.place(x=890,y=520)
        choice= self.vw.get()
        
        

       


        

    
    #printing the collection agency list
    def printcalist(self):
        list={}
       # self.ca_l=[]
        conn = psycopg2.connect(database="Household Waste Management", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        cur = conn.cursor()
       
        self.ch=self.vw.get()
        ch=self.ch
        postgreSQL_select_Query = "select agency_id,agency_name,waste_type,city from collection_agency where waste_type = %s" 
        

        cur.execute(postgreSQL_select_Query,[ch])
        
        l = cur.fetchall()
        print(l)
        '''for row in l:
            self.choice = self.vw.get()
            
            if(self.choice==row[2]):
                list[row[0]]=row[1]
                
              
               
        for i in list:
            self.ca_l.append((i, list[i]))
       # print(self.ca_l)'''
        if len(l)==0:
            
            self.h4 = Label(self.root,text = "Sorry Collection Agencies are not Available",font=("times new roman",22,"bold"),bg='white',fg="dark olive green")
            self.h4.pack(pady=50)
            self.h4.place(x=1300,y=400)
            
        else:
            
            self.frame1 = Frame(self.root,bg='White',width=250,height =500)

            self.frame1.place(x=1200,y=500)
            self.h5 = Label(self.root,text = "Collection Agencies Available",font=("times new roman",22,"bold"),bg='white',fg="dark olive green")
            self.h5.pack(pady=50)
            self.h5.place(x=1300,y=400)
            self.h6=Label(self.root,text = "CA_ID                                   CA_Name",font=("times new roman",16,"bold"),bg='white',fg="dark olive green")
            self.h6.pack(pady=50)
            self.h6.place(x=1300,y=480)
            
           
            for i in range(len(l)):
                for j in range(2):
                    self.e=Entry(self.frame1,width=20,fg='blue',font=('Arial',16,'bold'))
                    self.e.grid(row=i,column=j)
                    self.e.insert(END,l[i][j])
            proceed_button = tkinter.Button(self.root, text='Proceed to Request',command=sub_req.Submit_Request_page)
            proceed_button.pack()
            proceed_button.place(x=1000,y=520)
        return(self.ch)
           
   
        
                
               




    # home button command function
   


    '''     
    # function to the proceed button
    def Submit_Request_page(self):

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
                 self.ca_l[i][0],
                 c_id,
                 status,
                 w_t,
                 w_a,
                 total_amt

                 ))

                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your request is sent",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
       


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
            choice = self.printcalist()
            
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
        back= tkinter.Button(ch, text='Back',command=lambda : [f() for f in [ch.destroy,self.root.destroy,o.book()]])
        back.pack()
        back.place(x=500,y=400)

        



        
    
        
        

    
    # Execute tkinter

        ch.resizable(True, True)
        ch.mainloop()
    '''
    def home_p(self):
        self.root.destroy()
        import home






#function for entry into the booking table

#o.root.mainloop()
