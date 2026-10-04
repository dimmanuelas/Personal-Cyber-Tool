import time
import os
from colorama import Fore, Back, Style

from script import PhoneNumber

USER = "DP-00001"
CLIENTVER = "PCT-1"

MENU = ["Find Username",
        "Phone Number's Information",
        "Credits",
        "Exit PCT"]

def UpperText():
    print(Fore.GREEN, "██████╗░███████╗██████╗░░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░  ░█████╗░██╗░░░██╗██████╗░███████╗██████╗░")
    print("██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗")
    print("██████╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║███████║██║░░░░░  ██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝")
    print("██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║██╔══██║██║░░░░░  ██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗")
    print("██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║███████╗  ╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║")
    print("╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝\n")
    print("████████╗░█████╗░░█████╗░██╗░░░░░  ░░░░░░  ██████╗░░█████╗░████████╗")
    print("╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ░░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝")
    print("░░░██║░░░██║░░██║██║░░██║██║░░░░░  █████╗  ██████╔╝██║░░╚═╝░░░██║░░░")
    print("░░░██║░░░██║░░██║██║░░██║██║░░░░░  ╚════╝  ██╔═══╝░██║░░██╗░░░██║░░░")
    print("░░░██║░░░╚█████╔╝╚█████╔╝███████╗  ░░░░░░  ██║░░░░░╚█████╔╝░░░██║░░░")
    print("░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ░░░░░░  ╚═╝░░░░░░╚════╝░░░░╚═╝░░░")
    print(Fore.GREEN, "="*40)
    print(Fore.BLUE, "USER: " + USER)
    print(Fore.CYAN, "CLIENTVER: " + CLIENTVER)
    print(Fore.GREEN, "="*40)



def Menu():

    listnum = 1

    for v in MENU:
        print(Fore.WHITE, str(listnum) + ". " + v)
        listnum += 1

def reload():
    os.system('cls')
    print(Fore.WHITE, "Reloading...")
    main()

def main():
    os.system('cls')
    UpperText()
    Menu()
    _input1 = int(input("Select: "))

    if _input1 == 1:
        os.system('cls')
        print("1. Famous Social Media Links Only\n2. All Links\n3. Back")
        _input2 = int(input("Select: "))
        if _input2 == 1:
            os.system('cls')
            print("Get Username From Across Internet")
            print("API: PCTs API")
            username = input("Enter the username to search: ")
            os.system('cls')
            print(Fore.WHITE, f"Searching for {username}...")
            print("This may take a second or minute...\n")
            print(f"Result of '{username}'")
            print(Fore.YELLOW, "="*40)
            import script.Username as Username
            results = Username.limited_search(username)
            print(Fore.YELLOW, "="*40)
            print(Fore.WHITE)
            key2 = input("Would you save this result? (Y/n)")

            if key2 == "Y" or "y":

                folder_name = "username_folder"

                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
        
                file_name = os.path.join(folder_name, f"{username}.txt")

                with open(file_name, "w") as file:
                    
                    for val, result in results.items():

                        file.write(val + " : " + str(result) + "\n")
                        

                print(f"Successfully save as '{username}.txt'")

                input("Press Enter to back home...")

                reload()

            elif key2 == "N" or "n":

                reload()
                

        elif _input2 == 2:

            os.system('cls')
            print("Get Username From Across Internet")
            print("API: PCTs API")

            import script.Username as Username

            username = input("Enter the username to search: ")
            os.system('cls')
            print(Fore.WHITE, f"Searching for {username}...")
            print("This may take a second or minute...\n")
            print(f"Result of '{username}'")
            print(Fore.YELLOW, "="*40)
            results2 = Username.search(username)

            for platform, result in results2.items():
                print(Fore.YELLOW, "="*40)
                print(Fore.WHITE)
                key2 = input("Would you save this result? (Y/n)")
                if key2 == "Y" or "y":
                    folder_name = "username_folder"
                    
                    if not os.path.exists(folder_name):
                        os.mkdir(folder_name)
                            
                    file_name = os.path.join(folder_name, f"{username}.txt")
                    
                    with open(file_name, "w") as file:
                                        
                        for val, result in results.items():
                    
                            file.write(val + " : " + str(result) + "\n")

                elif key2 == "N" or "n":
                    reload()
                
    elif _input1 == 2:

        os.system('cls')
        target = input("Enter Phone Number (+621234567890): ").strip()

        temp_target = target[1:] if target.startswith('+') else target

        if not temp_target.isdigit():
            print(Fore.RED, "Error: The input you entered must be numbers!")
            input("Press Enter To Return...")
            reload()

        if target:
            print(Fore.WHITE, f"Searching for {target}...")
            information = PhoneNumber.getinformation(target)
            print(f"Result of '{target}'")
            print(Fore.YELLOW, "="*40)
            print(Fore.WHITE, f"Phone Number: {information["Phone Number"]}") 
            print(Fore.WHITE, f"International Format: {information["International Format"]}") 
            print(Fore.WHITE, f"National Format: {information["National Format"]}") 
            print(Fore.WHITE, f"Service Provider: {information["Service Provider"]}") 
            print(Fore.WHITE, f"Country: {information["Country"]}") 
            print(Fore.WHITE, f"Geographical Region: {information["Geographical Region"]}") 
            print(Fore.WHITE, f"Time Zone: {information["Time Zone"]}") 
            print(Fore.WHITE, f"Current Time: {information["Current Time"]}") 
            print(Fore.YELLOW, "="*40)

            print(Fore.WHITE)
            key2 = input("Would you save this result? (Y/n)")
            if key2 == "Y" or "y":
                folder_name = "phonenumber_folder"
                                
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                                        
                file_name = os.path.join(folder_name, f"{information["Phone Number"]}.txt")
                                
                with open(file_name, "w") as file:
                                                    
                    for val, result in information.items():
                                
                        file.write(val + " : " + str(result) + "\n")

                reload()
            
            elif key2 == "N" or "n":
                reload()

        else:
            print(Fore.RED, "Phone Number Can Not Be Empty")
            input("Press Enter To Return...")
            reload()

def load():

    print(Fore.YELLOW, "Welcome to Personal Cyber Tool (PCT)")
    key = input("\nAre you sure to start PCT? (Y/n)")

    if key == "Y" or "y":
        main()
    elif key == "N" or "n":
        exit()
