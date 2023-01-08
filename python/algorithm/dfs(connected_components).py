"""
C - Count Connected Components
https://atcoder.jp/contests/abc284/tasks/abc284_c
"""

import io
import sys

_INPUT = """\
4 6
1 2
1 3
1 4
2 3
2 4
3 4
"""

sys.stdin = io.StringIO(_INPUT)

###################################

import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

def dfs(v, g, seen):
    seen.add(v)

    for cv in g[v]:
        if cv in seen:
            continue
        else:
            dfs(cv, g, seen)

n, m = map(int, input().split())

if m == 0:
    print(n)
    exit(0)

g    = defaultdict(list)
seen = set()

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0
for v in range(n):
    if v not in seen:
        ans += 1
        dfs(v, g, seen)

print(ans)
