############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Tirth Patel"


############################################################
# Section 1: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]


def concatenate(seqs):
    return [y for x in seqs for y in x]


def transpose(matrix):
    r = len(matrix)
    c = len(matrix[0])
    result = [[] for i in range(c)]
    for i in range(r):
        for j in range(c):
            result[j].append(matrix[i][j])
    return result


############################################################
# Section 2: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]


def all_but_last(seq):
    return seq[:-1]


def every_other(seq):
    return seq[::2]


############################################################
# Section 3: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[0:i]


def suffixes(seq):
    for i in range(len(seq)):
        yield seq[i:]
    yield seq[0:0]


def slices(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            yield seq[i:j]
        yield seq[i:]


############################################################
# Section 4: Text Processing
############################################################

def normalize(text):
    return text.strip(" ").lower()


def no_vowels(text):
    s = ""
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            continue
        s = s + i
    return s


def digits_to_words(text):
    l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    s = ""
    for i in text:
        if i.isdigit():
            s += l[int(i)]
            s += " "
    return s.strip(" ")


def to_mixed_case(name):
    name = name.strip("_")
    l = name.split("_")
    l = list(filter(lambda x: x != '', l))
    for i in range(len(l)):
        l[i] = l[i].lower()
        if i == 0:
            continue
        l[i] = l[i].capitalize()
    return "".join(l)


############################################################
# Section 5: Polynomials
############################################################
class Polynomial(object):

    def __init__(self, polynomial):
        l = []
        for i in polynomial:
            temp = (i[0], i[1])
            l.append(temp)
        self.p = tuple(l)

    def get_polynomial(self):
        return self.p

    def __neg__(self):
        l = []
        for i in self.p:
            temp = (-i[0], i[1])
            l.append(temp)
        return Polynomial(l)

    def __add__(self, other):
        return Polynomial(self.p + other.p)

    def __sub__(self, other):
        return Polynomial(self.p + (-other).p)

    def __mul__(self, other):
        l = []
        for i in self.p:
            for j in other.p:
                temp = (i[0] * j[0], i[1] + j[1])
                l.append(temp)
        return Polynomial(l)

    def __call__(self, x):
        return sum([i[0] * (x ** i[1]) for i in self.p])

    def simplify(self):
        d = {}
        l = []
        for i in self.p:
            if i[1] in d.keys():
                d[i[1]] += i[0]
            else:
                d[i[1]] = i[0]
        temp = list(d.keys())
        temp.sort(reverse=True)
        for i in temp:
            if d[i] == 0:
                continue
            l.append((d[i], i))
        if len(l) == 0:
            l.append((0, 0))
        self.p = tuple(l)

    def __str__(self):
        l = []
        for i in range(len(self.p)):
            if i == 0:
                l.append(self.get_term(self.p[i][0], self.p[i][1]))
            else:
                if self.p[i][0] >= 0:
                    l.append("+")
                    l.append(self.get_term(self.p[i][0], self.p[i][1]))
                else:
                    l.append("-")
                    l.append(self.get_term(-self.p[i][0], self.p[i][1]))
        return " ".join(l)

    def get_term(self, c, p):
        if p == 0:
            return "{}".format(c)
        elif p == 1:
            if c == 1:
                return "x"
            elif c == -1:
                return "-x"
            else:
                return "{}x".format(c)
        else:
            if c == 1:
                return "x^{}".format(p)
            elif c == -1:
                return "-x^{}".format(p)
            else:
                return "{}x^{}".format(c, p)


############################################################
# Section 6: Feedback
############################################################

feedback_question_1 = """
It took me 6.5 hours to complete homework 1.
I have learnt python before but didn't remember much, so I had to get used to it again 
while doing the homework because of which it took me more time than it should.
"""

feedback_question_2 = """
The first four sections were somewhat easy. The last two methods of section polynomials were bit challenging
beacuse it had so many cases to look for.  
"""

feedback_question_3 = """
I liked almost all the section. I did not find the list comprehension section useful because it requires
you to rewrite a existing logic in more compact way. Though it reduces the code, list comprehension takes 
the same time as normal logic. I liked the last section more than others because it was more challenging.
Overall, I would say i enjoyed writing this code and it helped me get used to python.
"""
