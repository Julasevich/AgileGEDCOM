# Project 02
from prettytable import PrettyTable

# Get file
gedFile = open("MyFamily.ged", "r")
# Acceptable tags
projectTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

individuals = []

namebool = False
idnum = " "

# Unique Family Values Container
families = []
currentFam = ''
currentMarr = ''
currentDiv = ''
currentHusb = ''
currentWife = ''
currentChildren = []
stillMarried = True

# Main loop
for line in gedFile:
    # Common Variables
    # Split words of line up, may come with spaces so must strip later
    words = line.split()

    if namebool:
        individuals.append([idnum, words[2], words[3]])
        namebool = False

    level = words[0]
    # Tag Line
    if level == "0":
        if len(words) >= 3:
            if words[2] == "INDI":
                idnum = words[1][1:-1]
                namebool = True
            tag = words[2]
            lineID = words[1]
            valid = ""
            if tag in projectTags:
                valid = "Y"
                if tag == "FAM":
                    if currentFam != '' and currentHusb != '' and currentWife != '':
                        if currentChildren == []:
                            currentChildren = "NA"
                        if currentDiv == '':
                            currentDiv = "NA"
                        addFam = [currentFam, currentMarr, currentDiv, currentHusb, currentWife, currentChildren]
                        families.append(addFam)
                        currentMarr = ''
                        currentDiv = ''
                        currentHusb = ''
                        currentWife = ''
                        currentChildren = []
                    currentFam = words[1]
            else:
                valid = "N"

            # Input
            print("--> " + line.strip())
            # Output
            print("<-- " + level.strip() + "|" + lineID.strip() + "|" + tag + "|" + valid.strip())
            # Space out pairings of i/o
            print("")
        else:
            tag = words[1]
            valid = ""
            if tag in projectTags:
                valid = "Y"
            else:
                valid = "N"
            # Input
            print("--> " + line.strip())
            # Output
            print("<-- " + level.strip() + "|" + tag + "|" + valid.strip())
            # Space out pairings of i/o
            print("")
    else:
        tag = words[1]
        valid = ""
        arguments = ""
        if len(words) >= 2:
            for word in words[2:]:
                arguments = arguments + " " + word
        else:
            arguments = ""
        if tag in projectTags:
            valid = "Y"
            if tag == "HUSB":
                currentHusb = words[2]
            elif tag == "WIFE":
                currentWife = words[2]
            elif tag == "CHIL":
                currentChildren.append(words[2])
            elif tag == "MARR":
                stillMarried = True
            elif tag == "DIV":
                stillMarried = False
            elif tag == "DATE":
                if stillMarried is True:
                    currentMarr = words[2:]
                else:
                    currentDiv = words[2:]

        else:
            valid = "N"
        # Input
        print("--> " + line.strip())
        # Output
        print("<-- " + level.strip() + "|" + tag.strip() + "|" + valid + "|" + arguments.strip())
        # Space out pairings of i/o
        print("")

# Close file
gedFile.close()

if currentFam != '' and currentHusb != '' and currentWife != '':
    if currentChildren == []:
        currentChildren = "NA"
    if currentDiv == '':
        currentDiv = "NA"
    addFam = [currentFam, currentMarr, currentDiv, currentHusb, currentWife, currentChildren]
    families.append(addFam)

# Print Individuals
print("Table of Unique Individuals")
for individual in individuals:
    print(individual[0] + " " + individual[1] + " " + individual[2])

print("")

# Print Family Table
FamIDs = []
MarrDates = []
DivDates = []
HusbIDs = []
WifeIDs = []
ChildrenIDs = []
HusbNames = []
WifeNames = []

for family in families:
    FamIDs.append(family[0][1:-1])
    MarrDates.append(family[1])
    DivDates.append(family[2])
    husbID = family[3][1:-1]
    HusbIDs.append(husbID)
    wifeID = family[4][1:-1]
    WifeIDs.append(wifeID)
    ChildrenIDs.append(family[5])
    husbName = ''
    wifeName = ''
    for individual in individuals:
        if individual[0] == husbID:
            husbName = individual[1] + " " + individual[2]
        elif individual[0] == wifeID:
            wifeName = individual[1] + " " + individual[2]
    HusbNames.append(husbName)
    WifeNames.append(wifeName)

famTable = PrettyTable()
famTable.add_column("ID", FamIDs)
famTable.add_column("Married", MarrDates)
famTable.add_column("Divorced", DivDates)
famTable.add_column("Husband ID", HusbIDs)
famTable.add_column("Husband Name", HusbNames)
famTable.add_column("Wife ID", WifeIDs)
famTable.add_column("Wife Name", WifeNames)
famTable.add_column("Children", ChildrenIDs)
print(famTable)
