import customer as cs
import tkinter as tk
import psycopg2 
from tkinter import*
from tkinter import messagebox
from subprocess import call

def login():
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    uname = e1.get()
    passw = e2.get()

    sql = "select * from login where username = %s and password = %s"
    cur.execute(sql,[(uname),(passw)])
    results = cur.fetchall()

    if results:
        messagebox.showinfo("","Login Success")
        return True
    
    else:
        messagebox.showinfo("","Incorrect")
        return False


def LoginPage():



    root = tk.Tk()
    root.title('Login')
    root.geometry('300x200')
    global e1,e2

    

    tk.Label(root, text="Username",background="#34A2FE").place(x=10,y=10)
    tk.Label(root,text="Password",background="#34A2FE").place(x=10,y=40)

    e1 = Entry(root)
    e1.place(x=140,y=10)

    e2 = Entry(root)
    e2.place(x=140,y=40)
    e2.config(show='*')

    Button(root,text = 'Login',command = login,height = 3, width = 13,).place(x=10,y=100)
    

    uname = e1.get()
    passw = e2.get()

    root.mainloop()

LoginPage()