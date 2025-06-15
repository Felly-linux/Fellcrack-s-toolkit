import pyfiglet 
import os
from colorama import Fore, Back, init
from time import sleep
import subprocess
import sys
init()
banner_console = pyfiglet.figlet_format("Felly's console...", font = "digital")
print(Fore.RED + banner_console)
sleep(2)
os.system("sudo ./console_subprocess.sh")
