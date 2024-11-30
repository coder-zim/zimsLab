# Coder: Zim (aka b3nd0r)
# Lists and Real Estate Analyzer

#import stat module
import statistics

#setup input validation function
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

#median function 
def getMedian(list):
    
    iListLength = len(list)
    if iListLength % 2 == 0:
        value1 = list[iListLength // 2]
        value2 = list[iListLength // 2 -1]
        result = (value1 + value2) / 2

    else:
        result = list[iListLength // 2]
    return result

#main function (input / continue[y or n])
def main():

    lstSales = []
    
    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        lstSales.append(fSalesPrice)

        sUserChoice = input("Enter another value Y or N: ").lower()
        while sUserChoice not in ['y', 'n']:
            sUserChoice = input("Enter another value Y or N: ").lower()

        if sUserChoice == 'n':
            break

#organize list and set counter
    lstSales.sort()
    iNumber = 1
    for x in lstSales:
        print(f"Property #{iNumber}: ${x:,.2f}")
        iNumber += 1

    fTotal = sum(lstSales)
    fCommission = fTotal * .03

#print results
    print(f"Minimum:     ${min(lstSales):,.2f}")
    print(f"Maximum:     ${max(lstSales):,.2f}")
    print(f"Total:       ${fTotal:,.2f}")
    print(f"Average:     ${statistics.mean(lstSales):,.2f}")
    print(f"Median:      ${getMedian(lstSales):,.2f}")
    print(f"Commission:  ${fCommission:,.2f}")

#main funciton call
main()





