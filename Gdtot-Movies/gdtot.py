import re
import json
import requests
from bs4 import BeautifulSoup
#--------------------------------------------------------------------------------------------------------------------------------------------
# This is a python script i made to crawl ,scrap data(moveis) from Gdtot.xyz
# 
# Out put example : 
"""
https://new.gdtot.xyz/file/137 -> GDToT | TamilYogi.com_-_Manithan_(2016)[720p_HD_5_1_AVC_MP4_2_2GB_ESUBS_Tamil]_HD_720p.mp4
https://new.gdtot.xyz/file/143 -> GDToT | www.Tamilblasters.wf - Kovil (2003) Tamil [WebDL 720p HD AVC - 2.0 320kbps 1.5GB].mkv
https://new.gdtot.xyz/file/158 -> GDToT | HubDrive | The Great Father 2020.1080p.AMZN.WeB.DL.AVC.DDP.2.0.Dus-IcTv.mkv
https://new.gdtot.xyz/file/159 -> GDToT | HubDrive | Bharathi Kannamma 1997.1080p.AMZN.WeB.DL.AVC.DDP.2.0.Dus-IcTv.mkv
https://new.gdtot.xyz/file/160 -> GDToT | GDToT | Kill Dil 2014 BluRay 1080p Hindi DD 5.1 x264 ESub - mkvCinemas [Telly].mkv
https://new.gdtot.xyz/file/161 -> GDToT | GDToT | Happy New Year 2014 BluRay 1080p Hindi DD 5.1 x264 ESub 14GB - mkvCinemas [Telly].mkv
https://new.gdtot.xyz/file/197 -> GDToT | GDToT | Kill Dil 2014 BluRay 1080p Hindi DD 5.1 x264 ESub - mkvCinemas [Telly].mkv
https://new.gdtot.xyz/file/199 -> GDToT | GDToT | Happy New Year 2014 BluRay 1080p Hindi DD 5.1 x264 ESub 14GB - mkvCinemas [Telly].mkv
https://new.gdtot.xyz/file/200 -> GDToT | Alex Pandian 2013 Tamil KTV HD 720p HDTVRip UNTOUCHED x264 AVC 3.2GB (2 Parts - 1.7GB + 1.5GB).mp4
"""
#---------------------------------------------------------------------------------------------------------------------------------------------

Gurl = 'https://new.gdtot.xyz/file/'

id = 1 # change id if you need "https://new.gdtot.xyz/file/{id}"

for i in range(100000):
	
	html = requests.get(Gurl+str(id))
	soup = BeautifulSoup(html.text,'lxml')
	title =	soup.find('title')
	pid = id
	id += 1
	if title.string is None : #to remove files that are Nonetype
		continue
	elif ".mkv.torrent" in title.string: #to remove .torrent files
		continue
	elif ".mkv" in title.string or ".mp4" in title.string and title.string != 'GDToT | Simple Plot to Manage and Share Drive with your Friends': # Tp print only files that have extension .mkv and .mp4
		print(Gurl+	str(pid)+" -> "+title.string)
	else:
		pass
# github.com/shinas101
