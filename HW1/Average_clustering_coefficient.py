import json
from scipy.special import comb, perm

def main():

    with open ('data.json') as file:
        data = json.load(file)
    
    C = 0
    for num in data:
        num_len = len(data[num])
        if num_len > 1:
            num_conn = comb(num_len, 2)
            num_nextconn = 0
            for i in range(num_len-1):
                for ele in data[data[num][i]]:
                    if ele in data[num][i+1:]:
                        num_nextconn += 1

            Ci = num_nextconn / num_conn
            C += Ci
    
    ACC = C / len(data)
    print('total: ' + str(C))
    print('avg: ' + str(ACC))
    

if __name__ == '__main__':
    main()