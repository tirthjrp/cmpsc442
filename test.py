import homework3_tpp5217
import homework2_tpp5217
import time
import queue

def solve(length,n,moves):
    l=[i if i<n else -1 for i in range(length)]
    for i in moves:
        l[i[1]]=l[i[0]]
        l[i[0]]=-1
    print(l)

length=11
n=5
start=time.time()
x=homework3_tpp5217.solve_distinct_disks(length,n)
print(x)
end=time.time()
print(end-start)

start=time.time()
y=homework2_tpp5217.solve_distinct_disks(length,n)
print(y)
end=time.time()
print(end-start)



solve(length,n,x)
print(len(x))
solve(length,n,y)
print(len(y))
#
b = [[False] * 3 for i in range(3)]
g = homework3_tpp5217.DominoesGame(b)
g.perform_move(0, 1, True)
start=time.time()
print(g.get_best_move(False,1))
end=time.time()
print(end-start)

b =[[4,1,2], [0,5,3], [7,8,6]]
p = homework3_tpp5217.TilePuzzle(b)
start=time.time()
print(p.find_solution_a_star())
end=time.time()
print(end-start)


scene = [[True if j==50 and i<50 else False for j in range(100)]for i in range(100)]
start=time.time()
print(homework3_tpp5217.find_path((0, 0), (0,99), scene))
end=time.time()
print(end-start)
