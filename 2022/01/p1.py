from aocd import get_data, submit
import os
import browser_cookie3 

os.environ.get('AOC_SESSION')
# browser_cookie3.load('adventofcode.com')
data = get_data(day=1, year=2022)

# split input up into arrays by blank lines
# for each array, add all values together
# add each total into a new array
# find the max value in the new array
# return max value

class handleinput:

    def formatinput(data):
        # input = open("C:/Users/Austin/OneDrive/MyCodingProjects/Python_Projects/Web Scrapers/djangowebscraper/input.txt", "r").read()
        elfinventorylist = data.split("\n\n")
        elfinventorylist = [x.split() for x in elfinventorylist]
        return elfinventorylist
            
    def sumelfinventories(elfinventorylist):
        elftotals = []
        for elfinventory in elfinventorylist:
            elfinventory = [eval(x) for x in elfinventory]
            elftotal = sum(elfinventory)
            elftotals.append(elftotal)
        return elftotals
    
    def findmaxelftotal(elftotals):
        maxelftotal = max(elftotals)
        return maxelftotal
    
def outputmax():
    elfinventorylist = handleinput.formatinput(data)
    elftotals = handleinput.sumelfinventories(elfinventorylist)
    maxelftotal = handleinput.findmaxelftotal(elftotals)
    return maxelftotal

outputmax()

submit(outputmax(), part="a", day=1, year=2022)