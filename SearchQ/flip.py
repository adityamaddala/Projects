import requests
from bs4 import BeautifulSoup


#keyword = input('Enter a search keyowrd:')

f = open('kw.txt','r')


for keyword in  f.readlines():

    print('+------------------------ Top 10 search results for keyword: '+keyword+' -------------------------+')
    
    url ='https://www.flipkart.com/search?q='+keyword+''

    res = requests.get(url,'lxml').content


    soup = BeautifulSoup(res,'html.parser')


    #ratings = soup.find_all('div',class_='hGSR34')
    #rate_count = soup.find_all('span',class_='_38sUEc')


    #----------------------------- Verticle List Items --------------------------------------------#

    title = soup.find_all('div',class_='_3wU53n')
    c =1
    for i in title:
        print(c,'-',i.text)
        c+=1
        if c == 11:
            break;

    #----------------------------- Horizontal List Items --------------------------------------------#
    items = soup.find_all('a',class_='_2cLu-l')
    c =1
    for item in items:
        print(c,'-',item.text)
        c+=1
        if c==11:
            break

