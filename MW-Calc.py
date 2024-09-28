AtomicDataList=['H', 1.00797, 'He', 4.0026, 'Li', 6.941, 'Be', 9.01218, 'B',\
                10.81, 'C', 12.011, 'N', 14.0067, 'O', 15.9994, 'F', 18.998403\
                , 'Ne', 20.179, 'Na', 22.98977, 'Mg', 24.305, 'Al', 26.98154, \
                'Si', 28.0855, 'P', 30.97376, 'S', 32.06, 'Cl', 35.453, 'K', \
                39.0983, 'Ar', 39.948, 'Ca', 40.08, 'Sc', 44.9559, 'Ti', 47.9,\
                'V', 50.9415, 'Cr', 51.996, 'Mn', 54.938, 'Fe', 55.847, 'Ni', \
                58.7, 'Co', 58.9332, 'Cu', 63.546, 'Zn', 65.38, 'Ga', 69.72, \
                'Ge', 72.59, 'As', 74.9216, 'Se', 78.96, 'Br', 79.904, 'Kr', \
                83.8, 'Rb', 85.4678, 'Sr', 87.62, 'Y', 88.9059, 'Zr', 91.22, \
                'Nb', 92.9064, 'Mo', 95.94, 'Tc', 98.0, 'Ru', 101.07, 'Rh', \
                102.9055, 'Pd', 106.4, 'Ag', 107.868, 'Cd', 112.41, 'In', \
                114.82, 'Sn', 118.69, 'Sb', 121.75, 'I', 126.9045, 'Te', \
                127.6, 'Xe', 131.3, 'Cs', 132.9054, 'Ba', 137.33, 'La', \
                138.9055, 'Ce', 140.12, 'Pr', 140.9077, 'Nd', 144.24, 'Pm', \
                145.0, 'Sm', 150.4, 'Eu', 151.96, 'Gd', 157.25, 'Tb', 158.9254\
                , 'Dy', 162.5, 'Ho', 164.9304, 'Er', 167.26, 'Tm', 168.9342, \
                'Yb', 173.04, 'Lu', 174.967, 'Hf', 178.49, 'Ta', 180.9479, 'W'\
                , 183.85, 'Re', 186.207, 'Os', 190.2, 'Ir', 192.22, 'Pt', \
                195.09, 'Au', 196.9665, 'Hg', 200.59, 'Tl', 204.37, 'Pb', \
                207.2, 'Bi', 208.9804, 'Po', 209.0, 'At', 210.0, 'Rn', 222.0, \
                'Fr', 223.0, 'Ra', 226.0254, 'Ac', 227.0278, 'Pa', 231.0359, \
                'Th', 232.0381, 'Np', 237.0482, 'U', 238.029, 'Pu', 242.0, \
                'Am', 243.0, 'Bk', 247.0, 'Cm', 247.0, 'No', 250.0, 'Cf', \
                251.0, 'Es', 252.0, 'Hs', 255.0, 'Mt', 256.0, 'Fm', 257.0, \
                'Md', 258.0, 'Lr', 260.0, 'Rf', 261.0, 'Bh', 262.0, 'Db', \
                262.0, 'Sg', 263.0, 'Uun', 269.0, 'Uuu', 272.0, 'Uub', 277.0]
def normalize(string): #turns input into a list made of strings and integers
# In examples " * " is wildcard, meaning any letter or digit
    NormString=[]
#    print("NormString:",NormString)
#    print("string:",string)
    for i in range(len(string)-1,3,-1):
        if string[i].isdigit() and string[i-1].isdigit() and string[i-2].isdigit() and string[i-3].isdigit():
            print("the code will not calculate atom quantities greater than 999")
            NormString="error"
            break
    if string[0].isdigit():
        print("First character was a number. Molecular Formulas begin with an atom")
        NormString="error"
    while True:
        if NormString == "error":
            break
        elif len(string) > 3:
#            print("len of string > 3")
            if string[0].isupper() and string[1].islower() and (string[2].isupper() or string[2].isdigit()): #Example NeF or Ne5
                NormString.append(string[0:2])
#                print("ran if 1")
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isupper() and string[1].islower() and string[2].islower(): #Example Uun
#                print("ran if 2")
                NormString.append(string[0:3])
                string=string[3:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isupper() and (string[1].isupper() or string[1].isdigit()): #Example FG or F5
#                print("ran if 3")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].islower(): #exmaple f
                NormString="error"
                print("invalid input: lowercase letter out of place")
                break
            elif string[0].isdigit() and string[1].isupper(): #Example 3F
#                print("ran if 4")
                NormString.append(string[0])
                string=string[0+1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isdigit() and string[2].isdigit(): #Example 108
#                print("ran if 5")
                NormString.append(string[0:3])
                string=string[3:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isdigit() and string[2].isupper():  #Example 12H
#                print("ran if 6")
                NormString.append(string[0:2])
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            else: 
                print("unaccounted method: program could not parse your input")
                NormString="error"
                break
        elif len(string) == 3:
#            print("len of string is 3")
            if string[0].isupper() and string[1].islower() and string[2].islower(): #Example Uun
                NormString.append(string[0:3])
#                print("ran if 7")
                string=string[3:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isupper() and string[1].islower() and (string[2].isdigit() or string[2].isupper()): #Example Ne5 or NeF
#                print("ran if 8")
                NormString.append(string[0:2])
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isupper(): #Example 5F*
#                print("ran if 9")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isdigit() and string[2].isdigit(): #Example 100
                NormString.append(string[0:3])
#                print("ran if 10")
                string=string[3:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isdigit() and string[2].isupper(): #Example 55F
#                print("ran if 11")
                NormString.append(string[0:2])
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isupper() and (string[1].isupper() or string[1].isdigit()): #Example FG* or F5*
#                print("ran if 12")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            else:
                print("unaccounted method: program could not parse your input")
                NormString="error"
                break
        elif len(string) == 2:
#            print("len of string is 2")
            if string[0].isupper() and string[1].islower(): #Example Ne
#                print("ran if 13")
                NormString.append(string[0:2])
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isupper() and (string[1].isupper() or string[1].isdigit): #Example FH or F5
#                print("ran if 14")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isdigit(): #Example 12
#                print("ran if 15")
                NormString.append(string[0:2])
                string=string[2:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            elif string[0].isdigit() and string[1].isupper(): #Example 3F
#                print("used if 16")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            else:
                print("unaccounted method: program could not parse your input")
                NormString="error"
                break
        elif len(string) == 1:
#            print("len of string is 1")
            if string[0].isupper() or string[0].isdigit(): #Example F or 5
#                print("ran if 17")
                NormString.append(string[0])
                string=string[1:len(string)]
#                print("NormString:",NormString)
#                print("string:",string)
            else:
                print("unaccounted method: program could not parse your input")
                NormString="error"
                break
        elif len(string) == 0:
#            print("normalizing done")
            break
    return NormString

def Calculator(Listification):
    k=0
    TotalMW=0
    one=[1]
    SaveFront=''
    SaveBack=''
#    print(Listification)
    while k < len(Listification)-1:
#        print("k =",k)
        if type(Listification[k]) == float and type(Listification[k+1]) == float:
            SaveFront=Listification[0:k+1]
            SaveBack=Listification[k+1:len(Listification)]
            Listification=SaveFront+one+SaveBack
            k+=2
#            print("k+=2")
        else: 
            k+=1
#            print("k+=1")
    if type(Listification[len(Listification)-1]) == float:
        SaveFront=Listification[0:len(Listification)]
        Listification=SaveFront+one
#    print(Listification)
    for i in range(0,len(Listification),2):
        TotalAW=Listification[i]*Listification[i+1]
        TotalMW=TotalMW+TotalAW
    return TotalMW

def Listificate(Formula): #main function
    AtomicDataList=['H', 1.00797, 'He', 4.0026, 'Li', 6.941, 'Be', 9.01218, 'B',\
                10.81, 'C', 12.011, 'N', 14.0067, 'O', 15.9994, 'F', 18.998403\
                , 'Ne', 20.179, 'Na', 22.98977, 'Mg', 24.305, 'Al', 26.98154, \
                'Si', 28.0855, 'P', 30.97376, 'S', 32.06, 'Cl', 35.453, 'K', \
                39.0983, 'Ar', 39.948, 'Ca', 40.08, 'Sc', 44.9559, 'Ti', 47.9,\
                'V', 50.9415, 'Cr', 51.996, 'Mn', 54.938, 'Fe', 55.847, 'Ni', \
                58.7, 'Co', 58.9332, 'Cu', 63.546, 'Zn', 65.38, 'Ga', 69.72, \
                'Ge', 72.59, 'As', 74.9216, 'Se', 78.96, 'Br', 79.904, 'Kr', \
                83.8, 'Rb', 85.4678, 'Sr', 87.62, 'Y', 88.9059, 'Zr', 91.22, \
                'Nb', 92.9064, 'Mo', 95.94, 'Tc', 98.0, 'Ru', 101.07, 'Rh', \
                102.9055, 'Pd', 106.4, 'Ag', 107.868, 'Cd', 112.41, 'In', \
                114.82, 'Sn', 118.69, 'Sb', 121.75, 'I', 126.9045, 'Te', \
                127.6, 'Xe', 131.3, 'Cs', 132.9054, 'Ba', 137.33, 'La', \
                138.9055, 'Ce', 140.12, 'Pr', 140.9077, 'Nd', 144.24, 'Pm', \
                145.0, 'Sm', 150.4, 'Eu', 151.96, 'Gd', 157.25, 'Tb', 158.9254\
                , 'Dy', 162.5, 'Ho', 164.9304, 'Er', 167.26, 'Tm', 168.9342, \
                'Yb', 173.04, 'Lu', 174.967, 'Hf', 178.49, 'Ta', 180.9479, 'W'\
                , 183.85, 'Re', 186.207, 'Os', 190.2, 'Ir', 192.22, 'Pt', \
                195.09, 'Au', 196.9665, 'Hg', 200.59, 'Tl', 204.37, 'Pb', \
                207.2, 'Bi', 208.9804, 'Po', 209.0, 'At', 210.0, 'Rn', 222.0, \
                'Fr', 223.0, 'Ra', 226.0254, 'Ac', 227.0278, 'Pa', 231.0359, \
                'Th', 232.0381, 'Np', 237.0482, 'U', 238.029, 'Pu', 242.0, \
                'Am', 243.0, 'Bk', 247.0, 'Cm', 247.0, 'No', 250.0, 'Cf', \
                251.0, 'Es', 252.0, 'Hs', 255.0, 'Mt', 256.0, 'Fm', 257.0, \
                'Md', 258.0, 'Lr', 260.0, 'Rf', 261.0, 'Bh', 262.0, 'Db', \
                262.0, 'Sg', 263.0, 'Uun', 269.0, 'Uuu', 272.0, 'Uub', 277.0]
    NormString=normalize(Formula)
    MolecularWeight=''
    if NormString == "error":
        MolecularWeight=NormString
    else:
        NormList=NormString
        for i in range(0,len(NormString)):
            if NormString[i].isdigit():
#                print(NormString[i],"is a number")
                NormList[i]=int(NormString[i])
            elif NormString[i][0].isupper():
#                print(NormString[i][0], "is uppercase")
                for j in range(0,len(AtomicDataList),2):
                    if NormString[i] == AtomicDataList[j]:
                        NormList[i] = AtomicDataList[j+1]
#                        print(NormList[i])
                        break
                    elif j == len(AtomicDataList)-2:
                        MolecularWeight="error"
                        break
        if MolecularWeight == "error":
            print("invalid input: Your input did not match any known elements")
        else:
            MolecularWeight=Calculator(NormList)
    return print("Molecular Weight is:", MolecularWeight)

def MW(Formula): #main function
    NormString=normalize(Formula)
    MolecularWeight=''
    if NormString == "error":
        MolecularWeight=NormString
    else:
        NormList=NormString
        for i in range(0,len(NormString)):
            if NormString[i].isdigit():
#                print(NormString[i],"is a number")
                NormList[i]=int(NormString[i])
            elif NormString[i][0].isupper():
#                print(NormString[i][0], "is uppercase")
                for j in range(0,len(AtomicDataList),2):
                    if NormString[i] == AtomicDataList[j]:
                        NormList[i] = AtomicDataList[j+1]
#                        print(NormList[i])
                        break
                    elif j == len(AtomicDataList)-2:
                        MolecularWeight="error"
                        break
        if MolecularWeight == "error":
            MolecularWeight=0.00
            print("invalid input: Your input did not match any known elements")
        else:
            MolecularWeight=Calculator(NormList)
    return MolecularWeight

def Main():
    string1="start"
    print('Welcome! Type "Help" for valid formula rules or "Exit" to quit.')
    run=0
    while True:
        if run == 0: 
            string1=input("Enter the Formula Here: ")
            run+=1
        else: string1=input("Input next formula: ")
        if string1 == "Exit" or "exit" or "Quit" or "quit" or "stop":    
            break
        elif string1 == "Help":
            print("You may only enter symbols for elements between Hydrogen and "\
                  "Ununbiium. Do not enter a number as the first character of "\
                  "your formula. Also, you may only have up to 999 of a atom. For"\
                  "example, if you ask for C499H1000, you will get an error. I "\
                  "cannot fathom needing 1000 of an atom. The formulas do not "\
                  "need to be 'real' molecules; any combination atoms and amounts"\
                  "(under 1000) will work. Example:FNe10C5I5Be10Y. If you get the"\
                  "'unaccounted method' error, you probably have a typo(like a "\
                  "lowercase letter that should be uppercase). If you're certain "\
                  "you don't have a typo, it's probably a problem with the code."\
                  "Let me know, I guess. If you want to change the molecular "\
                  "weight an atom uses, open the .py in a text editor an make "\
                  "your changes on the 7th and following lines. All you need to "\
                  "do is change the number after the atomic symbol for the "\
                  "element you wish to change. For example, I could change 'H', "\
                  "1.00797 to 'H', 1.008 and the code will now use 1.008 for the"\
                  " atomic weight of hydrogen")
        else:
            Listificate(string1)
            continue
if __name__ == "__main__":
    Main()
