

# split input up into arrays by blank lines
# for each array, add all values together
# add each total into a new array
# find the max value in the new array
# return max value

class handleinput:

    def formatinput():
        input = open("C:/Users/Austin/OneDrive/MyCodingProjects/Python_Projects/Web Scrapers/djangowebscraper/input.txt", "r").read()
        elfinventorylist = input.split("\n\n")
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
    
def main():
    elfinventorylist = handleinput.formatinput()
    elftotals = handleinput.sumelfinventories(elfinventorylist)
    maxelftotal = handleinput.findmaxelftotal(elftotals)
    print("\n", maxelftotal)

main()