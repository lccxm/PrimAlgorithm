import re
import os

class vertice():
    def __init__(self, p, e, label):
        super().__init__()
        self.p  = p
        self.e = e
        self.label = label
    def __repr__(self):
        return "<p="+self.p+", e="+self.e+", label="+self.label+">"

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
    return grafo
    
contents = read_file('tests/prim_10_sparse.dot')
pattern = r'\d+'

lst = get_matches(contents, pattern)

grafo = make_graph(lst)

tests_names = os.listdir('tests/')


print(lst)

print(grafo)
