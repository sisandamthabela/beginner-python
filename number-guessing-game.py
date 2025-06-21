import random

print("=====================")
print('   Number Guessing   ')
print("=====================")
print('''
Try and Guess the number between 1 and 100.
You have 10 Attempts.
Good Luck!🥰
''')
secret_number = random.randint(1, 100)
tries = 0
while tries <= 10:
    tries += 1
    print('Enter a number between 1 - 100: ')
    users_guess = int(input('>'))
    if users_guess > secret_number:
        print('Too high')
    elif users_guess < secret_number:
        print('Too low')
    elif users_guess < 1 or users_guess > 100:
        print('Please enter a number between 1 - 100!')
    elif users_guess == secret_number:
        print('You won!')
        break
    elif tries == 10:
        print('Sorry you ran out of attempts')
    else :
        print("Invalid input!")


