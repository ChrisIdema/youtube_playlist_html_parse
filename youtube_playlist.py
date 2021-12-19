from bs4 import BeautifulSoup
import re

html_filename = 'food - YouTube.htm'

regex_uid = r"(?<=v=)[^&]*"
regex_index = r"(?<=&index=)\d*"

video_list = []
     
with open(html_filename, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for link in soup.find_all('a'):
        link_id = link.get('id')

        if link_id == "video-title":
            #get title:    
            title = link.get('title')

            href = link.get('href')
            
            #extract video uid from href:
            uid_find = re.search(regex_uid, href)
            uid = uid_find.group()
            
            #extract video playlist index from href
            index_find = re.search(regex_index, href)
            index = index_find.group()

            #get duration
            time_span_id = 'ytd-thumbnail-overlay-time-status-renderer'
            ggp_spans = link.parent.parent.parent.find_all('span')
            duration = next(filter(lambda s: s.get('class') != None and time_span_id in s.get('class'), ggp_spans), None).text.strip()

            #print(duration)

            #extract channel name from grand parent
            for grandparent_link in link.parent.parent.find_all('a'):
                classes = grandparent_link.get('class')
                if classes != None and "yt-formatted-string" in classes:
                    channel_name = grandparent_link.text                    
                    #print(index, uid, title, channel_name)

            channel_name_class = 'yt-formatted-string'
            gp_links = link.parent.parent.find_all('a')
            channel_name = next(filter(lambda l: l.get('class') != None and channel_name_class in l.get('class'), gp_links), None).text
            #print(channel_name)

            #extract channel name from grand parent
            for grandparent_link in link.parent.parent.find_all('a'):
                classes = grandparent_link.get('class')
                if classes != None and "yt-formatted-string" in classes:
                    channel_name = grandparent_link.text                    
                    #print(index, uid, title, channel_name)

            #print(index, uid, title, duration, channel_name)
            video_list.append((index, uid, title, duration, channel_name))

print(video_list)
