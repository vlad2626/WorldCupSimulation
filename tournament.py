import random


# variables to hold team and dict to count how many wins per team
teams = {}
count = {}
bracket= {}

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
    for i in bracket:
        if team1== i:
            rating1 = teams[team1]
        if team2 ==i:
            rating2 = teams[team2]
        winner=getWinner(rating1,rating2)
        print(" the winner of " , team1 , " VS" + team2 , " is " + str(winner) )



def getWinner(rating1,rating2):
    winner = 0
    algo = 0
    algo = int(rating1) - int(rating2)

    if algo == 100:
        winner= rating2  # when they are close rating 2 has a change of winning .
    else:
        winner=rating1

    return winner




def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    createBracket()
    simulate_round(teams)



def createBracket():
    listedTeams = list(teams.keys())
    listedRatings= list(teams.values())
    listedRatings2= list(teams.values())
    listedRatings.sort()
    listedRatings2.sort(reverse = True)





    tourneyMatchups = {}
    tourneyLen = len(listedRatings)-1
    counter =0
    for i in  range(8):
        team= findTeam(listedRatings[i])
        lowerSeed= findTeam(listedRatings[tourneyLen])
        bracket[team]= lowerSeed
        tourneyLen= tourneyLen-1














    


def findTeam(rating):
    for key,value in teams.items():
        if rating == value:
             team= key
             break


    print(team)
    return team







def main():
    simulate_tournament(teams)


main()