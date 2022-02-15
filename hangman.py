import urllib.request
import json
import random

randomword_url = "https://www.randomlists.com/data/words.json"

# Initialise the word chosen by computer
with urllib.request.urlopen(randomword_url) as response:
    data = json.load(response)
    word = random.choice(data['data'])

# Initialise the guess of user
guess_word = ""
i = 0
while i < len(word):
    guess_word += '_'
    i += 1

# Initiate guessing
strikes = 0
MAX_STRIKES = 6
previous_guesses = []
while strikes < MAX_STRIKES:
    print(f"\nStrikes: {strikes}")
    print(f"Previous guesses: {previous_guesses}")
    print(f"Current word: {guess_word}.")
    guess = input("Guess a letter or guess the word: ")

    if guess in previous_guesses:
        guess = input("Guess something new: ")

    if guess == word:
        print(f"The word was {word}.")
        print("You win!!!")
        break
    elif guess in word:
        # Obtain the position of letters
        lst = []
        for pos, char in enumerate(word):
            if char == guess:
                lst.append(pos)

        # Update guess accordingly
        for pos in lst:
            guess_word = list(guess_word)
            guess_word[pos] = guess
            guess_word = "".join(guess_word)
        if guess_word == word:
            print(f"The word was {word}.")
            print("You win!!!")
            break
        print(guess_word + '\n')
    else:
        strikes += 1
        previous_guesses.append(guess)
        if strikes == MAX_STRIKES:
            print(f"The word was {word}.")
            print("You lose.")
