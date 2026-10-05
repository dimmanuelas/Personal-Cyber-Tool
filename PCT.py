import time
import os
import platform
from colorama import Fore
import re
import requests

from script.osint import PhoneNumber

MENU = ["OSINT",
        "Reconnaissance Tools",
        "Credits",
        "Exit PCT"]

global APP_DATA

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
    print("░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ░░░░░░  ╚═╝░░░░░░╚════╝░░░░╚═╝░░░\n")
    print(Fore.MAGENTA, "Use Ctrl + C to return to the home.")

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def Menu():

    listnum = 1

    for v in MENU:
        print(Fore.WHITE, str(listnum) + ". " + v)
        listnum += 1

def credit_text():
    clear_terminal()
    UpperText()
    print(Fore.CYAN, "home/credits\n")
    print(Fore.CYAN, "="*40)
    print(Fore.CYAN, "- Head Developer: Dimmanuel (DimDev)\n- Developer & Contributor: Ceva")
    print(Fore.CYAN, "="*40)
    print(Fore.YELLOW)
    input("Press Enter to back home...")
    reload()

def reload():
    print(Fore.WHITE, "Reloading...")
    clear_terminal()
    main()

def save_file(dir_name, file_name, value):
    print(Fore.CYAN)
    key2 = input("Would you save this result? (Y/n)")

    main_name, extention = os.path.splitext(file_name)
    symbol = r'[\\/:*?"<>|.]'
    clean_name = re.sub(symbol, '_', main_name)
    clean_name = re.sub(r'_+', '_', clean_name).strip('_')
    final_name = clean_name + extention
    
    if key2.lower() == "y":
        
        folder_name = dir_name
    
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            
        file = os.path.join(folder_name, f"{final_name}")
    
        with open(file, "w") as file:
                        
            for val, result in value.items():
    
                file.write(val + " : " + str(result) + "\n")
                            
    
        print(Fore.LIGHTGREEN_EX, f"Successfully save as '{final_name}'")
        print(Fore.WHITE)
        input("Press Enter to back home...")
        reload()
    
    elif key2.lower() == "n":
        reload()

def main():
    clear_terminal()
    UpperText()
    print(Fore.CYAN, "home\n")
    Menu()
    try:
        _input1 = int(input("Select: "))
    except Exception as e:
        reload()
    
    if _input1 == 1:
        osint()
    elif _input1 == 2:
        reconnaissance_tools()
    elif _input1 == 3:
        credit_text()
    elif _input1 == 4:
        clear_terminal()
        print(Fore.RED)
        inp = input("Continue Shutdown? [Y/n]: ").strip().lower()
        if inp=="y":
            clear_terminal()
            print(Fore.GREEN, "Goodbye.")
            time.sleep(1)
        elif inp=="n":
            main()
    else:
        reload()

def osint():
    clear_terminal()
    UpperText()
    print(Fore.CYAN, "home/osint\n")
    menu_list = ["Username Search", "Phone Number Information", "Website Search"]
    listnum = 1
    for v in menu_list:
        print(Fore.WHITE, str(listnum) + ". " + v)
        listnum += 1
    try:
        _input1 = int(input("Select: "))
    except Exception as e:
        osint()

    if _input1 == 1:
        clear_terminal()
        print("1. Famous Social Media Links Only\n2. All Links\n3. Back")
        _input2 = int(input("Select: "))
        if _input2 == 1:
            clear_terminal()
            print("Get Username From Across Internet")
            print("API: PCTs API")
            username = input("Enter the username to search: ")
            clear_terminal()
            print(Fore.WHITE, f"Searching for {username}...")
            print("This may take a second or minute...\n")
            print(f"Result of '{username}'")
            print(Fore.YELLOW, "="*40)
            import script.osint.Username as Username
            results = Username.limited_search(username)
            print(Fore.YELLOW, "="*40)
            print(Fore.WHITE)
            save_file("username_folder", f"{username}.txt", results)

        elif _input2 == 2:

            clear_terminal()
            print("Get Username From Across Internet")
            print("API: PCTs API")

            import script.osint.Username as Username

            username = input("Enter the username to search: ")
            clear_terminal()
            print(Fore.WHITE, f"Searching for {username}...")
            print("This may take a second or minute...\n")
            print(f"Result of '{username}'")
            print(Fore.YELLOW, "="*40)
            results2 = Username.search(username)

            save_file("username_folder", f"{username}.txt", results2)
        else:
            print(Fore.RED, "option error")
            osint()
                
    elif _input1 == 2:

        clear_terminal()
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
            for val in information:
                print(Fore.WHITE, f"{val}: {information[val]}") 
            print(Fore.YELLOW, "="*40)

            print(Fore.WHITE)
            save_file("phonenumber_folder", f"{information["Phone Number"]}.txt", information)

        else:
            print(Fore.RED, "Phone Number Can Not Be Empty")
            input("Press Enter To Return...")
            reload()

    elif _input1 == 3:
        clear_terminal()
        UpperText()
        print(Fore.CYAN, "home/osint/websearch\n")
        print(Fore.WHITE)
        user_query = input("Enter the keywords you want to search for on the internet: ")
        try:
            user_query2 = int(input("(default 10) max_results="))
        except Exception as e:
            user_query2 = 10
    
        done=False
    
        while done==False:
            if user_query.strip():
                from script.osint import websearch
                    
                result = websearch.search_internet(user_query, max_results=user_query2)
                                          
                print(Fore.LIGHTGREEN_EX + f"\nResult for: '{user_query}'")
                for i, item in enumerate(result, 1):
                    print(Fore.MAGENTA,f"\n{i}. {item['title']}")
                    print(Fore.CYAN,"   Snippet: " + Fore.WHITE, f"{item['snippet']}")
                    print(Fore.CYAN,"   URL:" + Fore.WHITE, f" {item['url']}")
    
                usr_input = input('Type "r" to retry, leave it blank to continue: ').strip().lower()
                if usr_input=='r':
                    print(Fore.YELLOW, "Retrying...\n")
                else:
                    done=True
                    save_file("reconnaissance_folder", f"(web_search)_{user_query}.txt", enumerate(result, 1))
            else:
                print(Fore.RED + "[!] keywords cannot be empty.")

    else:
        print(Fore.RED, "option error")
        osint()

def reconnaissance_tools():
    clear_terminal()
    UpperText()
    print(Fore.CYAN, "home/reconnaissance_tools\n")
    menu_list = ["Whois", "Port Scan"]
    listnum = 1
    for v in menu_list:
        print(Fore.WHITE, str(listnum) + ". " + v)
        listnum += 1
    try:
        _input1 = int(input("Select: "))
    except Exception as e:
        reconnaissance_tools()
    if _input1 == 1:
        clear_terminal()
        UpperText()
        print(Fore.CYAN, "home/reconnaissance_tools/whois\n")
        print(Fore.WHITE)
        from script.reconnaissance_tools import whois
        target = input("Enter domain (e.g., example.com): ").strip()
        print(Fore.YELLOW, f"\n[*] Fetching WHOIS information for {target}...")
        result = whois.get_whois_info(target)
        print(Fore.YELLOW, "="*40)
        for key, value in result.items():
            if isinstance(value, list):
                value_str = ", ".join(str(v) for v in value)
            else:
                value_str = str(value)
                
            print(Fore.WHITE, f"{key}: {value_str}")
        print(Fore.YELLOW, "="*40)
        save_file("reconnaissance_folder", f"(whois)_{target}.txt", result)
    elif _input1 == 2:
        clear_terminal()
        UpperText()
        print(Fore.CYAN, "home/reconnaissance_tools/portscan\n")
        print(Fore.WHITE)
        from script.reconnaissance_tools import portscan
        target = input("Enter target IP or domain: ").strip()
            
        print("\nPilih Mode Port Scan:")
        print("1. Common Ports")
        print("2. All Ports (Scan from port 1 - 1024)")
        scan_choice = input("Select Mode (1/2): ").strip()
            
        mode = "common" if scan_choice == '1' else "all" if scan_choice == '2' else None
            
        if not mode:
            print("\n[!] Invalid scan mode.")
                
        print(f"\n[*] Scanning target {target} (Mode: {mode})... Please wait.")
        response = portscan.scan_ports(target, mode=mode)
            
        if not response["success"]:
            print(f"[-] Error: {response['error']}")
        else:
            print(Fore.YELLOW, "="*40)
            print(f"{'Port'} : {'Status'}")
            for item in response["results"]:
                port_str = str(item["port"])
                status_str = item["status"]
                print(f"{port_str} : {status_str} ")
            print(Fore.YELLOW, "="*40)
            save_file("reconnaissance_folder", f"(port_scan)_{target}.txt", response["results"])
    
       
    else:
        reconnaissance_tools()

def load():

    try:
        APP_DATA_response = requests.get("https://raw.githubusercontent.com/dimmanuelas/Personal-Cyber-Tool/refs/heads/main/THIS_IS_APP_DATA/datas.json")
        APP_DATA_response.raise_for_status()
        APP_DATA = APP_DATA_response.json()
    except Exception as e:
        print(Fore.RED, "[!] An error occurred while retrieving application data.")

    clear_terminal()
    print(Fore.YELLOW, f"Welcome to Personal Cyber Tool (PCT). Ver{APP_DATA['Version']}")
    key = input("\nAre you sure to start PCT? (Y/n)")

    if key.lower() == "y":
        main()
    elif key.lower() == "n":
        clear_terminal()
        print(Fore.RED)
        inp = input("Continue Shutdown? [Y/n]: ").strip().lower()
        if inp=="y":
            clear_terminal()
            print(Fore.YELLOW, "LOL... So why did you start PCT?")
            print(Fore.GREEN, "Goodbye.")
            time.sleep(1)
        elif inp=="n":
            load()
