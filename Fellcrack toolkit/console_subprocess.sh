clear
date | lolcat
echo "Who the heck r u? :"
read user
echo "Put tha freaking password :"
read password
if [ $user = "Fellcrack" ]; then
   if [ $password = "Fellcrack_was_here" ]; then
     echo "Welcome, Fellcrack..." | lolcat -a -d 500
     sudo curl -L popcat.egpl.dev
     sleep 5
     clear 
else
   echo "The password or the username is incorrect..."
   exit
exit

