user=y
while [[ $user = y ]]
do
echo "Choose a Menu option:"
echo "1. Hello World"
echo "2. Ping a website or IP address:"
echo "3 Run ifconfig"
read input
if [[ $input = 1 ]]
then echo "Hello World"
elif [[ $input = 2 ]]
then
echo "Enter the website or IP address to ping:"
read address
ping -c 5 $address
elif [[ $input = 3 ]]
then
ifconfig
else
echo "invalid entry"
fi
echo "Would you like to play again? Y/N"
read user
done
echo "Great Work"