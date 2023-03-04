from tkinter import *
from tkinter import ttk


root=Tk()
root.config(bg="#D1D0CE")


def convert():      #convertion will take place through Indian Rupee being intermediate b/w two

    
    val=(1/float(options[str(clicked.get())]))*fvalue.get()*float(options[str(toclicked.get())])
    out=Label(root, text=str(round(val,2)), height=1, width=18, bg="white", relief="sunken",).place(x=312, y=125)
    
    


#Main window
root.title("            Currency Converter")
root.maxsize(500,270)
root.minsize(500,270)

#heading
hl=Label(root, text = 'CURRENCY CONVERTER',
         fg = 'white', bg = '#306EFF', borderwidth = 7, padx=10)
hl.config(font = ('Courier',15,'bold'))
hl.pack(fill="x")


#from to
fr=Label(root, text = 'From       ⟶        To', pady= 10, bg="#D1D0CE")
fr.config(font = ('Courier',15,))
fr.pack(fill="x")


file=open('CurrencyData.txt','r')
f=file.readlines()          #list containing tuple


options= {}

k,v=list(),list()
for line in f:
	parsed = line.split("\t")
	
	p=parsed[1].split("\n")
	
	options[parsed[0]] = p[0]  
	
	k.append(parsed[0])  
	v.append(p[0])       
	
	



#print(v)

#FROM
clicked=StringVar()
clicked.set("Indian Rupee")
drop=ttk.Combobox(root,textvariable=clicked, values=k).place(x=65, y=90)



#TO
             
toclicked=StringVar()
toclicked.set("US Dollar")
todrop=ttk.Combobox(root,textvariable=toclicked, values=k).place(x=305, y=90)


#Entry box
fvalue=IntVar()
fvalue.set('0')
box=Entry(root, textvariable=fvalue, justify='center', highlightthickness='2',
          highlightbackground = "#306EFF", highlightcolor="#306EFF").place(x=72, y=125)


#output label
out=Label(root, text=" ", height=1, width=18, bg="white",relief="sunken").place(x=312, y=125)


#convert button
bt=Button(root, text="Convert", bg="#306EFF", fg="white", width="20", height='1',
          command=convert).place(x=182, y=180)




root.mainloop()
