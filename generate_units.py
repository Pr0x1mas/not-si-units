# REGENERATES UNITS FROM CSV FILES, LIQUID REPLACES JS TO MAKE UNITS STATIC

import csv
from os import close, remove, path

with open('base.csv', encoding="utf8") as base:
    baseReader = csv.reader(base, delimiter=",")
    for row in baseReader:
        row += ['undefined'] * (6 - len(row))
        print(row)
        newUnitFileName = "_units/" + row[3] + ".md"
        if not path.isfile(newUnitFileName):
            with open(newUnitFileName, "a", encoding="utf8") as newUnit:
                newUnit.write("---\n")
                newUnit.write("base: true" + "\n")
                newUnit.write("measurement: " + row[0].replace("_", " ") + "\n")
                newUnit.write("si: " + row[1].replace("_", " ") + "\n")
                newUnit.write("siUnit: " + row[2].replace("_", " ") + "\n")
                newUnit.write("name: " + row[3].replace("_", " ") + "\n")
                newUnit.write("unit: " + row[4].replace("_", " ") + "\n")
                newUnit.write("ratio: " + row[5].replace("_", " ") + "\n")
                newUnit.write("---\n")
            newUnit.close()

base.close()

with open('units.csv', encoding="utf8") as units:
    unitsReader = csv.reader(units, delimiter=",")
    for row in unitsReader:
        row += ['undefined'] * (6 - len(row))
        print(row)
        newUnitFileName = "_units/" + row[3] + ".md"
        if not path.isfile(newUnitFileName):
            with open(newUnitFileName, "a", encoding="utf8") as newUnit:
                newUnit.write("---\n")
                newUnit.write("base: false" + "\n")
                newUnit.write("measurement: " + row[0].replace("_", " ") + "\n")
                newUnit.write("si: " + row[1].replace("_", " ") + "\n")
                newUnit.write("siUnit: " + row[2].replace("_", " ") + "\n")
                newUnit.write("name: " + row[3].replace("_", " ") + "\n")
                newUnit.write("unit: " + row[4].replace("_", " ") + "\n")
                newUnit.write("ratio: " + row[5].replace("_", " ") + "\n")
                newUnit.write("---\n")
            newUnit.close()

units.close()
remove("_units/equivalent.md")