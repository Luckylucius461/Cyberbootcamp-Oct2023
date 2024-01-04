import random
R=random.randint(1,20)
t=1
while 1==1: #t<4:    
    N=int(input ("pick a number"))
    print (t)
    print (R)
    if (N == R): #or (t==3):
        print ("you guessed it in",t,"guesses" )
        break    
    elif R > N:
        print ("too Low")
        print ("try again")
        t=t+1
    elif R < N:
        print ("too High")
        print ("Try again")
        t=t+1