import networkx as nx
from operator import itemgetter
import community #This is the python-louvain package we installed.
import json

def main():
    with open ('PA_data.json') as file:
        data = json.load(file)
    
    G = nx.Graph()
    for num in data:
        for node in data[num]:
            G.add_edge(int(num), int(node))
    
    # G = nx.Graph({'0':['1','3'], '1':['0','3'], '2':['4'], '3':['0','1'], '4':['2']})
    print(nx.info(G))
    
    # If your Graph has more than one component, this will return False:
    print('is_connected: ' + str(nx.is_connected(G)))

    # Next, use nx.connected_components to get the list of components,
    # then use the max() command to find the largest one:
    print('components: ' + str(nx.number_connected_components(G)))
    components = nx.connected_components(G)
    largest_component = max(components, key=len)
    print(len(largest_component))
    # Create a "subgraph" of just the largest component
    # Then calculate the diameter of the subgraph, just like you did with density.
    #
    subgraph = G.subgraph(largest_component)
    print(len(subgraph))
    print(nx.info(subgraph))
    print('is_connected: ' + str(nx.is_connected(subgraph)))
    print('components: ' + str(nx.number_connected_components(subgraph)))
    # diameter = nx.diameter(subgraph)
    # print("Network diameter of largest component:", diameter)

if __name__ == '__main__':
    main()