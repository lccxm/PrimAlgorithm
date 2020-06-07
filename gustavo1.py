import heapq
import re
import functools


@functools.total_ordering
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.p = None
        self.adj = []
    def __repr__(self):
        return "<name="+str(self.name)+", visited="+str(self.visited)+". p="+str(self.p)+">"
    def __cmp__(self, other):
        return self.cmp(self.name, other.name)
    def __lt__(self, other):
        return self.name < other.name
    def __eq__(self, other):
        return self.name == other.name
@functools.total_ordering
class Edge(object):
    def __init__(self, w, source_vert, target_vert):
        self.w = w
        self.source_vert = source_vert
        self.target_vert = target_vert
    def __cmp__(self, other):
        return self.cmp(self.w, other.w)
    def __lt__(self, other):
        return self.w < other.w
    def __eq__(self, other):
        return (self.w == other.w) and (self.source_vert ==other.souce_vert) and (self.target_vert == other.target_vert)
    def __repr__(self):
        return "<weight="+str(self.w)+", souce_vert="+str(self.source_vert.name)+", target="+str(self.target_vert.name)+">"
class Prim(object):
    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.spanning_tree = []
        self.edge_heap = []
        self.full_cost = 0

    def construct_spanning_tree(self, vertex):
        #tira root
        #vertex = self.unvisited_list.pop()
        #self.unvisited_list.remove(vertex)
        while self.unvisited_list:
            print("unvisited: ")
            print(self.unvisited_list)
            print("vertex adj_list:")
            print(vertex.adj)
            for edge in vertex.adj:
                if edge in self.unvisited_list:
                    heapq.heappush(self.edge_heap, edge)
            min_edge = heapq.heappop(self.edge_heap)
            self.spanning_tree.append(min_edge)
            print(f'Edge to the spanding tree: {min_edge.source_vert.name} - {min_edge.target_vert.name}')
            self.full_cost += int(min_edge.w)
            vertex = min_edge.target_vert
            self.unvisited_list.remove(vertex)

def read_file(filename): #'prim_10_sparse.dot'
    with open(filename, 'r') as f:
        return f.read()

def get_matches(contents, regex):
    pattern = re.compile(regex) 
    matches = pattern.findall(contents)
    it = iter(matches)
    tuples = [(x, next(it), next(it)) for x in it ]
    vert_set = set()
    for t in tuples:
        vert_set.add(t[0])
    verts = []
    flag = True
    for vert_name in vert_set:
        if flag:
            root = Vertex(vert_name)
            flag = False
        verts.append(Vertex(vert_name))
    edges = []
    for x in tuples:
        edges.append(Edge(x[2], Vertex(x[0]), Vertex(x[1])))
    return verts, edges, root

def get_edge(lst, source, target):
    for e in lst:
        if source==e.source_vert.name and target==e.target_vert.name:
            return e
def get_vert(lst, name):
    for v in lst:
        if v.name == name:
            return v
    


verts, edges, root = get_matches("1 2 2; 1 3 8; 1 4 6; 1 3 3; 3 1 5", r'\d+')
print(edges)
print()
#print(get_edge(edges, '45', '46'))

for edge in edges:
    for vert in verts:
        if edge.source_vert.name == vert.name:
            vert.adj.append(edge)
            break

'''print(verts)
print(get_vert(verts, '45').adj)
print(get_vert(verts, '45').adj[1])'''

algorithm = Prim(verts)
vertex = algorithm.unvisited_list.pop()
algorithm.construct_spanning_tree(vertex)