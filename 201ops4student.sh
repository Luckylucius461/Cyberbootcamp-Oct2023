add()
{
    c=$(expr $a + $b)
    b=$(expr $a - $b)
    e=$(expr $a \* $b)
    f=$(expr $a / $b)
    echo "the sum of two numbers is $c"
    echo "the difference is $b"
    echo "the product is $f"
    echo "the quotient is $e"
}
echo "add the first number"
read a 
echo "add the second number"
read b
add $a $b