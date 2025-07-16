# core/leak_scanner.py - Leak Detection via Pastebin & GitHub

import requests
import re
from bs4 import BeautifulSoup

def scan_pastebin_github(domain):
    print("[LEAK SCANNER] Searching for leaked data...")
    leaks = []

    # Pastebin search (basic Google dorking simulation)
    try:
        print("[+] Scanning Pastebin via Google dork...")
        query = f"site:pastebin.com {domain}"
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'pastebin.com/' in a['href']:
                link = re.search(r'(https://pastebin\.com/\w+)', a['href'])
                if link:
                    leaks.append({"source": "Pastebin", "url": link.group(1)})
    except Exception as e:
        print(f"[-] Pastebin scan failed: {e}")

    # GitHub code search (regex simulation)
    try:
        print("[+] Scraping GitHub code results...")
        gh_url = f"https://github.com/search?q={domain}&type=code"
        res = requests.get(gh_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        code_links = soup.find_all('a', href=re.compile("/.*?/.*?/blob/"))
        for link in code_links:
            href = link['href']
            if domain in href:
                leaks.append({"source": "GitHub", "url": f"https://github.com{href}"})
    except Exception as e:
        print(f"[-] GitHub scan failed: {e}")

    return leaks
