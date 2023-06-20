from aocd import get_data, submit
from p1 import handleinput, outputmax
import os
import browser_cookie3 

session = os.environ.get('AOC_SESSION')
# browser_cookie3.load('adventofcode.com')
data = get_data(session, day=1, year=2022)


# calculate total of three largest 'elftotals'

# get all the 'elftotals' in a list using the functions from p1.py
elfinventorylist = handleinput.formatinput(data)
elftotals = handleinput.sumelfinventories(elfinventorylist)

def topthreesum():
    # sort the list
    sortedtotals = sorted(elftotals)
    # take the last three elements of the list 
    topthree = sortedtotals[-3:]
    # and sum them up
    return sum(topthree)

submit(topthreesum(), part="b", day=1, year=2022)