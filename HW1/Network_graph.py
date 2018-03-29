import plotly.plotly as py
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import networkx as nx
import json
import collections

def main():
    #找出最多degree的node
    with open ('PA_data.json') as file:
        data = json.load(file)
    for num in data:
        if (len(data[num]) == 9):
            max_num = num
            print(num)
            break

    #從其node開始往外擴張直到node數>1000
    PA_node = {max_num: []}
    PA_node[max_num] = data[max_num]
    total = 0
    seen, queue = set([max_num]), collections.deque([max_num])
    while(1):
        popTimes = len(queue)
        total += len(queue)
        if total >= 1000:break
        for i in range(popTimes):
            vertex = queue.popleft()                #一次只能左移出一個元素
            for node in data[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
                    PA_node.setdefault(node,[])
                    PA_node[node] = data[node]
                    
                    print(node,total)
        
        
    #畫圖
    # G=nx.random_geometric_graph(200,0.125)
    # pos=nx.get_node_attributes(G,'pos')

    G = nx.Graph()
    for num in PA_node:
        
        for node in PA_node[num]:
            G.add_edge(int(num), int(node))
    print(nx.info(G))
    pos = nx.spring_layout(G)           #給每個node位置

    dmin=1
    ncenter=0
    for n in pos:
        x,y=pos[n]
        print(x,y)
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d

    p=nx.single_source_shortest_path_length(G,ncenter)         

    edge_trace = Scatter(
        x=[],
        y=[],
        line=Line(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=True,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='YIGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for node, adjacencies in enumerate(G.adjacency_list()):
        node_trace['marker']['color'].append(len(adjacencies))
        node_info = '# of connections: '+str(len(adjacencies))
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                    title='Road network of Pennsylvania<br>Node:674502',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
    plot(fig)

if __name__ == '__main__':
    main()