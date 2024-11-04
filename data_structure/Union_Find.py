# Union-Find Tree // 1-indexed 
# vertex = 1, 2, ... , N
class unionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * (n + 1)
        self.size = [1] * (n + 1)       # size of subtrees

    # searching root of tree (the elements that doesn't have parent) // with path compression
    def root(self, vertex):
        if self.parent[vertex] == -1:
            return vertex
        else:
            self.parent[vertex] = self.root(self.parent[vertex])    # path compression
        return self.parent[vertex]
    
    # unite element u and v // Union-by-size
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if (self.size[root_u] <= self.size[root_v]):
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            elif (self.size[root_u] > self.size[root_v]):
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
    
    def isSame(self, u, v):
        return (self.root(u) == self.root(v))       # bool
    
    def member(self, u):
        root_u = self.root(u)
        return [e for e in range(1, self.n + 1) if self.root(e) == root_u]
    
    def rootList(self):
        return [i for i in range(1, self.n + 1) if self.parent[i] == -1]

    def groupList(self):
        return [self.member(u) for u in self.rootList()]
    
# vertex: any object // labels: any collection
class unionFindSet(unionFind):
    def __init__(self, labels):
        self.Set = set(labels)
        self.n = len(self.Set)
        self.parent = [-1] * self.n
        self.SetToIndex = {key: (i+1) for i, key in enumerate(labels)}
        self.IndexToSet = {i+1: key for i, key in enumerate(labels)}

    def find(self, x):
        return self.IndexToSet[super().root(self.SetToIndex[x])]
    
    def unite(self, x, y):
        super().unite(self.SetToIndex[x], self.SetToIndex[y])
    
    def isSame(self, x, y):
        return super().isSame(self.SetToIndex[x], self.SetToIndex[y])
    
    def member(self, x):
        root_x = self.root(self.SetToIndex[x])
        return [self.IndexToSet[i] for i in range(1, self.n + 1) if self.root(i) == root_x]
    
    def rootList(self):
        return [self.IndexToSet[i] for i in range(1, self.n + 1) if self.parent[i] == -1]

    def groupList(self):
        return [self.member(u) for u in self.rootList()]