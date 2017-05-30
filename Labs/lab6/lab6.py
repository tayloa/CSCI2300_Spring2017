from collections import defaultdict, deque
import networkx as nx


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.edges[toNode].append(fromNode)
        self.distances[(fromNode, toNode)] = distance
        
'''
This algorithm takes a graph and a source node as parameters. It then finds all the nodes reachable from source and
returns the total cost of the path.
'''
def dijkstra(G, source):
    # all the nodes that we reached from the source
    visited = {source: 0}   # the source node (where we start) has distance 0
    path = {}               # path is all the edges from the current node we are at
                            # keys are neighbor nodes, values are minimu
    nodes = set(G.nodes) # set of all nodes in the graph

    # loop thorough nodes to find the minimum node and set min_node
    # if one doesn't exist, break
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                # if the node has been visited and we have no min_node, it will be the default
                if min_node is None:
                    min_node = node
                # if there is a node with a lower cost then our source, it will become our min_node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        # pop the current node off the stack because we are currently visiting it
        nodes.remove(min_node)
        # the current weight is our source node
        current_weight = visited[min_node]

        # iterate through all the neighbors of the min_node and take the shortest paths
        for neighbor in G.edges[min_node]:
            # see if there is a distance from the min to another edge in the graph
            # not all nodes have distances
            try:
                weight = current_weight + G.distances[(min_node, neighbor)]
            except:
                continue
            '''
            if the edge has yet to be visited or if we find a shorter distance path
            from the source to the neighbor, update the the distance for visited and the path
            we must take.
            '''
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight # save the cost  of going from the source node to this node
                path[neighbor] = min_node  # save the node w etraveled through to get to the neighbor
    return visited, path




'''
Finds the shortest path from the source node to another node in the graph
'''
def shortest_path(G, source, destination):

    # if the node is trying to get to itself the distance is zero
    if source == destination:
        return 0, list(source)

    # use the algorithm to get the visited and paths from the spurce
    visited, paths = dijkstra(G, source)
    # use a queue to constuct the path
    full_path = deque()
    # get the node we must go through to get to the destination 
    try:
      _destination = paths[destination]
    except:
      _destination = "∞"
      return "∞", list(full_path)

    # while we haven't reached the source, backtrace through the source's neighbors and add it to the path
    # append left because we are backtracing through the queue and want to keep the order
    while _destination != source:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    # add the starting nodes and ending nodes 
    full_path.appendleft(source)
    full_path.append(destination)

    # return the desitination of what's been visited and the list of paths
    return visited[destination], list(full_path)



if __name__ == '__main__':

    graph = Graph()
    nodes = set()    
    fname = input("Enter your file name: ")
    '''
    *** for input.txt: the source node is 1 ***
    *** for input2.txt: the source node is 0 ***
    '''
    source = input("Enter your source node: ")
    f = open(fname,'r')

    
    # build the graph
    for line in f:
        curLine = line.strip().split(' ')
        nodes.add(curLine[0])
        nodes.add(curLine[1])
        graph.add_node(curLine[0])
        graph.add_node(curLine[1])            
        graph.add_edge(str(curLine[0]),str(curLine[1]),int(curLine[2]))
          
    # find the shortest paths
    for node in sorted(nodes):
        distance, path = shortest_path(graph, source, str(node))
        print(str(node) + ': ' + str(distance) + ", [" +  ", ".join(path) + "]")

        

        