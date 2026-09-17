words= ["python", "robot","hangman", "coding", "sensor"]   #words list
#random.choice()
import random
secret_word= random.choice(words)
print(secret_word) 
display= ["-"]  * len(secret_word)  #to print - for num of random secret word
print(display)
#wrong attempts 0:6
wrong_guesses= 0  #start of hangman game
#player inputg
#guess= input("Guess a letter: ")   #player input the letter of secret word
#if rule to verify the letter is wrong or correct
#if guess in secret_word:
 # print("Corrrect")
#else:
 # print("Wrong")  
  #repeat tring to input a letter for game 0:6
while wrong_guesses < 6 :              #wrong_guesses <6 repeat the attempts
    guess = input("Guess a letter:")

#to appear the correct letter insted of -
    for i in range(len(secret_word)):
       if guess == secret_word[i]:
          display[i] = guess

    if guess in secret_word:
       print("Correct")
    else:
       print("Wrong")
       wrong_guesses += 1  #if this guess is wrong increas wrong_guesses 1 
    print(display)   #to print the correct letter
# win condition
    if "-" not in display:
     print("YOU WIN !")
     break
# lose condition
    if wrong_guesses == 6 :
     print("YOU LOSE !")
     print("The word was :", secret_word)
