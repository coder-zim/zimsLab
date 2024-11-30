# Coder: Zim (aka b3nd0r)
# BMI Analyzer Code

# -Step 1: Greet User and specify program
print("Welcome to Matty Sim's Body Mass Index Analyzer!")

# -Step 2: Acquire name
sName = str(input("\nFirst, enter your name: "))

# -Step 3: Reply with name and acquire weight (lbs)
fHeight = float(input("Greetings, " + sName + "! \nNext, provide your Height in Inches: "))

# -Step 4: Acquire height (inches)
fWeight = float(input("And lastly, provide your Weight in Pounds: "))

# -Step 5: Convert pounds to kilos and inches to meters
fHeightMeters = fHeight / 39.36
fWeightKilos = fWeight / 2.2

# -Step 6: Create variable for ease of functionality
fHeightMetersSq = fHeightMeters ** 2

# -Step 7: Calculate Body Mass Index using provided info
fBMI = float(fWeightKilos / (fHeightMetersSq))

# -Step 8: Display results for user
print(sName + "'s calculated BMI is: " + (format(fBMI,"1.2f")))

# -Step 9: Run an if loop to determine BMI category and display result to user
if fBMI < 18.50:
    print("BMI finding that subject is: Underweight")
    
if fBMI >= 18.51 and fBMI <= 24.90:
        print("BMI finding that subject is: Normal")

if fBMI >= 24.91 and fBMI <= 29.90:
        print("BMI finding that subject is: Overweight")

if fBMI >= 29.91:
    print("BMI finding that subject is: Obese")

