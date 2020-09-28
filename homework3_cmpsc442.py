############################################################
# CMPSC 442: Homework 3
############################################################

student_name = "Tirth Patel"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import copy
import random
import heapq
import math
from dataclasses import dataclass, field
from typing import Any



############################################################
# Section 1: Tile Puzzle
############################################################
@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: Any=field(compare=False)

def create_tile_puzzle(rows, cols):
    l=[[0 if j==(rows*cols) else j for j in range(((i-1)*cols)+1,((i-1)*cols)+1+cols) ]for i in range(1,rows+1)]
    return TilePuzzle(l)

class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self._board=board
        self._r=len(board)
        self._c=len(board[0])
        self._empty=[]
        self.parent=None
        self.move=None
        self.g=None
        flag=False
        for i in range(self._r):
            for j in range(self._c):
                if self._board[i][j] == 0:
                    self._empty.append(i)
                    self._empty.append(j)
                    flag=True
                    break
            if flag:
                break

    def get_board(self):
        return self._board

    def perform_move(self, direction):

        if direction=="up":
            if (self._empty[0]-1)>=0:
                self._board[self._empty[0]][self._empty[1]],self._board[self._empty[0]-1][self._empty[1]]=self._board[self._empty[0]-1][self._empty[1]],self._board[self._empty[0]][self._empty[1]]
                self._empty[0]-=1
                return True

        elif direction=="down":
            if (self._empty[0] + 1)< self._r:
                self._board[self._empty[0]][self._empty[1]], self._board[self._empty[0] + 1][self._empty[1]] = self._board[self._empty[0] + 1][self._empty[1]], self._board[self._empty[0]][self._empty[1]]
                self._empty[0] += 1
                return True

        elif direction=="right":
            if (self._empty[1] + 1) < self._c:
                self._board[self._empty[0]][self._empty[1]], self._board[self._empty[0]][self._empty[1]+1] = \
                self._board[self._empty[0]][self._empty[1]+1], self._board[self._empty[0]][self._empty[1]]
                self._empty[1] += 1
                return True

        elif direction=="left":
            if (self._empty[1] - 1) >= 0:
                self._board[self._empty[0]][self._empty[1]], self._board[self._empty[0]][self._empty[1]-1] = \
                self._board[self._empty[0]][self._empty[1]-1], self._board[self._empty[0]][self._empty[1]]
                self._empty[1] -= 1
                return True

        return False



    def scramble(self, num_moves):
        for _ in range(num_moves):
            direction=random.choice(["up","down","right","left"])
            self.perform_move(direction)


    def is_solved(self):
        for i in range(self._r):
            for j in range(self._c):
                if i==self._r-1 and j==self._c-1:
                    if self._board[i][j]!=0:
                        return False
                else:
                    if self._board[i][j]!=i*self._c+j+1:
                        return False
        return True



    def copy(self):
        return TilePuzzle(copy.deepcopy(self._board))

    def successors(self):
        if (self._empty[0]-1)>=0:
            temp=self.copy()
            temp.perform_move("up")
            yield ("up",temp)
        if (self._empty[0]+1)<self._r:
            temp=self.copy()
            temp.perform_move("down")
            yield ("down",temp)
        if (self._empty[1]-1)>=0:
            temp = self.copy()
            temp.perform_move("left")
            yield ("left", temp)
        if (self._empty[1]+1)<self._c:
            temp = self.copy()
            temp.perform_move("right")
            yield ("right", temp)

    # Required
    def find_solutions_iddfs(self):
        is_solved=False
        limit=0
        while not is_solved:
            for moves in self.iddfs_helper(limit,[]):
                yield moves
                is_solved=True
            limit+=1


    def iddfs_helper(self,limit,moves):
        if self.is_solved():
            yield moves
        elif len(moves)<limit:
            for move,new_puzzle in self.successors():
                # if new_puzzle.is_solved():
                #     yield moves+[move]
                # else:
                for solution in new_puzzle.iddfs_helper(limit,moves+[move]):
                    yield solution



    # Required
    def manhattan_distance(self,solved_board):
        d={}
        sum=0
        for i in range(self._r):
            for j in range(self._c):
                d[self._board[i][j]]=[i,j]
        for i in range(self._r):
            for j in range(self._c):
                pos=d[solved_board[i][j]]
                sum+=abs(i-pos[0])+abs(j-pos[1])
        return sum

    def tuple_board(self):
        l=[]
        for i in self._board:
            l.append(tuple(i))
        return tuple(l)

    def find_solution_a_star(self):
        # visited=set()
        # frontier={}
        # solved_board=create_tile_puzzle(self._r,self._c).get_board()
        # root_info=Info(None,None,0,0,0)
        # frontier[self]=root_info
        # while len(frontier)!=0:
        #     curr_puzzle=min(frontier,key=lambda x:frontier[x].f)
        #     curr_info=frontier.pop(curr_puzzle)
        #     if curr_puzzle.is_solved():
        #         solution=[]
        #         while curr_info.parent!=None:
        #             solution.append(curr_info.move)
        #             curr_info=curr_info.parent
        #         solution.reverse()
        #         return solution
        #     if curr_puzzle.tuple_board() not in visited:
        #         visited.add(curr_puzzle.tuple_board())
        #         for move,next_puzzle in curr_puzzle.successors():
        #             h=next_puzzle.manhattan_distance(solved_board)
        #             g=curr_info.g+1
        #             f=g+h
        #             next_info=Info(curr_info,move,f,g,h)
        #             frontier[next_puzzle]=next_info
        visited=set()
        frontier=[]
        heapq.heapify(frontier)
        solved_board=create_tile_puzzle(self._r,self._c).get_board()
        self.g=0
        heapq.heappush(frontier,PrioritizedItem(0,self))
        while len(frontier)!=0:
            m=heapq.heappop(frontier)
            curr_puzzle=m.item
            curr_puzzle_tuple=curr_puzzle.tuple_board()
            if curr_puzzle.is_solved():
                solution=[]
                while curr_puzzle.parent!=None:
                    solution.append(curr_puzzle.move)
                    curr_puzzle=curr_puzzle.parent
                solution.reverse()
                return solution
            if curr_puzzle_tuple not in visited:
                visited.add(curr_puzzle_tuple)
                for move,next_puzzle in curr_puzzle.successors():
                    h = next_puzzle.manhattan_distance(solved_board)
                    g=curr_puzzle.g+1
                    f=g+h
                    next_puzzle.move=move
                    next_puzzle.g=g
                    next_puzzle.parent=curr_puzzle
                    heapq.heappush(frontier,PrioritizedItem(f,next_puzzle))




############################################################
# Section 2: Grid Navigation
############################################################


class Node:
    def __init__(self,value,parent,move,g):
        self.value=value
        self.parent=parent
        self.move=move
        self.g=g

def find_path_successors(pos,scene):
    r=len(scene)
    c=len(scene[0])
    if pos[0]-1>=0 and (not scene[pos[0]-1][pos[1]]):
        yield ("up",(pos[0]-1,pos[1]))
    if pos[0]+1<r and (not scene[pos[0]+1][pos[1]]):
        yield ("down",(pos[0]+1,pos[1]))
    if pos[1]-1>=0 and (not scene[pos[0]][pos[1]-1]):
        yield ("left",(pos[0],pos[1]-1))
    if pos[1]+1<c and (not scene[pos[0]][pos[1]+1]):
        yield ("right",(pos[0],pos[1]+1))
    if pos[0]+1<r and pos[1]+1<c and (not scene[pos[0]+1][pos[1]+1]):
        yield ("down-right",(pos[0]+1,pos[1]+1))
    if pos[0]-1>=0 and pos[1]+1<c and (not scene[pos[0]-1][pos[1]+1]):
        yield ("up-right",(pos[0]-1,pos[1]+1))
    if pos[0]+1<r and pos[1]-1>=0 and (not scene[pos[0]+1][pos[1]-1]):
        yield ("down-left",(pos[0]+1,pos[1]-1))
    if pos[0]-1>=0 and pos[1]-1>=0 and (not scene[pos[0]-1][pos[1]-1]):
        yield ("up-left",(pos[0]-1,pos[1]-1))

def find_path_heuristic(pos,goal):
    return math.sqrt(math.pow(pos[0]-goal[0],2)+math.pow(pos[1]-goal[1],2))

def find_path(start, goal, scene):
    if scene[start[0]][start[1]] or scene[goal[0]][goal[1]]:
        return None
    visited=set()
    frontier=[]
    heapq.heapify(frontier)
    root_node=Node(start,None,None,0)
    heapq.heappush(frontier,PrioritizedItem(0,root_node))
    while len(frontier)!=0:
        m=heapq.heappop(frontier)
        curr_node=m.item
        curr_pos=curr_node.value
        if curr_pos==goal:
            solution=[]
            while curr_node!=None:
                solution.append(curr_node.value)
                curr_node=curr_node.parent
            solution.reverse()
            return solution
        if curr_pos not in visited:
            visited.add(curr_pos)
            for move,next_pos in find_path_successors(curr_pos,scene):
                h=find_path_heuristic(next_pos,goal)
                g=curr_node.g+find_path_heuristic(next_pos,curr_pos)
                f=g+h
                next_node=Node(next_pos,curr_node,move,g)
                heapq.heappush(frontier,PrioritizedItem(f,next_node))

    return None


############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################
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

def heuristic_linear_disk(board,length):
    sum=0
    for i in range(len(board)):
        sum+=abs(board[i]-(length-i-1))
    return sum


def solve_distinct_disks(length, n):
    board = tuple([i for i in range(n)])
    frontier=[]
    heapq.heapify(frontier)
    s = set()
    root_node=Node(board,None,None,0)
    heapq.heappush(frontier,PrioritizedItem(0,root_node))
    while len(frontier)!=0:
        m=heapq.heappop(frontier)
        curr_node=m.item
        curr_board=curr_node.value
        if is_solved_distinct(curr_board,length):
            solution=[]
            while curr_node.parent!=None:
                solution.append(curr_node.move)
                curr_node=curr_node.parent
            solution.reverse()
            return solution
        if curr_board not in s:
            s.add(curr_board)
            for move, next_board in successor_dictinct(curr_board, length):
                h=heuristic_linear_disk(next_board,length)
                g=curr_node.g+1
                f=g+h
                next_node=Node(next_board,curr_node,move,g)
                heapq.heappush(frontier,PrioritizedItem(f,next_node))

    return None

############################################################
# Section 4: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    return DominoesGame([[False for j in range(cols)]for i in range(rows)])

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self._board=board
        self._r=len(board)
        self._c=len(board[0])

    def get_board(self):
        return self._board

    def reset(self):
        for i in range(self._r):
            for j in range(self._c):
                if self._board[i][j]:
                    self._board[i][j]=not self._board[i][j]


    def is_legal_move(self, row, col, vertical):
        if vertical:
            if row+1<self._r:
                if self._board[row][col] or self._board[row+1][col]:
                    return False
            else:
                return False
        else:
            if col+1<self._c:
                if self._board[row][col] or self._board[row][col+1]:
                    return False
            else:
                return False
        return True


    def legal_moves(self, vertical):
        for i in range(self._r):
            for j in range(self._c):
                if self.is_legal_move(i,j,vertical):
                    yield (i,j)

    def perform_move(self, row, col, vertical):
        if self.is_legal_move(row,col,vertical):
            if vertical:
                self._board[row][col]=True
                self._board[row+1][col] = True
            else:
                self._board[row][col] = True
                self._board[row][col+1] = True

    def game_over(self, vertical):
        for i in range(self._r):
            for j in range(self._c):
                if self.is_legal_move(i,j,vertical):
                    return False
        return True


    def copy(self):
        return DominoesGame(copy.deepcopy(self._board))

    def successors(self, vertical):
        for i in range(self._r):
            for j in range(self._c):
                if self.is_legal_move(i,j,vertical):
                    temp=self.copy()
                    temp.perform_move(i,j,vertical)
                    yield (i,j),temp

    def get_random_move(self, vertical):
        l=[]
        for move,_ in self.successors(vertical):
            l.append(move)
        choice=random.choice(l)
        return choice

    # Required
    def max_value(self,depth,alpha,beta,vertical,m):
        if depth == 0 or self.game_over(vertical):
            static_eval = len(list(self.successors(vertical))) - len(list(self.successors(not vertical)))
            return m, static_eval, 1
        max_eval = float('-inf')
        best_move = m
        total = 0
        for move, next_state in self.successors(vertical):
            return_move, eval, count = next_state.min_value(depth - 1, alpha, beta, not vertical, move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            total += count
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move, max_eval, total

    def min_value(self,depth,alpha,beta,vertical,m):
        if depth == 0 or self.game_over(vertical):
            static_eval = len(list(self.successors(not vertical))) - len(list(self.successors(vertical)))
            return m, static_eval, 1
        min_eval = float('inf')
        best_move = m
        total = 0
        for move, next_state in self.successors(vertical):
            return_move, eval, count = next_state.max_value(depth - 1, alpha, beta, not vertical, move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            total += count
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move, min_eval, total

    def get_best_move(self, vertical, limit):
        return self.max_value(limit,float('-inf'),float('inf'),vertical,None)

############################################################
# Section 5: Feedback
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
