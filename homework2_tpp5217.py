############################################################
# CMPSC 442: Homework 2
############################################################
student_name = "Tirth Patel"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
import copy
import math




############################################################
# Section 1: N-Queens
############################################################
class Node_stack:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:


    def __init__(self):
        self.top = None
        self.count = 0


    def isEmpty(self):
        if (self.top == None):
            return True
        else:
            return False

    def __len__(self):
        return self.count


    def push(self, value):
        newnode = Node_stack(value)
        self.count += 1
        if (self.top == None):
            newnode.next = None
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if (self.top == None):
            return None
        else:
            self.count -= 1
            temp = self.top.value
            self.top = self.top.next
            return temp


def helper(n,b):
    r=len(b)
    for c in range(n):
        isAttacted = False
        for i, j in zip(range(r - 1, -1, -1), range(c + 1, n)):
            if b[i] == j:
                isAttacted = True
                break
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if b[i] == j:
                isAttacted = True
                break
        for i in range(r):
            if b[i] == c:
                isAttacted = True
                break
        if not isAttacted:
            p = copy.copy(b)
            p.append(c)
            yield p




def num_placements_all(n):
    num=math.factorial(n*n)
    denom=math.factorial(n*n-n)*math.factorial(n)
    return num//denom


def num_placements_one_per_row(n):
    return n**n


def n_queens_valid(board):
    cmax = max(board) + 1
    for r in range(len(board)):

        for i in range(r):
            if board[i] == board[r]:
                return False

        for i, j in zip(range(r - 1, -1, -1), range(board[r] + 1, cmax, 1)):
            if board[i] == j:
                return False
        for i, j in zip(range(r - 1, -1, -1), range(board[r] - 1, -1, -1)):
            if board[i] == j:
                return False
    return True


def n_queens_solutions(n):
    stack=Stack()
    s=set()
    for i in range(n):
        stack.push([i])
        while not stack.isEmpty():
            board=stack.pop()
            board_tuple=tuple(board)
            if board_tuple not in s:
                s.add(board_tuple)
                for new_board in helper(n,board):
                    if len(new_board)==n:
                        yield new_board
                    else:
                        new_board_tuple=tuple(new_board)
                        if new_board_tuple not in s:
                            stack.push(new_board)



############################################################
# Section 2: Lights Out
############################################################
class Node_queue:
    def __init__(self, value, parent, move):
        self.value = value
        self.next = None
        self.parent = parent
        self.move = move


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        # write your code here
        if (self.head == None and self.tail == None):
            return True
        else:
            return False

    def __len__(self):
        # write your code here
        return self.count

    def enqueue(self, value, parent, move):
        # write your code here
        newnode = Node_queue(value, parent, move)
        self.count += 1
        if (self.head == None and self.tail == None):
            newnode.next = None
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.next = None
            self.tail = newnode

    def dequeue(self):
        # write your code here
        if (self.head == None and self.tail == None):
            return None
        elif (self.head == self.tail):
            self.count -= 1
            temp = self.head
            self.head = self.tail = None
            return temp
        else:
            self.count -= 1
            temp = self.head
            self.head = self.head.next
            return temp


class LightsOutPuzzle(object):

    def __init__(self, board):

        temp = []
        for i in board:
            temp.append(list(i))
        self._board = temp
        self._m = len(board)
        self._n = len(board[0])

    def get_board(self):
        return self._board

    def perform_move(self, row, col):
        self._board[row][col] = not self._board[row][col]
        if (row - 1) >=0:
            self._board[row - 1][col] = not self._board[row - 1][col]
        if (row + 1) < self._m:
            self._board[row + 1][col] = not self._board[row + 1][col]
        if (col - 1) >=0:
            self._board[row][col - 1] = not self._board[row][col - 1]
        if (col + 1) < self._n:
            self._board[row][col + 1] = not self._board[row][col + 1]

    def scramble(self):
        for i in range(self._m):
            for j in range(self._n):
                if random.random() < 0.5:
                    self.perform_move(i, j)

    def is_solved(self):
        for i in range(self._m):
            for j in range(self._n):
                if self._board[i][j]:
                    return False
        return True

    def copy(self):
        return LightsOutPuzzle(copy.deepcopy(self._board))

    def successors(self):
        for i in range(self._m):
            for j in range(self._n):
                new_p = self.copy()
                new_p.perform_move(i, j)
                yield (i, j), new_p

    def convertToTuple(self):
        temp = copy.copy(self._board)
        for i in range(len(temp)):
            temp[i] = tuple(temp[i])
        return tuple(temp)

    def find_solution(self):
        visited = set()
        q = Queue()
        q.enqueue(self.convertToTuple(), None, None)
        while not q.isEmpty():
            n = q.dequeue()
            board = LightsOutPuzzle(n.value)
            if n.value not in visited:
                visited.add(n.value)
                for move, new_board in board.successors():
                    new_board_tuple = new_board.convertToTuple()
                    if new_board_tuple not in visited:
                        if new_board.is_solved():
                            solution = []
                            while n.parent:
                                solution.append(n.move)
                                n = n.parent
                            solution.reverse()
                            solution.append(move)
                            return solution
                        q.enqueue(new_board_tuple, n, move)

        return None


def create_puzzle(rows, cols):
    return LightsOutPuzzle([[False for j in range(cols)] for i in range(rows)])


############################################################
# Section 3: Linear Disk Movement
############################################################
def identical_disks_successor(board):
    for i in range(len(board)):
        if board[i]:
            try:
                if not board[i + 1]:
                    temp_board = copy.copy(board)
                    temp_board[i + 1] = temp_board[i]
                    temp_board[i] = None
                    yield (i, i + 1), temp_board
                if (not board[i + 2]) and board[i + 1]:
                    temp_board = copy.copy(board)
                    temp_board[i + 2] = temp_board[i]
                    temp_board[i] = None
                    yield (i, i + 2), temp_board
            except IndexError:
                pass


def identical_disks_is_solved(board, n):
    for i in range(len(board) - 1, len(board) - n - 1, -1):
        if not board[i]:
            return False
    return True



def solve_identical_disks(length, n):

    board = [1 if i < n else None for i in range(length)]
    q = Queue()
    q.enqueue(board, None, None)
    s = set()
    while not q.isEmpty():
        node = q.dequeue()
        board_tuple = tuple(node.value)
        if board_tuple not in s:
            s.add(board_tuple)
            for move, new_board in identical_disks_successor(node.value):
                if tuple(new_board) not in s:
                    if identical_disks_is_solved(new_board, n):
                        solution = []
                        while node.parent:
                            solution.append(node.move)
                            node = node.parent
                        solution.reverse()
                        solution.append(move)
                        return solution
                    q.enqueue(new_board, node, move)
    return None



def successor_dictinct(board,length):
    l=[-1 for i in range(length)]
    for i in board:
        l[i]=i

    for i in range(len(board)):
        try:
            if l[board[i]+1]==-1:
                board_list = list(board)
                board_list[i]=board_list[i]+1
                yield (board_list[i]-1,board_list[i]), tuple(board_list)
            if (l[board[i]+2]==-1) and l[board[i]+1]>=0:
                board_list = list(board)
                board_list[i] = board_list[i] + 2
                yield (board_list[i]-2, board_list[i]), tuple(board_list)
        except IndexError:
            pass

        if (board[i]-1)>=0:
            if l[board[i]-1]==-1:
                board_list = list(board)
                board_list[i]=board_list[i]-1
                yield (board_list[i]+1,board_list[i]), tuple(board_list)

        if (board[i]-2)>=0:
            if (l[board[i] - 2] == -1) and l[board[i] - 1] >= 0:
                board_list = list(board)
                board_list[i] = board_list[i] - 2
                yield (board_list[i]+2,board_list[i]), tuple(board_list)

def is_solved_distinct(board,length):

    for i in range(len(board)):
        if board[i]!=(length-i-1):
            return False
    return True



def solve_distinct_disks(length, n):

    board=tuple([i for i in range(n)])
    q=Queue()
    s=set()
    q.enqueue(board,None,None)
    while not q.isEmpty():
        node=q.dequeue()
        if node.value not in s:
            s.add(node.value)
            for move, new_board in successor_dictinct(node.value,length):

                if new_board not in s:
                    if is_solved_distinct(new_board,length):
                        solution=[]
                        while node.parent:
                            solution.append(node.move)
                            node=node.parent
                        solution.reverse()
                        solution.append(move)
                        return solution
                    q.enqueue(new_board,node,move)

    return None



############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
It took me about 10 hours.
"""

feedback_question_2 = """
I found the need to keep time complexity small for a function difficult.
"""

feedback_question_3 = """
I liked the implementation of dfs and bfs.
"""
