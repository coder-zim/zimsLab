# Coder: Zim (aka b3nd0r)
# Interplanetary Weight Conversion

# -Step 1: Declare Named Constants for each of the planet Surface Gravity Factors
nMERCURY_GRAVITY_FACTOR = 0.38
nVENUS_GRAVITY_FACTOR = 0.91
nMOON_GRAVITY_FACTOR = 0.165
nMARS_GRAVITY_FACTOR = 0.38
nJUPITER_GRAVITY_FACTOR = 2.34
nSATURN_GRAVITY_FACTOR = 0.93
nURANUS_GRAVITY_FACTOR = 0.92
nNEPTUNE_GRAVITY_FACTOR = 1.12
nPLUTO_GRAVITY_FACTOR = 0.066

# -Step 2: Greet the user and prompt them for their name
# -Step 2.1: Prompt them for their 'Earth weight'
# -Step 2.2: Added room for easier reading
userName = str(input("Yet another comes to us for answers...tell us your name, Earthling: "))
fPounds = float(input("\nGreetings, " + userName + "! Please enter your Earth weight in pounds(lbs): "))

# -Step 3: Multiple the Earth Weight by each of the planet’s Surface Gravity Factor
fWeightMercury = fPounds * nMERCURY_GRAVITY_FACTOR
fWeightVenus = fPounds * nVENUS_GRAVITY_FACTOR
fWeightMoon = fPounds * nMOON_GRAVITY_FACTOR
fWeightMars = fPounds * nMARS_GRAVITY_FACTOR
fWeightJupiter = fPounds * nJUPITER_GRAVITY_FACTOR
fWeightSaturn = fPounds * nSATURN_GRAVITY_FACTOR
fWeightUranus = fPounds * nURANUS_GRAVITY_FACTOR
fWeightNeptune = fPounds * nNEPTUNE_GRAVITY_FACTOR
fWeightPluto = fPounds * nPLUTO_GRAVITY_FACTOR


# -Step 4: Display the information for the user, addressing them yet again
# -Step 4.1: Use an apostrophe and add a line in between for aesthetic appeal.
print('{:45}'.format("\nHere is your weight on each of your Solar System's celestial bodies, " + userName +": \n"))

# -Step 5: Display the conversion list of each of the planets (and the Moon) with their new weights
# -Step 5.1: Format it using the amount of preferred spacing (I chose 33 because it's a lucky number and it looked nice) 
print('{:20}'.format("Weight on Mercury:") , "{:10.2f}".format(fWeightMercury))
print('{:20}'.format("Weight on Venus:") , "{:10.2f}".format(fWeightVenus))
print('{:20}'.format("Weight on the Moon:") , "{:10.2f}".format(fWeightMoon))
print('{:20}'.format("Weight on Mars:") , "{:10.2f}".format(fWeightMars))
print('{:20}'.format("Weight on Jupiter:") , "{:10.2f}".format(fWeightJupiter))
print('{:20}'.format("Weight on Saturn:") , "{:10.2f}".format(fWeightSaturn))
print('{:20}'.format("Weight on Uranus:") , "{:10.2f}".format(fWeightUranus))
print('{:20}'.format("Weight on Neptune:") , "{:10.2f}".format(fWeightNeptune))
print('{:20}'.format("Weight on Pluto:") , "{:10.2f}".format(fWeightPluto))

# -Step 6: Complete program with some sort of ending
print("\nQuite fascinating, is it not?! Now, unless you have some food...be gone!")
