import requests, sys, webbrowser ,bs4
res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup= bs4.BeautifulSoup(res.text, "html.parser")
linkElement = soup.select('.r a')
linkToOpen = min(5,len(linkElement))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElement[i].get('href'))
