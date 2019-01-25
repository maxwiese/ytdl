import requests, json

result = requests.get('https://www.googleapis.com/youtube/v3/search?q=sweetbutpsyco&maxResults=25&part=snippet&key=AIzaSyBs0UfD753iyxk4LLi9rIOvAp_KIwtpmiA').json()
for item in result['items']:
    print(item['id']['videoId'])
    print(item['snippet']['title'])