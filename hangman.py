import random
import hangman_words
import hangman_art

 
chosen_word = random.choice(hangman_words.word_list)
lives=6
from hangman_art import logo
print(logo)
display = []
for letter in chosen_word:
    display += "_"
print (display)

end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter =  chosen_word [position]
        if letter == guess:
            display[position] = letter
    print (display)
    
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print ("you loose")

    if "_" not in display:
        end_of_game = True
        print ("you win")
    from hangman_art import stages
    print (stages[lives])