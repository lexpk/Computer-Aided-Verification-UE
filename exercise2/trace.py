from logic import *

class Trace:
    '''
    This class implements (k, l)-loops as outlined on
    page 370 of the lecture notes.
    '''
    def __init__(self, k, l, labels):
        self.k = k
        self.l = l
        self.states = list(range(k))
        self.labels = labels
        self.initial = 0
        self.next = lambda i: i + 1 if i < k - 1 else l

    def subtrace(self, i):
        '''
        Return the subtrace starting from state i.
        '''
        if i < self.l:
            return Trace(self.k - i, self.l - i, self.labels[i:])
        elif (i - self.l) % (self.k - self.l) == 0:
            return Trace(self.k - self.l, 0, self.labels[self.l:])
        else:
            j = (i - self.l) % (self.k - self.l)
            return Trace(self.k - self.l, j, self.labels[self.l + j:] + self.labels[self.l:self.l + j])
    def subtraces(self):
        '''
        Return all subtraces of the trace.
        '''
        return [self.subtrace(i) for i in range(self.k)]

    def evaluate(self, formula):
        '''
        Evaluate if the formula holds on the trace.
        '''
        if isinstance(formula, BooleanExpression):
            return formula.evaluate(self.labels[self.initial])
        if isinstance(formula, G):
            for trace in self.subtraces():
                if not trace.evaluate(formula.formula):
                    return False
            return True
        if isinstance(formula, F):
            for trace in self.subtraces():
                if trace.evaluate(formula.formula):
                    return True
            return False
        if isinstance(formula, X):
            return self.subtrace(1).evaluate(formula.formula)
        if isinstance(formula, U):
            for i, trace in enumerate(self.subtraces()):
                if trace.evaluate(formula.right):
                    break
            else:
                return False
            for trace in self.subtraces()[:i]:
                if not trace.evaluate(formula.left):
                    return False
            else:
                return True