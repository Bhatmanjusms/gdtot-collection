import re
import json
import requests
from bs4 import BeautifulSoup


Gurl = 'https://new.gdtot.xyz/file/'

id = 136

for i in range(100000):
	
	html = requests.get(Gurl+str(id))
	soup = BeautifulSoup(html.text,'lxml')
	title =	soup.find('title')
	pid = id
	id += 1
	if title.string is None :
		continue
	elif ".mkv.torrent" in title.string:
		continue
	elif ".mkv" in title.string or ".mp4" in title.string and title.string != 'GDToT | Simple Plot to Manage and Share Drive with your Friends':
		print(Gurl+	str(pid)+" -> "+title.string)
	else:
		pass
