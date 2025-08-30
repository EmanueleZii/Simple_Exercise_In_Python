import random

word_list = ["python", "java", "javascript", "csharp", "ruby"]

def choose_word():
    word = random.choice(word_list)
    print("Random word chosen:", word)
    return word

print("Welcome to Hangman!")

chosen_word = choose_word()
guessed_letter = input("Chosen letter for guessing: ").lower()

for letter in chosen_word:
    if letter == guessed_letter:
        print("Correct guess!")
    else:
        print("Wrong guess!")








