# container, 29 ft high.
# 25 feet of it is liquid benzene, sg~.875 g/cm
# N2 occupies the rest, pressure is 300 psi. 1.02 atm ambient.
# What is total absolute pressure?
# Find pressure of weight of benzene, and gas with atmospheric pressure


# P Table with masses.
# SG Table
# Water tables
# BP MP of stuff
import csv
import Tkinter as tk

# PV = nRT
R = .0820574614 #(L*atm)/(mol*K) are the units!


gas_elements=[]
f = csv.reader(open("/Users/mschwart/Documents/Thermo_Program/Gas_Elements.csv", "rU"), dialect=csv.excel_tab)
for row in f:
    gas_elements.append(row[0].split(","))
for i in gas_elements:
    if i[1].find('0') != -1:
        i[1]=i[1].replace(i[1][i[1].find('0')],u'\u2080')
    if i[1].find('1') != -1:
        i[1]=i[1].replace(i[1][i[1].find('1')],u'\u2081')
    if i[1].find('2') != -1:
        i[1]=i[1].replace(i[1][i[1].find('2')],u'\u2082')
    if i[1].find('3') != -1:
        i[1]=i[1].replace(i[1][i[1].find('3')],u'\u2083')
    if i[1].find('4') != -1:
        i[1]=i[1].replace(i[1][i[1].find('4')],u'\u2084')
    if i[1].find('5') != -1:
        i[1]=i[1].replace(i[1][i[1].find('5')],u'\u2085')
    if i[1].find('6') != -1:
        i[1]=i[1].replace(i[1][i[1].find('6')],u'\u2086')
    if i[1].find('7') != -1:
        i[1]=i[1].replace(i[1][i[1].find('7')],u'\u2087')
    if i[1].find('8') != -1:
        i[1]=i[1].replace(i[1][i[1].find('8')],u'\u2088')
    if i[1].find('9') != -1:
        i[1]=i[1].replace(i[1][i[1].find('9')],u'\u2089')
    if i[0].find('_') != -1:
        i[0]=i[0].replace(i[0][i[0].find('_')],',')

gas_mass=[]
gas_compounds=[]
for i in gas_elements:
    gas_compounds.append(i[0] + ' == ' + i[1])
    gas_mass.append(float(i[2]))
gas_compounds = tuple(gas_compounds)


root = tk.Tk()

class Principal(tk.Tk):

    def __init__(self, *args, **kwargs):
        root.title("Thermodynamics Solver")
        box_title = tk.Label(text="This solves for Ideal Gas Law.")
        box_title.grid(row=0,column=0,columnspan=2)
        
        #Pressure Input
        self.P_label = tk.Label(text="Enter Pressure:")
        self.P_label.grid(row=1,column=0)
        self.P_input = tk.StringVar()
        self.P_entry = tk.Entry(root,textvariable=self.P_input,width=15)
        self.P_entry.grid(row=1,column=1)
        pressure_units = ('atm','psi','mm Hg','kPa','Pa','torr','lbs/ft'+u'\u00b2','Inch Hg')
        self.P_unit = tk.StringVar()
        self.P_units_options = tk.OptionMenu(root, self.P_unit,*pressure_units)
        self.P_units_options.config(width=8)
        self.P_units_options.grid(row=1,column=2)
        self.P_unit.set('atm')

        #Temperature Input
        self.T_label = tk.Label(text="Enter Temperature:")
        self.T_label.grid(row=2,column=0)
        self.T_input = tk.StringVar()
        self.T_entry = tk.Entry(root,textvariable=self.T_input,width=15)
        self.T_entry.grid(row=2,column=1)
        temperature_units = ('K','R',u'\N{DEGREE SIGN}'+'C',u'\N{DEGREE SIGN}'+'F')
        self.T_unit = tk.StringVar()
        self.T_units_options = tk.OptionMenu(root, self.T_unit,*temperature_units)
        self.T_units_options.config(width=8)
        self.T_units_options.grid(row=2,column=2)
        self.T_unit.set('K')



        #Number of Moles Input
        self.n_label = tk.Label(text="Enter Amount of Gas (in moles):")
        self.n_label.grid(row=3,column=0)
        self.n_input = tk.StringVar()
        self.n_entry = tk.Entry(root,textvariable=self.n_input,width=15)
        self.n_entry.grid(row=3,column=1)
        amount_units = ('mol','kg','g','lb')
        self.n_unit = tk.StringVar()
        self.n_units_options = tk.OptionMenu(root, self.n_unit,*amount_units)
        self.n_units_options.config(width=8)
        self.n_units_options.grid(row=3,column=2)
        self.n_unit.set('mol')


        #Volume Input
        self.V_label = tk.Label(text="Enter Volume of Gas (in Liters):")
        self.V_label.grid(row=4,column=0)
        self.V_input = tk.StringVar()
        self.V_entry = tk.Entry(root,textvariable=self.V_input,width=15)
        self.V_entry.grid(row=4,column=1)
        volume_units = ('L','ft'+u'\u00b3','m'+u'\u00b3','cm'+u'\u00b3','gal')
        self.V_unit = tk.StringVar()
        self.V_units_options = tk.OptionMenu(root, self.V_unit,*volume_units)
        self.V_units_options.config(width=8)
        self.V_units_options.grid(row=4,column=2)
        self.V_unit.set('L')
        
        
        
        self.compute = tk.Button(text='Compute Ideal Gas Law',command=self.Ideal_Gas)
        self.compute.grid(row=5,column=0,columnspan=2)


    def Ideal_Gas(self):
        n = self.n_input.get()
        V = self.V_input.get()
        T = self.T_input.get()
        P = self.P_input.get()
        
        n_unit=self.n_unit.get()
        V_unit=self.V_unit.get()
        T_unit=self.T_unit.get()
        P_unit=self.P_unit.get()
        params_list = filter(None,[n,V,T,P])
        if len(params_list)<=2:
            self.underspecified_error_window = tk.Toplevel(root)
            self.underspecified_error_window.title('Error')
            tk.Label(self.underspecified_error_window,text="Error! System Underspecified!").pack()
            tk.Label(self.underspecified_error_window,text="Specify three variables please.").pack()
            return
        if len(params_list) == 4:
            self.overspecified_error_window = tk.Toplevel(root)
            self.overspecified_error_window.title('Error')
            tk.Label(self.overspecified_error_window,text="Error! System Overspecified!").pack()
            tk.Label(self.overspecified_error_window,text="Specify three variables please.").pack()
            return
        #Check to see what the unspecified variable is, solve for it.
        try:
            params_list = [float(l) for l in params_list]
            for i in params_list:
                if i<=0:
                    self.negatives_error_window = tk.Toplevel(root)
                    self.negatives_error_window.title('Error')
                    tk.Label(self.negatives_error_window,text="Error! Negative Values Detected!").pack()
                    tk.Label(self.negatives_error_window,text="Enter only positive values please.").pack()
                    return
        except ValueError:
            self.nonnumeric_error_window = tk.Toplevel(root)
            self.nonnumeric_error_window.title('Error')
            tk.Label(self.nonnumeric_error_window,text="Error! Non-Numeric Entries Detected!").pack()
            tk.Label(self.nonnumeric_error_window,text="Use only numbers please.").pack()
            return
        if n_unit != 'mol':
            self.Molecular_Weight(n_unit)
        else:
            pass

        ##Pressure Defaults!
        if P_unit == 'atm':
            R_val = R
        if P_unit == 'psi':
            R_val = R*14.6959
        if P_unit == 'mm Hg':
            R_val = R*760
        if P_unit == 'kPa':
            R_val = R*101.325
        if P_unit == 'Pa': 
            R_val=R*101.325*1000
        if P_unit == 'torr':
            R_val=R*760
        if P_unit == 'lbs/ft'+u'\u00b2':
            R_val = R*2116.220402
        if P_unit == 'inch Hg':
            R_val = R *760*0.0393701


        ##Volume Defaults!
        if V_unit == 'L':
            V=V
        if V_unit == 'gal':
            V=V*0.264172
        if V_unit == 'm'+u'\u00b3':
            V=V*.001
        if V_unit == 'm'+u'\u00b3':
            V= V* .001 * 35.3147
        if V_unit == 'cm'+u'\u00b3':
            V=V*1000

        ##Temperature Defaults!
        if T_unit == 'K':
            pass #Default setting in this case!
        if T_unit == 'R':
            T=float(T)*1.8
        if T_unit == u'\N{DEGREE SIGN}'+'C':
            T=float(T)+273.15
        if T_unit == u'\N{DEGREE SIGN}'+'F':
            T= (float(T) + 459.67) *5/9
            
            
        if n == '':
            number_of_moles = (P*V/R_val*T)
            self.n_entry.insert(0,round(number_of_moles,6))
        elif P == '':
            Pressure=(float(n)*float(R_val)*float(T))/float(V)
            self.P_entry.insert(0,round(Pressure,6))
        elif T == '':
            Temp = (float(P)*float(V))/(float(R_val)*float(n))
            self.T_entry.insert(0,round(Temp,6))
        elif V == '':
            Volume = (float(n)*float(R_val)*float(T))/float(P)
            self.V_entry.insert(0,round(Volume,6))
        else:
            print("Error: Specify Variables!")

    def Molecular_Weight(self,n_unit): #Opens an additional window so that someone may enter molecular weight.
        self.mass_window = tk.Toplevel(root)
        self.mass_window.title('Molecular Weight ID')
        self.molecular_weight_label = tk.Label(self.mass_window,text="Input Molecular Weight:")
        self.molecular_weight_label.grid(row=0,column=0)
        mweight_units = ('g/mol','kg/mol','lb/mol')
        self.molecular_weight_input = tk.StringVar()
        self.molecular_weight_entry = tk.Entry(self.mass_window,textvariable=self.molecular_weight_input,width=15)
        self.molecular_weight_entry.grid(row=0,column=1)
        self.molecular_weight_units = tk.StringVar()
        self.molecular_weight_options = tk.OptionMenu(self.mass_window,self.molecular_weight_units,*mweight_units)
        self.molecular_weight_options.config(width=8)
        self.molecular_weight_options.grid(row=0,column=2)
        self.molecular_weight_units.set('g/mol')
        
        self.molecular_id_label = tk.Label(self.mass_window,text="Or Choose Gas:")
        self.molecular_id_label.grid(row=1,column=0)
        self.molecular_id_input = tk.StringVar()
#        gas_compounds=("ttt") #COME BACK HERE!
        self.molecular_id_options = tk.OptionMenu(self.mass_window,self.molecular_id_input,*gas_compounds)
        self.molecular_id_options.config(width=25)
        self.molecular_id_options.grid(row=1,column=1,columnspan=2)
        self.molecular_id_input.set("Water Vapor (steam): H"+u"\u2082"+"O")
        
        self.mweight_button = tk.Button(self.mass_window,text='Submit Molecular Weight',
                                        command=self.mass_window.destroy)
        self.mweight_button.grid(row=2,column=0,columnspan=3)


    def submit_molecular_weight(self):
        print(self.molecular_weight_units.get())
app = Principal()
root.mainloop()


