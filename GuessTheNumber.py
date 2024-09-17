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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        
        feedback = input(f'Is {guess} too high (h), too low (l), or correct (C)').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Computer guessed it corerctly the number, {guess}')


computer_guess(10)


