import json
import jieba
import jieba.posseg
import re
from tqdm import tqdm


def main():
    with open('Gossiping_text.json') as file:
        data = json.load(file)
    jieba.initialize('dict/dict.txt.big')
    jieba.load_userdict("dict/mydict")
    stopwords = stopwordslist('dict/stop_words.txt')  # 这里加载停用词的路径

    flag_list = ['n','nr','ns','nsf','nt','nz','nl','ng','x']
    content_list = []
    for ele in tqdm(data):
        content = ''
        for line in ele.split('\n'):
            seg_list = jieba.posseg.lcut(line)
            for text in seg_list:
                if text.flag in flag_list and text.word not in stopwords:
                    content += text.word + ' '
        content_list.append(content)
    json.dump(content_list, open('Gossiping.json', 'w'))


def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords 


if __name__ == '__main__':
    main()