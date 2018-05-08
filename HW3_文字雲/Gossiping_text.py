import requests
from bs4 import BeautifulSoup
import json
import time
import jieba
import jieba.posseg
import re

def main():
    with open ('Gossiping_url.json') as file:
        url_list = json.load(file)
    
    jieba.initialize('dict/dict.txt.big')
    jieba.load_userdict("dict/mydict")
    flag_list = ['n','nr','ns','nsf','nt','nz','nl','ng','x','m']
    data = []
    total_list = []
    for url in url_list:
        print(url)
        content = ''
        total = ''
        try:
            res2 = requests.get(url ,cookies={'over18': '1'})
        except :
            time.sleep(60)
            res2 = requests.get(url ,cookies={'over18': '1'})

        soup2 = BeautifulSoup(res2.text,'lxml')
        try:
            title = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]','',soup2.select('.article-meta-value')[2].text)
            total += title + '\n'
            seg_list = jieba.posseg.lcut(title)
            for text in seg_list:
                if text.flag in flag_list:
                    content += text.word + ' '
        except:
            print('===')

        try:
            main_content = soup2.select('#main-content')[0].text
        except:
            print('===')
            
        for ele in main_content.split('\n')[1:]:
            ele = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]','',ele)
            if '發信站' in ele:
                break
            elif ele == '' or 'http' in ele:
                continue
            else:
                total += ele + '\n'
                seg_list = jieba.posseg.lcut(ele)
                for text in seg_list:
                    if text.flag in flag_list:
                        content += text.word + ' '
        # print(content)

        name_flag = ''
        push_content = ''
        for push in soup2.select('.push'):
            if '檔案過大！部分文章無法顯示' in push:
                continue
            
            userid = push.select('.push-userid')[0].text.replace(' ','')
            if userid != name_flag :
                push_content += '\n'

            push_content += push.select('.push-content')[0].text.replace(':','',1).strip()
            name_flag = userid
        
        for ele in push_content.split('\n')[1:]:
            ele = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]','',ele)
            if ele == '' or 'http' in ele:
                continue
            else:
                total += ele + '\n'
                seg_list = jieba.posseg.lcut(ele)
                for text in seg_list:
                    if text.flag in flag_list:
                        content += text.word + ' '

        data.append(content)
        total_list.append(total)


    json.dump(data, open('Gossiping_jieba.json', 'w'))
    json.dump(total_list, open('Gossiping_text.json', 'w'))
       
if __name__ == '__main__':
    main()