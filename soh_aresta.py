
import re
from queue import PriorityQueue

inf = 9999

class aresta():
    def __init__(self, target, p=None):
        self.p = p
        self.target = int(target)
        self.chave = inf
        self.visited = False
    def __cmp__(self, other):
        return self.cmp(self.w, other.w)
    def __lt__(self, other):
        return self.target<other.target
    def __eq__(self, other):
        return self.target==other.target
    def __repr__(self):
        if self.p == None:
            return "<target_vert="+str(self.target)+">"
        else:
            return "<target_vert="+str(self.target)+", PAI="+str(self.p)+">"


def read_file(filename, regex):  # 'prim_10_sparse.dot'
     with open(filename, 'r') as f:
        contents = f.read()
        pattern = re.compile(regex)
        matches = pattern.findall(contents)
        it = iter(matches)
        return [[int(x), int(next(it)), int(next(it))] for x in it]

def W(aresta1, aresta2):
    i = 0
    for i in range(len(G)):
        if mat[i][0] == aresta1 and mat[i][1] == aresta2:
            return mat[i][2]
        i += 1

def Adj(aresta):
    i = 0
    lst = []
    for i in range(len(mat)):
        if mat[i][0] == aresta:
            lst.append(mat[i][1])
    return lst

def carrega_obj(G):
    lst = []
    for line in G:
        lst.append(aresta(line[1]))
    return lst

def Prim(G, r):
    r.chave = 0
    Q = G.copy()
    #for g in G:
    #    Q.put(g)
    while Q:
        menor = inf
        for q in Q:
            if q.chave < menor:
                menor = q.chave
                index = Q.index(q)
        u = Q.pop(index)
        for v in Adj(u.target):
            for q in Q:
                #print(q.target, v)
                if q.target == v:
                    v = q
                    break
            if v in Q and W(u.target, v.target) < v.chave:
                v.p = u
                v.chave = W(u.target, v.target)
    print(G)
    print(mat)
mat = read_file('tests/prim_10_sparse.dot', r'\d+')
#print(Adj('7'))
G = carrega_obj(mat)

Prim(G, G[0])