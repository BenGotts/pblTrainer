import json
import random

def getCases(topCases, bottomCases, y):

    with open('algs.json') as f:
        data = json.load(f)

    trainingCases = []

    for case in data['cases']:
        if(y == 'yes'):
            if((case['bottom'] in bottomCases) and (case['top'] in topCases)):
                trainingCases.append(case)

        else:
            if(case['bottom'] in bottomCases):
                trainingCases.append(case)
            elif(case['top'] in topCases):
                trainingCases.append(case)


    f.close()
    return trainingCases

def getUserTopCases():
    topCases = []
    x = "yes"

    print("Which cases on 'top' do you want? (enter one case at a time)")
    while x != "no":
        case = input("Enter a case: ")
        topCases.append(case)
        x = input("Another case? (yes/no): ")
        if(x == "no"):
            return topCases

def getUserBottomCases():
    bottomCases = []
    x = "yes"

    print("Which cases on 'bottom' do you want? (enter one case at a time)")
    while x != "no":
        case = input("Enter a case: ")
        bottomCases.append(case)
        x = input("Another case? (yes/no): ")
        if(x == "no"):
            return bottomCases

def main():
    print("PBL Trainer")
    print("Choose specific cases or train all PBLs")
    print("Valid inputs: A-, A+, adj, Ba, Bb, Ca, Cb, Da, Db, E, F, Ga, Gb, Gc, Gd, H, Ja, Jb, Ka, Kb, M, Na, Nb, O-, O+, opp, Pa, Pb, pJ, pN, Q, Ra, Rb, Sa, Sb, T, U-, U+, V, W, X, Y, Z, -")

    x = input("Train all cases? (yes/no): ")
    y = 'no'
    if(x == "no"):
        y = input("Exact cases? (yes/no): ")
        topCases = getUserTopCases()
        bottomCases = getUserBottomCases()
    else:
        topCases = ['A-', 'A+', 'adj', 'Ba', 'Bb', 'Ca', 'Cb', 'Da', 'Db', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb', 'Ka', 'Kb', 'M', 'Na', 'Nb', 'O-', 'O+', 'opp', 'Pa', 'Pb', 'pJ', 'pN', 'Q', 'Ra', 'Rb', 'Sa', 'Sb', 'T', 'U-', 'U+', 'V', 'W', 'X', 'Y', 'Z', '-']
        bottomCases = ['A-', 'A+', 'adj', 'Ba', 'Bb', 'Ca', 'Cb', 'Da', 'Db', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb', 'Ka', 'Kb', 'M', 'Na', 'Nb', 'O-', 'O+', 'opp', 'Pa', 'Pb', 'pJ', 'pN', 'Q', 'Ra', 'Rb', 'Sa', 'Sb', 'T', 'U-', 'U+', 'V', 'W', 'X', 'Y', 'Z', '-']

    # Default to not exact cases
    trainingCases = getCases(topCases, bottomCases, y)

    if(len(trainingCases) == 0):
        print("\nTraining all cases; parity or bad input was detected")
        topCases = ['A-', 'A+', 'adj', 'Ba', 'Bb', 'Ca', 'Cb', 'Da', 'Db', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb', 'Ka', 'Kb', 'M', 'Na', 'Nb', 'O-', 'O+', 'opp', 'Pa', 'Pb', 'pJ', 'pN', 'Q', 'Ra', 'Rb', 'Sa', 'Sb', 'T', 'U-', 'U+', 'V', 'W', 'X', 'Y', 'Z', '-']
        bottomCases = ['A-', 'A+', 'adj', 'Ba', 'Bb', 'Ca', 'Cb', 'Da', 'Db', 'E', 'F', 'Ga', 'Gb', 'Gc', 'Gd', 'H', 'Ja', 'Jb', 'Ka', 'Kb', 'M', 'Na', 'Nb', 'O-', 'O+', 'opp', 'Pa', 'Pb', 'pJ', 'pN', 'Q', 'Ra', 'Rb', 'Sa', 'Sb', 'T', 'U-', 'U+', 'V', 'W', 'X', 'Y', 'Z', '-']
        trainingCases = getCases(topCases, bottomCases)

    x = 'yes'
    while(x == 'yes'):
        randCase = trainingCases[random.randint(0,len(trainingCases))]
        print("\n(" + randCase['top'], randCase['bottom'] + ")", randCase['inv'])
        x = input("Another case? (yes/no): ")

main()
