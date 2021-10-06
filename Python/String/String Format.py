''' Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, M and  3 is  N times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    '''

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
c='.|.'
#Upper Half
for i in range(N//2):
    print((c*i).rjust((M//2-1),'-')+ c +(c*i).ljust((M//2-1),'-'))
#Center
print('WELCOME'.center((M),'-'))

# Lower Half

for j in range(N//2+2,N+1):
    print((c*(N-j)).rjust(M//2-1,'-') + c + (c*(N-j)).ljust(M//2-1,'-'))
