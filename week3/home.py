import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk
import gui as ll
from tkinter import *
import os

root = tk.Tk()
root['bg'] = 'blue'
root.title('Household Waste Management System')
root.geometry("1000x700")

canvas = Canvas(root, width = 300, height = 300)  
canvas.pack() 
img=PIL.Image.open('waste_management.jpg') 
img = ImageTk.PhotoImage(img, master=root)  
canvas.create_image(20, 20, anchor=NW, image=img)


tk.Label(root,text='---HOME PAGE---',font='Verdana 15 bold',bg='#673',fg='White').place(relx=.5)
tk.Button(root,text='login',font='Verdana 12 bold',command=ll. LoginPage,bg='#567',fg='White').place(relx=.5, rely=.4)

root.mainloop()