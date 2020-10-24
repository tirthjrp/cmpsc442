############################################################
# CMPSC 442: Homework 4
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from itertools import product



############################################################
# Section 1: Propositional Logic
############################################################

class Expr(object):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

class Atom(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, name):
        self.name = name
        self.hashable = name

    def __eq__(self, other):
        return True if self.name==other.name else False
    def __repr__(self):
        return "Atom"+"(" + str(self.name) + ")"
    def atom_names(self):
        return set(self.name)
    def evaluate(self, assignment):
        return True if assignment[self.name] else False
    def to_cnf(self):
        return self

class Not(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, arg):
        self.arg = arg
        self.hashable = arg
    def __eq__(self, other):
        return True if self.arg==other.arg else False
    def __repr__(self):
        return "Not"+"("+repr(self.arg)+")"
    def atom_names(self):
        return self.arg.atom_names()
    def evaluate(self, assignment):
        return not self.arg.evaluate(assignment)
    def to_cnf(self):
        pass
        
class And(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, *conjuncts):
        self.conjuncts = frozenset(conjuncts)
        self.hashable = self.conjuncts
    def __eq__(self, other):
        return True if self.conjuncts==other.conjuncts else False
    def __repr__(self):
        temp="And("
        for i in self.conjuncts:
            temp+=repr(i)+","
        temp=temp[:-2]
        temp+=")"
        return temp
    def atom_names(self):
        temp=set()
        for i in self.conjuncts:
            temp=temp.union(i.atom_names())
        return temp

    def evaluate(self, assignment):
        for i in self.conjuncts:
            if not i.evaluate(assignment):
                return False
        return True

    def to_cnf(self):
        pass

class Or(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, *disjuncts):
        self.disjuncts = frozenset(disjuncts)
        self.hashable = self.disjuncts
    def __eq__(self, other):
        return True if self.disjuncts==other.disjuncts else False
    def __repr__(self):
        temp = "Or("
        for i in self.disjuncts:
            temp += repr(i) + ","
        temp = temp[:-2]
        temp += ")"
        return temp
    def atom_names(self):
        temp = set()
        for i in self.disjuncts:
            temp = temp.union(i.atom_names())
        return temp
    def evaluate(self, assignment):
        for i in self.disjuncts:
            if i.evaluate(assignment):
                return True
        return False
    def to_cnf(self):
        pass

class Implies(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)
    def __eq__(self, other):
        return True if (self.left==other.left and self.right==other.right) else False
    def __repr__(self):
        return "Implies("+repr(self.left)+","+repr(self.right)+")"
    def atom_names(self):
        return self.left.atom_names().union(self.right.atom_names())
    def evaluate(self, assignment):
        left=self.left.evaluate(assignment)
        right=self.right.evaluate(assignment)
        if left:
            if right:
                return True
            else:
                return False
        else:
            return True
    def to_cnf(self):
        pass

class Iff(Expr):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)
    def __eq__(self, other):
        return True if (self.left==other.left and self.right==other.right) else False
    def __repr__(self):
        return "Iff("+repr(self.left)+","+repr(self.right)+")"
    def atom_names(self):
        return self.left.atom_names().union(self.right.atom_names())
    def evaluate(self, assignment):
        p=self.left.evaluate(assignment)
        q=self.right.evaluate(assignment)
        if p and q:
            return True
        elif not p and not q:
            return True
        else:
            return False
        
    def to_cnf(self):
        pass





def satisfying_assignments(expr):
    s=expr.atom_names()
    l=list(s)
    for i in product([False, True], repeat=len(l)):
        d={}
        for j in range(len(l)):
            d[l[j]]=i[j]
        if expr.evaluate(d):
            yield d










class KnowledgeBase(object):
    def __init__(self):
        pass
    def get_facts(self):
        pass
    def tell(self, expr):
        pass
    def ask(self, expr):
        pass

############################################################
# Section 2: Logic Puzzles
############################################################

# Puzzle 1

# Populate the knowledge base using statements of the form kb1.tell(...)
kb1 = KnowledgeBase()

# Write an Expr for each query that should be asked of the knowledge base
mythical_query = None
magical_query = None
horned_query = None

# Record your answers as True or False; if you wish to use the above queries,
# they should not be run when this file is loaded
is_mythical = None
is_magical = None
is_horned = None

# Puzzle 2

# Write an Expr of the form And(...) encoding the constraints
party_constraints = None

# Compute a list of the valid attendance scenarios using a call to
# satisfying_assignments(expr)
valid_scenarios = None

# Write your answer to the question in the assignment
puzzle_2_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

# Puzzle 3

# Populate the knowledge base using statements of the form kb3.tell(...)
kb3 = KnowledgeBase()

# Write your answer to the question in the assignment; the queries you make
# should not be run when this file is loaded
puzzle_3_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

# Puzzle 4

# Populate the knowledge base using statements of the form kb4.tell(...)
kb4 = KnowledgeBase()

# Uncomment the line corresponding to the guilty suspect
# guilty_suspect = "Adams"
# guilty_suspect = "Brown"
# guilty_suspect = "Clark"

# Describe the queries you made to ascertain your findings
puzzle_4_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
