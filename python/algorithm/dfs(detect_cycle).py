"""
C - Find it!
https://atcoder.jp/contests/abc311/tasks/abc311_c
"""

import io
import sys

_INPUT = """\
8
3 7 4 7 3 3 8 2
"""

sys.stdin = io.StringIO(_INPUT)

###################################

import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

def dfs(v, g, seen, ans):
    seen.add(v)
    ans.append(v)

    for cv in g[v]:
        if cv in seen:
            ans.append(cv)
            idx = ans.index(cv)
            ans = ans[idx+1:]
            print(len(ans))
            print(*ans)
            exit(0)

        else:
            dfs(cv, g, seen, ans)

n = int(input())
a = list(map(int, input().split()))

g    = defaultdict(list)
seen = set()

for i in range(n):
    g[i+1].append(a[i])

for v in range(n):
    ans = list()
    dfs(v, g, seen, ans)
