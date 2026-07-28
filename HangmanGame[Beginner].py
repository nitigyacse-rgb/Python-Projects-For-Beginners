import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
stages = [
'''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]

word = random.choice(someWords)

if __name__ == '__main__':

    print('Guess the word! HINT: word is a fruit.')

    for _ in word:
        print('_', end=' ')
    print()

    letterGuessed = ''
    wrong_guesses = 0
    max_chances = len(stages) - 1
    flag = 0

    try:
        while wrong_guesses < max_chances and flag == 0:

            print()
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('Enter only a letter!')
                continue

            elif len(guess) > 1:
                print('Enter only a single letter!')
                continue

            elif guess in letterGuessed:
                print('You already guessed that letter!')
                continue

            if guess in word:
                letterGuessed += guess * word.count(guess)
            else:
                wrong_guesses += 1
                print(stages[wrong_guesses])

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        if wrong_guesses == max_chances:
            print('\nYou lost! The word was:', word)

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')