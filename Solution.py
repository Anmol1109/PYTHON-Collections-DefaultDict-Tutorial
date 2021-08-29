# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
n, m = map(int,input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]
d = defaultdict(list)
ind = 0
for i in A:
    d[i].append(A.index(i,ind) + 1)
    ind = ind + 1
for i in B:
    if i not in A:
        print(-1)
    else:
        print(" ".join(map(str,d[i])))
