def compute_AverageScore(game1, game2, game3):
    '''Calculate the average score of three bowling scores.'''
    AverageScore = (game1 + game2 + game3) / 3
    return AverageScore

def compute_handicapAverageScore(handicap):
    '''Calculate the average score with handicap.'''
    handicapAverageScore = (AverageScore + handicap) 
    return handicapAverageScore

# Main Program
lastName = input("Enter your last name: ")

game1 = int(input("What's the score of the first bowling game? "))
game2 = int(input("What's the score of the second bowling game? "))
game3 = int(input("What's the score of the third bowling game? "))
handicap = int(input("What's the handicap? "))
print()

AverageScore = compute_AverageScore(game1, game2, game3)
handicapAverageScore = compute_handicapAverageScore(handicap)

print(f"Last Name: {lastName}")
print(f"Average Score: {AverageScore:.2f}")
print(f"Handicap Average Score: {handicapAverageScore:.2f}")