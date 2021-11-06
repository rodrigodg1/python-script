
import os
import subprocess
import time
from colors import *




def success_msg():
    print(bcolors.OKGREEN + "\nSuccess !" + bcolors.ENDC)


def system_info():
    print("System Information ...")
    os.system('sudo apt-get install screenfetch | screenfetch')

def clear_cache():
    print("Clear apt cache in /var/cache/apt/archives ... ")
    os.system('sudo apt-get clean')
    success_msg()

def clear_orphaned_packages():
    print("removing orphaned packages ... ")
    os.system('sudo apt-get --purge autoremove')
    success_msg()

def show_ip_addr():
    print(bcolors.WARNING + "\nIp Address:" + bcolors.ENDC)
    os.system('hostname -I')

def install_dev_packages():

    print("Updating repository")
    time.sleep(3)
    os.system("sudo apt-get update")


    print("\nInstalling Git ...")
    time.sleep(3)
    os.system("sudo apt-get install git -y")

    print("\nInstalling C++ ...")
    time.sleep(3)
    os.system("sudo apt-get install c++ -y")

    print("\nInstalling C ...")
    time.sleep(3)
    os.system("sudo apt-get install gcc -y")

    print("\nInstalling make ...")
    time.sleep(3)
    os.system("sudo apt-get install make -y")

    print("\nInstalling python 3 ...")
    time.sleep(3)
    os.system("sudo apt-get install python3")

    print("\nInstalling pip3 ...")
    time.sleep(3)
    os.system("sudo apt install python3-pip")

while (True):
    op = input("""
1 - System Information (screenfetch) and IP Address 
2 - Show IP Address 
3 - Clear apt cache 
4 - Remove orphaned packages
5 - Install dev packages
6 - Schedule shutdown 
> """)

    if(op == "1"):
        system_info()
    elif (op == "2"):
        show_ip_addr()
    elif (op == "3"):
        clear_cache()
    elif (op == "4"):
        clear_orphaned_packages()
    elif (op == "5"):
        install= input("Will be installed:  git, C++, GCC, make, python3. Continue ? y/n: ")
        if(install == "y"):
            install_dev_packages()
    elif (op == "5"):
        install= input("Will be installed:  git, C++, GCC, make, python3, pip3. Continue ? y/n: ")
        if(install == "y"):
            install_dev_packages()
    elif (op == "6"):
        os.system("chmod +x shutdown-auto.sh")
        os.system("./shutdown-auto.sh")
        #subprocess.call(["sh", "./shutdown-auto.sh"])
