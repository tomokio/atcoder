"""
C - Make Takahashi Happy
https://atcoder.jp/contests/abc293/tasks/abc293_c
"""

import io
import sys

_INPUT = """\
3 3
3 2 2
2 1 3
1 5 4
"""

sys.stdin = io.StringIO(_INPUT)

###################################

h, w = map(int, input().split())
a    = [list(map(int, input().split())) for _ in range(h)]

dp   = [[[] for _ in range(w)] for _ in range(h)]
dp[0][0] = [[a[0][0]]]

for i in range(h):
    for j in range(w):
        for ls in dp[i][j]:
            if i < h - 1 and a[i+1][j] not in ls:
                dp[i+1][j].append(ls+[a[i+1][j]])
            if j < w - 1 and a[i][j+1] not in ls:
                dp[i][j+1].append(ls+[a[i][j+1]])

print(len(dp[-1][-1]))
