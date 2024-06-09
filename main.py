# importing required libraries
import os
import hashlib

# function - returns the md5 hash of the file 
def applyHash(file):
    
    # opens the file to read
    openedFile = open(file)
    readFile = openedFile.read()
    
    # returns the hexidecimal format of the MD5 hash
    md5Hash = hashlib.md5( readFile.encode() )
    return (md5Hash.hexdigest())

# function - checks integrity of the files in the baseline
def checkIntegrity():
    
    # opens the baseline.txt file
    baselineFile = open('baseline.txt', 'r')
   
    # iterates through every line in the baseline file
    for line in baselineFile.readlines():
       
        # applies the hashing function to the file in the line
        currentHash = applyHash( (line.split('|')[0]) )
       
        # if the hash generated does not match the hash stored in the baseline file, notify the user
        if not currentHash == line.split('|')[1]:
            print("file: " + line.split('|')[0] +" has been altered.")
        else:
            print("file: " + line.split('|')[0] +" has remained the same.")


# function - adds a file and its MD5 hash to the baseline.txt file
def addFile(): 
    
    directory = input("Enter the FULL path of the file to add to the baseline. ")
    
    # attempts to hash the specified file, and store the file path with its hash in the baseline.txt file, displays an error message if unable to do so
    try: 
        hashedFile = applyHash(directory)
        with open("baseline.txt", "a") as baseline:
            baseline.write(directory + "|" + hashedFile +"\n")
        print("Successfully added file to the baseline")
    except:
        print("Invalid path")


# function - clears the baseline.txt file 
def wipeBaseline():
    open('baseline.txt', 'w').close()
    print("The baseline has been successfully wiped.")


print("File Integrity Analyzer")
print("""
Would you like to: 

      1. Check integrity of files in the baseline.
      2. Add a file to the baseline.
      3. Wipe the baseline.

      """)


validInput = False

# iteration - loop is broken once a valid input is entered
while not validInput:
    action = int(input("Enter the number of the action you would like to complete. "))  
    
    if action < 4 and action > 0:
        validInput = True
        
        # depending on the user input - loads the correct function
        match action:
            case 1:
                checkIntegrity() 
            case 2:
                addFile()
            case 3:
                wipeBaseline()
    else:
        print("Invalid Input")


