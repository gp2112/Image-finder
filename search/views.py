from django.shortcuts import render, redirect
from search.searcher import *

def index(request):
	try:
		url = request.GET.get('url')

	except AttributeError:
		return render(request, 'index.html')

	if url == '' or url is None:
		return render(request, 'index.html')

	urls = get_images(url)

	if isinstance(urls, str):
		return render(request, 'index.html', {'error':urls})
	else:
		return render(request, 'found.html', {'urls':urls, 'u':url})
