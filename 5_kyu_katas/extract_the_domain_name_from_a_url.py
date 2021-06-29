"""
Kata description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

import re


def domain_name(url):
    if '/' in url:
        return re.split('[/ .]', url)[2] if 'www' not in url else re.split('[/ .]', url)[3]
    else:
        return url.split('.')[1] if 'www' in url else url.split('.')[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
