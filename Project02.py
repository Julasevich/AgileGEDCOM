from prettytable import PrettyTable
import time

months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10,
          "NOV": 11, "DEC": 12}
today = time.strftime("%Y %m %d")


def dateVal(date):
    return int(date[2]) * 10000 + months[date[1]] * 100 + int(date[0])


def deathBeforeBirth(birthday, deathday):
    '''US03 - Function to find any instances of death before birth'''
    if deathday == "NA":
        return False
    return dateVal(deathday) < dateVal(birthday)


def divBeforeMarr(marrDate, divDate):
    '''US04 - Function to find any instances of divorce before marriage.'''
    if divDate == "NA":
        return False
    else:
        return dateVal(divDate) < dateVal(marrDate)


def deathBeforeMarr(marrDate, indi):
    '''US05 - Function to find any instances of death before marriage.'''
    deathDate = individuals[indi]["death"]
    if deathDate == 'NA':
        return False
    return dateVal(deathDate) < dateVal(marrDate)


def deathBeforeDivorce(divDate, indi):
    '''US06 - Function to find any instances of death before divorce'''
    deathDate = individuals[indi]["death"]
    if deathDate == "NA":
        return False
    if divDate == "NA":
        return False
    return dateVal(deathDate) < dateVal(divDate)


def getAge(today, birthday, alive, deathday):
    '''Take today's date and compute an age.'''
    if alive:
        # Compute Age normally
        date = today.split()
        today_year = date[0]
        today_month = date[1]
        today_day = date[2]
        age = int(today_year) - int(birthday[2])
        age += (int(today_month) / 12.0) - (months[birthday[1]] / 12.0)
        age += (int(today_day) / 365.0) - (int(birthday[0]) / 365.0)
        return (int(age))
    else:
        # Compute Age up to death day
        death_year = deathday[2]
        death_month = months[deathday[1]]
        death_day = deathday[0]
        age = int(death_year) - int(birthday[2])
        age += (int(death_month) / 12.0) - (months[birthday[1]] / 12.0)
        age += (int(death_day) / 365.0) - (int(birthday[0]) / 365.0)
        return int(age)


def pastDate(date):
    '''
    Function that takes in a date and returns false if the date has not happened yet and true if it has.
    Input is taken as a list containing date information as stored in a GED file
    '''
    today = time.strftime("%Y %m %d").split()
    if date == "NA":
        return True
    if int(date[2]) < int(today[0]):
        return True
    elif int(today[0]) < int(date[2]):
        return False
    else:
        if months[date[1]] < int(today[1]):
            return True
        elif int(today[1]) < months[date[1]]:
            return False
        else:
            if int(today[2]) < int(date[0]):
                return False
            return True


def birthBfrMarr(fam, fid):
    '''
    Function that takes in a birth date and a marriage date and checks that the marriage occurs after the birth
    Input is taken as two string lists containing birth date and marriage date information as stored in a GED file
    '''
    marr = dateVal(fam["marrDate"])
    husb = dateVal(individuals[fam["husband"]]["birthday"])
    wife = dateVal(individuals[fam["wife"]]["birthday"])
    if marr < husb:
        print("ERROR: FAMILY: US02: " + addF(fid) + ": Husband (" + addi(fam["husband"]) + ") born on " + '-'.join(
            individuals[fam["husband"]]["birthday"]) + " after marriage on " + '-'.join(fam["marrDate"]))
    if marr < wife:
        print("ERROR: FAMILY: US02: " + addF(fid) + ": Wife (" + addi(fam["wife"]) + ") born on " + '-'.join(
            individuals[fam["wife"]]["birthday"]) + " after marriage on " + '-'.join(fam["marrDate"]))
    return


def checkBigamy(indi, marrDate, fam):
    marriages = individuals[indi]["spouse"]
    if individuals[indi]["sex"] == "M":
        spouse = "husband's ("
    else:
        spouse = "wife's ("
    for m in marriages:
        if divBeforeMarr(marrDate, families[m]["marrDate"]):
            if not divBeforeMarr(marrDate, families[m]["endDate"][0]):
                print("ERROR: FAMILY: US11: " + addF(fam) + ": Family married on " + '-'.join(
                    marrDate) + " before " + spouse + addi(indi) + ") marriage in family " + addF(
                    m) + " ended on " + '-'.join(families[m]["endDate"][0]))
    return





# Get file
gedFile = open("MyFamily.ged", "r")
# Acceptable tags
projectTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV",
               "DATE", "HEAD", "TRLR", "NOTE"]

# Unique Individual Values
individuals = {}
idNum = ''
indiFirstName = {"firstName": ''}
indiLastName = {"lastName": ''}
indiSex = {"sex": ''}
indiBirthday = {"birthday": ''}
indiAge = {"age": ''}
indiAlive = {"alive": True}
indiDeath = {"death": ''}
indiChild = {"child": ''}
indiSpouse = {"spouse": []}
birthday = False
deathday = False

# Unique Family Values
families = {}
famID = ''
currentMarr = {"marrDate": ''}
currentDiv = {"divDate": ''}
endDate = {"endDate": ['', '']}
currentHusb = {"husband": ''}
currentWife = {"wife": ''}
currentChildren = {"children": []}
stillMarried = True

# Main loop
for line in gedFile:
    # Common Variables
    # Split words of line up, may come with spaces so must strip later
    words = line.split()

    level = words[0]
    # Tag Line
    if level == "0":
        if len(words) >= 3:
            tag = words[2]
            lineID = words[1]
            valid = ""
            if tag in projectTags:
                valid = "Y"
                if tag == "INDI":
                    if indiFirstName["firstName"] != '' and indiLastName["lastName"] != '' and idNum != '':
                        if indiDeath["death"] == '':
                            indiDeath["death"] = "NA"
                        if indiChild["child"] == '':
                            indiChild["child"] = "NA"
                        if indiSpouse["spouse"] == []:
                            indiSpouse["spouse"] = "NA"
                        indiAge["age"] = getAge(today, indiBirthday["birthday"], indiAlive["alive"], indiDeath["death"])
                        # individuals.append([idnum, indiFirstName, indiLastName, indiSex, indiBirthday, indiAge, indiAlive, indiDeath, indiChild, indiSpouse])
                        # indiDict = {idNum: [indiFirstName, indiLastName, indiSex, indiBirthday, indiAge, indiAlive, indiDeath, indiChild, indiSpouse]}
                        indiDict = {idNum: {}}
                        indiDict[idNum].update(indiFirstName)
                        indiDict[idNum].update(indiLastName)
                        indiDict[idNum].update(indiSex)
                        indiDict[idNum].update(indiBirthday)
                        indiDict[idNum].update(indiAge)
                        indiDict[idNum].update(indiAlive)
                        indiDict[idNum].update(indiDeath)
                        indiDict[idNum].update(indiChild)
                        indiDict[idNum].update(indiSpouse)
                        individuals.update(indiDict)
                        indiFirstName["firstName"] = ''
                        indiLastName["lastName"] = ''
                        indiSex["sex"] = ''
                        indiAge["age"] = ''
                        indiAlive["alive"] = True
                        indiDeath["death"] = ''
                        indiChild["child"] = ''
                        indiSpouse["spouse"] = []
                    idNum = int(words[1][2:-1])
                elif tag == "FAM":
                    if famID != '' and currentHusb["husband"] != '' and currentWife["wife"] != '':
                        if currentChildren["children"] == []:
                            currentChildren["children"] = "NA"
                        if currentDiv["divDate"] == '':
                            currentDiv["divDate"] = "NA"
                        # addFam = [currentFam, currentMarr, currentDiv, currentHusb, currentWife, currentChildren, endDate]
                        # families.append(addFam)
                        famDict = {famID: {}}
                        famDict[famID].update(currentMarr)
                        famDict[famID].update(currentDiv)
                        famDict[famID].update(currentHusb)
                        famDict[famID].update(currentWife)
                        famDict[famID].update(currentChildren)
                        famDict[famID].update(endDate)
                        families.update(famDict)
                        currentMarr["marrDate"] = ''
                        currentDiv["divDate"] = ''
                        currentHusb["husband"] = ''
                        currentWife["wife"] = ''
                        currentChildren["children"] = []
                    famID = int(words[1][2:-1])
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
                currentHusb["husband"] = int(words[2][2:-1])
            elif tag == "WIFE":
                currentWife["wife"] = int(words[2][2:-1])
            elif tag == "CHIL":
                currentChildren["children"].append(int(words[2][2:-1]))
            elif tag == "MARR":
                stillMarried = True
            elif tag == "DIV":
                stillMarried = False
            elif tag == "DATE":
                if stillMarried is True and birthday is False and deathday is False:
                    currentMarr["marrDate"] = words[2:]
                elif birthday is False and deathday is False:
                    currentDiv["divDate"] = words[2:]
                elif deathday is False:
                    indiBirthday["birthday"] = words[2:]
                    birthday = False
                else:
                    indiDeath["death"] = words[2:]
                    deathday = False
            elif tag == "NAME":
                indiFirstName["firstName"] = words[2]
                indiLastName["lastName"] = words[3]
            elif tag == "SEX":
                indiSex["sex"] = words[2]
            elif tag == "BIRT":
                birthday = True
            elif tag == "DEAT":
                deathday = True
                indiAlive["alive"] = False
            elif tag == "FAMC":
                indiChild["child"] = words[2][1:-1]
            elif tag == "FAMS":
                indiSpouse["spouse"].append(int(words[2][2:-1]))
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

# Check if any new families are waiting to be added
if famID != '' and currentHusb["husband"] != '' and currentWife["wife"] != '':
    if currentChildren["children"] == []:
        currentChildren["children"] = "NA"
    if currentDiv["divDate"] == '':
        currentDiv["divDate"] = "NA"
    famDict = {famID: {}}
    famDict[famID].update(currentMarr)
    famDict[famID].update(currentDiv)
    famDict[famID].update(currentHusb)
    famDict[famID].update(currentWife)
    famDict[famID].update(currentChildren)
    famDict[famID].update(endDate)
    families.update(famDict)

# Check if any new individuals are waiting to be added
if indiFirstName["firstName"] != '' and indiLastName["lastName"] != '':
    if indiDeath["death"] == '':
        indiDeath["death"] = "NA"
    if indiChild["child"] == '':
        indiChild["child"] = "NA"
    if indiSpouse["spouse"] == []:
        indiSpouse["spouse"] = "NA"
    indiAge["age"] = getAge(today, indiBirthday["birthday"], indiAlive["alive"], indiDeath["death"])
    indiDict = {idNum: {}}
    indiDict[idNum].update(indiFirstName)
    indiDict[idNum].update(indiLastName)
    indiDict[idNum].update(indiSex)
    indiDict[idNum].update(indiBirthday)
    indiDict[idNum].update(indiAge)
    indiDict[idNum].update(indiAlive)
    indiDict[idNum].update(indiDeath)
    indiDict[idNum].update(indiChild)
    indiDict[idNum].update(indiSpouse)
    individuals.update(indiDict)

# Print Individuals Table
IndiIDs = []
IndiNames = []
IndiSexs = []
IndiBirthdays = []
IndiAges = []
IndiAlives = []
IndiDeaths = []
IndiChilds = []
IndiSpouses = []

individs = [value for (key, value) in sorted(individuals.items())]


def addi(x):
    return "I" + str(x)


def addF(x):
    return "F" + str(x)


rawIDs = list(individuals.keys())
IndiIDs = list(map(addi, sorted(rawIDs)))

for individual in individs:
    IndiNames.append(individual["firstName"] + " " + individual["lastName"])
    IndiSexs.append(individual["sex"])
    IndiBirthdays.append('-'.join(individual["birthday"]))
    IndiAges.append(individual["age"])
    IndiAlives.append(individual["alive"])
    if individual["death"] != "NA":
        IndiDeaths.append('-'.join(list(individual["death"])))
    else:
        IndiDeaths.append("NA")
    IndiChilds.append(individual["child"])
    if individual["spouse"] == "NA":
        IndiSpouses.append("NA")
    else:
        IndiSpouses.append(list(map(addF, individual["spouse"])))

indiTable = PrettyTable()
indiTable.add_column("ID", IndiIDs)
indiTable.add_column("Name", IndiNames)
indiTable.add_column("Sex", IndiSexs)
indiTable.add_column("Birthday", IndiBirthdays)
indiTable.add_column("Age", IndiAges)
indiTable.add_column("Alive", IndiAlives)
indiTable.add_column("Death", IndiDeaths)
indiTable.add_column("Child", IndiChilds)
indiTable.add_column("Spouse", IndiSpouses)
print(indiTable)
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

fams = [value for (key, value) in sorted(families.items())]
rawFIDs = list(families.keys())
FamIDs = list(map(addF, sorted(rawFIDs)))

for ID in families:
    MarrDates.append('-'.join(families[ID]["marrDate"]))
    if families[ID]["divDate"] == "NA":
        DivDates.append("NA")
    else:
        DivDates.append('-'.join(families[ID]["divDate"]))
    husbID = families[ID]["husband"]
    HusbIDs.append(addi(husbID))
    wifeID = families[ID]["wife"]
    WifeIDs.append(addi(wifeID))
    if families[ID]["children"] == "NA":
        ChildrenIDs.append("NA")
    else:
        ChildrenIDs.append(list(map(addi, families[ID]["children"])))
    husbName = ''
    wifeName = ''
    husbDeath = ''
    wifeDeath = ''
    husbName = individuals[husbID]["firstName"] + " " + individuals[husbID]["lastName"]
    husbDeath = individuals[husbID]["death"]
    wifeName = individuals[wifeID]["firstName"] + " " + individuals[wifeID]["lastName"]
    wifeDeath = individuals[wifeID]["death"]
    HusbNames.append(husbName)
    WifeNames.append(wifeName)
    if husbDeath == "NA" and wifeDeath == "NA":
        families[ID]["endDate"] = [families[ID]["divDate"], "Divorce"]
    elif husbDeath == "NA":
        families[ID]["endDate"] = [wifeDeath, "Wife"]
    elif wifeDeath == "NA":
        families[ID]["endDate"] = [husbDeath, "Husband"]
    else:
        if dateVal(husbDeath) > dateVal(wifeDeath):
            families[ID]["endDate"] = [wifeDeath, "Wife"]
        else:
            families[ID]["endDate"] = [husbDeath, "Husband"]

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

# Print individual errors
for indi in individuals:
    if not pastDate(individuals[indi]["birthday"]):
        print("ERROR: INDIVIDUAL: US01: " + addi(indi) + ": Birthday " + '-'.join(
            individuals[indi]["birthday"]) + " occurs in the future")
    if not individuals[indi]["alive"]:
        if not pastDate(individuals[indi]["death"]):
            print("ERROR: INDIVIDUAL: US01: " + addi(indi) + ": Death " + '-'.join(
                individuals[indi]["death"]) + " occurs in the future")
    if deathBeforeBirth(individuals[indi]["birthday"], individuals[indi]["death"]):
        print("ERROR: INDIVIDUAL: US03: " + addi(indi) + ": Died " + '-'.join(
            individuals[indi]["death"]) + " before being born on " + '-'.join(individuals[indi]["birthday"]))
    if individuals[indi]["age"] >= 150:
        errmsg = ("ERROR: INDIVIDUAL: US07: " + addi(indi) + ": More than 150 years old ")
        if (individuals[indi]["alive"]):
            errmsg += ("- Birth date " + '-'.join(individuals[indi]["birthday"]))
        else:
            errmsg += ("at death - Birth " + '-'.join(individuals[indi]["birthday"]) + ": Death " + '-'.join(
                individuals[indi]["death"]))
        print(errmsg)

# Print family Errors
for fam in families:
    if not pastDate(families[fam]["marrDate"]):
        print("ERROR: FAMILY: US01: " + addF(fam) + ": Marriage date " + '-'.join(
            families[fam]["marrDate"]) + " is in the future")

    if not pastDate(families[fam]["divDate"]):
        print("ERROR: FAMILY: US01: " + addF(fam) + ": Divorce date " + '-'.join(
            families[fam]["divDate"]) + " is in the future")

    if divBeforeMarr(families[fam]["marrDate"], families[fam]["divDate"]):
        print("ERROR: FAMILY: US04: " + addF(fam) + ": Divorced on " + '-'.join(
            families[fam]["divDate"]) + " before marriage on " + '-'.join(families[fam]["marrDate"]))

    if deathBeforeMarr(families[fam]["marrDate"], families[fam]["husband"]):
        print("ERROR: FAMILY: US05: " + addF(fam) + ": Married " + '-'.join(
            families[fam]["marrDate"]) + " after husband's (" + addi(
            families[fam]["husband"]) + ") death on " + '-'.join(individuals[families[fam]["husband"]]["death"]))

    if deathBeforeMarr(families[fam]["marrDate"], families[fam]["wife"]):
        print("ERROR: FAMILY: US05: " + addF(fam) + ": Married " + '-'.join(
            families[fam]["marrDate"]) + " after wife's (" + addi(families[fam]["wife"]) + ") death on " + '-'.join(
            individuals[families[fam]["wife"]]["death"]))

    if deathBeforeDivorce(families[fam]["divDate"], families[fam]["husband"]):
        print("ERROR: FAMILY: US06: " + addF(fam) + ": Divorced " + '-'.join(
            families[fam]["divDate"]) + " after husband's (" + addi(
            families[fam]["husband"]) + ") death on " + '-'.join(individuals[families[fam]["husband"]]["death"]))

    if deathBeforeDivorce(families[fam]["divDate"], families[fam]["wife"]):
        print("ERROR: FAMILY: US06: " + addF(fam) + ": Divorced " + '-'.join(
            families[fam]["marrDate"]) + " after wife's (" + addi(families[fam]["wife"]) + ") death on " + '-'.join(
            individuals[families[fam]["wife"]]["death"]))

    checkBigamy(families[fam]["husband"], families[fam]["marrDate"], fam)

    checkBigamy(families[fam]["wife"], families[fam]["marrDate"], fam)

    birthBfrMarr(families[fam], fam)