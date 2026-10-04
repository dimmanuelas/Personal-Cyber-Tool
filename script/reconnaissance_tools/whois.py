import sys
import whois

def get_whois_info(domain):
    
    try:
        w = whois.whois(domain)
        result = {
            "Domain Registrar": w.registrar ,
            "Creation Date": w.creation_date ,
            "Expiration Date": w.expiration_date ,
            "Name Servers":w.name_servers
        }
        return result
    except Exception as e:
        return f"[-] Error: {e}"
