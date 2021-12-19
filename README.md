# youtube_playlist_html_parse
Parses the html file of a YouTube playlist page. 
Great way to backup your playlists before the YouTube overlords censor videos or delete your account or if you want to close your account.

# How to parse a playlist
- open any playlist or "liked videos" page in the browser by clicking on the sidebar on the left (this view is just the playlist page without a video next to it)
- your url should look like this: `https://www.youtube.com/playlist?list=<playlist_id>`
- scroll down all all the way using page-down so the entire list is loaded in your tab
- save the page as htm or html
- repeat for all playlists you want parsed
- drop the files in this folder and run `python youtube_playlist.py`

# How it works
It uses BeautifulSoup to parse html code and regular expressions to parse urls.

It doesn't use API calls but relies on attribute values and the hierarchy of html tags, so when YouTube changes its layout or html code this script might break. Since no API calls are used, no restrictions apply and all your lists can be exported at once.

# recovermy.video
I recommend the following tool if you want to detect and recover video titles from deleted videos in your playlists: `www.recovermy.video` . 
- It works great, but doesn't support exporting of playlists anymore at the time of writing
- it requires you to create an account and give the site permissions to your google account
- Since it relies on API calls it only syncs your playlists once in a while and it can only recover video names if it synced before the video was deleted. 
- Even if it cannot recover the video name, it provides the UID of the video and provides clickable links to `google` and `archive.org`. This often allows you to find a backup or copy of your deleted video. I used this feature to recover hundreds of censored videos.
