from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter.filedialog import askopenfilename
import calendar
from run_app_classes import *

 
def file():
  filename=askopenfilename()
  print(filename)
  file_obj=Open_File(xronos(),filename)
  file_obj.run_on_time()

def istoselida():
  pass

def minima():
  minima_=input('Δώσε μύνημα : ')
  minima_obj=Open_Message(xronos(),minima_)
  minima_obj.run_on_time()
  
def email():
  pass
   
def xronos():
  str_time=entry1.get()
  time=dt.strptime(str_time,"%Y-%m-%d %H:%M:%S.%f")
  print ('Χρονος εκτέλεσης : {}'.format(time.ctime()))
  return time

def calend():
  a=calendar.TextCalendar()
  calframe=Tk()
    
  calframe.title('Ημερολόγιο '+str(dt.now().year))
  text=Text(calframe)
  text.pack(expand=YES, fill= BOTH, padx=10, pady=10)
  text.insert(0.0,a.formatyear(dt.now().year) )
  text.configure(state='disabled')
  #label=ttk.Label(calframe,text=a.formatyear(dt.now().year))
  #label.pack(expand=YES, fill= BOTH)
  calframe.mainloop()
    
root=Tk()
root.title('Ξεχασιάρης')
mainframe=ttk.Frame(root, borderwidth=5, relief="sunken")
mainframe.pack(expand=YES, fill=BOTH)
label1=ttk.Label(mainframe,text='Aνοίξτε έγγραφα, ιστοσελίδες, δέστε μυνήματα\n\
στείλτε εμαιλ την ώρα που θέλετε',font='12')
label1.grid(row=0,columnspan=3, padx=5, pady=5)
label2=ttk.Label(mainframe,text='Όρισε το χρόνο εκτέλεσης', font='12')
label2.grid(row=1,column=0, columnspan=2, padx=5, pady=5)
entry1=ttk.Entry(mainframe, width=20)
entry1.insert(0,dt.now())
entry1.grid(row=1, column=2)

button5=ttk.Button(mainframe,text='χρόνος', command=xronos)
button5.grid(row=1,column=3, padx=5, pady=5)
button1=ttk.Button(mainframe,text='Επιλογή Αρχείου', command=file)
button1.grid(row=2, padx=5, pady=5)
button2=ttk.Button(mainframe,text='Ιστοσελίδα', command=istoselida)
button2.grid(row=2,column=1, padx=5, pady=5)
button3=ttk.Button(mainframe,text='Μύνημα', command=minima)
button3.grid(row=2,column=2, padx=5, pady=5)
button4=ttk.Button(mainframe,text='email', command=email)
button4.grid(row=2,column=3, padx=5, pady=5)
 
button6=ttk.Button(mainframe,text='Ημερολόγιο', command=calend)
button6.grid(row=3,column=0, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(0, weight=1) 
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
  
root.mainloop()




