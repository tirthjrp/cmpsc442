from homework4_tpp5217 import Atom, And, Or, Implies, Not, Iff,satisfying_assignments,KnowledgeBase
a, b, c = map(Atom, "abc")
kb = KnowledgeBase()
kb.tell(Iff(a, Or(b, c)))
kb.tell(Not(a))
print(list(kb.ask(x) for x in [a,Not(a)]))







