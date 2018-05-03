import requests
from bs4 import BeautifulSoup
import json
import time

def main():
    data = {}
    url_list = []
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
    res = requests.get(url,cookies={'over18': '1'})
    soup = BeautifulSoup(res.text,'lxml')
    tmp = soup.select('.wide')[1]['href']
    totalpage = int(tmp[tmp.find('index') + 5 : tmp.find('.html')]) + 1
    
    num = 0
    while (1):
        for ele in soup.select('.title a'):
            title = ele.text
            content_url = 'https://www.ptt.cc' + ele['href']

            if '習近平' in title:
                num += 1
                print(num)
                url_list.append(content_url)
                print(title)
      
        if totalpage - 1 == 0:
            break
        else:
            totalpage -= 1
        
        url = 'https://www.ptt.cc/bbs/Gossiping/index' + str(totalpage) + '.html'
        res = requests.get(url,cookies={'over18': '1'})
        soup = BeautifulSoup(res.text,'lxml')
        
        print('===================')
        print(totalpage)

    json.dump(url_list, open('Gossiping_url.json', 'w'))
if __name__ == '__main__':
    main()