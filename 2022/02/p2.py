from aocd import get_data, submit
import os
import browser_cookie3

session = os.environ.get('AOC_SESSION')
data = get_data(session, day=2, year=2022)
# data = open("input.txt file", "r").read()

# x = lose
# y = draw
# z = win

# rock = 1 
# paper = 2
# scissors = 3

# if round[1] is z then choose round[0] value from wins dict
# if round[1] is x then choose round[0] value from losers dict
# if round[1] is y then choose round[0] value from draws dict

swap = {'X': 'A', 'Y': 'B', 'Z': 'C'}    
draws = {'A': 'A', 'B': 'B', 'C': 'C'}
wins = {'A': 'B', 'B': 'C', 'C': 'A'}
losers = {'B': 'A', 'C': 'B', 'A': 'C'}
values = {'A': 1, 'B': 2, 'C': 3}


finalscore = 0 

def formatinput(data):
    for x, y in swap.items():
        data = data.replace(x, y)
    rounds = data.split("\n")
    rounds = [x.split() for x in rounds]
    return rounds

def score(rounds):
    finalscore = 0 
    for x, y in rounds:
        if y == 'A':
            # calculate value from draws dict
            finalscore += values[losers[x]]
            finalscore += 0
        elif y == 'B':
            # calculate value from wins dict
            finalscore += values[draws[x]]
            finalscore += 3
        else: 
            # calculate value from losers dict
            finalscore += values[wins[x]]
            finalscore += 6
    return finalscore

def outputscore():
    therounds = formatinput(data)
    total = score(therounds)
    return total

submit(outputscore(), part="b", day=2, year=2022)
