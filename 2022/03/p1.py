from aocd import get_data, submit
import os
import browser_cookie3

session = os.environ.get('AOC_SESSION')
data = get_data(session, day=3, year=2022)

# assign 1-26 to a-z
# assign 27-52 to A-Z
# for each line in data
# divide line in two halves
# sets to remove duplicates in each half
# find what item appears in both sides
# for each of those items
    # match with value in dict
    # add value to total

def formatinput(data):
    rucksacks = data.split("\n")
    for x in rucksacks:
        x.split()
    return rucksacks

def score(rucksacks):
    total = 0
    lowerdict= {}
    upperdict = {}
    for x in range(1, 27):
        y = chr(x+96)
        lowerdict[y] = x
        upperdict[y.upper()] = x + 26
    for sack in rucksacks:
        compartment1 = set(sack[:len(sack)//2])
        compartment2 = set(sack[len(sack)//2:])
        for item in compartment1:
            if item in compartment2:
                if item.islower():
                    total += lowerdict[item]
                else:
                    total += upperdict[item]
    return total

def outputscore():
    rucksacks = formatinput(data)
    total = score(rucksacks)
    return total

submit(outputscore(), part="a", day=3, year=2022)