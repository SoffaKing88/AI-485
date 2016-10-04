graph = {'S': set(['A', 'D']),
		 'A': set(['S', 'D', 'F']),
		 'B': set(['E', 'C']),
		 'C': set(['B', 'F', 'G']),
		 'D': set(['S', 'A', 'E']),
		 'E': set(['D', 'B', 'F']),
		 'F': set(['A', 'E', 'C']),
		 'G': set(['C'])}
'''
def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

print(dfs(graph, 'S'))
'''

def dfs_path(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

print(list(dfs_path(graph, 'S', 'G')))
