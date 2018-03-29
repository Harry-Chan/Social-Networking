import json

def main():
    
    # data = {}                                              #data set
    # with open ('roadNet-PA.txt') as file:
    #     for line in file:
    #         tmp = line.rstrip().split("\t")
    #         num = tmp[0]
    #         data.setdefault(num, [])
    #         data[num].append(tmp[1])
    # json.dump(data, open('data.json','w'))
    
    with open ('data.json') as file:
        data = json.load(file)
    
    totdagree = 0
    totnum = 0
    prenum = -1

    for ele in data:
        totdagree += len(data[ele])
    totnum = len(data)

    avgdagree = totdagree/totnum
    print('total_num: ' + str(totnum))
    print('total_degree: ' + str(totdagree))
    print('avg_degree: ' + str(avgdagree))

    


if __name__ == '__main__':
    main()