from collections import defaultdict, deque


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

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)

    ## loop thorough nodes to find the minimum node and set min_node

    ## if one doesn't exist, break
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue

            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path





def shortest_path(graph, origin, destination):

    if origin == destination:
        return 0, list(origin)

    ## use the algorithm to get the visited and paths
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    ## return the desitination of what's been visited and the list of paths
    return visited[destination], list(full_path)



if __name__ == '__main__':

    graph = Graph()

    nodes = set()

    

    with open("input.txt") as text:
        for line in text:
            curLine = line.strip().split(' ')
            nodes.add(curLine[0])
            nodes.add(curLine[1])
            graph.add_node(curLine[0])
            graph.add_node(curLine[1])            

    with open("input.txt") as text1:
        for line in text1:
            ## strips everything so there's no spaces and then re-spaces it accordingly
            ## now it can be indexed
            curLine = line.strip().split(' ')
            graph.add_edge(str(curLine[0]),str(curLine[1]),int(curLine[2]))
          
    for i in nodes:
        distance, path = shortest_path(graph, '0', str(i))
        print(str(i) + ': ' + str(distance) + ", [" +  ", ".join(path) + "]")

        

        