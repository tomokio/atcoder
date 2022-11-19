"""
C - Ladder Takahashi
https://atcoder.jp/contests/abc277/tasks/abc277_c
"""

import io
import sys

_INPUT = """\
4
1 4
4 3
4 10
8 3
"""

sys.stdin = io.StringIO(_INPUT)

##########################################

import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

def dfs(v, g, seen, ans):
    seen.add(v)
    ans = max(ans, v + 1)

    for cv in g[v]:
        if cv in seen:
            continue
        else:
            ans = dfs(cv, g, seen, ans)

    return ans

n = int(input())
g = defaultdict(list)
seen = set()

for _ in range(n):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

if 0 in g:
    print(dfs(0, g, seen, 0))
else:
    print(1)
