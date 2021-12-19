from bs4 import BeautifulSoup
import re

html_filename = 'food - YouTube.htm'

regex_uid = r"(?<=v=)[^&]*"
regex_index = r"(?<=&index=)\d*"

'''
#prints index, video uid and video title
with open(html_filename, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for link in soup.find_all('a'):
        link_id = link.get('id')
        #print(link)
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
            #print(link)
                
            
        #    print(link)
        #print(link.get('href'))
'''

'''
#prints own channel name too
with open(html_filename, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for a in soup.find_all('a'):
        #print(a)
        classes = a.get('class')
        #print(classes)
        #print(a.text)
        #"yt-simple-endpoint style-scope yt-formatted-string"
        if classes != None and "yt-formatted-string" in classes:
            #print(div)   
            #print(div.get('id'))
            print(a.text)
            # print(a)
'''


#uses grand parent tag of video url to find channel name of video            
with open(html_filename, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for link in soup.find_all('a'):
        link_id = link.get('id')

        classes = link.get('class')

        if link_id == "video-title":    
            title = link.get('title')

            href = link.get('href')
            
            #extract video uid from href:
            uid_find = re.search(regex_uid, href)
            uid = uid_find.group()
            
            #extract video playlist index from href
            index_find = re.search(regex_index, href)
            index = index_find.group()

            time_span_id = 'ytd-thumbnail-overlay-time-status-renderer'
            for parent_span in link.parent.parent.parent.find_all('span'):
                classes = parent_span.get('class')
                if classes != None and time_span_id in classes:
                    print(parent_span.text.strip())



            #extract channel name from grand parent
            for grandparent_link in link.parent.parent.find_all('a'):
                classes = grandparent_link.get('class')
                if classes != None and "yt-formatted-string" in classes:
                    channel_name = grandparent_link.text                    
                    #print(index, uid, title, channel_name)

