# REGENERATES UNITS FROM CSV FILES, LIQUID REPLACES JS TO MAKE UNITS STATIC

import csv
import os

print("--------------------------------")

print(os.getcwd())

def getRatio(formula): # do I need a function for this? Probably not but I anticipated this being more complicated
    try:
        return(str(eval(formula))) ## literally just parse the formula as code and it works itself out :pog:
    except Exception as e: # if there is no formula to derive it such as radians. Should have just put 'None' but I like my shruggies
        print("cannot determine ratio from " + row[1])
        print("ERROR: " + str(e) + " on unit " + row[1])
        return "undefined"

# IMPORT BASE UNITS
with open('unitGen/base.csv', encoding="utf8") as base:
    baseReader = csv.reader(base, delimiter=",")
    for row in baseReader:
        row += ['undefined'] * (6 - len(row)) # pad out each row with 'undefined' if a column is not populated
        newUnitFileName = "_units/" + row[3] + ".md" # generate path to page because jekyll is a bitch and can't do it itself (or I forgot to set the permalink parameter but I'll deal with that eventually). Either way it's useful for file operations here
        oldUnitContent = ""
        if os.path.isfile(newUnitFileName): # check if file already exists
            with open(newUnitFileName, "r", encoding="utf8") as oldUnit: # store old description content
                frontMatterCount = 0
                for line in oldUnit:  # skip front matter
                    if '---' in line:
                        frontMatterCount += 1
                    if frontMatterCount == 2 and not '---' in line: # store content
                        oldUnitContent += line
            oldUnit.close()
            os.remove(newUnitFileName) # delete file



        with open(newUnitFileName, "a", encoding="utf8") as newUnit: # create new file
            # write front matter
            newUnit.write("---\n")
            newUnit.write("base: true" + "\n")
            newUnit.write("layout: unit" + "\n")
            newUnit.write("measurement: " + row[0].replace("_", " ") + "\n")
            newUnit.write("si: " + row[1].replace("_", " ") + "\n")
            newUnit.write("siUnit: " + row[2].replace("_", " ") + "\n")
            newUnit.write("name: " + row[3].replace("_", " ") + "\n")
            newUnit.write("unit: " + row[4].replace("_", " ") + "\n")

            newUnit.write("urlName: units/" + row[3] + "\n")

            newUnit.write("ratio: " + row[5].replace("_", " ") + "\n")

            newUnit.write("---\n")

            try:
                exec(row[2] + " = float('" + row[5] + "')") # yes I'm using exec(), fuck you. This creates variables for each base unit so I can calculate ratios later on
            except Exception as e:
                print("ERROR: " + str(e) + " on unit " + row[1])

            try:
                newUnit.write(oldUnitContent) # write the existing description content if it exists
            except Exception:
                pass
        newUnit.close()

base.close()
print("---")

# IMPORT MAIN UNITS
# LITERALLY THE SAME CODE AGAIN SO NO REPEATED COMMENTS, READ IT YOURSELF
with open('unitGen/units.csv', encoding="utf8") as units:
    unitsReader = csv.reader(units, delimiter=",")
    for row in unitsReader:
        row += ['undefined'] * (6 - len(row))
        newUnitFileName = "_units/" + row[3] + ".md"
        oldUnitContent = ""
        if os.path.isfile(newUnitFileName):
            with open(newUnitFileName, "r", encoding="utf8") as oldUnit:
                frontMatterCount = 0
                for line in oldUnit:
                    if '---' in line:
                        frontMatterCount += 1
                    if frontMatterCount == 2 and not '---' in line:
                        oldUnitContent += line
            oldUnit.close()
            os.remove(newUnitFileName)

        with open(newUnitFileName, "a", encoding="utf8") as newUnit:
            newUnit.write("---\n")
            newUnit.write("layout: unit" + "\n")
            newUnit.write("base: false" + "\n")
            newUnit.write("measurement: " + row[0].replace("_", " ") + "\n")
            newUnit.write("si: " + row[1].replace("_", " ") + "\n")
            newUnit.write("siUnit: " + row[2].replace("_", " ") + "\n")
            newUnit.write("name: " + row[3].replace("_", " ") + "\n")
            newUnit.write("unit: " + row[4].replace("_", " ") + "\n")

            newUnit.write("urlName: units/" + row[3] + "\n")

            newUnit.write("ratio: " + getRatio(row[5]) + "\n") # get the ratio using the formula
            newUnit.write("---\n")
            newUnit.write(oldUnitContent)
        newUnit.close()

units.close()
os.remove("_units/equivalent.md")