import urllib.request, urllib.parse, sys

def GetHtml(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as response:
        html = response.read()
    return html

def SaveHtml(file_name,file_content):
    with open(file_name.replace('/','_')+".html","wb") as f:  
        f.write(file_content)
        f.flush()
        f.close()
    with open(file_name.replace('/','_')+".html", "r", encoding="utf-8") as f:
        return f.read()

def Download(song):
    params = {'csrf_token': '', 'type': 1, 's': song}
    query_string = urllib.parse.urlencode(params)
    url = "http://music.163.com/api/search/get/web?" + query_string
    html = GetHtml(url)
    SaveHtml("Tmp", html)