import homework3_tpp5217
import homework2_tpp5217
import time

# def solve(length,n,moves):
#     l=[i if i<n else -1 for i in range(length)]
#     for i in moves:
#         l[i[1]]=l[i[0]]
#         l[i[0]]=-1
#     print(l)
#
#
#
#
#
# length=18
# n=4
# start=time.time()
# x=homework3_tpp5217.solve_distinct_disks(length,n)
# print(x)
# end=time.time()
# print(end-start)
#
# start=time.time()
# y=homework2_tpp5217.solve_distinct_disks(length,n)
# print(y)
# end=time.time()
# print(end-start)
#
#
#
# solve(length,n,x)
# print(len(x))
# solve(length,n,y)
# print(len(y))

# b = [[False] * 3 for i in range(3)]
# g = homework3_tpp5217.DominoesGame(b)
# g.perform_move(0, 1, True)
# start=time.time()
# print(g.get_best_move(False,2))
# end=time.time()
# print(end-start)

# b =[[1,2,3], [4,0,5], [6,7,8]]
# p = homework3_tpp5217.TilePuzzle(b)
# start=time.time()
# print(p.find_solution_a_star())
# end=time.time()
# print(end-start)

#
# scene = [[False for j in range(200)]for i in range(100)]
# start=time.time()
# print(homework3_tpp5217.find_path((0, 0), (0,0), scene))
# end=time.time()
# print(end-start)
