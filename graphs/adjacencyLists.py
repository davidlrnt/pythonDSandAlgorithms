# Graph represented using adjacency lists approach

graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E','C', 'A'] 
graph['C'] = ['A', 'B', 'E','F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C'] 



#EXERCISE: Turn previous graph to matrix format:
#        A  B  C  E  F
#	  A [0, 1, 1, 0, 0]
#	  B [1, 0, 1, 1, 0]
#	  C [1, 1, 0, 1, 1]
#	  E [0, 1, 1, 0, 0]
#	  F [0, 0, 1, 0, 0]


def aListToMatrix(graph):
	keys = sorted(graph.keys())
	size = len(keys)
	matrix = [[0 for y in range(size)] for i in range(size)]

	keyIndex = {}

	for i, key in enumerate(keys):
		keyIndex[key] = i

	for i in range(size):
		edges = graph[keys[i]]
		row = matrix[i]

		for n in edges:
			row[keyIndex[n]] = 1

	return matrix




res = aListToMatrix(graph)

print(res)