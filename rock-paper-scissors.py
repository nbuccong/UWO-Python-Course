#Rock, paper, scissors

#Enter choices
print('Enter rock, paper, or scissors:')

a = input()

print('Enter rock, paper, or scissors:')

b = input()

#Convert choices to numbers
if a == 'rock':
    a = 1
elif a == 'paper':
    a = 2
elif a == 'scissors':
    a = 3
else :
    print('That is not a valid option')

if b == 'rock':
    b = 1
elif b == 'paper':
    b = 2
elif b == 'scissors':
    b = 3
else :
    print('That is not a valid option')

#Determine who wins
if a == b:
    print('Tie game, please play again')

elif a == 1 and b == 3:
    print('Player 1 wins!')

elif a == 3 and b == 1:
    print('Player 2 wins!')

elif a > b:
    print('PLayer 1 wins!')

elif b > a:
    print('Player 2 wins!')




