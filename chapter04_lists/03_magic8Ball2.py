import random, sys

magicEightBall = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']

print(random.choice(magicEightBall))

try:
    while True:
        print('Would you like your faith guessed? (y) or (n)')
        answer = input()
        if answer == 'n':
            sys.exit()
        elif answer != 'y':
            print('Please choose an accurate response')
            continue
        else:
            print(random.choice(magicEightBall))
except KeyboardInterrupt:
    sys.exit()
