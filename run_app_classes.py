from datetime import datetime as dt
import time
from threading import Timer
import subprocess
import threading
import webbrowser
import smtplib
from tkinter import *
from tkinter import ttk

class Open_Web:
  def __init__(self, time,page):
    self.time=time
    self.page=page
      
  def run_on_time(self):
    Timer(self.time.timestamp()-time.time(), webbrowser.open, args=(self.page,)).start()
    
class Open_File:    
  def __init__(self, time,file,programm='start'):
    self.time=time
    self.file=file
    self.programm=programm
     
  def run_on_time(self):
    Timer(self.time.timestamp()-time.time(), subprocess.run, args=((self.programm, self.file),),
    kwargs={'shell':True}).start()


class Send_Email:
  mail_clients={'gmail' : 'smtp.gmail.com', 'outlook.com': 'smtp-mail.outlook.com',
  'hotmail.com':'smtp-mail.outlook.com' ,'yahoo': 'smtp.mail.yahoo.com'}

  def __init__(self, time, mail_client, mail_login, mail_to_send , password, message):
    self.time=time
    self.mail_client=type(self). mail_clients[mail_client]
    self.mail_login=mail_login
    self.mail_to_send=mail_to_send
    self.password=password
    self.message="Subject: Don't forget\n"+message
    
  def send_function(self):
    obj=smtplib.SMTP(self.mail_client, 587)
    obj.ehlo()
    obj.starttls()
    obj.login(self.mail_login, self.password)
    obj.sendmail(self.mail_login, self.mail_to_send,self.message)
    obj.quit()

  def run_on_time(self):
    Timer(self.time.timestamp()-time.time(), self.send_function).start()
    
class Open_Message:
  def __init__(self, time, message):
    self.time=time
    self.message=message
  
  def grafic(self):
    root=Tk()
    root.title('Ξεχασιάρης')
    mainframe=ttk.Frame(root, borderwidth=5, relief="sunken", width=200, height=100)
    mainframe.grid(row=0,column=0)
    label1=ttk.Label(mainframe,text=self.message, font='20')
    label1.grid() 
    root.mainloop()
  
  def run_on_time(self):
    Timer(self.time.timestamp()-time.time(), self.grafic).start()  
 

   
class Save:
  object_file=[]
  def save_object(self,object):
    type(self).object_file.append(object)