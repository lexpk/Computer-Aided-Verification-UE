from itertools import chain
from pyModelChecking import Kripke
from pyModelChecking.LTL.language import AtomicProposition


def enumerateModels(bound, formula):
    atoms = getatoms(formula)
    ### Your code here
    return [
        Kripke(R=[(i, i+1) for i in range(bound)] + [(bound, bound)], L={i: atoms for i in range(bound+1)})
    ]


def getatoms(formula):
    if isinstance(formula, AtomicProposition):
        return [formula]
    else:
        return list(chain(*[getatoms(f) for f in formula.subformulas()]))