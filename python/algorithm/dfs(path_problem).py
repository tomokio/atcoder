"""
C - Remembering the Days
https://atcoder.jp/contests/abc317/tasks/abc317_c
"""

import io
import sys

_INPUT = """\
4 4
1 2 1
2 3 10
1 3 100
1 4 1000
"""

sys.stdin = io.StringIO(_INPUT)

###################################

import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

def dfs(v, g, seen, s):
    global ans
    ans = max(ans, s)

    for (c, v) in g[v]:
        if not v in seen:
            seen.add(v)
            dfs(v, g, seen, s + c)
            seen.remove(v)

n, m = map(int,input().split())
g    = defaultdict(list)
ans  = 0

for _ in range(m):
    a, b, c  = map(int, input().split())
    a -= 1; b -= 1
    g[a].append([c,b])
    g[b].append([c,a])

for v in range(n):
    seen = set()
    seen.add(v)
    dfs(v, g, seen, 0)

print(ans)
