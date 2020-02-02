graph = dict() 
graph['A'] = ['B', 'G', 'D'] 
graph['B'] = ['A', 'F', 'E'] 
graph['C'] = ['F', 'H'] 
graph['D'] = ['F', 'A'] 
graph['E'] = ['B', 'G'] 
graph['F'] = ['B', 'D', 'C'] 
graph['G'] = ['A', 'E'] 
graph['H'] = ['C'] 


# EXERCISE: Traverse graph in breath-first traversal order, return list with vertex values in visited order


def BFT(graph):
	start = sorted(graph.keys())[0]
	queue = [start]
	visited = {}
	visited[start] = True
	orderedVisit = []

	while queue:
		curr = queue.pop()
		orderedVisit.append(curr)
		for adjacent in graph[curr]:
			if adjacent not in visited:
				visited[adjacent] = True
				queue.insert(0,adjacent)

	return orderedVisit


res = BFT(graph)

print(res)