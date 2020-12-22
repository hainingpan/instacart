from bs4 import BeautifulSoup
import urllib
import os
import pandas as pd

print('type HTML filename: (Press enter for all HTML files in the directory)')
filename=input()

if filename=='':
    filelist=[file for file in os.listdir() if file.endswith(".html")]
else:
    filelist=filename

for file in filelist:
    print('-'*10+file+'-'*10)
    with open(file, 'r') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    itemname=soup.find_all('div','item-name')
    itemprice=soup.find_all('div','item-price')
    params={}
    for price,name in zip(itemprice,itemname):
        price0=[x.contents for x in price.find_all('div') if not 'strike' in x["class"]]
        if price0:
            price_rm=(price0[0][0].replace('$',''))
            if float(price_rm)>0:
                name2=name.contents[0].replace('\n','')
                print(name2+'\t'+price_rm)
                params[name2]=float(price_rm)
    for charge_type,amount in zip(soup.find_all('td','charge-type'),soup.find_all('td','amount')):
        if charge_type.contents[0] in ['Sales Tax','Tip','Service Fee','Credit/Discount Applied','Heavy Order Fee','Checkout Bag Tax or Fee']:
            params[charge_type.contents[0]]=float(amount.contents[0].replace('$',''))
    sum=0
    for it in params:
        sum+=(params[it])
    params['total']=sum
    df=pd.Series(params).to_frame()
    df.to_csv(file.replace('html','csv'),header = False)
