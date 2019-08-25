#####################################################################
#                                                                   #
#            Common-Emitter Amplifier Design Script                 #
#                                                                   #
#####################################################################
# Author: Joao Nuno Carvalho                                        #
# Date:   2019.08.25                                                #
# License: MIT Open Source License.                                 #
# Description: This is a Python script to help in the design of a   #
#              simple Common Emitter Amplifier with a single bipolar#
#              transistor stage, bandlimited above f1 frequency.    #
#              This is based on a step by step guide and basic      #
#              program from a very good and old book called:        #
#              Exploring Electronic Devices                         #
#              by Mark Hazen                                        #
#####################################################################
# Manual: 1º Fill your specific data in the variables of the script.#
#         2º Execute the script.                                    #                           
#         3º Analyse the results, decide if it is correct for your  #
#            experiment.                                            #  
#####################################################################

import math

print("\n\n\n")
print("Common-Emitter Amplifier Design Script")


##########################
# Fill the following data:

# Vcc - Supply voltage in volts.
Vcc = 18
# Vce - Collector-Emitter voltage in volts.
Vce = 9
# F1 - The lowest frequency to be amplified in Hz.
F1 =  40
# B The minimum AC Beta for the transistor.
Beta =  150
# Av - The desired voltage gain ( 1 to 30). 
A =  20
# Rc - The desired collector resistance.
Rc = 6800
# RL - The load resistance.
RL = 8500



###############
# Calculations:

# AC collector resistance.
Rco = (RL * Rc) / float(RL + Rc)
# Total DC emitter resistance.
Re_dc = Rc / 10.0
# Emitter-collector current.
Ie = (Vcc - Vce) / float(Rc + Re_dc)
# Internal emitter resistance.
Re_int = 0.025 / Ie
# Base voltage.
Vb = (Ie * Re_dc) + 0.7  # Vce diode PN junction drop.
# Approximate base current.
Ib = Ie / float(Beta)
# Value of R2.
R2 = Vb / (10.0 * Ib)
# Value of R1.
R1 = (Vcc - Vb) / float(10.0 * Ib + Ib)
# Value of unbypassed emitter resistance.
Re_un = (Rco /float(A) - Re_int )
# Value of bypassed emitter resistor.
Re_byp = (Rc / 10.0) - Re_un
if Re_byp < 0.0:
    Re_byp = 0.0
# Approximate input impedance.
Zin = 1.0 / ((1.0 / R1) + (1.0 / R2) + (1.0 / (Beta * (Re_int + Re_un))))
# Input capacitor.
C1 = 0.159 / (F1 + Zin)
# Output capacitor.
C2 = 0.159 / (F1 * RL)
# Value of bypass capacitor
if Re_byp != 0.0:
    C3 = 1.59 / ((F1 / 2.0 ) * (Re_int + Re_un))


###############
# Print Output
print("R1 - Resistor ", str(R1), "Ohms")
print("R2 - Resistor", str(R2), "Ohms")
print("re - Unbypassed emitter resistor ", str(Re_un), "Ohms")
print("Re - Bypassed emitter resistor ", str(Re_byp), "Ohms")

print("C1 - Input capacitor ", str(C1), "Farads")
print("C2 - Output capacitor ", str(C2), "Farads")
if Re_byp == 0.0:
    print("There no need for a bypass capacitor")
else:
    print("C3 - Bypass capacitor greater than ", str(C3), "Farads")

print("Zin Input Impedance", str(Zin), "Ohms")




























