############################################################
# CMPSC 442: Homework 4
############################################################

student_name = "Tirth Patel"

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
        s=set()
        s.add(self.name)
        return s
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
        cnf=self.arg.to_cnf()
        temp=[]
        if type(cnf) is Atom:
            return Not(cnf)
        elif type(cnf) is Not:
            return cnf.arg
        elif type(cnf) is And:
            for i in cnf.conjuncts:
                temp.append(Not(i).to_cnf())
            return Or(*temp).to_cnf()
        elif type(cnf) is Or:
            for i in cnf.disjuncts:
                temp.append(Not(i).to_cnf())
            return And(*temp).to_cnf()


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
        temp=temp[:-1]
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
        temp=[i.to_cnf() for i in self.conjuncts]
        final=[]
        for i in temp:
            if type(i) is And:
                for j in i.conjuncts:
                    final.append(j)
            else:
                final.append(i)
        return And(*final)

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
        temp = temp[:-1]
        temp =temp + ")"
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
        cnf_list=[i.to_cnf() for i in self.disjuncts]
        and_list=[]
        or_list=[]
        for i in cnf_list:
            if type(i) is And:
                and_list.append(i)
            elif type(i) is Or:
                for j in i.disjuncts:
                    or_list.append(j)
            else:
                or_list.append(i)
        if len(and_list)>0:
            first=and_list[0]
            for i in range(1,len(and_list)):
                second=and_list[i]
                dis=[]
                for x in first.conjuncts:
                    temp_list = []
                    if type(x) is Or:
                        for j in x.disjuncts:
                            temp_list.append(j)
                    else:
                        temp_list.append(x)
                    for y in second.conjuncts:
                        temp=[]
                        if type(y) is Or:
                            for j in y.disjuncts:
                                temp.append(j)
                        else:
                            temp.append(y)

                        dis.append(Or(*(temp_list+temp)))
                first=And(*dis)
            solution=[]
            for i in first.conjuncts:
                temp=[]
                if type(i) is Or:
                    for j in i.disjuncts:
                        temp.append(j)
                else:
                    temp.append(i)

                temp=temp+or_list
                solution.append(Or(*temp))
            return And(*solution)
        else:
            return Or(*or_list)


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
        return Or(Not(self.left),self.right).to_cnf()

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
        return And(Or(Not(self.left),self.right),Or(Not(self.right),self.left)).to_cnf()


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
        self.fact_set = set()
    def get_facts(self):
        return self.fact_set
    def tell(self, expr):
        cnf = expr.to_cnf()
        self.fact_set.add(cnf)
    def ask(self, expr):
        clauses = set()
        new = set()
        temp=Not(expr).to_cnf()
        if type(temp) is And:
            for i in temp.conjuncts:
                clauses.add(i)
        else:
            clauses.add(temp)
        for i in self.fact_set:
            if type(i) is And:
                for j in i.conjuncts:
                    clauses.add(j)
            else:
                clauses.add(i)
        
        # while True:
        #     clauses_list = list(clauses)
        #     for i in range(len(clauses_list)-1):
        #         for j in range(i+1,len(clauses_list)):
        #
        #             first=clauses_list[i]
        #             second=clauses_list[j]
        #
        #             first_set=set()
        #             second_set=set()
        #             if type(first) is Or:
        #                 for x in first.disjuncts:
        #                     first_set.add(x)
        #             else:
        #                 first_set.add(first)
        #
        #             if type(second) is Or:
        #                 for x in second.disjuncts:
        #                     second_set.add(x)
        #             else:
        #                 second_set.add(second)
        #
        #
        #             full_final=set()
        #             main=False
        #             print(first_set)
        #             print(second_set)
        #             for x in first_set:
        #                 final = first_set.union(second_set)
        #                 flag=False
        #                 for y in second_set:
        #                     if type(x) is Atom and type(y) is Not:
        #                         if Not(x)==y:
        #                             final.remove(x)
        #                             final.remove(y)
        #                             flag=True
        #                             break
        #                     elif type(x) is Not and type(y) is Atom:
        #                         if x==Not(y):
        #                             final.remove(x)
        #                             final.remove(y)
        #                             flag = True
        #                             break
        #                 if flag:
        #                     main=True
        #                     if len(final)==0:
        #                         continue
        #                     if len(final)==1:
        #                         full_final=full_final.union(final)
        #                     else:
        #                         final_list=list(final)
        #                         for i range:
        #
        #                         full_final.add(Or(*final))
        #             print(full_final)
        #             if len(full_final)==0:
        #                 if not main:
        #                     continue
        #                 else:
        #                     print("bye")
        #                     return True
        #             else:
        #                 new=new.union(full_final)
        #             print("hey",new)
        #     final_flag=False
        #     for i in new:
        #         flag = False
        #         for j in clauses:
        #             if type(i) is type(j):
        #                 if i==j:
        #                     flag=True
        #                     break
        #         if not flag:
        #             final_flag=True
        #             break
        #
        #     if not final_flag:
        #         return False
        #
        #     clauses=clauses.union(new)




############################################################
# Section 2: Logic Puzzles
############################################################

# Puzzle 1

# Populate the knowledge base using statements of the form kb1.tell(...)
kb1 = KnowledgeBase()
kb1.tell(Implies(Atom("mythical"),Not(Atom("mortal"))))
kb1.tell(Implies(Not(Atom("mythical")),And(Atom("mortal"),Atom("mammal"))))
kb1.tell(Implies(Or(Not(Atom("mortal")),Atom("mammal")),Atom("horned")))
kb1.tell(Implies(Atom("horned"),Atom("magical")))

# Write an Expr for each query that should be asked of the knowledge base
mythical_query = Atom("mythical")
magical_query = Atom("magical")
horned_query = Atom("horned")


# Record your answers as True or False; if you wish to use the above queries,
# they should not be run when this file is loaded
is_mythical = False
is_magical = True
is_horned = True

# Puzzle 2

# Write an Expr of the form And(...) encoding the constraints
party_constraints = And(Implies(Or(Atom("m"),Atom("a")),Atom("j")),Implies(Not(Atom("m")),Atom("a")),Implies(Atom("a"),Not(Atom("j"))))

# Compute a list of the valid attendance scenarios using a call to
# satisfying_assignments(expr)
valid_scenarios = [{'j': True, 'a': False, 'm': True}]

# Write your answer to the question in the assignment
puzzle_2_question = """
John and Mary can attend party together without Ann.
"""

# Puzzle 3

# Populate the knowledge base using statements of the form kb3.tell(...)
kb3 = KnowledgeBase()
kb3.tell(Implies(Atom("s1"),And(Atom("p1"),Atom("e2"))))
kb3.tell(Implies(Atom("s2"),And(Or(Atom("p1"),Atom("p2")),Or(Atom("e1"),Atom("e2")))))
kb3.tell(Or(Atom("s1"),Atom("s2")))


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
guilty_suspect = "Brown"
# guilty_suspect = "Clark"

# Describe the queries you made to ascertain your findings
puzzle_4_question = """
Adam says that brown knows the victim and brown says that he does not know the victim. So, Adam or Brown are guilty.This means clark is right. Clark saw adam and brown in downtown with victim and also adam says that the victim is friend of brown. So brown is guilty.
"""

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = """
It took me 10 hours to do this.
"""

feedback_question_2 = """
I found the last part of the assignment challenging because it required formulating propositional logic.
"""

feedback_question_3 = """
I liked implementing methods of given classes espqcially to_cnf(). I would have like more coding than subject questions asked in last part of the assignment
"""
