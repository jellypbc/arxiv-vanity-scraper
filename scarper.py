# Libraries
import requests
from bs4 import BeautifulSoup

# Test Function (go through workflow of sample request)
def test():
	#get html and parse into beautiful soup
	response = requests.get("https://www.arxiv-vanity.com/papers/1603.09382/")
	soup = BeautifulSoup(response.content, 'html.parser')

	# remove script, style, and head tags
	[x.extract() for x in soup.findAll('script')]
	[x.extract() for x in soup.findAll('style')]
	[x.extract() for x in soup.findAll('head')]


	print(type(soup.prettify()))

test()
