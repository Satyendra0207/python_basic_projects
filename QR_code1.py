from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import qrcode
import tkinter 

wn=Tk()
wn.geometry('700x650')
wn.title('QR code generator')
#wn.config(bg='blue')

#adding background image 
icon= Image.open("D:\my python\python code\python-project\images.jpeg")
icon=icon.resize((1400,900),Image.ANTIALIAS)
wn.photo=ImageTk.PhotoImage(icon)
Label(wn,image=wn.photo).place(x=0,y=0)

#Label for the window
headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.10,rely=0.02,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code
Frame1 = Frame(wn,bg="SteelBlue3")
Frame1.place(relx=0.1,rely=0.14,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text/URL: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.05)

text = Entry(Frame1,font=('Century 10'))
text.place(relx=0.05,rely=0.4,relwidth=0.8, relheight=0.15)

#Getting input of the location to save QR Code
Frame2 = Frame(wn,bg="SteelBlue3")
Frame2.place(relx=0.1,rely=0.32,relwidth=0.7,relheight=0.3)

label2 = Label(Frame2,text="Enter the location to save the QR Code: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 10'))
loc.place(relx=0.05,rely=0.4, relwidth=0.8, relheight=0.15)

#Getting input of the QR Code image name
Frame3 = Frame(wn,bg="SteelBlue3")
Frame3.place(relx=0.1,rely=0.49,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 10'))
name.place(relx=0.05,rely=0.4, relwidth=0.8, relheight=0.15)

#Getting the input of the size of the QR Code
Frame4 = Frame(wn,bg="SteelBlue3")
Frame4.place(relx=0.1,rely=0.69,relwidth=0.7,relheight=0.28)

label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)

size = Entry(Frame4,font=('Century 10'))
size.place(relx=0.05,rely=0.4, relwidth=0.8, relheight=0.15)


#Function to generate the QR code and save it
def generateCode():
  def display(location):
    win=tkinter.Toplevel()
    win.geometry('400x400')
    win.title('Generated')
    win.config(bg='light blue')
    #display of image 
    icon_im= Image.open(f"{location}")
    icon_im=icon_im.resize((100,100),Image.ANTIALIAS)
    win.photo=ImageTk.PhotoImage(icon_im)
    Label1=Label(win,text=text.get(),font=('Courier',13,'bold'),fg='red')
    Label1.place(x=30,y=40)
    Label(win,image=win.photo).place(x=300,y=40)
    
                       
  #Creating a QRCode object of the size specified by the user
  qr = qrcode.QRCode(version = size.get(),
            box_size = 10,
            border = 5)
  qr.add_data(text.get()) #Adding the data to be encoded to the QRCode object
  qr.make(fit = True) #Making the entire QR Code space utilized
  img = qr.make_image() #Generating the QR Code
  fileDirec=loc.get()+'\\'+name.get() #Getting the directory where the file has to be save
  img.save(f'{fileDirec}.jpeg') #Saving the QR Code
  location=f'{fileDirec}.jpeg'
  #Showing the pop up message on saving the file
  messagebox.showinfo("QR Code Generator","QR Code is saved successfully!")
  display(location)
  
  
  #Button to generate and save the QR Code
button = Button(Frame4, text='Generate Code',fg='blue',font=('Courier',15,'normal'),command=generateCode)
button1=Button(Frame4,text='Exit',fg='blue',font=('courier',15,'normal'),command=quit)
button.place(relx=0.25,rely=0.7, relwidth=0.25, relheight=0.2)
button1.place(relx=0.53,rely=0.7,relwidth=0.15,relheight=0.2)


#Runs the window till it is closed manually
wn.mainloop()