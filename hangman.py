import random

hangman = (
    """
 ------
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   / \.
 |   
 |     
----------
""",
"""
 ------
 |    |
 |    O
 |   / \.
 |    |
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   / \.
 |    |
 |   / \.
----------
""",
)


max_wrong = len(hangman) - 1
words = ("hello", "lord","banana", "dart","earth", "death")
botWord = random.choice(words) 
# botWord = "banana"
so_far = "*" * len(botWord)
wrongGeusses = 0 
used = [] 

print("Hangman")

while wrongGeusses < max_wrong and so_far != botWord:

    print (hangman[wrongGeusses])
    print ("guesses : "),
    print (used)
    print ("\nyou right guesses:\t", so_far)

    guess = input("Enter your guess:\t")
    guess = guess.lower()

    while guess in used:
        print (" repeated guess:\t", guess)
        guess = input(" guess again:\t")
        guess = guess.lower()

    used.append(guess)

    if guess in botWord:
        print (f" The letter, '{guess}' is in the bot's word")
        new = ""
        for letter in range(len(botWord)):
            if guess == botWord [letter]:
                new += guess
            else:
                new += so_far [letter]
        so_far = new

    else:
        print (f"\n '{guess}' isn't in the bot's word")
        wrongGeusses += 1

if wrongGeusses == max_wrong:
    print (hangman[wrongGeusses])
    print (" you lost!")
    print(f"\n the word was {botWord}")
else:
    print("\n you win!")

input ("\n press Enter key to exit")