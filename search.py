import webbrowser
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
storename=('711','shoppersfood','giant','pricerite','costco','wegmans','aldi',\
'food-lion','safeway','cvs','harris-teeter','petco','bjs','target','staples','vitamin-shoppe')
print('What do you want? ')
item=input()
webbrowser.open('',new=1)
print('Finding: '+item)

for store in storename:
    url= 'https://www.instacart.com/store/'+store+'/search_v3/'+item
    # webbrowser.get(chrome_path).open(url,new=2)
    webbrowser.open(url,new=2)
