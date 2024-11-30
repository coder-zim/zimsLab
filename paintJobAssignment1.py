# Coder: Zim (aka b3nd0r)
# Paint Job w/ Function Output

# - Import python math module.
import math

# - Set input validation.
def getFloatInput(sPrompt):
    fInput = 0
    while fInput <= 0:
        try:
            fInput = float( input(sPrompt) )
            if fInput < 0:
                print("Input Must Be Positive.")
            else:          
                break                 
        except ValueError:
            print("Must Be a Positive Numeric Value.")
    return fInput

# - Define functions for each input (make sure round up for Paint & to set sales tax).
def getGallonsPaint(fWall_SqFt, fFt_Per_Gal):
    return math.ceil(fWall_SqFt / fFt_Per_Gal)

def getLaborHours(fLabor_Hrs_Per_Gal, iTotal_Gallons):
    return fLabor_Hrs_Per_Gal * iTotal_Gallons

def getPaintCost(iTotal_Gallons, fPaintPrice):
    return fPaintPrice * iTotal_Gallons

def getLaborCost(fLabor_Hrs_Per_Gal, fPaint_Labor_Per_Hr, iTotal_Gallons):
    return (fLabor_Hrs_Per_Gal * fPaint_Labor_Per_Hr) * iTotal_Gallons

def getSalesTax(sJob_State):
    fTax = 0
    if sJob_State == "MA":
        fTax = .0625
    elif sJob_State == "CT" or sJob_State == "VT":
        fTax = .06
    elif sJob_State == "ME":
        fTax = .085
    elif sJob_State == "RI":
        fTax = .07
    else:
        fTax = 0.0
    return fTax
        
# - Call and print results of cost estimate.
def showCostEstimate(iTotal_Gallons, fLabor_Hours, fPaintPrice, fLaborCost, fTax_Amount, fTotal_Cost):
    print(f"Gallons of paints: {iTotal_Gallons}")
    print(f"Hours of labor: {fLabor_Hours}")
    print(f"Paint charges: {fPaintPrice}")
    print(f"Labor charges: {fLaborCost}")
    print(f"Tax amount: {fTax_Amount}")
    print(f"Total cost: {fTotal_Cost}")

# - Main function / input code - connected with validation function.
def main():
    
    fWall_SqFt = getFloatInput("Enter the Square Feet of the Wall: ")
    fPaintPrice = getFloatInput("Enter the Paint Price: ")
    fFt_Per_Gal = getFloatInput("Enter the Feet per Gallon of Paint: ")
    fLabor_Hrs_Per_Gal = getFloatInput("Enter the Labor Hours per Gallon of Paint: ")
    fPaint_Labor_Per_Hr = getFloatInput("Enter the Painting Labor Charge per Hour: ")
    iTotal_Gallons = getGallonsPaint(fWall_SqFt, fFt_Per_Gal)
    fLabor_Hours = getLaborHours(fLabor_Hrs_Per_Gal, iTotal_Gallons)
    fPaintPrice = getPaintCost(iTotal_Gallons, fPaintPrice)
    fLaborCost = getLaborCost(fLabor_Hrs_Per_Gal , fPaint_Labor_Per_Hr, iTotal_Gallons)

# - Set variables and calculate for output.
    sJob_State = input("What State will the job take place in: ").upper()
    fTax_Rate = getSalesTax(sJob_State)
    sLast_Name = input("What is the customer's Last Name: ")
    fGross_Total = fPaintPrice + fLaborCost
    fTax_Amount = fGross_Total * fTax_Rate
    fTotal_Cost = fGross_Total + fTax_Amount

# - Call function in order to produce file and print for the customer.
    showCostEstimate(iTotal_Gallons, fLabor_Hours, fPaintPrice, fLaborCost, fTax_Amount, fTotal_Cost)
    with open(f"{sLast_Name}PaintJobOutput.txt", "w") as f:
        f.write(f"Gallons of paints: {iTotal_Gallons}\n")
        f.write(f"Hours of labor: {fLabor_Hours}\n")
        f.write(f"Paint charges: {fPaintPrice}\n")
        f.write(f"Labor charges: {fLaborCost}\n")
        f.write(f"Tax amount: {fTax_Amount}\n")
        f.write(f"Total cost: {fTotal_Cost}\n")

    print(f"File: {sLast_Name}_PaintJobOutput.txt was created.")     
    
main()




