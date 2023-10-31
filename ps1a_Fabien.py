#file = input("Please provide name file:")
filename = "ps1_cow_data.txt"
CowFile = open (filename, "r")
CowDict = dict()
for line in CowFile:
    CowLine = line.split(",")
    CowDict[CowLine[0]]= int(CowLine[1].strip("\n"))
print (CowDict)

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
    print (SortedCows)
    for c in SortedCows:
        if CowWeight + SortedCows.get(c) > limit:
            continue
        else:
            Trip.append(c)
            CowWeight = RemainingCows.get(c) + CowWeight
            print (Trip)
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
print (List)
