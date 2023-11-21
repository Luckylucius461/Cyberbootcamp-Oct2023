while 
do
echo "please select input"
echo "1. Hello world"
echo "2. ping a website or ip address"
echo "3. run ifconfig"
echo "enter 1-3"
read input 
if [[ $input -eq 01 ]]
then echo "Hello world"
elif [[ $input -eq 02 ]]
then echo "enter IP or website url"
read website
ping $website
elif [[ $input -eq 03 ]]
then  ifconfig
elif [[ $input -gt 03 ]]
then echo "invalid entry"
fi
echo "do you want to proceede y/n"
read x
if [[ $x = y ]] 
then echo "ok"
elif [[ $x = n ]]
then echo "ok"
    break 
fi
done

echo "done"