"""
D - Money in Hand
https://atcoder.jp/contests/abc286/tasks/abc286_d
"""

import io
import sys

_INPUT = """\
3 1001
1 1
2 1
100 10
"""

sys.stdin = io.StringIO(_INPUT)

###################################

l = list()
n, x = map(int,input().split())
for i in range(n):
    a, b = map(int,input().split())
    l.extend([a] * b)

# S: target number, num_list: list of numbers
S        = x
num_list = l
num_list = [0] + num_list

N  = len(num_list)
dp = [ [0 for _ in range(S+1)] for _ in range(N)]
dp[0][0] = 1

for i in range(1,N):
    for j in range(S+1):
        if j >= num_list[i]:
            dp[i][j] = dp[i-1][j-num_list[i]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

if dp[-1][-1]:
    print('Yes')
else:
    print('No')
