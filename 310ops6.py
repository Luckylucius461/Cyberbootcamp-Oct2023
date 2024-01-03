import random
R=random.randint(1,100)
while 1==1:    
    N=int(input ("pick a number"))

    print (R)
    if (N == R):
        print ("congrats you guessed right")
        break    
    elif R != N:
        print ("try again")
        
    