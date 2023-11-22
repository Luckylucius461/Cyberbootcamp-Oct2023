echo "Triangle Check"
echo "please type the first integer"
read x
echo "Please type the second integer"
read y
echo "Please type the final integer"
read z
if [ $x -eq $y -a $y -eq $z ]
then echo "EQUILATERAL"
elif [ $x -ne $y -a $y -ne $z ] 
then echo "SCALINE" 
elif [ $x -eq $y -a $x -ne $z -o $y -eq $z -a $y -ne $x ]
then echo "ISOSCELES"
fi