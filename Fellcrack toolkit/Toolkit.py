import pyfiglet 
import os
from colorama import Fore, Back, init
from time import sleep
import subprocess
import sys
init()
banner = pyfiglet.figlet_format("What do you want to do?", font = "digital")
start = pyfiglet.figlet_format("Fellcrack's toolkit", font = "digital")
banner2 = pyfiglet.figlet_format("We finish...", font = "digital")
print(Fore.MAGENTA + start)
sleep(2)
print(Fore.BLUE +"By Fellcrack")
sleep(0.1)
print(Fore.MAGENTA + banner)
os.system("sudo service tor start")
choice = int(input(Fore.BLUE +'''[1] Web Vulnerabilities
[2] MITM
[3] OSINT
[4] Update and Upgrade kali
[5] Create a diccionary
[6] Exit of the toolkit
Choose an option: '''))
if choice == 1: ##Option 1
    os.system("clear")
    print(Fore.MAGENTA +"Starting secure protocols...")
    sleep(0.1)
    os.system("sudo service tor start")
    print(Fore.GREEN +"Secure protocols started...")
    workspace = str(input(Fore.BLUE +"How do you will name this workspace? --> "))
    os.system("mkdir ", workspace)
    os.system("cd ", workspace ,"/")
    web = str(input("What is the web we are going to pentest? Ex: google.com --> "))
    os.system("ping ", web)
    sleep(1)
    os.system("^C")
    ip = str(input("What is IP of the web? Ex: 127.0.0.1 --> "))
    whois = "whois ", ip  # Reemplaza con tu comando
    resultado_whois = subprocess.run(whois, shell=True, capture_output=True, text=True)
    salida_whois = resultado_whois.stdout.strip()  # Elimina espacios en blanco
    archivo_output_whois = open("Output-", ip ,"-whois.txt", "w")
    archivo_output_whois.write(salida_whois)
    archivo_output_whois.close()
    os.system("sudo nmap -p- --open -sS --min-rate 5000 -v -n", ip ," -oN results-nmap-open-ports.txt")
    os.system("sudo nmap -A -V ", ip ," -oN results-nmap-os-objetive.txt")
    os.system("sudo nmap -sC -sS -sV -T5 ", ip ," -oN results-nmap-ports-scan-services.txt")
    os.system("sudo nmap -v --reason -sV -oX results-nmap.xml --webxml")
    os.system("sudo masscan ", ip ," --ports 0-10000 -oX results-masscan.xml")
    wordlist = str(input("Do you will use a specific wordlist? If you don't pick anyone we are going to use rockyou (y/n): "))
    if wordlist == ("y"):
        wordlist_dir = str(input("Where is the wordlists? Ex: /usr/share/wordlists/rockyou.txt : "))
        os.system("sudo dnsmap ", web ," -w ", wordlist_dir ," -r dnsmap-specific-wordlist.txt")
    if wordlist == ("n"):
        os.system("sudo dnsmap ", web ," -w /usr/share/wordlists/rockyou.txt -r dnsmap-rockyou.txt")
    else:
        print(Fore.RED +'''That's not a option...
        Exiting...''')
        sys.exit()
    os.system("sudo dnsenum -o results-dnsenum -v ", web)
    os.system("sudo dnsrecon -j -v ", web)
    cypher = str(input("the web is https? (y/n) --> "))
    if cypher == ("y"): 
        os.system("dirb https://", web ," -o results-dirb.txt")
    if cypher == ("n"):
        os.system("dirb http://", web ," -o results-dirb.txt")
    else:
        print('''That's not a option...
        Exiting...''')
        sys.exit()
    os.system("nikto -output . -h ", web)
    os.system("wapiti -u https://", web +" --tor -S aggressive -v 2")
    os.system("whatweb -v -a 4 ", web)
if choice == 2:  ## Option 2
    arpspoof = str(input("Do you wanna do a arp.spoof? (y/n) --> "))
    netsniff = str(input("Do you wanna do a net.sniff? (y/n) --> "))
    bettercap_time = int(input("How many time do you wanna to see the network in bettercap (Seconds) --> "))
    if arpspoof == netsniff == ("n"):
        os.system("sudo bettercap")
        os.system("net.probe on")
        os.system("ticker on")
        sleep(bettercap_time)
        choice_bettercap = str(input("Do you wanna to exit? (y/n) --> "))
        if choice_bettercap == ("y"):
            sys.exit()
        if choice_bettercap == ("n"):
            sleep(60)
            print("exiting...")
            sys.exit()
    if arpspoof == netsniff == ("y"):
        os.system("sudo bettercap")
        os.system("net.probe on")
        os.system("ticker on")
        arp_ip = str(input("What IP do you want to arp.spoof? --> "))
        sniff_ip = str(input("What IP do you want to sniff? --> "))
        os.system("set arp.spoof.targets ", arp_ip)
        os.system("arp.spoof on")
        os.system("set net.sniff.targets ", sniff_ip)
        os.system("net.sniff on")
        sleep(bettercap_time)
        choice_bettercap2 = str(input("Do you wanna exit of bettercap? (y/n) --> "))
        if choice_bettercap2 == ("y"): 
            sys.exit()
        if choice_bettercap2 == ("n"):
            sleep(bettercap_time)
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()          
    if arpspoof == ("y"):
        arp_ip2 = str(input("What IP do you want to arp.spoof? --> "))
        os.system("set arp.spoof.targets ", arp_ip2)
        os.system("arp.spoof on")
        sleep(bettercap_time)
        choice_bettercap3 = str(input("Do you wanna exit of bettercap (y/n) --> "))
        if choice_bettercap3 == ("y"):
            sys.exit()
        if choice_bettercap3 == ("n"):
            sleep(bettercap_time)
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
    if netsniff == ("y"): 
        sniff_ip2 = str(input("What IP do you want to sniff? --> "))
        os.system("set net.sniff.targets ", sniff_ip2)
        os.system("net.sniff on")
        sleep(bettercap_time)
        choice_bettercap4 = str(input("Do you wanna exit of bettercap (y/n) --> "))
        if choice_bettercap4 == ("y"):
            sys.exit()
        if choice_bettercap4 == ("n"):
            sleep(bettercap_time)
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
    if netsniff == ("n") :
        sleep(bettercap_time)
        choice_bettercap5 = str(input("Do you wanna exit of bettercap (y/n) --> "))
        if choice_bettercap5 == ("y"):
            sys.exit()
        if choice_bettercap5 == ("n"):
            sleep(bettercap_time)
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
    if arpspoof == ("n"):
        sleep(bettercap_time)
        choice_bettercap6 = str(input("Do you wanna exit of bettercap (y/n) --> "))
        if choice_bettercap6 == ("y"):
            sys.exit()
        if choice_bettercap6 == ("n"):
            sleep(bettercap_time)
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
    sys.exit()
if choice == 3 : ## Option 3
    osint_choice = int(input(Fore.BLUE +'''What do you will to OSINT?
    
    [1] Username
    [2] Web (This OSINT take so much time but it get so big information)
    [3] Phone number
    [4] Email
    --> '''))
    print(Fore.WHITE +"")
    if osint_choice == 1:
        print("")
        user = str(input("Who is the user we are going to OSINT? --> "))
        sherlock_output = str(input("How we are going to name the output of the OSINT? --> "))
        sherlock_nsfw = str(input("Can we search on NSFW DB's? (y/n) --> "))
        instagram = str(input("The user has instagram? (y/n) --> "))
        if instagram == ("y"):
            user_instagram = str(input("Who is the user? --> "))
            os.system("instaloader ", user_instagram)
        if instagram == ("n"):
            print("Has no instagram...")
        else: 
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
        if sherlock_nsfw == ("n"):
            os.system("sherlock --verbose ", user ," --output ", sherlock_output ," --tor")
        if sherlock_nsfw == ("y"):
            os.system("sherlock --verbose ", user ," --output ", sherlock_output ,".txt --tor --nsfw")
        else:
            print(Fore.RED +'''That's not a option...
            Exiting...''')
            sys.exit()
        os.system("DetectDee")
        os.system("go run . detect -n ", user)
        os.system("go run . screenshots")
        os.system("mv results.txt", user ,".txt")
        os.system("mkdir ", user)
        os.system("mv ", user ,".txt ", user ,"/ && mv screenshots/ ", user ,"/ && mv ", sherlock_output ,".txt", user ,"/")
        os.system("mv ", user ,"/ ..")
        print(Fore.GREEN +"We been finished the OSINT, you can see the results on the folder")
    if osint_choice == 2:
        print("")
        osint_web = str(input("What web we are going to OSINT? Ex: google.com --> "))
        osint_web_name = str(input("How we are going to save this OSINT? (name) --> "))
        osint_web_dir = str(input("Where we are going to save this OSINT? (Dir) Ex: /usr/home/kali/ --> "))
        print("Types of posibles documents: .pdf .doc/.docx .xls/.xlsx .ppt .odt")
        osint_web_docs = str(input("Put a type of documents we are going to search in the web Ex: pdf --> "))
        osint_web_docs_download = int(input("How many documents we are going to download? Ex: 25 --> "))
        print(Fore.GREEN +'''We are going to start the OSINT...
        When we get ready all the modules press Enter key for start the OSINT, we notificate you''')
        print(Fore.WHITE +"")
        sleep(0.1)
        os.system("metagoofil -d", osint_web ," -t", osint_web_docs ," -l 100 -n ", osint_web_docs_download ," -o ", osint_web_name ,"-metadata -f ", osint_web_name ,".html")
        os.system("sudo bbot -t ", osint_web ," -p kitchen-sink --allow-deadly -n ", osint_web_name ," -o ", osint_web_dir)
    if osint_choice == 3:
        phone_number = str(input("What is the phone number what we are going to OSINT? Ex: +57 xxxxxxxxx  (inside a quotation marks) --> "))
        output_folder = str(input("How we are going to save this (Output) --> "))
        os.system("mkdir ", output_folder)
        comando_number = "phoneinfoga scan -n", phone_number  # Reemplaza con tu comando
        resultado_number = subprocess.run(comando_number, shell=True, capture_output=True, text=True)
        salida_number = resultado_number.stdout.strip()  # Elimina espacios en blanco
        archivo_output_number = open("Output-", phone_number ,".txt", "w")
        archivo_output_number.write(salida_number)
        archivo_output_number.close()
        os.system("mv Output-",phone_number ,".txt", output_folder ,"/")
    if osint_choice == 4:
        email = str(input("What is the email that we are going to OSINT? Ex: user@outlook.com --> "))
        os.system("mkdir ", email)
        comando = "holehe -NP ", email  # Reemplaza con tu comando
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        salida = resultado.stdout.strip()  # Elimina espacios en blanco
        archivo_output = open("Output-", email ,".txt", "w")
        archivo_output.write(salida)
        archivo_output.close()
        os.system("mv Output-", email ,".txt", email ,"/")
    else:
        print(Fore.RED +'''That's not a option...
        Exiting...''')
        sleep(0.5)
        sys.exit()
if choice == 4:
    print(Fore.BLUE +"Updating and Upgrading OS")
    print(Fore.WHITE +"")
    sleep(0.1)
    os.system("sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt autoremove")
    print(Fore.BLUE +"Everything now is to date")
    print(Fore.RED +"Exiting...")
    sys.exit()
if choice == 5: 
    print(Fore.BLUE +"Starting diccionary creation tool...")
    print(Fore.WHITE +"")
    diccionary_type = int(input('''[1] Analyze a website for create the diccionary
    [2] Use names for create the diccionary 
    [3] Create random characteres diccionary
    ---> '''))
    if diccionary_type == 3:
        minimum_char = int(input("How many characters will be the minimum? --> "))
        maximum_char = int(input("How many characters will be the maximum? --> "))
        crunch_output = str(input("Where we are going to save this diccionary? Ex: wordlist --> "))
        os.system("crunch ", minimum_char , maximum_char ," -o ", crunch_output ,".txt")
        print(Fore.GREEN +"Diccionary created...")
        print(Fore.WHITE +"")
    if diccionary_type == 2: 
        os.system("cd username-anarchy")
        diccionary_user = str(input("What user we are going to use to create the diccionary? Ex: Jane doe --> "))
        diccionary_user_output = str(input("Where we are going to save the diccionary? Ex: wordlist -->"))
        os.system("./username-anarchy ", diccionary_user ,">", diccionary_user_output ,".txt")
        print(Fore.GREEN +"Diccionary created...")
        print(Fore.WHITE +"")
    if diccionary_type == 1:
        web_page = int(input("What web page we will analizate? Ex: https//:google.com --> "))
        output_diccionary = str(input("How do you'll save the diccionary? Ex: pass --> "))
        type_cewl = int(input('''[1] Basic diccionary 
        [2] Advanced diccionary 
        ---> '''))
        if type_cewl == 1: 
            os.system("cewl ", web_page ," -w ", output_diccionary ,"-d 2")
            print(Fore.GREEN +"Diccionary created...")
            print(Fore.WHITE +"")
        if type_cewl == 2:
           word_numbers = int(input("How many words will be the diccionary? --> "))
           limitaded_longuitude = int(input("How may words will be the limit longuitude of the diccionary? Ex: 4 --> "))
           os.system("cewl ", web_page ," -w ", output_diccionary ,"-d 2 -m ", limitaded_longuitude ," -n ", word_numbers)
           print(Fore.GREEN +"Diccionary created...")
           print(Fore.WHITE +"")
        else:
           print(Fore.RED +'''That's not a option...
           Exiting...''')
           sys.exit()   
if choice == 6:
    print(Fore.BLUE +"Exiting...")
    sleep(0.5)
    sys.exit()
else:
    print(Fore.RED +'''That's not a option...
    Exiting...''')
    sys.exit()
print(Fore.MAGENTA + banner2)
print("Thanks for using...")
sleep(2.5)
print("Exiting...")
sys.exit()