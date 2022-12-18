
import hangman_words
import random
from hangmanArt import stages, logo

#Random word is chosen from list
wordList = hangman_words.word_List

wordChosen = random.choice(wordList)



playersLives = 6


#print(wordChosen)
wordLen = len(wordChosen)


#empty list that fills with "_" based on length of word
wordProgress = []

for letter in wordChosen:
    wordProgress.append("_")

print(logo)


#While loop runs while there is "_" still present in
#the players guess and player is not out of lives
while "_" in wordProgress and playersLives != 0:

#Printing current progress of players word progress and their lives
    print(wordProgress)
    print(stages[playersLives])
    guess = input("Guess a letter").lower()



#Checks if guess is in word chosen
#If guess is correct, will replace the guessed letter where it is present in the chose word
#If guess is incorrect, -1 life
    if guess in wordChosen:
        for position in range(wordLen):
            if wordChosen[position] == guess:
                wordProgress[position] = guess
    else:
        print("You guess the letter " + guess + ", that's not in the word. -1 life.")
        playersLives -= 1


#Print final stage of word progress and life
#Player wins if lives are not 0
print(wordProgress)
print(stages[playersLives])

if playersLives == 0:
    print("You lose")
else:
    print("You win")



