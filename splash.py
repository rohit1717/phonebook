from Tkinter import *
root=Tk()
root.geometry('800x500')
Label(root,text='Project Title :PhoneBook',font='times 20 bold').grid(row=0,column=0)
Label(root,text='Project of Python and database',font='times 20 bold ').grid(row=1,column=1)
Label(root,text='Developed By: Rohit Singh',font='times 20 bold ', fg = 'blue').grid(row=2,column=1)
Label(root,text='---------------------------',font='times 20 bold ').grid(row=3,column=1)
Label(root,text='make mouse movement over this screen to close',font='times',fg='red').grid(row=4,column=1)
def close(e=1):
	root.destroy()
root.bind('<Motion>',close)
root.mainloop()
