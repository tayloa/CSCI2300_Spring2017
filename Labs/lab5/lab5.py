def create_matrix(file):
    matrix = {}
    f = open(file,'r')
    for line in f:
        temp = []
        edge = line.strip().split()
        if int(edge[0]) in matrix:
            matrix[int(edge[0])].append(int(edge[1]))
        else:
            matrix[int(edge[0])] = []
            matrix[int(edge[0])].append(int(edge[1]))
    return matrix

def explore(G,v,visited):
    # if we have visited the node we are at in the graph, don't go down it's path
    if v in visited:
        return
    # add the node to visited since we are going down it's path
    visited.append(v)
    # look at what else the node points to
    if v in G:
        node = G[v]
        # go to each neighbor node and explore it if we haven't visited it
        for neighbor in node:
            if neighbor not in visited:
                explore(G,neighbor,visited)
    return

def dfs(G):
    preorder = []
    for node in G:
        for child in G[node]:
            if child not in preorder:
                preorder.append(child)
    return preorder


def reverse(G):
    GR = {}
    for v in G:
        for node in G[v]:
            if node not in GR:
                GR[node] = []
                GR[node].append(v)
            else:
                GR[node].append(v)
    return GR

# def get_scc(GR,visited):


if __name__ == '__main__':
    file_name = input("Enter your file name: ")
    print(file_name,"\n")
    visited = []
    visited2 = []
    adj_list = create_matrix(file_name)
    print("Adjcency List Format:",adj_list,"\n")
    # print(dfs(adj_list))
    # visited = explore(adj_list,1,visited)
    # print("Visited Nodes:",visited,"\n")
    reverse_adj_list = reverse(adj_list)
    print("Reversed Adjacency List:",reverse_adj_list,"\n")
    print(dfs(reverse_adj_list))

    # visited2 = explore(adj_list,5,visited2)
    # print("Visited Nodes:",visited2,"\n")
