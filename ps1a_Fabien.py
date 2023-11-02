from ps1_partition import get_partitions
#file = input("Please provide name file:")
filename = "ps1_cow_data.txt"
CowFile = open (filename, "r")
CowDict = dict()
for line in CowFile:
    CowLine = line.split(",")
    CowDict[CowLine[0]]= int(CowLine[1].strip("\n"))
print ("List of Cows:", CowDict)

""""
Create greedy algorithm

"""""
limit =10
CowWeight = 0
cows = CowDict
RemainingCows = cows.copy()
#print (len(cows))
#for l in cows:
#    RemainingCows.append(l)
Trip = []
List = []
#if RemainingCows !="":
#    print (RemainingCows)
#print (RemainingCows[1])
def SortedList (dict):
    Sorted = {}
    UnSorted = dict.copy()
    item = 0
    i=0
    while i < len(dict):
            for c in UnSorted:
                if item < UnSorted.get(c):
                    item = UnSorted.get(c)
                    temp = c
            Sorted[temp] = UnSorted.get(temp)
            del UnSorted[temp]
            item = 0
            i+=1

    return Sorted

while bool (RemainingCows):
    SortedCows = SortedList (RemainingCows)
#    print ("List of Sorted cows:", SortedCows)
    for c in SortedCows:
        if CowWeight + SortedCows.get(c) > limit:
            continue
        else:
            Trip.append(c)
            CowWeight = RemainingCows.get(c) + CowWeight
#            print (Trip)
            del RemainingCows[c]

    List.append(Trip)
    Trip = []
    CowWeight =0
#    print (Trip)
#    print (RemainingCows
#    print (len(List))
#    weight = 0
#    Trip = []
#    for c in cows:
#        cowsname = cows
#        weight = cows.get(c) + weight
#        if weight < limit:
#            List.append (c)
            #cows.pop()
print("Greedy algorithm")
print ("Trips:",List)

"""""
Create brute force algorithm
"""""
#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
def ApprovedTrip(List,limit):
    for item in List:
        i = 0
        weight = 0
        while len(item) > i:
            weight = cows.get(item[i]) + weight
#            print (weight)
            i += 1
            if weight > limit:
                return False
    return True

AllSolution = []
FinalList =[]
for partition in get_partitions (cows):
    Status = ApprovedTrip(partition,10)
    if Status == True:
        AllSolution.append(partition)
print ("Brute force algorithm")
Finalist = AllSolution[0]
for item in AllSolution:
    if len(item) < len(FinalList):
        Finalist = item
print (Finalist)
