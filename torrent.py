import urllib.request as urllib2
from urllib.parse import quote
from bs4 import BeautifulSoup
import webbrowser
import json
import time
import subprocess
import os
def get_page(url):
    hdr={'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request("https:"+url, headers=hdr)
    print (req.__dict__)
    return urllib2.urlopen(req).read()
        
def go_to_next_page(souppage):
  try:
    data = []
    fdata=[]
    datacol=[]
    sdata=[]
    table = soup.find_all('div', class_ = 'inner_container')
    table_body = table[1].find_all('div', class_ = 'grey_bar3')
    for t in table_body[1:]:
     para= t.find('p')
     if para is not None:
         simplearray=[]    
         simplearray.append(para.find('a').get_text())
         simplearray.append(para.find('a')['href'])
         spandata= t.find_all('span')
     for sd in spandata:
       simplearray.append(sd.get_text())
     datacol.append(simplearray)
    i=1
    for d in datacol:
         print (str(i)+') '+d[0]+'||'+d[4]+'||'+d[3]+'||'+d[5])
         i = i+1 
    Inputvalue=int(input("Enter the no.of torrent you wish to download:"))
    link = datacol[Inputvalue][1]
    return link
  except KeyboardInterrupt:
    # quit
    print('\nTorrent terminated')
    sys.exit()
        
def get_magnet(magnetsouppage):
    magnet_area = magnetsouppage.find_all('div', class_ = 'grey_bar1 back_none')
    magnet_anchor = magnet_area[1].find_all('a')
    magnet_link =  magnet_anchor[0]['href']
    return magnet_link

searchItem=input("Enter the torrent you wish to search:")
completeUrl="//www.torrentdownloads.me/search/?search="+searchItem.replace(" ", "%20")
pageContent=get_page(completeUrl)
soup = BeautifulSoup(pageContent, 'html.parser') 
print ("30% done")
newUrl="//www.torrentdownloads.me"+go_to_next_page(soup).replace("download","torrent")
print ("link successfully generated - "+newUrl)
nextPageContent=get_page(newUrl)
nextpagesoupe = BeautifulSoup(nextPageContent, 'html.parser') 
if nextpagesoupe!=False:
    print ("60% done")
    magnet=get_magnet(nextpagesoupe)
    print ("100% done")
    if magnet==False:
        print ("Error in finding torrent")
    if magnet!=False:
        print ("Torrent downloading ")
        webbrowser.open(magnet)
                
        