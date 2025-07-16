# core/email_hunter.py - Email Pattern Inference Module

import re
import requests
from bs4 import BeautifulSoup

def infer_email_patterns(domain):
    print("[EMAIL HUNTER] Scraping public sources for email patterns...")
    email_list = set()

    sources = [
        f"https://www.google.com/search?q=site:linkedin.com/in+%22@{domain}%22",
        f"https://www.google.com/search?q=site:github.com+%22@{domain}%22",
    ]

    headers = {"User-Agent": "Mozilla/5.0"}

    for url in sources:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            text = soup.get_text()
            emails = re.findall(rf"[\w.+-]+@{re.escape(domain)}", text)
            for email in emails:
                email_list.add(email.lower())
        except Exception as e:
            print(f"[-] Error querying {url}: {e}")

    # Infer pattern(s) from collected emails
    patterns = set()
    for email in email_list:
        name = email.split("@")[0]
        if "." in name:
            patterns.add("first.last@domain")
        elif "_" in name:
            patterns.add("first_last@domain")
        elif name.isalpha() and len(name) > 6:
            patterns.add("fullname@domain")
        elif len(name) <= 3:
            patterns.add("initials@domain")

    return {
        "emails_found": list(email_list),
        "patterns": list(patterns)
    }
