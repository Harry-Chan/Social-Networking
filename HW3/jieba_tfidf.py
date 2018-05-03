#encoding=utf-8
import jieba
import jieba.posseg
import jieba.analyse
import json
from sklearn.feature_extraction.text import CountVectorizer
from tqdm import tqdm
def main():
    # s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
    # for x, w in jieba.analyse.textrank(s, withWeight=True):
    #     print('%s %s' % (x, w))

    with open('HatePolitics_text.json') as file:
        data = json.load(file)

    jieba.initialize('dict/dict.txt.big')
    jieba.load_userdict("dict/mydict")

    test = ["習近平 習近平 習近平 習近平 安安 中國 台灣 席包子",
    "習近平 台灣 兩岸 李克強 黨主席 巴拿馬 席大大",
    "習近平 中國 香港 美國 馬英九 馬英九"]

    vectorizer = CountVectorizer() 
    X = vectorizer.fit_transform(data).toarray()
    word_rank = {}


    word_total_list = []
    total = 0
    for ele in X:
        tmp = 0
        for n in ele:
            tmp += n
            total += n
        word_total_list.append(tmp)


    num = 0
    for ele in tqdm(data):
        tmp = {}
        for x, w in jieba.analyse.extract_tags(ele, withWeight=True, allowPOS=('n','nr','ns','nsf','nt','nz','nl','ng','x')):
            if w != 0:
                tmp.setdefault(x,w)
        tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        
        for ele in tmp:
            word_rank.setdefault(ele[0],0)
            word_rank[ele[0]] += ele[1] * (word_total_list[num] / total)
        num += 1


    word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)
    result = ''
    for ele in word_rank[:500]:
        result += str(ele[0]) +'\t' + str(ele[1]) + '\n'

    with open('HatePolitics_jieba_rank.txt','w') as outfile:
        outfile.write(result)
    print(result)





    with open('Gossiping_text.json') as file:
        data = json.load(file)

    vectorizer = CountVectorizer() 
    X = vectorizer.fit_transform(data).toarray()
    word_rank = {}

    word_total_list = []
    total = 0
    for ele in X:
        tmp = 0
        for n in ele:
            tmp += n
            total += n
        word_total_list.append(tmp)


    num = 0
    for ele in tqdm(data):
        tmp = {}
        for x, w in jieba.analyse.extract_tags(ele, withWeight=True, allowPOS=('n','nr','ns','nsf','nt','nz','nl','ng','x')):
            if w != 0:
                tmp.setdefault(x,w)
        tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        
        for ele in tmp:
            word_rank.setdefault(ele[0],0)
            word_rank[ele[0]] += ele[1] * (word_total_list[num] / total)
        num += 1


    word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)
    result = ''
    for ele in word_rank[:500]:
        result += str(ele[0]) +'\t' + str(ele[1]) + '\n'

    with open('Gossiping_jieba_rank.txt','w') as outfile:
        outfile.write(result)
    print(result)


if __name__ == '__main__':
    main()