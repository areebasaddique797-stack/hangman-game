
word = "python"
guessed = ""
chances = 5

print("Welcome to Hangman Game")

while chances > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("word:", display)

    if display == word:
        print("You win!")
        break

    guess = input("Guess a letter : ")
    guessed += guess

    if guess not in word:
        chances -= 1
        print(f"Wrong! {chances} chances left")

if chances == 0:
    print("You lose! The word was", word)

