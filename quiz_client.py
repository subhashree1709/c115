import socket
from threading import Thread
from tkinter import *

nickname= input('CHOOSE YOUR NICKNAME: ')

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address= '127.0.0.1'
port= 8000
client.connect((ip_address,port))

print('connected to server...')


class GUI:
    def __init__(self):
        self.Window= Tk()
        self.Window.withdraw()

        self.login= Toplevel()
        self.login.title('login')


        self.Window.configure(bg= 'lightblue')
        self.Window.resize(300,300)

        login_label= Label(self.Window,text='Please login to continue',fg='black',bg='lightblue',font=('Helvetica 14 bold',12),bd=1)
        login_label.place(x=140,y=250)
                

        name_label= Label(self.Window,text='name: ',fg='black',bg='lightblue',font=('Calibri',12),bd=1)
        name_label.place(x=20,y=90)

        user_name= Entry(self.Window,text='',bd=2,width=22)
        user_name.place(x=150,y=92)


        self.go= Button(self.login,
                        text= 'CONTINUE',
                        font= 'Helvetica 14 Bold',
                        command= lambda: self.goAhead(self.entryname.get()))
        
    def layout(self,name):
        self.name = name
        self.window.deiconify()
        self.Window.title(" CHATROOM")
        self.Window.resizable(width = False,height = False)
        self.Window.configure(width = 470,height = 550,bg = "#17202A")

    def goAhead(self,name):
        self.login.destroy()
        self.layout(name)
        rcv= Thread(target=self.recieve)
        rcv.start()

    def recieve(self):
      while True:
        try:
            message= client.recv(2048).decode('utf-8')
            if message== 'NICKNAME':
                client.send(self.name.encode('utf-8'))
            else :
                print(message)
        except:
            print('an error occured')
            client.close()
            break

    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg=msg
        self.entrymsg.delete(0, END)
        snd= Thread(target = self.write)
        snd.start()

    def show_message(self, message):
        self.textCons.config(state = NORMAL)
        self.textCons.insert(END, message+"\n\n")
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)
    

    def write(self):
        self.textCons.config (state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode( 'utf-8'))
            self.show_message(message)
            break

gui= GUI()