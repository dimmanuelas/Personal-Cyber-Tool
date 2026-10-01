import requests
from colorama import Fore, Back, Style
import json

def limited_search(username):


    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Replit": f"https://replit.com/@{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
    }
    
    results = {}
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:

                print(Fore.GREEN, f"[+] {platform}: {url}")
                results[platform] = f"{url}"
            elif response.status_code == 404:

                print(Fore.RED, f"[-] {platform}: Username not found")
                results[platform] = "Username not found"
            else:

                print(Fore.RED, f"[-] {platform}: Unexpected response {response.status_code}")
                results[platform] = f"Unexpected response {response.status_code}"
        except requests.exceptions.RequestException as e:

            print(Fore.RED, f"[-] {platform}: Error / Failed")
            results[platform] = f"Error / Failed"

    return results

def search(username):


    platforms = {}

    with open("./resources/sitedata.json", "r") as data_file3:

        data3 = json.load(data_file3)

        data3 = {}
    
    with open("./resources/detailsitedata.json", "r") as data_file:

        data = json.load(data_file)

        for key, value in data.items():

            data[key] = value["url"]

    with open("./resources/sitedata.json", "w") as site_file:

        json.dump(data, site_file)

    with open("./resources/sitedata.json", "r") as data_file2:

        data2 = json.load(data_file2)

        for v, r in data2.items():
            platforms[v] = r

    results = {}

    for platform, url2 in platforms.items():

        if "{}" in url2:
            url = url2.replace("{}", f"{username}")

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:

                print(Fore.GREEN, f"[+] {platform}: {url}")
                results[platform] = f"{url}"
            elif response.status_code == 404:

                print(Fore.RED, f"[-] {platform}: Username not found")
                results[platform] = "Username not found"
            else:

                print(Fore.RED, f"[-] {platform}: Unexpected response {response.status_code}")
                results[platform] = f"Unexpected response {response.status_code}"
        except requests.exceptions.RequestException as e:

            print(Fore.RED, f"[-] {platform}: Error / Failed")
            results[platform] = f"Error / Failed"

    return results