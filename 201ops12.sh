user=y
while [[ $user = y ]]
do
echo "how was your day"
echo "please answer only using good or bad"
read n
case $n in
good)
echo "thats good to hear" ;;
bad)
echo "I hope it gets better" ;;
*)
echo "error can not compute. please only use good or bad" ;;
esac
echo "would you like to try again? Y/N"
read user
done
echo "thank you I hope you have a wonderfull day"
