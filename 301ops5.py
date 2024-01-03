#number = int(input("which number do you want to check?"))
#if(number % 2) == 0:
#    print ("the number is even")
#else:
 #   print ("the number is odd")


from datetime import date 
today = date.today()
d1 = int(today.strftime("%d"))
m1 = int(today.strftime("%m"))
y2 = int(today.strftime("%y"))

#print (d1,m1,y2)
agey=int(input("what is your birth year"))
agem=int(input("what is your birth month"))
aged=int(input("what is your birth day"))
x=(32872.5)
z=(1080.74)
y1=(90)

ya=(y1-agey)
d2=((ya*365)-aged)
m2=((ya*12)-agem)

ym=((ya-y2))
dm=(( x+aged )-d2)
mm=(( z+agem )-m2)

kd=(dm*365)
km=(mm*12)

print ('you have ', (ym) ,' years left')
print ('you have ', (km),' months left')
print ('you have ', (kd), ' days left')