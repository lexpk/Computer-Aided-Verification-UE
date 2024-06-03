class Transition:
    def __init__(self, init, invar, nxt):
        self.variables = {}
        self.init = init
        self.invar = invar
        self.next = nxt
