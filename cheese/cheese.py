from bs4 import BeautifulSoup
html_doc = open('y-cheeses.txt', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')

tag=soup.div
type(tag)

print(tag)

tag.name = 'div'

print(tag['summary'])
