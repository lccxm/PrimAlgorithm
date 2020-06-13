import re
import os
import heapq
import functools

inf = 99999
from queue import PriorityQueue
mat = []


@functools.total_ordering
class vertice():
    def __init__(self, nome):
        super().__init__()
        self.visited = None
        self.nome = nome
        self.adj = []
        self.p = None
        self.chave = inf
        self.w = 0
    def __cmp__(self, other):
        return self.cmp(self.nome,other.nome)
    def __lt__(self, other):
        return self.nome < other.nome
    def __eq__(self, other):
        return self.nome == other.nome

@functools.total_ordering
class aresta():
    def __init__(self, source_vert, target_vert, w):
        self.w = w
        self.chave = inf
        self.source_vert = source_vert
        self.target_vert = target_vert
    def __cmp__(self, other):
        return self.cmp(self.w, other.w)
    def __lt__(self, other):
        return self.w < other.w
    def __eq__(self, other):
        return (self.w == other.w) and (self.source_vert ==other.souce_vert) and (self.target_vert == other.target_vert)
    def __repr__(self):
        return "<weight="+str(self.w)+", souce_vert="+str(self.source_vert)+", target="+str(self.target_vert)+">"



def read_file(filename):  # 'prim_10_sparse.dot'
     with open(filename, 'r') as f:
         return f.read()




def read_graph(contents, regex):
        pattern = re.compile(regex)
        matches = pattern.findall(contents)
        it = iter(matches)
        arestas =  [aresta(source_vert=x, target_vert=next(it), w=next(it)) for x in it]
        mat = []
        for aresta in arestas:
            mat.append([aresta.source_vert, aresta.target_vert, aresta.w])
        verts = []
        for ar in arestas:
            flag = False
            for vert in verts:
                if ar.source_vert == vert.nome:
                    vert.adj.append(ar)
                    flag = True
            if flag == False:
                vert = vertice(ar.source_vert)
                vert.adj.append(ar)
                verts.append(vert)
        return arestas, verts, verts[0]


# def get_matches(contents, regex):
#     pattern = re.compile(regex)
#     matches = pattern.findall(contents)
#     it = iter(matches)
#     return [vertice(p=x, e=next(it), label=next(it)) for x in it]
#
#

def w(u, v):
    i = 0
    for i in range(len(mat)):
        if mat[i][0] == u.nome and mat[i][1] == v.target_vert:
            return mat[i][2]


# def MST_prim(G, w, r):
# #     for u in G:
# #         for e in G[u]:
# #             if e is not None:
# #                 e.chave = inf
# #                 e.p = None
# #             if e is r:
# #                 e.chave = 0
# #     Q = heapq.heapify()

def MST_prim(grafo, root):
    root.chave = 0
    #Q = heapq.heapify(grafo)
    Q = PriorityQueue()
    for x in grafo:
        Q.put(x)
    while Q:
        u = Q.get()
        for v in u.adj:
            if v in Q.queue:
                if v.w < u.chave:
                    v.p = u
                    u.chave = v.chave
    cost = 0
    for v in grafo:
        cost += v.chave
    print(cost)
    print("a")





contents = read_file('tests/prim_10_sparse.dot')
pattern = r'\d+'

ars, vers, root = read_graph(contents, pattern)
MST_prim(vers, root)


#
# grafo = make_graph(lst)
#
# tests_names = os.listdir('tests/')
#
# print(lst)
#
# print(grafo)
#
#
# root = lst[0]
# for u in grafo:
#     print(u)
#     for e in grafo[u]:
#         if e is not None:
#             e.chave = inf
#             e.p = None
#         if e is root:
#             e.chve = 0
# Q = heapq.heapify(lst)
# while Q:
#     u = heapq.heappop(Q)
#     for v in grafo[u.e]:
#         if(v in Q) and (w(u,v) < v.chave):
#             v.p = u
#             v.chave = w(u, v)
#
# print(grafo)