
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

def install_dev_packages(git=True,cplusplus=True,c=True,make=True,python3=True):
    os.system("sudo apt-get update")
    if(git):
        print("\nInstalling Git ...")
        os.system("sudo apt-get install git -y")
    if(cplusplus):
        print("\nInstalling C++ ...")
        os.system("sudo apt-get install c++ -y")
    if(c):
        print("\nInstalling C ...")
        os.system("sudo apt-get install gcc -y")
    if(make):
        print("\nInstalling make ...")
        os.system("sudo apt-get install make -y")
    if(python3):
        print("\nInstalling python 3 ...")
        os.system("sudo apt-get install python3")

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
        install= input("Will be installed:  git, C++, GCC, make, python3. Continue ? y/n: ")
        if(install == "y"):
            install_dev_packages()
    elif (op == "6"):
        os.system("chmod +x maintenance/shutdown-auto.sh")
        os.system("maintenance/shutdown-auto.sh")
        #subprocess.call(["sh", "./shutdown-auto.sh"])