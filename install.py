from termcolor import colored
import os
import time
import pyfiglet
import colorama
banner = f"""
\033[1;31m                                                                                                           >
                   A
                 A AAA
                 AA  DAAA
                 DBA  NAAAAAAAAAAA
               AAAAAA  QAAAAAAAAAAAAAA
             AAAAAAAAABJHAAAAAAAAAAAAAAAA
           AAAAB  AAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAABDAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
       AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAA   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                                                                          AAAAA  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                                                                             AAAAAAA     AAAAAAAAAAAAAAAAAAAA AAAAAAAA
        AAAAA        AAAAAAA V-1.0AAAAAAAAAAAAAAAA
                     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                      AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                       AAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        AAAAAAAAAAAAAAAAAAAAAAAAAAA
\033[0m

Tools Name:FrostWolf
Author    :Easin Hossain(shawon)
Github    :Easin-6T9
YouTube   :Xerathil
\033[1;31m=========================================================\033[0m
"""
def main_menu():
    os.system("clear")
    print(banner)
    os.system("termux-open-url https://youtube.com/@xerathil?si=sHpS9L1_dP8V49Sg")
    
    print(colored("1)Nmap\n2)Sqlmap\n3)Wafw00f\n4)RED HAWK\n5)Exiftool\n0)Exit",attrs=["bold"]))
    print(colored("=========================================================", "red", attrs=["bold"]))
    user =(input("[•]Select a options: "))
    if user=="1":
        print(colored("[•]Nmap Tool is downloading", "yellow", attrs=["bold"]))
        time.sleep(2)
        os.system("apt install nmap -y")
        print(colored("[•]Nmap Tool Downloaded Successfully...!", "yellow",attrs=["bold"]))
    elif user=="2":
            print(colored("[•]Sqlmap is installing...", "yellow", attrs=["bold"]))
            time.sleep(2)
            os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
            print(colored("[•]Sqlmap is successfully installed...", "yellow", attrs=["bold"]))
            
    elif user=="3":
        print(colored("[•]Wafw00f is installing...", "yellow", attrs=["bold"] ))
        time.sleep(2)
        os.system("git clone https://github.com/enablesecurity/wafw00f.git")
        print(colored("[•]Wafw00f is successfully installed...", "yellow", attrs=["bold"]))
    elif user=="4":
        print(colored("[•]RED_HAWK is installing...", "yellow", attrs=["bold"]))
        time.sleep(2)
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
        print(colored("[•]RED_HAWK is successfully installed...", "yellow", attrs=["bold"]))
    elif user=="5":
        print(colored("[•]ExifTool is installing...", "yellow", attrs=["bold"]))
        time.sleep(2)
        os.system("pkg install exiftool")
        print(colored("[•]ExifTool is successfully installed...", "yellow", attrs=["bold"]))
        
    elif user=="0":
      os.system("exit")
      
            
    else:
        print(colored("[•]Invalid Input plz try again...", "red", attrs=["bold"]))     
        



main_menu()
