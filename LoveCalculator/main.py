def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    score = int(f"{true_count}{love_count}")
    print(score)

# Esempio di chiamata
calculate_love_score("Kanye West", "Kim Kardashian")
