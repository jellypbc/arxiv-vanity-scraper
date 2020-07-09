# Libraries
import requests
from bs4 import BeautifulSoup

# Test Function (go through workflow of sample request)
def test():
	#get html and parse into beautiful soup
	response = requests.get("https://www.arxiv-vanity.com/papers/1603.09382/")
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

	print(soup)
	htmlFile = open('test.html', 'w')
	a = htmlFile.write(soup.prettify())
	htmlFile.close()
	
	'''
	to remove:
		<div class="arxiv-vanity-wrapper">
		<div class="arxiv-vanity-wrapper">
	'''

test()