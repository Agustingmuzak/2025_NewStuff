import random

five_letters = ['p','e', 'n', 'a', 'l']



def letter_picker(list):
    word = []
    word_list = []

    for letter in list:
        choice = random.choice(list)
        if choice not in word:
            word.append(choice)
        
    return word
        
print(letter_picker(five_letters))

