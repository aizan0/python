#snake water Gun game
import random

def game(comp,you):
    if comp == you:
        return None
# all the possibilities with s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    #all the possibilities with w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
#all the possibilities with g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("comp move: Snake(s) water(w) Gun(g)")
number = random.randint(1,3)
if number == 1:
    comp = 's'
if number == 2:
    comp = 'w'
if number == 3:
    comp = 'g'

you = input("snake(s) water(w) Gun(g)")
a = game(comp,you)

print(f"comp choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The Game is Tie")
elif a:
    print("you win")
else:
    print('you loose...!')   
