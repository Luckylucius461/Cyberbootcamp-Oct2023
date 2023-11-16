echo "Enter the directory:"
read -r directory
if [ ! -d "$directory" ]; 
then
    echo "Creating Directory"
    mkdir -p "$directory"
fi
echo "Enter the permissions number:"
read -r permissions
cd "$directory"
chmod "$permissions" .
echo "directory contents and permissions are:"
ls -l