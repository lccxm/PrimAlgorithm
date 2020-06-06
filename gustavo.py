import re
import os
import heapq
import functools
import itertools
import queue
from dataclasses import dataclass, field
from typing import Any

@functools.total_ordering
class vertice():
    def __init__(self, e, label, p=None, chave=0):
        super().__init__()
        self.p  = p
        self.e = e
        self.label = label
        self.chave = 0
        priority = self.chave
    def __hash__(self):
        return hash(str(self.e))
    def __eq__(self, other):
        return self.label == other.label
    @functools.total_ordering
    def __lt__(self, other):
        return self.label < other.label
    def __repr__(self):
        return "<p="+str(self.p)+", e="+str(self.e)+", label="+str(self.label)+"chave="+str(self.chave)+">"


def read_file(filename): #'prim_10_sparse.dot'
    with open(filename, 'r') as f:
        return f.read()

def get_matches(contents, regex):
    pattern = re.compile(regex) 
    matches = pattern.findall(contents)
    it = iter(matches)
    return [vertice(p=x, e=next(it), label=next(it)) for x in it ]

def make_graph(lst):
    grafo = {}
    for v in lst:
        if v.p in grafo:
            grafo[v.p].append(v)
        else:
            grafo[v.p] = [v]
    for v in grafo:
        grafo[v].append(None)
    return grafo
    
contents = read_file('tests/prim_10_sparse.dot')
pattern = r'\d+'

lst = get_matches(contents, pattern)

grafo = make_graph(lst)

tests_names = os.listdir('tests/')

def w(u, v):
    for vert in grafo[u.e]:
        if vert.e == v.e:
            return vert.label


    
'''Q = pq()
for e in lst:
    Q.add(e, priority=e.chave)'''
root = lst[0]
for u in grafo:
    for e in grafo[u]:
        if e is not None:
            e.chave = 999
            e.p = None
        if e is root:
            e.chave=0
Q = []
heapq.heapify(lst)
while True:
    print(heapq.heappop(lst))
'''while Q:
    u = heapq.heappop(Q)
    for v in grafo[u.e]:
        if (v in Q) and (w(u, v)<v.chave):
            v.p = u
            v.chave = w(u, v)'''


print(grafo)
