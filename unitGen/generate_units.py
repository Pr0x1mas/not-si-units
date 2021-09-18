# REGENERATES UNITS FROM CSV FILES, LIQUID REPLACES JS TO MAKE UNITS STATIC

import csv
import os

print(os.getcwd())

with open('unitGen/base.csv', encoding="utf8") as base:
    baseReader = csv.reader(base, delimiter=",")
    for row in baseReader:
        row += ['undefined'] * (6 - len(row))
        print(row)
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
                newUnit.write(oldUnitContent)
            except Exception:
                pass
        newUnit.close()

base.close()

with open('unitGen/units.csv', encoding="utf8") as units:
    unitsReader = csv.reader(units, delimiter=",")
    for row in unitsReader:
        row += ['undefined'] * (6 - len(row))
        print(row)
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

            newUnit.write("ratio: " + row[5].replace("_", " ") + "\n")
            newUnit.write("---\n")
            newUnit.write(oldUnitContent)
        newUnit.close()

units.close()
os.remove("_units/equivalent.md")