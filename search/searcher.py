from urllib.request import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup

def get_images(url):
	if 'http:' not in url.split('/'):
		url = 'http://' + url

	try:
		html = urlopen(url)

	except (HTTPError, URLError) as e:
		return "Url not found"

	if html is None:
		return "Url not found"
	
	bjObj = BeautifulSoup(html.read(), 'lxml')

	try:
		images = bjObj.findAll('img')
		if images is None:
			return "No images found in the currently website"

	except AttributeError:
		return "No images found in the currently website"

	urls = []
	for img in images:
		try:
			src = img.attrs['src']
			if 'http:' not in src.split('/') and 'https:' not in src.split('/'):
				src = url +'/'+ src
		except AttributeError:
			continue

		urls.append(src)

	return urls