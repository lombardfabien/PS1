###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================
filename = input("what is the name of the file:")
# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string
    """""

    """"
    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    CowFile = open (filename, "r")
    CowDict = dict()
    for line in CowFile:
        CowLine = line.split(",")
        CowDict[CowLine[0]]= int(CowLine[1].strip("\n"))
    print (CowDict)
    return CowDict
        # TODO: Your code here
    pass

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
#    limit =10
    CowWeight = 0
#    cows = CowDict
    RemainingCows = cows.copy()
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
#        print (SortedCows)
        for c in SortedCows:
            if CowWeight + SortedCows.get(c) > limit:
                continue
            else:
                Trip.append(c)
                CowWeight = RemainingCows.get(c) + CowWeight
#                print (Trip)
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
    print (List)# TODO: Your code here
    pass

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
cows = load_cows(filename)
greedy_cow_transport(cows, 10)
