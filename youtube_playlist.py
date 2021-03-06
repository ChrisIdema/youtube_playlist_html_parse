from bs4 import BeautifulSoup
import re
import csv

def playlist_parse(html_filename):
    with open(html_filename, encoding="utf8") as fp:
        
        video_list = []
        video_list.append(('index', 'uid', 'title', 'duration', 'channel_name'))
        soup = BeautifulSoup(fp, "html.parser")

        regex_uid = r"(?<=v=)[^&]*"
        regex_index = r"(?<=&index=)\d*"
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

                #get duration:
                time_span_id = 'ytd-thumbnail-overlay-time-status-renderer'
                ggp_spans = link.parent.parent.parent.find_all('span')
                duration = next(filter(lambda s: s.get('class') != None and time_span_id in s.get('class'), ggp_spans), None)
                if duration == None:
                    duration = '0'
                else:
                    duration = duration.text.strip()

                #get channel name:
                channel_name_class = 'yt-formatted-string'
                gp_links = link.parent.parent.find_all('a')
                channel_name = next(filter(lambda l: l.get('class') != None and channel_name_class in l.get('class'), gp_links), None).text

                video_list.append((index, uid, title, duration, channel_name))
    return video_list

def write_playlist(video_list, csv_filename):
    #use utf-8 encoding, because video titles can contain unicode characters
    #set newline to empty as csv-writer adds newlines too
    with open(csv_filename, 'w', encoding='utf-8', newline='') as f: 
        # use tab as delimiter, because video titles and channels can contain punctuation
        write = csv.writer(f, delimiter='\t') 
        write.writerows(video_list) 


import os
playlist_html_files = [each for each in os.listdir() if each.endswith('.htm') or each.endswith('html') ]

for f_name in playlist_html_files:
    print('parsing {}'.format(f_name))     
    video_list = playlist_parse(f_name)
    list_name = os.path.splitext(f_name)[0].removesuffix(" - YouTube")
    write_playlist(video_list, list_name + '.csv')
