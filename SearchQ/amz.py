
import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

f = open('kw.txt','r')

data = f.readlines()
print(data)

#keywords = data.split(',')
#print(keywords)

for i in data:
    keyword = i.strip()
    #print(i.strip())


#keyword =input('Enter a keyword:')

    url = 'https://www.amazon.in/s?k='+keyword+'&ref=nb_sb_noss_2'


    res = requests.get(url,headers=headers).content

    soup = BeautifulSoup(res,'lxml')

#print(soup)


    data = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
#print(data.text)
    i=1
    for book in data:
        print(i,'-',book.text)
        i+=1
        if i==11:
            break

    print('+------------------------------------------ Results Ends here ------------------------ +')
    if i==1:
        data = soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal')
#print(data.text)
        i=1
        for book in data:
            print(i,'-',book.text)
            i+=1
            if i==11:
                break

        print('+------------------------------------------ new Results Ends here ------------------------ +')


