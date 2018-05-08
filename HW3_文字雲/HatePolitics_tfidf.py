import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.feature_extraction.text import TfidfVectorizer
import math
import time

def main():
    with open('HatePolitics.json') as file:
        data = json.load(file)

    print(len(data))
    tmp = ["習近平 習近平 習近平 習近平 安安 中國 台灣 席包子",
    "習近平 台灣 兩岸 李克強 黨主席 巴拿馬 席大大",
    "習近平 中國 香港 美國 馬英九 馬英九"]

    #将文本中的词语转换为词频矩阵  
    vectorizer = CountVectorizer()  
    #计算个词语出现的次数  
    X = vectorizer.fit_transform(data).toarray()
    #获取词袋中所有文本关键词  
    word = vectorizer.get_feature_names()  
    
    #将词频矩阵X统计成TF-IDF值  
    transformer = TfidfTransformer() 
    tfidf = transformer.fit_transform(X)
    weight = tfidf.toarray()
    idf = transformer.idf_

    word_rank = {}
    word_rank2 = {}
    # print(tfidf,word)
    # for j in range(len(word)):
    #     word_rank.setdefault(word[j],transformer.idf_[j])
    word_total_list = []
    total = 0
    for ele in X:
        tmp = 0
        for n in ele:
            tmp += n
            total += n
        word_total_list.append(tmp)
    print(total)

    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词
        tmp = {}
        tmp2 = {}
        for j in range(len(word)):
            if weight[i][j] != 0:
                tmp.setdefault(word[j], (X[i][j] / word_total_list[i]) * math.log(idf[j]))
                tmp2.setdefault(word[j], weight[i][j])

                # print(word[j],X[i][j],word_total_list[i],idf[j],word_total_list[i],total,(X[i][j] / word_total_list[i]) * idf[j])
        tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        tmp2 = sorted(tmp2.items(), key=lambda x: x[1], reverse=True)

        for ele in tmp[:20]:
            word_rank.setdefault(ele[0],0)
            word_rank[ele[0]] += ele[1] * (word_total_list[i] / total)

        for ele in tmp2[:20]:
            word_rank2.setdefault(ele[0],0)
            word_rank2[ele[0]] += ele[1] * (word_total_list[i] / total)

            

    word_rank = sorted(word_rank.items(), key=lambda x: x[1], reverse=True)
    result = '=========== 1~100 ===========\n'
    num = 0 
    for ele in word_rank[:300]:
        num += 1
        if num == 100:
            result += '=========== 101~200 ===========\n'
        elif num == 200:
            result += '=========== 201~300 ===========\n'
        result += str(ele[0]) +'\t' + str(ele[1]) + '\n'
    
    print(result)

    with open('HatePolitics_rank300.txt','w') as outfile:
        outfile.write(result)


    print('+'*20)
    word_rank2 = sorted(word_rank2.items(), key=lambda x: x[1], reverse=True)
    result = '=========== 1~100 ===========\n'
    num = 0 
    for ele in word_rank2[:300]:
        num += 1
        if num == 100:
            result += '=========== 101~200 ===========\n'
        elif num == 200:
            result += '=========== 201~300 ===========\n'
        result += str(ele[0]) +'\t' + str(ele[1]) + '\n'

    print(result)
    
    with open('HatePolitics_rank300_sklearn.txt','w') as outfile:
        outfile.write(result)

if __name__ == '__main__':
    main()