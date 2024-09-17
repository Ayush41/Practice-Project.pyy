import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess num between 1 and {x}: '))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
    print(f'Congo. you got guessed the correct num {random_number} correctly')

guess(20)