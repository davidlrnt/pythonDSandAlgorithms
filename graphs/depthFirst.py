graph = dict() 
graph['A'] = ['B', 'S'] 
graph['B'] = ['A'] 
graph['S'] = ['A','G','C'] 
graph['D'] = ['C'] 
graph['G'] = ['S','F','H'] 
graph['H'] = ['G','E'] 
graph['E'] = ['C','H'] 
graph['F'] = ['C','G'] 
graph['C'] = ['D','S','E','F'] 
# EXERCISE: Traverse graph in depth-first traversal order, return list with vertex values in visited order


def DFT(graph):
	start = sorted(graph.keys())[0]

	stack = [start]
	visited = {}
	visited[start] = True
	orderVisited = []

	while stack:
		curr = stack.pop()
		orderVisited.append(curr)
		for adjacent in sorted(graph[curr])[::-1]:
			if adjacent not in visited:
				stack.append(adjacent)
				visited[adjacent] = True


	return orderVisited


res = DFT(graph)

print(res)