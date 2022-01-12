from tkinter import * 
from tkinter import messagebox
import webbrowser

# Define App class, a subclasss of Tk which acts as the root window
# Class includes method which creates a Toplevel 'about' window tied to menu
# Binds intance method avx to enter key
class App(Tk):

	def __init__(self):		
		super().__init__()
		self.title("TDEE Calculator")
		self.geometry('450x435')
		try:
			self.iconbitmap('l_icon_fT4_icon.ico')
		except:
			pass
		self.option_add('*tearOff',FALSE)
		self.menu = Menu(self)	
		submenu = Menu(self.menu)
		self.menu.add_cascade(label='Menu',menu=submenu)
		submenu.add_command(label = 'About',command=self.about)
		submenu.add_separator()
		submenu.add_command(label = 'Quit',command=self.quit)		
		self.bind('<Return>',lambda event:mainframe.avx())
		self.config(menu=self.menu)		

	def about(self):
		abt = Toplevel(self)
		abt.geometry('300x200')
		abt.iconbitmap('l_icon_fT4_icon.ico')
		abt_lbl = Label(abt,anchor = 'w', text="TDEE v011122: Created by Larremy Gray to \n demonstrate" +
			" basic knowledge of python and Tkinter.\nTested with Windows 11 and Python 3.9")
		abt_lbl.grid(sticky='EW',row=0,column=0,padx = 5, pady=35)
		wbl_lbl= Label(abt,text="Wikipedia page about BMR",fg='blue',cursor='hand2')
		wbl_lbl.grid(sticky='NEW',row=1,column=0,padx = 5, pady=35)
		wbl_lbl.bind('<Button-1>',lambda e:
		webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Basal_metabolic_rate#Physiology"))

# Defines LabelFrame subclass used to create such widgets used for selection options two radio button options		
class OptionFrame(LabelFrame):
	def __init__(self,parent,title,option_1,option_2,variable):
		super().__init__()
		self['text'] = title
		self.unit_radio1 = Radiobutton(self,text=option_1,variable=variable,value=1)
		self.unit_radio1.grid(sticky='W',row=0,column=1)
		self.unit_radio2 = Radiobutton(self,text=option_2,variable=variable,value=2)
		self.unit_radio2.grid(sticky='W',row=1,column=1)

# Defines LabelFrame subclass used for Activity Multiplier
class FivexFrame(LabelFrame):
	def __init__(self,parent,title,option_1,option_2,option_3,option_4,option_5,variable):
		super().__init__()
		self['text'] = title
		self.activity_radio1 = Radiobutton(self,text=option_1,variable=variable,value=1)
		self.activity_radio1.grid(sticky='W',row=0,column=1)
		self.activity_radio2 = Radiobutton(self,text=option_2,variable=variable,value=2)
		self.activity_radio2.grid(sticky='W',row=1,column=1)
		self.activity_radio3 = Radiobutton(self,text=option_3,variable=variable,value=3)
		self.activity_radio3.grid(sticky='W',row=2,column=1)
		self.activity_radio4 = Radiobutton(self,text=option_4,variable=variable,value=4)
		self.activity_radio4.grid(sticky='W',row=3,column=1)
		self.activity_radio5 = Radiobutton(self,text=option_5,variable=variable,value=5)
		self.activity_radio5.grid(sticky='W',row=4,column=1)
# Defines main input frame
class MainInput(LabelFrame):
	def __init__(self,parent,title):
		super().__init__()
		self['text'] = title
		self.sex_label= Label(self,anchor = 'w', text="Select Sex")
		self.sex_label.grid(sticky="W",row=0,column=0)
		self.sex_button_f = Radiobutton(self,text="Female",variable=sex,value=1)
		self.sex_button_f.grid(sticky='E',row=0,column=1,padx=5)
		self.sex_button_m = Radiobutton(self,text="Male",variable=sex,value=2)
		self.sex_button_m.grid(sticky='W',row=0,column=2,padx=5)
		self.age_label = Label(self,anchor = 'w', text="Age")
		self.age_label.grid(sticky="W",row=1,column=0)
		self.weight_label= Label(self,anchor = 'w', text="Weight")
		self.weight_label.grid(sticky="W",row=2,column=0)
		self.height_label = Label(self,anchor = 'w', text="Height")
		self.height_label.grid(sticky="W",row=3,column=0)
		self.age_entry = Entry(self,textvariable=age,validate='key',validatecommand=check_nbr_input)
		self.age_entry.grid(sticky='W',row=1,column=2,padx=5)
		self.weight_entry = Entry(self,textvariable=weight,validate='key',validatecommand=check_nbr_input)
		self.weight_entry.grid(sticky='W',row=2,column=2,padx=5)
		self.height_entry = Entry(self,textvariable=height,validate='key',validatecommand=check_nbr_input)
		self.height_entry.grid(sticky='W',row=3,column=2,padx=5)
		self.bodyfat_label= Label(self,anchor = 'w', text="Bodyfat % (Required for Katch-McCardle)")
		self.bodyfat_label.grid(sticky="W",row=4,column=0)
		self.bodyfat_entry = Entry(self,textvariable=bodyfat,validate='key',validatecommand=check_nbr_input)
		self.bodyfat_entry.grid(sticky='W',row=4,column=2,padx=5)

# Defines ResultsFrame subclass used to output results. Included is the method that determines the output
class ResultsFrame(LabelFrame):
	def __init__(self,parent):
		super().__init__()
		self['text'] = 'Results'
		self.label = Label(self,width=58,height=1,anchor='center')
		self.label.grid(sticky='EW',row=0,column=0,padx=5)

	# The function to determine the results
	def calc(self):
		check1=False
		check2=False
		check3=False

		try:
			u = units.get()
			m = model.get()
			h = float(height.get())
			w = float(weight.get())
			
			s = sex.get()
			a = float(age.get())
			am = activity_multiplier.get()
			check1 = True
		
		except:
			messagebox.showwarning(message="Invalid entry. Review and try again", icon='warning',title='Entry Error')
			
		# Because of default values set, the only errors will occur if the bf% is cleared
		if check1:
			if m==2:
				try:
					b = float(bodyfat.get())/100
					check2=True
				except:
					messagebox.showwarning(message="Katch-McCardle requires valid bodyfat percentage", icon='warning',title='Entry Error')
					
		
		def actconv():
			if am == 1:
				return 1.20
			elif am == 2:
				return 1.375
			elif am == 3:
				return 1.55
			elif am == 4:
				return 1.725
			elif am == 5:
				return 1.9

		def htconv():
			if u == 1:
				return h * 2.54
			else:
				return h
		def wtconv():
			if u == 1:
				return w / 2.20462262
			else:
				return w
		
		if check1:
			ac = actconv()
			hc = htconv()
			wc= wtconv()

		if m == 1 and check1:
			if s == 1:
				bmr = 10 * wc + 6.25 *hc -5 * a - 161
			else:
				bmr = 10 * wc + 6.25 *hc -5 * a  + 5
			check3 = True
		if m==2 and check2:
			bmr = 370 +21.6*(1-b)*wc
			check3 = True
		if check3:
			tdee = bmr * ac
			
			# bmr = 
			self.label.config(text=f"BMR: {round(bmr)} kcal; TDEE: {round(tdee)} kcal")
		

# Creates the MainFrame subclass of tkinter Frame and assigns relative subframes
# The avx method accesses ResultFrame calc for use with button
class MainFrame(Frame):
	def __init__(self,parent):
		super().__init__()
		items = {'sticky':'E','row':4,'column':0,'columnspan':2}
		self.grid(**items)
		self.unit_lframe=OptionFrame(self,"Units","Imperial(in/lbs)","Metric(cm/kg)",units)
		self.unit_lframe.grid(sticky='EW',row=0,column=0,padx=5)
		self.model_mframe=OptionFrame(self,"Model","Mifflin St. Jeor","Katch-McCardle",model)
		self.model_mframe.grid(sticky='EW',row=0,column=1,columnspan=2,padx=5)
		self.main_input=MainInput(self,"Input")
		self.main_input.grid(sticky='EW',row=1,column=0,columnspan=3,padx=5)
		self.multiplier_frame=FivexFrame(self,"Activity Factor","Sedentary (little or no exercise)",
			"Light Activity (light exercise/sports 1-3 days/week)",
			"Moderate Activity (moderate exercise/sports 3-5 days/week)",
			"Very Active (hard exercise/sports 6-7 days a week)",
			"Extra Active (very hard exercise/sports and physical job)",
			activity_multiplier)	
		self.multiplier_frame.grid(sticky='EW',row=2,column=0,columnspan=3,padx=5)
		self.results_lframe =ResultsFrame(self)
		self.results_lframe.grid(sticky='EW',row=5,column=0,columnspan=3,rowspan=2,padx = 5)
		self.button_frame=Frame(self)
		self.button=Button(self,text="Submit",anchor='center',width=25,command=self.results_lframe.calc)
		self.button.grid(sticky='EW',row=0,column=1, padx = 25,columnspan=1)
		
	
	def avx(self):
		self.results_lframe.calc()

# Used to ensure valid entry with entry widgets
def nbrs_only(inpval):
	for c in inpval:
		return all( (c.isnumeric() or c=='.') for c in inpval)

# Initiate root
app=App()
# Assign function for input validation
check_nbr_input = (app.register(nbrs_only),'%P')
# Define and set tkinter text variables
units = IntVar()
units.set(1)
model = IntVar()
model.set(1)
activity_multiplier = IntVar()
activity_multiplier.set(1)
sex = IntVar()
sex.set(1)
age = StringVar()
height = StringVar()
weight = StringVar()
bodyfat = StringVar()
bodyfat.set('0.00')
# Initiate the main window
mainframe = MainFrame(App)
# Loop
app.mainloop()