import splash
from Tkinter import *
import sqlite3
from tkMessageBox import *
con =sqlite3.Connection('PhoneBook')
cur=con.cursor()
cur.execute('PRAGMA foreign_keys=ON')
cur.execute('create table if not exists contact(contactid integer primary key AUTOINCREMENT,fname varchar2(30),mname varchar(30),lname varchar(30),company varchar(30),address varchar(30),city varchar(30),pin number,web varchar(30),dob varchar(30))')
cur.execute('create table if not exists phonenum(contactid number references contact(contactid) on delete cascade ,contacttype varchar(10),pnum number ,primary key(contactid,pnum))')
cur.execute('create table if not exists email(contactid number references contact(contactid) on delete cascade,emailtype varchar(10),emailid varchar(50) ,primary key(contactid,emailid))')
root=Tk()
root.title('Phone Book')
root.geometry('700x700')
p=PhotoImage(file="phb1.gif")
Label(root,image=p).grid(row=0,column=1)
Label(root,text='    First Name    ').grid(row=1,column=0)
Label(root,text='    Middle Name    ').grid(row=2,column=0)
Label(root,text='    Last Name    ').grid(row=3,column=0)
Label(root,text='    Company Name    ').grid(row=4,column=0)
Label(root,text='    Address    ').grid(row=5,column=0)
Label(root,text='    City    ').grid(row=6,column=0)
Label(root,text='    Pin Code    ').grid(row=7,column=0)
Label(root,text='    Website URL    ').grid(row=8,column=0)
Label(root,text='    Date of Birth    ').grid(row=9,column=0)
Label(root,text='Select Phone Type',font='times 15 bold',fg='blue').grid(row=10,column=0)
Label(root,text='    Phone Number    ').grid(row=11,column=0)
Label(root,text='Select Email Type',font='times 15 bold',fg='blue').grid(row=12,column=0)
Label(root,text='    Email Id    ').grid(row=13,column=0)
fn=Entry(root)
fn.grid(row=1,column=1)
mn=Entry(root)
mn.grid(row=2,column=1)
ln=Entry(root)
ln.grid(row=3,column=1)
cn=Entry(root)
cn.grid(row=4,column=1)
ad=Entry(root)
ad.grid(row=5,column=1)
ci=Entry(root)
ci.grid(row=6,column=1)
pi=Entry(root)
pi.grid(row=7,column=1)
we=Entry(root)
we.grid(row=8,column=1)
dob=Entry(root)
dob.grid(row=9,column=1)
pn=Entry(root)
pn.grid(row=11,column=1)
em=Entry(root)
em.grid(row=13,column=1)
et=IntVar()
pt=IntVar()
Radiobutton(root,text='Office',variable=pt,value=1).grid(row=10,column=1)
Radiobutton(root,text='Home',variable=pt,value=2).grid(row=10,column=2)
Radiobutton(root,text='Mobile',variable=pt,value=3).grid(row=10,column=3)
Radiobutton(root,text='Office',variable=et,value=1).grid(row=12,column=1)
Radiobutton(root,text='Personal',variable=et,value=2).grid(row=12,column=2)
pp=[]
i=[]
j=[]
k=[]
iid=[]
def savecon():
	try:
		global iid
		cur.execute('select fname from contact where contactid={}'.format(iid))
		qq=cur.fetchall()
		if len(qq)>0:
			cur.execute('delete from contact where contactid={}'.format(iid))
			iid=-1
		if pt.get()==1:
			ptt='Office'
		elif pt.get()==2:
			ptt='Home'
		elif pt.get()==3 or pt.get()==0:
			ptt='Mobile'
		if et.get()==1:
			ett='Office'
		elif et.get()==2 or et.get()==0:
			ett='Personal'

		cot=(str(fn.get()),str(mn.get()),str(ln.get()),str(cn.get()),str(ad.get()),str(ci.get()),str(pi.get()),str(we.get()),str(dob.get()))
		cur.execute('insert into contact(fname,mname,lname,company,address,city,pin,web,dob) values(?,?,?,?,?,?,?,?,?)',cot)
		cur.execute('select max(contactid) from contact')
		cid= cur.fetchall()
		if len(pn.get())!=0:
			cur.execute('insert into phonenum values(?,?,?)',(int(cid[0][0]),str(ptt),str(pn.get())))
		if len(em.get())!=0:
			cur.execute('insert into email values(?,?,?)',(int(cid[0][0]),str(ett),str(em.get())))	
       
	except:
		showerror('oops','something went wrong try again')
	else:
		showinfo('yo','contact saved')    
		con.commit()
		fn.delete(0,END)
		mn.delete(0,END)
		ln.delete(0,END)
		cn.delete(0,END)
		ad.delete(0,END)
		ci.delete(0,END)
		pi.delete(0,END)
		we.delete(0,END)
		dob.delete(0,END)
		pn.delete(0,END)
		em.delete(0,END)
		et.set(0)
		pt.set(0)
def search():
	top=Toplevel()
	top.title('search')
	Label(top,text='Searching Phone Book',font='times 20 bold',bg='lightblue').grid(row=0,column=0)
	Label(top,text='   Enter Name  ').grid(row=1,column=0)
	spn=Entry(top)
	spn.grid(row=2,column=0)
	lb=Listbox(top,width=100,height=25,selectmode=SINGLE)
	lb.grid(row=3,column=0)
	top.geometry('600x550')
	sc=spn.get()
	def show(e=0):
		lb.delete(0,END)
		sc=spn.get()
		cur.execute('select contactid,fname,mname,lname from contact where fname like "%{}%" or mname like "%{}%" or lname like "%{}%"'.format(sc,sc,sc))
		global pp
		pp=cur.fetchall()
		q=0
		while q<len(pp):
			nn=pp[q][1]+' '+pp[q][2]+' '+pp[q][3]
			lb.insert(0,nn)
			q+=1
	
	def showin(e=0):
		def edit():
			global pp,i,j,k
			top.destroy()
			top2.destroy()
			fn.insert(0,i[0][1])
			mn.insert(0,i[0][2])
			ln.insert(0,i[0][3])
			cn.insert(0,i[0][4])
			ad.insert(0,i[0][5])
			ci.insert(0,i[0][6])
			pi.insert(0,i[0][7])
			we.insert(0,i[0][8])
			dob.insert(0,i[0][9])
			if len(j)!=0:
				pn.insert(0,j[0][2])
				if j[0][1]=='Office':
					pt.set(1)
				elif j[0][1]=='Home':
					pt.set(2)
				elif j[0][1]=='Mobile':
					pt.set(3)
					
			if len(k)!=0:
				em.insert(0,k[0][2])
				if k[0][1]=='Office':
					et.set(1)
				elif k[0][2]=='Personal':
					et.set(2)
		
		global pp,i,j,k,iid
		per=lb.curselection()
		ind=per[0]
		lb.delete(0,END)
		ind =len(pp)-ind-1
		iid=pp[ind][0]
		top2=Toplevel()
		cur.execute('select * from contact where contactid={}'.format(iid))
		i=cur.fetchall()
		top2.geometry('350x350')
		Label(top2,text='Search Result',font='times 25').grid(row=0,column=1)
		Label(top2,text='Name:',font='times 13').grid(row=1,column=0)
		Label(top2,text=i[0][1]+' '+i[0][2]+' '+i[0][3],font='times 13').grid(row=1,column=1)
		Label(top2,text='Company Name:',font='times 13').grid(row=2,column=0)
		Label(top2,text=i[0][4],font='times 13').grid(row=2,column=1)
		Label(top2,text='Address:',font='times 13').grid(row=3,column=0)
		Label(top2,text=i[0][5],font='times 13').grid(row=3,column=1)
		Label(top2,text='City:',font='times 13').grid(row=4,column=0)
		Label(top2,text=i[0][6],font='times 13').grid(row=4,column=1)
		Label(top2,text='Pincode:',font='times 13').grid(row=5,column=0)
		Label(top2,text=i[0][7],font='times 13').grid(row=5,column=1)
		Label(top2,text='Website:',font='times 13').grid(row=6,column=0)
		Label(top2,text=i[0][8],font='times 13').grid(row=6,column=1)
		Label(top2,text='DOB:',font='times 13').grid(row=7,column=0)
		Label(top2,text=i[0][9],font='times 13').grid(row=7,column=1)
		cur.execute('select * from phonenum where contactid={}'.format(iid))
		j=cur.fetchall()
		Label(top2,text='Phone Type:',font='times 13').grid(row=8,column=0)
		Label(top2,text='Phone Number:',font='times 13').grid(row=9,column=0)
		if len(j)!=0:
			Label(top2,text=j[0][1],font='times 13').grid(row=8,column=1)
			Label(top2,text=j[0][2],font='times 13').grid(row=9,column=1)
		cur.execute('select * from email where contactid={}'.format(iid))
		k=cur.fetchall()
		Label(top2,text='Email Type:',font='times 13').grid(row=10,column=0)
		Label(top2,text='Email Id:',font='times 13').grid(row=11,column=0)
		if len(k)!=0:
			Label(top2,text=k[0][1],font='times 13').grid(row=10,column=1)
			Label(top2,text=k[0][2],font='times 13').grid(row=11,column=1)
		def delete():
			global iid
			mb=askquestion('Delete contact','Are you sure?',icon='warning')
			if mb=='yes':
				cur.execute('delete from contact where contactid={}'.format(iid))
				iid=-1
				top2.destroy()
				con.commit()
				showinfo('yo','contact deleted')
		def close():
			top2.destroy()
		Button(top2,text='Edit',command=edit).grid(row=12,column=0)
		Button(top2,text='Delete',command=delete).grid(row=12,column=1)
		Button(top2,text='Close',command=close).grid(row=12,column=2)
	def closet():
		top.destroy()
	Button(top,text='Close',command=closet).grid(row=4,column=0)
	lb.bind('<Double-Button-1>',showin)
	spn.bind('<Button-1>',show)
	top.bind('<Key>',show)

def Reset():
	global iid
	iid=-1
	fn.delete(0,END)
	mn.delete(0,END)
	ln.delete(0,END)
	cn.delete(0,END)
	ad.delete(0,END)
	ci.delete(0,END)
	pi.delete(0,END)
	we.delete(0,END)
	dob.delete(0,END)
	pn.delete(0,END)
	em.delete(0,END)
	et.set(0)
	pt.set(0)
def closer():
	root.destroy()
Button(root,text='+').grid(row=11,column=3)
Button(root,text='+').grid(row=13,column=3)
Button(root,text='Save',command=savecon).grid(row=14,column=0)
Button(root,text='Search',command=search).grid(row=14,column=1)
Button(root,text='Close',command=closer).grid(row=14,column=2)
Button(root,text='Edit',command=search).grid(row=14,column=3)
Button(root,text='Reset',command=Reset).grid(row=14,column=4)
root.mainloop()
