CowFile = open ("ps1_cow_data.txt", "r")
CowDict = dict()
for line in CowFile:
    CowLine = line.split(",")
    CowDict[CowLine[0]]= int(CowLine[1].strip("\n"))
print (CowDict)
