import random


# variables to hold team and dict to count how many wins per team
teams = {}
newTeams = {}
count = {}
bracket= {}
round2 ={}
round3 = {}
round4 ={}
losers =[]
winners= []
sortedTeams = {}
currentRound = 0
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
    #get winner returns the winner . add it to the list of winners. .
    winner=getWinner(team1, team2)
    winners.append(winner)
    teamName1 = findTeam(team1)
    teamName2 = findTeam(team2)
    #changes rating to team name
    winner= findTeam(winner)
    print(teamName1 + " " + "VS " + teamName2 + " : Winner " + str(winner))










def getWinner(rating1,rating2):

    algo = 0
    algo = int(rating1) * int(rating2)  / 2
    #loser
    if algo == 100:
       return rating1 # when they are close rating 2 has a change of winning .
    else:#winner
        losers.append(rating1)
        return rating2




def removeLoser():
    # checks the loser bracket against the sorted teams. if the rating is not in the sorted teams. it is added to the new teams dict.
    newTeams.clear()
    counter = 0
    index = 0
    toDelete= []
    # separates new winners from old ones.
    print("Winning teams " + str(winners) + "\n")

    for winner in winners:
        counter
        for loser in losers:
            if winner == loser:
                 index = counter
                 toDelete.append(index)


    #adds winners to new team
    for i in range(len(toDelete)):
        winners.pop(toDelete[i])

    for winner in winners:
        team = findTeam(winner)
        newTeams[team] = winner













def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO

    createBracket(teams)
    simulate_round(teams)
    removeLoser()
    winners.clear()
    losers.clear()
    bracket.clear()
    print(str(newTeams.items()) + " New Teams \n")

    bracket.clear()
    createBracket(newTeams)
    simulate_round(teams)
    removeLoser()
    winners.clear()
    losers.clear()
    print(str(newTeams.items()) + " New Teams \n")

    bracket.clear()
    createBracket(newTeams)
    simulate_round(teams)
    removeLoser()
    winners.clear()
    losers.clear()
    print(str(newTeams.items()) + " New Teams \n")

    bracket.clear()
    createBracket(newTeams)
    simulate_round(teams)
    removeLoser()
    winners.clear()
    losers.clear()
    print(str(newTeams.items()) + " New Teams \n")


    for key, value in newTeams.items():
        print("the winner of the tournament is " + str(key) + " With a rating of " + str(value))








def createBracket(teams):

    if len(teams) == 16:
        currentRound = 1
    if len(teams) == 18:
        currentRound = 2
    if len(teams) == 14:
        currentRound = 3
    if len(teams) == 12:
        currentRound = 4
    if len(teams) == 1:
        print("The winner of the tournament is :" + teams.items())


    teamsbyRating= list(teams.values())
    lowSeed = []
    highSeed = []
    num = 0
    for i in range(len(teamsbyRating)):
        num = int(teamsbyRating[i])
        teamsbyRating[i] = num
    teamsbyRating.sort()
    for j in teamsbyRating:
        team = findTeam(j)
        sortedTeams[team] = j

    length = len(teamsbyRating)-1
    counter=0
    matches = int(len(teamsbyRating) / 2)
    #organicaly create bracket for whathever round we are in .
    # i need to get the key .
    teams = list(sortedTeams.keys())
    ratings= list(sortedTeams.values())

    for i in range(matches):
        bracket.update({ratings[i]: ratings[length]})
        length =length-1

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