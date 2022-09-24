from newsapi import NewsApiClient
import cv2
import numpy as np
import urllib.request
newsapi = NewsApiClient(api_key='4dbc17e007ab436fb66416009dfb59a8')

top_headlines = newsapi.get_top_headlines(category = 'general',
                                          language='en',
                                          country='in')
#business entertainment general health science sports technology

art = top_headlines['articles']
print(len(art))
print((top_headlines['totalResults']))
for i in range(len(art)):
    print(i)
    print((art[i]['title']))
    print((art[i]['urlToImage']))
    print((art[i]['description']))
    #print((art[i]['content']))
try:
    data = urllib.request.urlretrieve("https://nextbigfuture.s3.amazonaws.com/uploads/2018/02/9bb428833a7ead92ca48a42076f21572-1024x490.png", "local-filename.jpg")
except:
    print("issue")
img = cv2.imread("local-filename.jpg")
s = max(img.shape[0:2])
f = np.zeros((s,s,3),np.uint8)
f[f==0]=255
ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2
f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img
cv2.imwrite("img2square.png",f)