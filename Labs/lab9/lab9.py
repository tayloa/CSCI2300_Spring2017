import networkx as nx


# Ford-Fulkerson maximum-flow algorithm
def max_flow(G,s,t):
	# find all paths from source to sink
	max_flow = 0
	residual = G.copy()
	path = nx.dijkstra_path(residual,s,t)
	'''
	find the min flow for each path by comparing each edge capacity to the next in the path
	'''
	while path:
		min_flow = residual[path[0]][path[1]]['weight']
		for i in range(1,len(path)):
			capacity = G[path[i-1]][path[i]]['weight']
			min_flow = min(min_flow,capacity)		
		'''
		adjust the residual paths using the 
		'''
		for i in range(1,len(path)):
			capacity = G[path[i-1]][path[i]]['weight']
			''' if it has a back edge, decrement it'''
			if residual.has_edge(path[i],path[i-1]):
				residual[path[i]][path[i-1]]['weight'] += min_flow
				residual[path[i-1]][path[i]]['weight'] -= min_flow
			'''else add a back edge'''
			else:
				residual.add_edge(path[i],path[i-1],min_flow) # back edge
				residual[path[i-1]][path[i]]['weight'] = capacity - min_flow) # forward
		max_flow += min_flow
		try:
			path = nx.dijkstra_path(residual,s,t)
		except nx.NetworkXNoPath:
			break
		print("Path:",path,"Min Flow:",min_flow,"Max Flow:",max_flow)

def min_cut(G,s,t):
	return 0

if __name__ == "__main__":
	G = nx.DiGraph()
	nodes = set([])
	with open("example.txt") as text:
		for line in text:
			values = list(map(int, line.strip().split(' ')))
			nodes.add(values[0])
			nodes.add(values[1])
			G.add_edge(values[0],values[1],weight=values[2])
	max_flow(G,min(nodes),max(nodes))

