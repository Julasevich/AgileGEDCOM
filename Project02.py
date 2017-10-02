from prettytable import PrettyTable
import time

months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}
today = time.strftime("%Y %m %d")


def birth_before_death(birthday, deathday):
    '''US03 - Function to find any instances of death before birth'''
    if len(deathday) < 3:
        return False
    if(birthday[2] > deathday[2]):
        return False
    elif(birthday[2] == deathday[2]):
        if (months[birthday[1]] > months[deathday[1]]):
            return False
        elif (months[birthday[1]] == months[deathday[1]]):
            if (birthday[0] > deathday[0]):
                return False
    return True


def divBeforeMarr(date_marr, date_div):
    '''US04 - Function to find any instances of divorce before marriage.'''
    if len(date_div) < 3:
        return False
    if(date_marr[2] < date_div[2]):
        return False
    elif(date_marr[2] == date_div[2]):
        if(date_marr[1] < date_div[1]):
            return False
        elif(date_marr[1] == date_div[1]):
            if(date_marr[0] < date_div[0]):
                return False
    return True


def deathBeforeMarr(date_marr, date_death_husb, date_death_wife):
    '''US05 - Function to find any instances of death before marriage.'''
    if len(date_death_husb) < 3 and len(date_death_wife) < 3:
        return False
    if (len(date_death_husb) >= 3 and date_marr[2] < date_death_husb[2]) or (len(date_death_wife) >= 3 and date_marr[2] < date_death_wife[2]):
        return False
    elif len(date_death_husb) >= 3 and date_marr[2] == date_death_husb[2]:
        if(date_marr[1] < date_death_husb[1]):
            return False
        elif(date_marr[1] == date_death_husb[1]):
            if(date_marr[0] < date_death_husb[0]):
                return False
    elif len(date_death_wife) >= 3 and date_marr[2] == date_death_wife[2]:
        if(date_marr[1] < date_death_wife[1]):
            return False
        elif(date_marr[1] == date_death_wife[1]):
            if(date_marr[0] < date_death_wife[0]):
                return False
    return True


def div_before_death(div_date, deathday):
    '''US06 - Function to find any instances of death before marriage'''
    if len(deathday) < 3:
        return False
    if (div_date[2] > deathday[2]):
        return False
    elif (div_date[2] == deathday[2]):
        if (months[div_date[1]] > months[deathday[1]]):
            return False
        elif (months[div_date[1]] == months[deathday[1]]):
            if (div_date[0] > deathday[0]):
                return False
    return True


def getAge(today, birthday, alive, deathday):
    '''Take today's date and compute an age.'''
    if alive:
        # Compute Age normally
        date = today.split()
        today_year = date[0]
        today_month = date[1]
        today_day = date[2]
        age = int(today_year) - int(birthday[2])
        age += (int(today_month) / 12.0) - (months[birthday[1]]/12.0)
        age += (int(today_day)/365.0) - (int(birthday[0])/365.0)
        if int(age) >= 150:
            age = 0
        return(int(age))
    else:
        # Compute Age up to death day
        death_year = deathday[2]
        death_month = months[deathday[1]]
        death_day = deathday[0]
        age = int(death_year) - int(birthday[2])
        age += (int(death_month) / 12.0) - (months[birthday[1]]/12.0)
        age += (int(death_day)/365.0) - (int(birthday[0])/365.0)
        if int(age) >= 150:
            age = 0
        return int(age)


#Needs to be fixed in Sprint 2
def noBigamy(spouses, divorces):
    '''US11 - Function to check status of marrage'''
    if (spouses-divorses) > 1:
        return False
    else:
        return True



def pastDate(date):
    '''
    Function that takes in a date and returns false if the date has not happened yet and true if it has.
    Input is taken as a list containing date information as stored in a GED file
    '''
    today = time.strftime("%Y %m %d").split()
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

def birthBfrMarr(birth, marry):
    '''
    Function that takes in a birth date and a marriage date and checks that the marriage occurs after the birth
    Input is taken as two string lists containing birth date and marriage date information as stored in a GED file
    '''
    if int(birth[2]) < int(marry[2]):
        return True
    elif int(marry[2]) < int(birth[2]):
        return False
    else:
        if months[birth[1]] < months[marry[1]]:
            return True
        elif months[marry[1]] < months[birth[1]]:
            return False
        else:
            if int(int(birth[0]) >= int(marry[0])):
                return False
            return True

# Get file
gedFile = open("MyFamily.ged", "r")
# Acceptable tags
projectTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

# Unique Individual Values
individuals = []
idnum = ''
indiFirstName = ''
indiLastName = ''
indiSex = ''
indiBirthday = ''
indiAge = ''
indiAlive = True
indiDeath = ''
indiChild = ''
indiSpouse = ''
birthday = False
deathday = False

# Unique Family Values
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
                    if indiFirstName != '' and indiLastName != '' and idnum != '':
                        if indiDeath == '':
                            indiDeath = "NA"
                        if indiChild == '':
                            indiChild = "NA"
                        if indiSpouse == '':
                            indiSpouse = "NA"
                        indiAge = getAge(today, indiBirthday, indiAlive, indiDeath)
                        if indiAge >= 150:
                            indiAge = 0
                        individuals.append([idnum, indiFirstName, indiLastName, indiSex, indiBirthday, indiAge, indiAlive, indiDeath, indiChild, indiSpouse])
                        indiFirstName = ''
                        indiLastName = ''
                        indiSex = ''
                        indiAge = ''
                        indiAlive = True
                        indiDeath = ''
                        indiChild = ''
                        indiSpouse = ''
                    idnum = words[1][1:-1]
                elif tag == "FAM":
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
                if stillMarried is True and birthday is False and deathday is False:
                    currentMarr = words[2:]
                elif birthday is False and deathday is False:
                    currentDiv = words[2:]
                elif deathday is False:
                    indiBirthday = words[2:]
                    birthday = False
                else:
                    indiDeath = words[2:]
                    deathday = False
            elif tag == "NAME":
                indiFirstName = words[2]
                indiLastName = words[3]
            elif tag == "SEX":
                indiSex = words[2]
            elif tag == "BIRT":
                birthday = True
            elif tag == "DEAT":
                deathday = True
                indiAlive = False
            elif tag == "FAMC":
                indiChild = words[2][1:-1]
            elif tag == "FAMS":
                indiSpouse = words[2][1:-1]
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
if currentFam != '' and currentHusb != '' and currentWife != '':
    if currentChildren == []:
        currentChildren = "NA"
    if currentDiv == '':
        currentDiv = "NA"
    addFam = [currentFam, currentMarr, currentDiv, currentHusb, currentWife, currentChildren]
    families.append(addFam)

# Check if any new individuals are waiting to be added
if indiFirstName != '' and indiLastName != '':
    if indiDeath == '':
        indiDeath = "NA"
    if indiChild == '':
        indiChild = "NA"
    if indiSpouse == '':
        indiSpouse = "NA"
    indiAge = getAge(today, indiBirthday, indiAlive, indiDeath)
    individuals.append([idnum, indiFirstName, indiLastName, indiSex, indiBirthday, indiAge, indiAlive, indiDeath, indiChild, indiSpouse])

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

for individual in individuals:
    IndiIDs.append(individual[0])
    IndiNames.append(individual[1] + " " + individual[2])
    IndiSexs.append(individual[3])
    IndiBirthdays.append(individual[4])
    IndiAges.append(individual[5])
    IndiAlives.append(individual[6])
    IndiDeaths.append(individual[7])
    IndiChilds.append(individual[8])
    IndiSpouses.append(individual[9])

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

#Print individual errors
for indi in individuals:
    if  not pastDate(indi[4]):
        print("ERROR: INDIVIDUAL: US01: " + indi[0] + ": Birthday " + indi[4][0] + " " + indi[4][1] + " " + indi[4][2] + " occurs in the future")
    if  not indi[6]:
        if not pastDate(indi[7]):
            print("ERROR: INDIVIDUAL: US01: " + indi[0] + ": Death " + indi[4][0] + " " + indi[4][1] + " " + indi[4][2] + " occurs in the future")
    #if  not birth_before_death(indi[4], indi[7]):
        #print("ERROR: INDIVIDUAL: US03: " + indi[0] + ": Died " + indi[7][0] + " " + indi[7][1] + " " + indi[7][2] + " before born " + indi[4][0] + " " + indi[4][1] + " " + indi[4][2])
    if indi[5] >= 150:
        errmsg = ("ERROR: INDIVIDUAL: US07: " + indi[0] + " More than 150 years old ")
        if(indi[6]):
            errmsg += ("- Birth date " + indi[4][0] + " " + indi[4][1] + " " + indi[4][2])
        else:
            errmsg += ("at death - Birth " + indi[4][0] + " " + indi[4][1] + " " + indi[4][2] + ": Death " + indi[7][0] + " " + indi[7][1] + " " + indi[7][2])
        print(errmsg)


# Print family Errors
for i, family in enumerate(families):
    husbID = family[3][1:-1]
    wifeID = family[4][1:-1]
    husbIndex = 0
    wifeIndex = 0
    for y, individual in enumerate(individuals):
        if individual[0] == husbID:
            husbIndex = y
        elif individual[0] == wifeID:
            wifeIndex = y

    if divBeforeMarr(family[1], family[2]) is True:
        print("ERROR: FAMILY: " + family[0][1:-1] + " -- Divorced before married.")
    if deathBeforeMarr(family[1], IndiDeaths[husbIndex], IndiDeaths[wifeIndex]):
        print("ERROR: FAMILY: " + family[0][1:-1] + " -- Death before married.")
    # Implement in Sprint 2
    #if not noBigamy(individual[9].count, family[2].count):
        #print("ERROR: FAMILY: US11: " + family[0][1:-1] + " -- Married again without divorcing.")
    #if div_before_death(family[2], IndiDeaths[husbIndex]) is False:
        #print("ERROR: FAMILY: " + family[0][1:-1] + " -- Divorce after death")
    #if div_before_death(family[2], IndiDeaths[wifeIndex]) is False:
        #print("ERROR: FAMILY: " + family[0][1:-1] + " -- Divorce after death")
