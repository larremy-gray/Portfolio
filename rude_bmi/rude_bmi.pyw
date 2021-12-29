from tkinter import * 
from tkinter import messagebox

# Define App class, a subclasss of Tk which acts as the root window
# Class includes method which creates a Toplevel 'about' window tied to menu
# Binds intance method avx to enter key
class App(Tk):

	def __init__(self):		
		super().__init__()
		self.title("Rude BMI Calculator")
		self.geometry('335x250')
		try:
			self.iconbitmap('l_icon_fT4_icon.ico')
		except:
			pass
		self.option_add('*tearOff',FALSE)
		self.menu = Menu(self)	
		submenu = Menu(self.menu)
		self.menu.add_cascade(label='Menu',menu=submenu)
		submenu.add_command(label = 'Quit',command=self.quit)
		submenu.add_separator()
		submenu.add_command(label = 'About',command=self.about)
		self.bind('<Return>',lambda event:mainframe.avx())
		self.config(menu=self.menu)		

	def about(self):
		abt = Toplevel(self)
		abt.geometry('300x200')
		abt.iconbitmap('l_icon_fT4_icon.ico')
		abt_lbl = Label(abt,anchor = 'w', text="Rude BMI v122821: Created by Larremy Gray to \n demonstrate" +
			" basic knowledge of python and Tkinter.\nTested with Windows 11 and Python 3.9")
		abt_lbl.grid(sticky='EW',row=0,column=0,padx = 5, pady=35)

# Defines LabelFrame subclass used to create such widgets used for selection options		
class OptionFrame(LabelFrame):
	def __init__(self,parent,title,option_1,option_2,variable):
		super().__init__()
		self['text'] = title
		self.unit_radio1 = Radiobutton(self,text=option_1,variable=variable,value=1)
		self.unit_radio1.grid(sticky='W',row=0,column=1)
		self.unit_radio2 = Radiobutton(self,text=option_2,variable=variable,value=2)
		self.unit_radio2.grid(sticky='W',row=1,column=1)

# Defines LabelFrame subclass used to create such widgets used for dimension (height/weight) entry
class DimFrame(LabelFrame):
	def __init__(self,parent,title,variable):
		super().__init__()
		self['text'] = title
		self.wt_entry = Entry(self,textvariable=variable,validate='key',validatecommand=check_nbr_input)
		self.wt_entry.grid(sticky='W',row=0,column=1)

# Defines ResultsFrame subclass used to output results. Included is the method that determines the output
class ResultsFrame(LabelFrame):
	def __init__(self,parent):
		super().__init__()
		self['text'] = 'Results'
		self.label = Label(self,width=45)
		self.label.grid(sticky='EW',row=0,column=1,columnspan=3)

	def calc(self):
		try:
			u = units.get()
			t = tone.get()
			h = float(height.get())
			w = float(weight.get())
			if u == 1:
				bmi = round(w/(h**2)*703,1)
			
			elif u ==2:
				bmi = round(w/((h/100)**2),1)
			cat = category(bmi)
			if t == 1:
				comment = ''
			elif t==2:
				comment = ' ' + rude(cat)
			self.label.config(text=f"Your BMI is {bmi}. This is considered {cat}.\n{comment}")	
		except ZeroDivisionError as e:
			messagebox.showwarning(message="Height cannot be zero!", icon='warning',title='Entry Error')
		except:
			messagebox.showwarning(message="Invalid entry. Review and try again", icon='warning',title='Entry Error')

# Creates the MainFrame subclass of tkinter Frame and assigns relative subframes
# The avx method accesses ResultFrame calc for use with button
class MainFrame(Frame):
	def __init__(self,parent):
		super().__init__()
		items = {'sticky':'W','row':4,'column':0}
		self.grid(**items)
		self.unit_lframe=OptionFrame(self,"Units","Imperial(in/lbs)","Metric(cm/kg)",units)
		self.unit_lframe.grid(sticky='W',row=0,column=0,padx=5)
		self.tone_lframe=OptionFrame(self,"Tone","Normal","Rude",tone)
		self.tone_lframe.grid(sticky='W',row=1,column=0,padx=5)
		self.height_lframe=DimFrame(self,"Enter Height",height)
		self.height_lframe.grid(sticky='NE',row=0,column=1,padx=5)
		self.weight_lframe=DimFrame(self,"Enter Weight",weight)
		self.weight_lframe.grid(sticky='NE',row=1,column=1,padx=5)				
		self.results_lframe =ResultsFrame(self)
		self.results_lframe.grid(sticky='EW',row=5,column=0,columnspan=2,padx = 5)
		self.button=Button(self,text="Submit",command=self.results_lframe.calc)
		self.button.grid(sticky='W',row=4,column=0, padx = 5)
	
	def avx(self):
		self.results_lframe.calc()

# Used to ensure valid entry with entry widgets
def nbrs_only(inpval):
	for c in inpval:
		return all( (c.isnumeric() or c=='.') for c in inpval)

# determines the bmi category, used in calc function
def category(bmi):
	if bmi < 18.5:
		return "underweight"
	elif bmi < 25.0:
		return "healthy"
	elif bmi < 30:
		return "overweight"
	else:
		return "obese"

# returns a mean remark, used in calc fumction
def rude(cat):
	c_dict = {'underweight':"Why don't you eat something?",'healthy':"What? You think you're better than me?",
	'overweight':"Looks like you've put on quite a few pounds there, buddy!",
	'obese':"Maybe you should try NOT eating so many potato chips?"}
	return c_dict[cat]

# Initiate root
app=App()
# Assign function for input validation
check_nbr_input = (app.register(nbrs_only),'%P')
# Define and set tkinter text variables
units = IntVar()
units.set(1)
tone = IntVar()
tone.set(1)
height = StringVar()
weight = StringVar()
# Initiate the main window
mainframe = MainFrame(App)
# Loop
app.mainloop()