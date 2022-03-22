# importing whole module 
from tkinter import *
from tkinter import messagebox
from turtle import left
from PIL import Image,ImageTk
# importing strftime function to
from time import strftime

from matplotlib.pyplot import text

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# This function is used to
# display time on the label
def time():
	string = strftime('%H:%M:%S %p \n %x \n %A')
	lbl.config(text = string)
	lbl.after(1000, time)

# creating tkinter window
root = Tk()
root.title('Digital Clock')
root.geometry('350x200')

# Styling the label widget so that clock
# will look more attractive
icon=Image.open(r"D:\my python\python code\python-project\toughtimesquotes.jpeg")
icon=icon.resize((1400,900),Image.ANTIALIAS)
img=ImageTk.PhotoImage(icon)
Label(root,image=img).place(x=0,y=0)

lbl = Label(root,font = ('calibri', 35, 'bold'),background='#A1C0D5',foreground = 'red',relief='flat')
#root.wm_attributes("-transparentcolor", 'grey')

#adding another image
icon1=Image.open(r"D:\my python\python code\python-project\smile-quotes-1518106970.jpg")
icon1=icon1.resize((460,635),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(icon1)
label1=Label(root,image=img1)
label1.place(x=8,y=10)

# Placing clock at the centre
# of the tkinter window
lbl.place(x=900,y=40,bordermode='ignore')
time()

frame = Frame(root,bg='#A1C0D5')
frame.place(x=900,y=280)
Label(root,text="Today's Event ",font=("times",20,'bold'),bg="#E87E77",fg='yellow').place(x=900,y=240)

lb = Listbox(frame,width=25,height=8,font=('Times', 18),bd=0,bg='#70EC7A',fg='#464646',highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT,fill=BOTH)

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
Label(root,text="Add New task:",bg='#C7E0E8',fg='red',font=('courier',14,'bold')).place(x=900,y=530)
my_entry = Entry(root,font=('times', 17),bg='#EED6D4')
my_entry.place(x=900,y=550)

frame1 = Frame(root)
frame1.place(x=400,y=100)

# creating button
#button = Button(frame1, text='Generate Code',fg='blue',font=('Courier',15,'normal'),command=newTask)

button = Button(root, text='Add Task',bg='#A1C0D5',fg='blue',font=('Courier',15,'bold'),command=newTask)
button1=Button(root,text='Delete Task',bg='#A1C0D5',fg='blue',font=('courier',15,'bold'),command=deleteTask)
button.place(x=900,y=600)
button1.place(x=1020,y=600)

mainloop()
