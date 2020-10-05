import homework3_tpp5217
import homework2_tpp5217
import time

def solve(length,n,moves):
    l=[i if i<n else -1 for i in range(length)]
    for i in moves:
        l[i[1]]=l[i[0]]
        l[i[0]]=-1
    print(l)





length=12
n=6
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



# b = [[False] * 3 for i in range(4)]
# g = homework3_tpp5217.DominoesGame(b)
# start=time.time()
# print(g.get_best_move(True,3))
# end=time.time()
# print(end-start)