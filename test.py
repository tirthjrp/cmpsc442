from homework4_tpp5217 import Atom, And, Or, Implies, Not, Iff,satisfying_assignments
from itertools import product
expr=And(Atom("a"),Atom("b"))

print(list(satisfying_assignments(expr)))

