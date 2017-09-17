# Jacob Ulasevich
# 9/9/2017
# Project 02

# Get file
gedFile = open("Alex-Buhse-Family.ged", "r")
# Acceptable tags
projectTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

individuals = [];

namebool = False;
idnum = " ";
# Main loop
for line in gedFile:
    # Common Variables
    # Split words of line up, may come with spaces so must strip later
    words = line.split()
    
    if namebool:
        individuals.append([idnum, words[2], words[3]])
        namebool = False;
    
        
    level = words[0]
    # Tag Line
    if level == "0":
        if len(words) >= 3:
            if words[2] == "INDI":
                idnum = words[1][1:-1];
                namebool = True;
            tag = words[2]
            lineID = words[1]
            valid = ""
            if tag in projectTags:
                valid = "Y"
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

for individual in individuals:
    print(individual[0] + " " + individual[1] + " " + individual[2])