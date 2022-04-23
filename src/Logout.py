from tkinter import*


def Logout():
    root1=Tk()
    root1.title("LogOut")
    root1.geometry("400x300")
    root1.configure(bg='light blue')
    label2=Label(root1,text="Logout Successful",font=("Nueva Std Cond",15,"bold"),fg='green',bg='light blue').place(x=100.5,y=120.0)
    root1.after(2000, lambda: root1.destroy())
    root1.mainloop()