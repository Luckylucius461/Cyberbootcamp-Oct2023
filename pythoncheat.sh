echo " please enter a number "
read n
if [ $n -lt 100 ] 
 then echo " $n is less then 100 "
elif [ $n -gt 100 ]
 then echo " $n is greater then 100 "
elif [ $n -eq 100 ] 
 then echo " $n is equal to 100 "
 fi