import json


def main():

    data = {}
    with open('roadNet-CA.txt') as file:
        for line in file:
            tmp = line.rstrip().split('\t')
            data.setdefault(str(tmp[0]), [])
            data[tmp[0]].append(tmp[1])

    json.dump(data,open('CA_data.json','w'))

if __name__ == '__main__':
    main()