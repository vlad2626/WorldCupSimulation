import random


# variables to hold team and dict to count how many wins per team
teams = {}
count = {}
bracket= {}
sortedTeams = {}

afile = open("2018m.csv", "r")

for line in open("2018m.csv", "r"):
    words = line.split(",")
    teams[words[0]] = words[1]

def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""






def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    for key, value in bracket.items():
        simulate_game(key,value)

    # Simulate games for all pairs of teams



def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    #find the rating
    #store rating in variable
    # run algorithm to decide the match
    #return the winner.
    rating1= 0
    rating2=0
    dispWinner = " "
    curRound = 0
    counter = 0
    winningTeam = []
    # loop through original bracket.
    for i,k in bracket.items():
        print(i)
        counter += 1
        print("Current match " + str(counter))
        if team1== i:
            rating1 = teams[i]
        if team2 ==i:
            rating2 = teams[i]

        winner=getWinner(rating1,rating2)

        for key, value in teams.items():
            if winner == value:
                dispWinner = key
                winningTeam.append(dispWinner)


        if winner!= 0:
            print(" the winner of ", team1, " VS " + team2, " is " + dispWinner)

        else:
            continue
        counter+=1





def getWinner(rating1,rating2):
    winner = 0
    algo = 0
    algo = int(rating1) - int(rating2)

    if algo == 100:
       return rating2 # when they are close rating 2 has a change of winning .
    else:
        return rating1




def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    createBracket()




def createBracket():
    teamsbyRating= list(teams.values())
    lowSeed = []
    highSeed = []
    num = 0
    for i in range(len(teamsbyRating)):
        num = int(teamsbyRating[i])
        teamsbyRating[i] = num

    teamsbyRating.sort()
    print(teamsbyRating)

    for j in teamsbyRating:
        team = findTeam(j)
        sortedTeams[team] = j

    print(sortedTeams)
    length = len(teamsbyRating)-1
    counter=0
    matches = int(len(teamsbyRating) / 2)
    #organicaly create bracket for whathever round we are in .
    # i need to get the key .
    for i in range(matches):
        key = int(sortedTeams.get[])
        value= int(sortedTeams[length])
        print(key)
        bracket[key] = bracket[value]
        length =length-1



    print(lowSeed)

















    


def findTeam(rating):
    team=""
    for key,value in teams.items():
        L = int(value)
        if rating == L:
             team= key
             break
    return team







def main():
    simulate_tournament(teams)


main()