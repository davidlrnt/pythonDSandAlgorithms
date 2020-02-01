class HashTable:
    def __init__(self):
        self.count = 0
        self.space = [None for i in range(255)]

    def hash(self, item):
        count = 1
        result = 0
        for char in item:
            result += ord(char) * count
        return result % len(self.space)

    def append(self, item, value):
        hashvalue = self.hash(item)
        if self.space[hashvalue] is None:
            self.space[hashvalue] = [item, value]
        else:
            foundSpace = False
            count = 1
            while not foundSpace:
                if self.space[hashvalue + count] is None:
                    foundSpace = True
                    self.space[hashvalue + count] = [item, value]

    def get(self, item):
        hashvalue = self.hash(item)
        if self.space[hashvalue] and self.space[hashvalue][0] == item:
            return self.space[hashvalue][1]
        else:
            foundSpace = False
            count = 1
            while not foundSpace:
                if self.space[hashvalue + count] and self.space[hashvalue + count][1] == item:
                    foundSpace = True
                    return self.space[hashvalue + count][1]

    def __setitem__(self, key, value): 
        self.append(key, value) 

    def __getitem__(self, key): 
        return self.get(key) 

table = HashTable()


table.append("apple", 5)
table.append("mayo", 1)
table.append("avocado", 2)
table.append("lemon", 2)
table.append("lime", 3)

print(table.get("avocado"))
print(table.get("lime"))


table["pear"] = 5

print(table["pear"])