import requests
from bs4 import BeautifulSoup
import time

def wikiSet(url):
	response = requests.get(url)
	content = BeautifulSoup(response.content, 'html.parser')
	return (content)

def wikiLinks(url):
	soup = wikiSet(url)
	links=[]
	for link in soup.find(id="bodyContent").find_all(linkLogic):
		links.append(link)
	return(links)

def linkLogic(tag):
	return tag.has_attr('title') and not tag.has_attr('class')

def wikiDef(url,n):
	soup = wikiSet(url)
	title = soup.find(id="firstHeading")
	text = soup.find(id="mw-content-text").find_all("p",limit=n)
	fullText = ""
	for p in text:
		fullText = fullText + "\n"+p.text
	print(title.string+": "+ fullText)
	return(True)

def autoScrap(url):
	links = wikiLinks(url)
	print(links[0]['title'])
	time.sleep(5)
	autoScrap("https://es.wikipedia.org"+links[0]['href'])

wikiDef("https://es.wikipedia.org/wiki/Python",2)
autoScrap("https://es.wikipedia.org/wiki/Python")