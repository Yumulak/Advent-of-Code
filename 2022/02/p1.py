from aocd import get_data, submit
import os
import browser_cookie3 

session = os.environ.get('AOC_SESSION')
data = get_data(session, day=2, year=2022)

# opponent
    # A = Rock
    # B = Paper
    # C = Scissors

# me
    # x = Rock
    # y = Paper
    # z = Scissors

# split input up into arrays by blank lines, called rounds
# for each round, use if statements to determine points added to tinal score
# return total

draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}
wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
values = {'X': 1, 'Y': 2, 'Z': 3}

def formatinput(data):
    rounds = data.split("\n")
    rounds = [x.split() for x in rounds]
    return rounds

def score(rounds):
    finalscore = 0
    for (x, y) in rounds:
        finalscore += values[y]
        if y == draws[x]:
            finalscore += 3
        elif wins[x] == y:
            finalscore += 6
        else:
            finalscore += 0
    return finalscore

def outputscore():
    therounds = formatinput(data)
    total = score(therounds)
    return total

thefinalscore = outputscore()

submit(outputscore(), part="a", day=2, year=2022)