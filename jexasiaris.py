from datetime import datetime as dt
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import calendar
from jexasiaris_classes import *


class Jexasiaris(ttk.Frame):
  def __init__(self, parent=None,**kwargs):
    super().__init__(parent,**kwargs)
    self.config(borderwidth=5)
    self.pack(expand=YES, fill=BOTH)
    self.add_children()
    self.configure_layout()
    
  def add_children(self):
    s=ttk.Style()
    #s.theme_use('clam')
    s.configure('mm.TButton',font=(12), padding=3)
    label1=ttk.Label(self,text='Aνοίξτε έγγραφα, ιστοσελίδες, δέστε μυνήματα\n\
στείλτε εμαιλ την ώρα που θέλετε',font='12')
    label1.grid(row=0,columnspan=4, padx=5, pady=5)
    label2=ttk.Label(self,text='Όρισε το χρόνο εκτέλεσης', font='12')
    label2.grid(row=1,column=0, columnspan=2, padx=5, pady=5)
    self.entry1=ttk.Entry(self, width=30,font=('12'))
    self.entry1.insert(0,dt.now())
    self.entry1.grid(row=1, column=2,columnspan=2)
    buttons_frame=ttk.Frame(self)
    buttons_frame.grid(row=2,column=0, columnspan=4)
    button1=ttk.Button(buttons_frame,text='Επιλογή Αρχείου', style='mm.TButton', command=self.file)
    button1.grid(row=2, column=0)
    button2=ttk.Button(buttons_frame,text='Ιστοσελίδα', command=self.open_web_modal,style='mm.TButton' )
    button2.grid(row=2,column=1)
    button3=ttk.Button(buttons_frame,text='Μύνημα', command=self.minima_window, style='mm.TButton')
    button3.grid(row=2,column=2)
    button4=ttk.Button(buttons_frame,text='email', command=self.mail_widget, style='mm.TButton')
    button4.grid(row=2,column=3)
    button6=ttk.Button(buttons_frame,text='Ημερολόγιο', command=self.calend, style='mm.TButton')
    button6.grid(row=3,column=0)
  
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
    selida=self.entry3.get()
    istoselida_obj=Open_Web(self.xronos(),selida)
    self.win_web.destroy()
    istoselida_obj.run_on_time()
  
  def open_web_modal(self):
    self.win_web = Toplevel() # make a new window
    label=Label(self.win_web, text='Δώσε την ιστοσελίδα', font=(12))
    label.pack(side=TOP)
    self.entry3=Entry(self.win_web, width=30, font=(12))
    self.entry3.pack(side=TOP)
    button=Button(self.win_web, text='OK',font=(12), command=self.istoselida)
    button.pack()
    self.win_web.focus_set() 
      
  def read_entry_minima(self):
    minima=self.entry2.get()
    minima_obj=Open_Message(self.xronos(),minima)
    self.top_minima.destroy()
    minima_obj.run_on_time()
  
  def minima_window(self):
    self.top_minima=Toplevel()
    self.top_minima.title('Δώσε Μύνημα')
    self.entry2=Entry(self.top_minima, width=40, font=('12'))
    self.entry2.pack()
    button=Button(self.top_minima, text='ok',font=('12'),command=self.read_entry_minima)
    button.pack()
    self.entry2.focus_set()
   
  def email(self):
    mail_obj=Send_Email(self.xronos(),self.entry_mail1.get(),
    self.entry_mail5.get(),self.entry_mail2.get(),self.entry_mail3.get(),
    self.entry_mail4.get())
    mail_obj.run_on_time()
    self.mail_win.destroy()
   
  def mail_widget(self):
    entries=['mail_login', 'mail_to_send' , 'password', 'message']
    self.mail_win=Toplevel()
    label1=Label(self.mail_win, text='mail_client')
    self.entry_mail1=Entry(self.mail_win, width=60)
    label5=Label(self.mail_win, text='mail_login')
    self.entry_mail5=Entry(self.mail_win, width=60 )
    label2=Label(self.mail_win, text='mail_to_send')
    self.entry_mail2=Entry(self.mail_win, width=60)  
    label3=Label(self.mail_win, text='password')
    self.entry_mail3=Entry(self.mail_win, width=60, show='*')
    label4=Label(self.mail_win, text='message')
    self.entry_mail4=Entry(self.mail_win, width=60)
    label1.grid(column=0, row=0)
    label2.grid(column=0, row=2)
    label3.grid(column=0, row=3)
    label4.grid(column=0, row=4)
    label5.grid(column=0, row=1)
    self.entry_mail1.grid(column=1,row=0)
    self.entry_mail2.grid(column=1,row=2)
    self.entry_mail3.grid(column=1,row=3)
    self.entry_mail4.grid(column=1,row=4)
    self.entry_mail5.grid(column=1,row=1)
    self.entry_mail1.insert(0,'gmail ή outlook.com ή hotmail.com ή yahoo')
    self.entry_mail5.insert(0,'Το username σας')
    button_ok=Button(self.mail_win, text='Έτοιμος', command=self.email)
    button_ok.grid(column=0, row=5, columnspan=2)
   
  def calend(self):
    a=calendar.TextCalendar()
    b=Toplevel()
    b.title('Ημερολόγιο '+str(dt.now().year))
    text=Text(b)
    text.pack(expand=YES, fill= BOTH, padx=10, pady=10)
    text.insert(0.0,a.formatyear(dt.now().year) )
    text.configure(state='disabled')

  def xronos(self):
    str_time=self.entry1.get()
    time=dt.strptime(str_time,"%Y-%m-%d %H:%M:%S.%f")
    return time  

if __name__=='__main__': 
  a=Tk()
  a.title('Ξεχασιάρης')
  b=Jexasiaris(a)
  a.mainloop()

