from ddgs import DDGS
from colorama import Fore

def search_internet(query, max_results=10):
    print(Fore.YELLOW + f"[+] searching for: '{query}' on internet...")
    print(Fore.WHITE, end="")
    
    results_list = []
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=max_results)]
            
            if not results:
                print(Fore.RED + "[!] No result found.")
                return []
                
            for idx, result in enumerate(results, 1):
                title = result.get('title')
                href = result.get('href')
                body = result.get('body')
                
                results_list.append({
                    "title": title,
                    "url": href,
                    "snippet": body
                })
                
        return results_list

    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while searching: {e}")
        return []