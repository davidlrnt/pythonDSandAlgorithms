class HashTable:
    def __init__(self, size = 255):
        self.count = 0
        self.space = [None for i in range(size)]

    def hash(self, item):
        count = 1
        result = 0
        for char in item:
            result += ord(char) * count
            count += 1
        return result % len(self.space)

    def append(self, item, value):
        hashvalue = self.hash(item)
        if self.space[hashvalue] is None:
            self.space[hashvalue] = [item, value]
            self.count += 1
        else:
            foundSpace = False
            count = 1
            while not foundSpace:
                if self.space[hashvalue + count] is None:
                    foundSpace = True
                    self.space[hashvalue + count] = [item, value]
                    self.count += 1
                count += 1

    def get(self, item):
        hashvalue = self.hash(item)
        if self.space[hashvalue] and self.space[hashvalue][0] == item:
            return self.space[hashvalue][1]
        else:
            foundSpace = False
            count = 1
            while not foundSpace and (hashvalue + count) < len(self.space):
                if self.space[hashvalue + count] and self.space[hashvalue + count][1] == item:
                    foundSpace = True
                    return self.space[hashvalue + count][1]
                count += 1

            return None

    def delete(self, item):
        hashvalue = self.hash(item)
        if self.space[hashvalue] and self.space[hashvalue][0] == item:
            self.space[hashvalue] = None
            self.count -= 1
        else:
            foundSpace = False
            count = 1
            while not foundSpace:
                if self.space[hashvalue + count] and self.space[hashvalue + count][1] == item:
                    foundSpace = True
                    self.space[hashvalue + count] = None
                    self.count -= 1
                count += 1

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

table.delete("pear")

print(table["pear"])
