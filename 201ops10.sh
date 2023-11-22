counter = 0
until [[ $counter -eq 11 ]]
do 
echo "count: $counter"
(( counter++ ))
done