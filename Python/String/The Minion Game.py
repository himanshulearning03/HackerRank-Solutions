'''
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string,S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings

Scoring
A player gets +1 point for each occurrence of the substring in the string .
For Example:

String  S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format'''

def minion_game(string):
    vowels = 'AEIOU'
    sum1 = 0
    sum2 = 0
    for i in range(len(string)):
        if string[i] in vowels:
            sum1=sum1+(len(string)-i)
        else:
            sum2=sum2+(len(string)-i)
    if sum1>sum2:
        print("Kevin",sum1)
    elif sum2>sum1:
        print("Stuart",sum2)
    else:
        print("Draw")
if __name__ == '__main__':
