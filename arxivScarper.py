import requests
from bs4 import BeautifulSoup

'''
	Function that takes post from arxiv vanity and returns cleaned html to be parsed into jelly

	Input:
		arxivID: id of paper on arxiv website
		fileName: name of html file to be generated/updated

	Output:
		Generated HTML file
'''
def scrapeVanity(arxivID, fileName):

	#get html and parse into beautiful soup
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
	'''
	IDList = []
	for tag in soup.find_all():
		if 'href' in tag.attrs:
			if '/papers/' in tag.attrs['href']:
				newId = tag.attrs['href'].replace('/papers/','').replace('/','')
				IDList.append(newId)

	# BIG if (lets see what happens lol)
	if len(IDList) > 0:
		scrapeVanity(IDList[0], IDList[0] + '.html')
	'''

	
# Sample run of function
scrapeVanity('1603.09382', 'test.html')