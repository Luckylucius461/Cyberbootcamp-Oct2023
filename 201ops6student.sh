echo "enter a website: "
read website

function gather_info() {
    whois $website >> whois.txt
    echo "----" >> whois.txt
    dig $website >> whois.txt
    echo "----" >> whois.txt
    host $website >> whois.txt
    echo "----" >> whois.txt
    nslookup $website >> whois.txt
}
gather_info 
xdg-open whois.txt