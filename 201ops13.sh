echo "hello user"
echo "please enter a number between 2-5"
read n
if [ $n -ge 2 -a $n -lt 5 ]
then 
    echo "valid number entered"
    echo "your number is $n"
elif [ $n -gt 5 -o $n -lt 2 ]
then 
    echo "your number is invalid"
    echo "please try again"
fi