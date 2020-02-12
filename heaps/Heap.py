class Heap:
	def __init__(self):
		self.nodes = [0]
		self.count = 0

	def arrange(self):
		parent = len(self.nodes)//2
		lastInsert = len(self.nodes) - 1

		while self.nodes[parent] > self.nodes[lastInsert]:
			self.nodes[lastInsert], self.nodes[parent] = self.nodes[parent], self.nodes[lastInsert]
			lastInsert = parent
			parent = parent//2

	def sink(self):
		root = 1

		left = root * 2
		right = root * 2 + 1

		if self.nodes[left] < self.nodes[right]:
			self.nodes[left], self.nodes[root] = self.nodes[root], self.nodes[left]
		elif self.nodes[right] < self.nodes[right]:
			self.nodes[right], self.nodes[root] = self.nodes[root], self.nodes[right]


	def insert(self, v):
		self.nodes.append(v)
		self.count += 1
		if self.count > 1:
			self.arrange()

	#pop heap root
	def pop(self):
		self.nodes[1] = self.nodes[-1]
		self.nodes.pop()
		self.sink()











heap = Heap()
heap.insert(18)
heap.insert(12)
heap.insert(5)
heap.insert(15)

print(heap.nodes)

heap.pop()

print(heap.nodes)