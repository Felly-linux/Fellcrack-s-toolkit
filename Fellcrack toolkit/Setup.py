import os
from colorama import Fore, Back, init
import pyfiglet
from time import sleep
init()
banner = pyfiglet.figlet_format("Setup tool...", font = "digital")
print(Fore.BLUE + banner)
print("By: Fellcrack...")
sleep(0.1)
print(Fore.BLUE +"Setuping the toolkit...")
print(Fore.WHITE +'''
''')
sleep(0.1)
print(Fore.GREEN +"Checking tools and new repo's of kali")
print(Fore.WHITE +'''
''')
sleep(0.1)
os.system("sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt autoremove")
os.system("pip3 install -r requieriments.txt")
os.system('''sudo apt install lolcat sudo apt install crunch && sudo apt install cewl && sudo apt install metagoofil && sudo apt install tor && sudo apt-get install golang && sudo apt install git && sudo apt install nmap && sudo apt install masscan && sudo apt install dnsmap && sudo apt install dnsenum && sudo apt install dnsrecon && sudo apt install wapiti && sudo apt install dirb && sudo apt install nikto && sudo apt install whatweb && sudo apt install sherlock && sudo apt install instaloader && sudo apt install bettercap && sudo apt install wordlists && sudo apt install pipx''')
os.system("pipx install bbot")
os.system('''bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )
sudo install ./phoneinfoga /usr/local/bin/phoneinfoga''')
os.system('''git clone https://github.com/piaolin/DetectDee.git
cd DetectDee
go mod tidy
cd ..''')
os.system('''git clone https://github.com/megadose/holehe.git
cd holehe/
sudo python3 setup.py install
cd ..''')
os.system('''
sudo apt install ruby -y
git clone https://github.com/urbanadventurer/username-anarchy.git
cd username-anarchy''')
os.system("cd ..")
print(Fore.GREEN +"Every requirements and setup is ready")