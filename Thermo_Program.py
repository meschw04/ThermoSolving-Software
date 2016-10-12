
# container, 29 ft high.
# 25 feet of it is liquid benzene, sg~.875 g/cm
# N2 occupies the rest, pressure is 300 psi. 1.02 atm ambient.
# What is total absolute pressure?
# Find pressure of weight of benzene, and gas with atmospheric pressure


# P Table with masses.
# SG Table
# Water tables
# BP MP of stuff

import Tkinter as tk
import thermo_parse_files

# PV = nRT
R = .0820574614 #(L*atm)/(mol*K) are the units!

gas_compounds = thermo_parse_files.parse_gas_compounds("/Users/mschwart/ThermoSolving-Software/Gas_Elements.csv")
#NOTE: Come back to this, you will eventually want to change this so that it doesn't have to take the file path.
#This way, it can work on any computer and not just yours with the specific file path. Good luck!


root = tk.Tk()

class Principal(tk.Tk):

    ####################################################################################################################
    ################################################# MAIN MENU LAYOUT #################################################
    ####################################################################################################################
#This is a test comment.

    def __init__(self, *args, **kwargs):
        root.title("ThermoSolving Software")
        self.main_label = tk.Label(root,text='Themodynamics Main Window')
        self.main_label.grid(row=0,column=0)
        
        self.species_database_button = tk.Button(root,text="Add Species to Database",command=self.species_database)
        self.species_database_button.config(width=30)
        self.species_database_button.grid(row=1,column=0)
        
        self.ideal_gas_button = tk.Button(root,text="Ideal Gas Law",command=self.ideal_gas_law)
        self.ideal_gas_button.config(width=30)
        self.ideal_gas_button.grid(row=2,column=0)

        self.saturation_pressure_calc = tk.Button(root, text='Saturation Pressure Solver',command=self.sat_pressure_calc)
        self.saturation_pressure_calc.config(width=30)
        self.saturation_pressure_calc.grid(row=3,column=0)
        
        self.equation_of_state_solver = tk.Button(root, text='Equation of State Solver',command=self.eos_solver)
        self.equation_of_state_solver.config(width=30)
        self.equation_of_state_solver.grid(row=4,column=0)
        
        self.fugacity_coeff_solver = tk.Button(root, text='Fugacity Coefficient Solver',command=self.fug_coeff_solver)
        self.fugacity_coeff_solver.config(width=30)
        self.fugacity_coeff_solver.grid(row=5,column=0)
        
        self.parameter_fitting = tk.Button(root,text='Models/Fittings for Excess Gibbs Energy',command=self.xs_gibbs)
        self.parameter_fitting.config(width=30)
        self.parameter_fitting.grid(row=6,column=0)
        
        self.bubble_dew_point_calcs = tk.Button(root,text='Bubble/Dew Point Calculations',command=self.bubble_dew_point)
        self.bubble_dew_point_calcs.config(width=30)
        self.bubble_dew_point_calcs.grid(row=7,column=0)
        
        self.chemical_reaction_equilibria = tk.Button(root,text='Chemical Reaction Equilibria',command=self.chem_rxn_equil)
        self.chemical_reaction_equilibria.config(width=30)
        self.chemical_reaction_equilibria.grid(row=8,column=0)


    ####################################################################################################################
    ################################################# SPECIES DATABASE #################################################
    ####################################################################################################################



    def species_database(self):
        return
        


    ###################################################################################################################
    ################################################## IDEAL GAS LAW ##################################################
    ###################################################################################################################        
        
    def ideal_gas_law(self):
        self.ideal_gas_window = tk.Toplevel(root)
        self.ideal_gas_window.title("Ideal Gas Solver")
        box_title = tk.Label(self.ideal_gas_window,text="This solves for Ideal Gas Law.")
        box_title.grid(row=0,column=0,columnspan=2)
        
        #Pressure Input
        self.P_label = tk.Label(self.ideal_gas_window,text="Enter Pressure:")
        self.P_label.grid(row=1,column=0)
        self.P_input = tk.StringVar()
        self.P_entry = tk.Entry(self.ideal_gas_window,textvariable=self.P_input,width=15)
        self.P_entry.grid(row=1,column=1)
        pressure_units = ('atm','psi','mm Hg','kPa','Pa','torr','lbs/ft'+u'\u00b2','Inch Hg')
        self.P_unit = tk.StringVar()
        self.P_units_options = tk.OptionMenu(self.ideal_gas_window, self.P_unit,*pressure_units)
        self.P_units_options.config(width=8)
        self.P_units_options.grid(row=1,column=2)
        self.P_unit.set('atm')

        #Temperature Input
        self.T_label = tk.Label(self.ideal_gas_window,text="Enter Temperature:")
        self.T_label.grid(row=2,column=0)
        self.T_input = tk.StringVar()
        self.T_entry = tk.Entry(self.ideal_gas_window,textvariable=self.T_input,width=15)
        self.T_entry.grid(row=2,column=1)
        temperature_units = ('K','R',u'\N{DEGREE SIGN}'+'C',u'\N{DEGREE SIGN}'+'F')
        self.T_unit = tk.StringVar()
        self.T_units_options = tk.OptionMenu(self.ideal_gas_window, self.T_unit,*temperature_units)
        self.T_units_options.config(width=8)
        self.T_units_options.grid(row=2,column=2)
        self.T_unit.set('K')



        #Number of Moles Input
        self.n_label = tk.Label(self.ideal_gas_window,text="Enter Amount of Gas (in moles):")
        self.n_label.grid(row=3,column=0)
        self.n_input = tk.StringVar()
        self.n_entry = tk.Entry(self.ideal_gas_window,textvariable=self.n_input,width=15)
        self.n_entry.grid(row=3,column=1)
        amount_units = ('mol','kg','g','lb')
        self.n_unit = tk.StringVar()
        self.n_units_options = tk.OptionMenu(self.ideal_gas_window, self.n_unit,*amount_units)
        self.n_units_options.config(width=8)
        self.n_units_options.grid(row=3,column=2)
        self.n_unit.set('mol')


        #Volume Input
        self.V_label = tk.Label(self.ideal_gas_window,text="Enter Volume of Gas (in Liters):")
        self.V_label.grid(row=4,column=0)
        self.V_input = tk.StringVar()
        self.V_entry = tk.Entry(self.ideal_gas_window,textvariable=self.V_input,width=15)
        self.V_entry.grid(row=4,column=1)
        volume_units = ('L','ft'+u'\u00b3','m'+u'\u00b3','cm'+u'\u00b3','gal')
        self.V_unit = tk.StringVar()
        self.V_units_options = tk.OptionMenu(self.ideal_gas_window, self.V_unit,*volume_units)
        self.V_units_options.config(width=8)
        self.V_units_options.grid(row=4,column=2)
        self.V_unit.set('L')
        
        
        
        self.compute = tk.Button(self.ideal_gas_window,text='Compute Ideal Gas Law',command=self.Ideal_Gas)
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
            root.wait_window(self.mass_window)
            n_conversion = float(self.molecular_weight_input.get()) #
            if n_unit == 'kg':
                n_val = float(n) * .001 * n_conversion
            if n_unit == 'g':
                n_val = float(n) * n_conversion
            if n_unit == 'lb':
                n_val = float(n) * 453.592 * n_conversion
        else:
            n_val = n

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
            pass
        if T_unit == 'R':
            T=float(T)*1.8
        if T_unit == u'\N{DEGREE SIGN}'+'C':
            T=float(T)+273.15
        if T_unit == u'\N{DEGREE SIGN}'+'F':
            T= (float(T) + 459.67) *5/9
            
            
        if n == '':
            number_of_moles = (float(P)*float(V)/R_val*float(T))
            self.n_entry.insert(0,round(number_of_moles,6))
        elif P == '':
            Pressure=(float(n_val)*float(R_val)*float(T))/float(V)
            self.P_entry.insert(0,round(Pressure,6))
        elif T == '':
            Temp = (float(P)*float(V))/(float(R_val)*float(n_val))
            self.T_entry.insert(0,round(Temp,6))
        elif V == '':
            Volume = (float(n_val)*float(R_val)*float(T))/float(P)
            self.V_entry.insert(0,round(Volume,6))
        else:
            self.error_window = tk.Toplevel(root)
            self.nonnumeric_error_window.title('Error')
            tk.Label(self.nonnumeric_error_window,text="Error! Incorrect Entry Detected!").pack()
            return


    def calculate_vals(self,event):
        self.gas_comp_list = list(gas_compounds)
        self.molecular_weight_entry.delete(0,'end')
        self.molecular_weight_entry.insert(0,str(gas_mass[self.gas_comp_list.index(self.molecular_id_input.get())]))


    def Molecular_Weight(self,n_unit): #Opens an additional window so that someone may enter molecular weight.
        self.mass_window = tk.Toplevel(root)
        self.mass_window.title('Molecular Weight ID')
        self.molecular_weight_label = tk.Label(self.mass_window,text="Input Molecular Weight (g/mol):")
        self.molecular_weight_label.grid(row=0,column=0)
        self.molecular_weight_input = tk.StringVar()
        self.molecular_weight_entry = tk.Entry(self.mass_window,textvariable=self.molecular_weight_input,width=15)
        self.molecular_weight_entry.insert(0,'18.02')        
        self.molecular_weight_entry.grid(row=0,column=1)
        
        self.molecular_id_label = tk.Label(self.mass_window,text="Or Choose Gas:")
        self.molecular_id_label.grid(row=1,column=0)
        self.molecular_id_input = tk.StringVar()
        self.molecular_id_options = tk.OptionMenu(self.mass_window,self.molecular_id_input,*gas_compounds,command=self.calculate_vals)
        self.molecular_id_options.config(width=25)
        self.molecular_id_options.grid(row=1,column=1,columnspan=2)
        self.molecular_id_input.set("Water Vapor (steam): H"+u"\u2082"+"O")
        
        self.mweight_button = tk.Button(self.mass_window,text='Submit Molecular Weight',
                                        command=self.mass_window.destroy)
        self.mweight_button.grid(row=2,column=0,columnspan=3)


    #####################################################################################################################
    ########################################## SATURATION PRESSURE CALCULATION ##########################################
    #####################################################################################################################


    def sat_pressure_calc(self):
        return
        

    ####################################################################################################################
    ############################################# EQUATION OF STATE SOLVER #############################################
    ####################################################################################################################



    def eos_solver(self):
        return


    #####################################################################################################################
    ############################################ FUGACITY COEFFICIENT SOLVER ############################################
    #####################################################################################################################

        
    def fug_coeff_solver(self):
        return


    #####################################################################################################################
    ####################################### EXCESS GIBBS ENERGY PARAMETER FITTING #######################################
    #####################################################################################################################


        
    def xs_gibbs(self):
        return


    #####################################################################################################################
    ###################################### BUBBLE POINT AND DEW POINT CALCULATIONS ######################################
    #####################################################################################################################

    
    def bubble_dew_point(self):
        self.bubble_dew_point_window = tk.Toplevel(root)
        self.bubble_dew_point_window.title('Bubble/Dew Point Calculations')

        self.main_label_point = tk.Label(self.bubble_dew_point_window,
                                         text='Choose the type of calculation you would like to make:')
        self.main_label_point.grid(row=0,column=0,columnspan=3)
        
        self.bubble_point_label = tk.Label(self.bubble_dew_point_window,text='Bubble Point (Xi Known):')
        self.bubble_point_label.grid(row=1,column=1)
        
        self.dew_point_label = tk.Label(self.bubble_dew_point_window,text='Dew Point (Yi Known):')
        self.dew_point_label.grid(row=1,column=2)
        
        self.T_known = tk.Label(self.bubble_dew_point_window,text='T known:')
        self.T_known.grid(row=2,column=0)

        self.P_known = tk.Label(self.bubble_dew_point_window,text='P known:')
        self.P_known.grid(row=3,column=0)
        
        self.dew_point_T_I = tk.Button(self.bubble_dew_point_window,text='Find Xi, P',command=self.find_I)
        self.dew_point_T_I.grid(row=2,column=2)

        self.dew_point_T_II = tk.Button(self.bubble_dew_point_window,text='Find Yi, P',command=self.find_II)
        self.dew_point_T_II.grid(row=2,column=1)

        self.dew_point_T_III = tk.Button(self.bubble_dew_point_window,text='Find Yi, T',command=self.find_III)
        self.dew_point_T_III.grid(row=3,column=1)

        self.dew_point_T_IV = tk.Button(self.bubble_dew_point_window,text='Find Xi, T',command=self.find_IV)
        self.dew_point_T_IV.grid(row=3,column=2)

        
    def find_I(self):
        return
    def find_II(self):
        return
    def find_III(self):
        return
    def find_IV(self):
        return

    ####################################################################################################################
    ########################################### CHEMICAL REACTION EQUILIBRIA ###########################################
    ####################################################################################################################

        
    def chem_rxn_equil(self):
        return



app = Principal()
root.mainloop()


