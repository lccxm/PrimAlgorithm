inf = 99999

class aresta():
    def __init__(self, p, target):
        self.p = p
        self.target = target
        self.key = inf


    def __cmp__(self, other):
        return self.cmp(self.w, other.w)
    def __lt__(self, other):
        return self.w < other.w
    def __eq__(self, other):
        return (self.w == other.w) and (self.source_vert ==other.souce_vert) and (self.target_vert == other.target_vert)
    def __repr__(self):
        return "<weight="+str(self.w)+", souce_vert="+str(self.source_vert)+", target="+str(self.target_vert)+">"


