import requests

def findVideo(title=""):
    #TODO: Titel auf leerzeichen prüfen
    # 

    vidId = None
    querry = []
    result = requests.get('https://www.googleapis.com/youtube/v3/search?q={0}&maxResults=10&part=snippet&key=AIzaSyBs0UfD753iyxk4LLi9rIOvAp_KIwtpmiA'.format(title)).json()
    for item in result['items']:
        if ("lyrics" in item['snippet']['title']) or ("Lyrics" in item['snippet']['title']):
                try:
                    vidId = item['id']['videoId']
                    break
                except:
                    pass
        
          
        elif ("official" in item['snippet']['title']) or ("Official" in item['snippet']['title']):
                try:
                    vidId = item['id']['videoId']
                    break
                except:
                    pass            
            
        else:    
            querry.append(item)
            
    if vidId == None:
        try:
            vidId = querry[0]['id']['videoId']
        except:
            for vid in querry:
                try:
                    vidId = vid['id']['videoId']
                    break
                except:
                    pass

    return "https://youtube.com/watch?v={0}".format(vidId)  