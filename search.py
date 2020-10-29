import webbrowser
import urllib.request
import re
import json
import time
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
sleeptime=1
print('Enter Zip code (5 digits):')
zipcode=input()

urlstores='https://www.instacart.com/grocery-delivery/md/near-me-in-college-park-md?zipcode={}'.format(zipcode)
response = urllib.request.urlopen(urlstores)
text=response.read().decode('utf-8')
retailers=re.search('"retailers":\[(\{.*?\})+\]',text).group(0)
retailersdict=json.loads(retailers.replace('"retailers":',''))
storename=[retailersdict['slug'].split('/')[-1] for retailersdict in retailersdict]
print('Stores found:')
[print(storename) for storename in storename]
# storename=('711','shoppersfood','giant','pricerite','costco','wegmans','aldi',\
# 'food-lion','safeway','cvs','harris-teeter','petco','bjs','target','staples','vitamin-shoppe')
print('What do you want? ')
item=input()
webbrowser.open('',new=1)
print('Finding: '+item)


for store in storename:
    url= 'https://www.instacart.com/store/'+store+'/search_v3/'+item
    # webbrowser.get(chrome_path).open(url,new=2)
    time.sleep(sleeptime)
    webbrowser.open(url,new=2)
