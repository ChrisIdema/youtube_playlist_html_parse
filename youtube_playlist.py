from bs4 import BeautifulSoup
import re

html_filename = 'food - YouTube.htm'

regex_uid = r"(?<=v=)[^&]*"
regex_index = r"(?<=&index=)\d*"

with open(html_filename, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for link in soup.find_all('a'):
        link_id = link.get('id')
        #print(link_id)
        if link_id == "video-title":    
            title = link.get('title')
            href = link.get('href')
            
            #print(link_id)
            #print(title)
            #print(href)
            
            uid_find = re.search(regex_uid, href)
            #if uid_find != None:
            uid = uid_find.group()
            #print(uid)  
            
            index_find = re.search(regex_index, href)
            #if index_find != None:
            index = index_find.group()
            #print(index)  
            
            print(index, uid, title)
                
            
        #    print(link)
        #print(link.get('href'))
        



