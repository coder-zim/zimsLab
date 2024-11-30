# Coder: Zim (aka b3nd0r)
# Grade Analyzer

# -Step 1: Import math operations
import math

# -Step 2: Acquire name of user
sName = str(input("Enter the person whose grades are being analyzed: "))

# -Step 3: Acquire the 4 test scores, one at a time
print("Enter your test scores: ")
iTest1 = int(input("Test #1: "))
iTest2 = int(input("Test #2: "))
iTest3 = int(input("Test #3: "))
iTest4 = int(input("Test #4: "))

# -Step 4: Make sure tests are within range 0-100
if iTest1 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest2 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest3 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

# -Step : Create variable of total sum of scores
iTotTestSum = iTest1 + iTest2 + iTest3 + iTest4
iTotTestAvg = iTotTestSum / 4

# -Step : Create variable of lowest score to drop
if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
    iLowestTestScore = iTest1
if iTest2 < iTest1 and iTest2 < iTest3 and iTest2 < iTest4:
    iLowestTestScore = iTest2
if iTest3 < iTest1 and iTest3 < iTest2 and iTest3 < iTest4:
    iLowestTestScore = iTest3
else:
    iLowestTestScore = iTest4
print(iLowestTestScore)
# -Step : Assign values to variables for ease of function
# iNewTestSum = iTotTestSum - iLowestTestScore
# iNewTestAvg = iNewTestSum / 3
    
# -Step : Inquire if user wishes to drop a test
sDropLowest = str(input("Do you wish to drop your lowest grade? [Y or N]: "))
if sDropLowest == "Y" or "y":
    iFinalTestAvg = iTotTestSum - iLowestTestScore
    print("Dropped your lowest score.")

elif sDropLowest == "N" or "n":
        iFinalTestAvg = iTotTestSum / 4
        print("Did not drop your lowest score.")
#if sDropLowest != "Y" or "N" or "y" or "n":
#    print("Must choose Y or N to drop your lowest score")
#    raise SystemExit
    
# -Step : Find letter grade average
if iFinalTestAvg >= 90 and iFinalTestAvg <= 100:
    print("Your letter grade average: A")
if iFinalTestAvg <= 89 and iFinalTestAvg >= 80:
    print("Your letter grade average: B")
if iFinalTestAvg <= 79 and iFinalTestAvg >= 70:
    print("Your letter grade average: C")
if iFinalTestAvg <= 69 and iFinalTestAvg >= 60:
    print("Your letter grade average: D")
if iFinalTestAvg < 59:
    print("Your letter grade average: F")



