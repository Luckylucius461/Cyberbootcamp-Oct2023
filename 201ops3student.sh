echo "guess a number"
read number

if [ $number -eq 05]
then
echo "equal to 05"
elif [ $number -gt 05 ] 
then
echo "greater than"
elif [ $number -lt 05 ]
then 
echo "less than"

fi
