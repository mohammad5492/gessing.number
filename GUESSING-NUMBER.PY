from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Select difficulty level 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        print("Invalid input! Please select 'easy' or 'hard' level.")
        level = input("Select difficulty level 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100.')
    chosen_number = randint(1, 100)
    turns = set_difficulty()
    print(f'You have {turns} attempts to guess the number.')

    for i in range(turns):
        guess = int(input('Make a guess: '))
        if guess == chosen_number:
            print(f'Congratulations! You guessed the number in {i+1} attempts!')
            return
        elif guess > chosen_number:
            print('Too high!')
        else:
            print('Too low!')
    print(f'Sorry, you have no more attempts. The number was {chosen_number}.')

play_game()
