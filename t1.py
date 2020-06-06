import re
import os
import heapq

class vertice():
    def __init__(self, p, e, label):
        super().__init__()
        self.p  = p
        self.e = e
        self.label = label
        self.chave = 0
    def __repr__(self):
        return "<p="+self.p+", e="+self.e+", label="+self.label+"chave="+str(self.chave)+">"

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


print(lst)

print(grafo)
root = lst[0]
for u in grafo:
    print(u)
    for e in grafo[u]:
        if e is not None:
            e.chave = 999
            e.p = None
        if e is root:
            e.chve=0


print(grafo)

from dataclasses import dataclass, field

# Setting frozen=True and eq=True makes a class immutable and hashable.
# eq=False is needed so that dictionary can contain multiple items with
# the same key (Node(idnum)) but with different values (cost)
@dataclass(eq=False)
class Node :
    idnum : int

@dataclass
class Graph :
    source  : int
    adjlist : dict

def PrimsMST(self):

        # Priority queue is implemented as a dictionary with
        # keys as object of 'Node' class and value.
        # Since the priority queue will can have multiple entries for the 
        # same adjnode but with different cost, we have to use objects as
        # keys so that they can be stored in a dictionary. 
        # [As dictionary can't have duplicate keys so objectify the key]

        priority_queue = { Node(self.source) : 0 }
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0

        while priority_queue :
            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)
            cost = priority_queue[node]

            # Remove the element from a dictionary in python
            del priority_queue[node]

            if added[node.idnum] == False :
                min_span_tree_cost += cost
                added[node.idnum] = True
                print("Added Node : " + str(node.idnum) + ", cost now : "+str(min_span_tree_cost))

                for item in self.adjlist[node.idnum] :
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False :
                        priority_queue[Node(adjnode)] = adjcost

        return min_span_tree_cost