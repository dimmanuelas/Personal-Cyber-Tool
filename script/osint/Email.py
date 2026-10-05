import requests
import re

def osint_email(email):
    
    print(f"\n[*] Analyze Email: {email}")
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        print("[!] Invalid Email Format")
        input("Press Enter To Return...")
        return

    print("[*] Checking for data leaks history...")
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    headers = {"OSINT": "Personal-Cyber-Tool"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("[ALERT] Email Found In Data Leaks")
            input("Press Enter To Return...")
        elif response.status_code == 404:
            print("[SAFE] The Email Was Not Found In Any Public Leak Database.")
            input("Press Enter To Return...")
        else:
            print(f"[?] Status: Unable to reach database (Code: {response.status_code})")
            input("Press Enter To Return...")
            
    except Exception as e:
        print(f"[!] Error: {e}")
