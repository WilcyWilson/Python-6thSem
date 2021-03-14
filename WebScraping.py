from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
# print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)
soup = BeautifulSoup(html, "html.parser")
# Tells to use HTML parser with html.parser
print(soup.title.text)
# Prints the title of the page
print(soup.get_text())
# Prints all the Texts in the webpage excluding html tags
for p in soup.find_all('img'):
	print(p.get('src'))

# Use an HTML Parser for Web Scraping in Python
# HTML parsers are software for automated Hypertext Markup Language parsing. 
# They have two main purposes: HTML traversal: offer an interface for programmers 
# to easily access and modify the "HTML string code".
 
# Canonical example: DOM parsers
# Use Beautiful Soup HTML Parser using python3 -m pip install beautifulsoup4
# Install pip in linux using package manager pacman -S python-pip 

