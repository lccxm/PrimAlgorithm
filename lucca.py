import re
import os
import heapq
from functools import total_ordering

inf = 99999




@total_ordering
class vertice():
    def __init__(self, adj, label, p=None, chave=0):
        super().__init__()
        self.p = p
        self.adj = adj
        self.label = label
        self.chave = chave


    def __repr__(self):
        return "<p=" + self.p + ", adj=" + self.adj + ", label=" + self.label + "chave=" + str(self.chave) + ">"

    def __lt__(self, other):
        return self.chave < other.chave




def read_file(filename):  # 'prim_10_sparse.dot'
     with open(filename, 'r') as f:
         return f.read()


def read_graph(contents, regex):
        pattern = re.compile(regex)
        matches = pattern.findall(contents)
        it = iter(matches)
        return [vertice(p=x, adj=next(it), label=next(it)) for x in it]



# def get_matches(contents, regex):
#     pattern = re.compile(regex)
#     matches = pattern.findall(contents)
#     it = iter(matches)
#     return [vertice(p=x, e=next(it), label=next(it)) for x in it]
#
#
def make_graph(lst):
    grafo = {}
    for v in lst:
        if v.p in grafo:
            grafo[v.p].append(v)
        else:
            grafo[v.p] = [v]
    return grafo

def w(u, v):
    for vert in grafo[u.adj]:
        if vert.adj == v.adj:
            return vert.label

# def MST_prim(G, w, r):
# #     for u in G:
# #         for e in G[u]:
# #             if e is not None:
# #                 e.chave = inf
# #                 e.p = None
# #             if e is r:
# #                 e.chave = 0
# #     Q = heapq.heapify()

def MST_prim(grafo, lst):
    r = lst[0]
    for u in grafo:
        for e in grafo[u]:
            e.chave = inf
            e.p = None
            if e is r:
                e.chave = 0
    Q = []
    print(Q)

    Q = heapq.heapify(lst)


contents = read_file('tests/prim_10_sparse.dot')
pattern = r'\d+'

lst = read_graph(contents, pattern)
grafo = make_graph(lst)

MST_prim(grafo,lst)



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