import random

print("Welcome to Hangman!")

word_list = ["python", "java", "javascript", "csharp", "ruby"]

def choose_word():
    word = random.choice(word_list)
    # print("Random word chosen:", word)  # Puoi togliere questo per non mostrare la parola
    return word

chosen_word = choose_word()
guessed_letters = []

while True:
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Current word:", display)

    if display == chosen_word:
        print("Congratulations! You've guessed the word:", chosen_word)
        break

    guessed_letter = input("Chosen letter for guessing: ").lower()
    if guessed_letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    if guessed_letter in chosen_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
    guessed_letters.append(guessed_letter)