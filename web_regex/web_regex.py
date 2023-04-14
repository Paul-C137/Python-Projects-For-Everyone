#!/usr/bin/python3

import re
import requests

def main():
    url = "INSERT URL TO SEARCH"
    search_pattern = "INSERT SEARCH TERM"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(url, headers=headers)
    search_source = response.text
    print(search_source)
    
    # insert search term or regex pattern
    conobj = re.search(search_pattern, search_source)
    print(conobj)
    if conobj:
        print(conobj.group())



if __name__ == "__main__":
    main()

