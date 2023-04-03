from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def homepage(request):
    results = ''
    if request.method == 'POST':
        url = request.POST.get('url')
        tag = request.POST.get('tag')
        attribute = request.POST.get('Attributes')
        response = requests.get(url)

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all instances of tag with attribute
        # for res in soup.find_all(tag, attrs={attribute: True}):
        results = soup.find_all(tag, attrs={attribute: True})
        print(soup.results())

        return render(request, 'scraper/results.html', {'results': results})
    return render(request, 'scraper/scraper.html',)
