from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import calendar
from run_app_classes import *

class Jaxasiaris(ttk.Frame):
  def __init__(self, parent=None,**kwargs):
    super().__init__(parent,**kwargs)
    self.config(borderwidth=5)
    self.pack(expand=YES, fill=BOTH)
    #parent.columnconfigure(0, weight=1)
    #parent.rowconfigure(0, weight=1)
    self.add_children()
    self.configure_layout()
    
  def add_children(self):
    label1=ttk.Label(self,text='Aνοίξτε έγγραφα, ιστοσελίδες, δέστε μυνήματα\n\
στείλτε εμαιλ την ώρα που θέλετε',font='12')
    label1.grid(row=0,columnspan=3, padx=5, pady=5)
    label2=ttk.Label(self,text='Όρισε το χρόνο εκτέλεσης', font='12')
    label2.grid(row=1,column=0, columnspan=2, padx=5, pady=5)
    self.entry1=ttk.Entry(self, width=30,font=('12'))
    self.entry1.insert(0,dt.now())
    self.entry1.grid(row=1, column=2,columnspan=2)
    #button5=ttk.Button(self,text='χρόνος', command=self.xronos)
    #button5.grid(row=1,column=3, padx=5, pady=5)
    button1=ttk.Button(self,text='Επιλογή Αρχείου', command=self.file)
    button1.grid(row=2, padx=5, pady=5)
    button2=ttk.Button(self,text='Ιστοσελίδα', command=self.istoselida)
    button2.grid(row=2,column=1, padx=5, pady=5)
    button3=ttk.Button(self,text='Μύνημα', command=self.minima)
    button3.grid(row=2,column=2, padx=5, pady=5)
    button4=ttk.Button(self,text='email', command=self.email)
    button4.grid(row=2,column=3, padx=5, pady=5)
    button6=ttk.Button(self,text='Ημερολόγιο', command=self.calend)
    button6.grid(row=3,column=0, padx=5, pady=5)

  def configure_layout(self):
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)
    self.rowconfigure(0, weight=1) 
    self.rowconfigure(1, weight=1)
    self.rowconfigure(2, weight=1)
    self.columnconfigure(3, weight=1)

  def file(self):
    filename=askopenfilename()
    file_obj=Open_File(self.xronos(),filename)
    file_obj.run_on_time()

  def istoselida(self):
    pass

  def minima(self):
    self.minima_window()
    
  def read_entry_minima(self):
    minima_obj=Open_Message(self.xronos(),self.entry2.get())
    minima_obj.run_on_time()
  
  def minima_window(self):
    top=Toplevel()
    top.title('Δώσε Μύνημα')
    self.entry2=Entry(top, width=40, font=('12'))
    self.entry2.pack()
    button=Button(top, text='ok',command=self.read_entry_minima)
    button.pack()
  
  def email(self):
    pass
   
  def xronos(self):
    str_time=self.entry1.get()
    time=dt.strptime(str_time,"%Y-%m-%d %H:%M:%S.%f")
    return time

  def calend(self):
    a=calendar.TextCalendar()
    b=Toplevel()
    b.title('Ημερολόγιο '+str(dt.now().year))
    text=Text(b)
    text.pack(expand=YES, fill= BOTH, padx=10, pady=10)
    text.insert(0.0,a.formatyear(dt.now().year) )
    text.configure(state='disabled')
 
if __name__=='__main__':    
  Jaxasiaris().mainloop()

