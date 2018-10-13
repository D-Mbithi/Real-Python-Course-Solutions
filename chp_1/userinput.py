word = input("Enter a word: ")

if len(word) > 5:
    print("The word has more than 5 charecters.")
elif len(word) < 5:
    print("The word has less than characters.")
else:
    print("The word has 5 charecters.")
