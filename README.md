# GuessingGame  in Python

--Guess the number--

This Guessing Game program is built on the following game rules: 
- The program generates a random integer between 0 and 100. 
- Then, it asks the user to guess a number between 0 and 100. 
- It compares the answer given by the user and the generated random number and return the following: 
    * the guess is less than 0 and more than a hundered: display the message ‘Keep your guess between 0 and 100.’ 
    * the guess is smaller than the answer: display the message ‘hmm…higher…’ 
    * the guess is bigger than the answer: display the message ‘hmm…lower…’ 
    * the guess is the correct answer: display the message ‘Bravo! The computer was thinking of number _#_ as well.’ 
- The program will ask the user to try again and again until the
correct answer is reached. 
- The game ends when the player guesses the correct answer. 
- When the player guesses the correct answer, a list of all choices given by the player and the total
number of tries (choices) the player had are displayed. But, not the guesses less than 0, more than a
100, and non-numerical values into the list.


--Steps taken--
1. Generate the random integer
2. Create an empty list to store the guesses
3. Write an introduction
4. Ask user to guess a number
5. take the user’s input as an integer
6. Write the games rules using a while loop
7. Set the condition to exit the while loop
8. Inside your while loop, write the conditions of the game
9. Under each statement, or condition, add the incorrect guess into the list of incorrect guesses
