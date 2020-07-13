import requests
from bs4 import BeautifulSoup
import random
import json

'''
	Function that takes post from arxiv vanity and returns cleaned html to be parsed into jelly

	Input:
		arxivID: id of paper on arxiv website
		fileName: name of html file to be generated/updated

	Output:
		Generated HTML file
'''
universalObject = {}
def scrapeVanity(arxivID, fileName):

	# get html and parse into beautiful soup
	response = requests.get("https://www.arxiv-vanity.com/papers/" + str(arxivID))
	soup = BeautifulSoup(response.content, 'html.parser')

	# remove unneeded tags
	[elem.extract() for elem in soup.findAll('script')]
	[elem.extract() for elem in soup.findAll('style')]
	[elem.extract() for elem in soup.findAll('head')]
	[elem.extract() for elem in soup.findAll('footer')]
	[elem.extract() for elem in soup.findAll('form')]
	[elem.extract() for elem in soup.findAll('div', {'class':'arxiv-vanity-wrapper'})]

	# remove inline styles, classes, ids
	for tag in soup.find_all():
		if 'style' in tag.attrs:
			del tag.attrs['style']
		if 'class' in tag.attrs:
			del tag.attrs['class']
		if 'id' in tag.attrs:
			del tag.attrs['id']


	# write to html file
	htmlFile = open(fileName, 'w')
	a = htmlFile.write(soup.prettify())
	htmlFile.close()

	print("Generated", fileName, "based on arxiv paper", arxivID)

	# recursion(?) (EXPERIMENTAL)

	IDList = []
	for tag in soup.find_all():
		if 'href' in tag.attrs:
			if tag.attrs['href'][:8] == "/papers/":
				print(tag.attrs['href'])
				newId = tag.attrs['href'].replace('/papers/','').replace('/','')
				IDList.append(newId)

	if arxivID not in universalObject:
		universalObject[arxivID] = IDList

	# Creates a json object with the key being the paper 
	# and value being an array of papers (that are on arxiv) that the key cites
	with open("links.json", "w") as outfile:
		json.dump(universalObject, outfile, indent=2) 

	# BIG if (lets see what happens lol)
	if len(IDList) > 0:
		for i in IDList:
			scrapeVanity(i, i + '.html')
	else:
		return



# Sample run of function
scrapeVanity('1603.09382', '1603.09382.html')
