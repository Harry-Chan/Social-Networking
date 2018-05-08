import json
import collections
import time
import random

def main():
    stime = time.time()
    with open('CA_data.json') as file:
        data = json.load(file)
    
    max_diameter = 0
    for i in range(50):                       #重複跑50次
        diameter = 0
        start_node = str(random.randint(0,len(data)))           #隨機random 一個node

        while(1):
            end_node, d = bfs(data,start_node)
            if d == diameter:
                break
            elif d > diameter:
                diameter = d
                start_node = end_node
                
        if diameter > max_diameter :
            max_diameter = diameter

    print('start_node: ' + str(start_node))
    print('end_node: ' + str(end_node))
    print('diameter: ' + str(max_diameter))
    etime = time.time()
    print(etime-stime)
    
    with open('CA_Diameter.txt','w') as outfile:
        outfile.write(str(start_node) + ' ' + str(end_node)+ ' ' +str(max_diameter) + ' ' + str(etime-stime))
    
def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])            #set(集合):可以快速加入元素，沒有記錄元素位置
    d = 0                                                           #deque(雙端陣列):可以list從頭刪除、新增資料
    while queue:                                                    # .popleft(), .appendleft()，且傳統list快速
        popTimes = len(queue)
        for i in range(popTimes):
            vertex = queue.popleft()                #一次只能左移出一個元素
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
        
        if len(queue) != 0 : d += 1
    
    return vertex, d

if __name__ == '__main__':
    main()