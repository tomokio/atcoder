"""
C - Rotate and Palindrome
https://atcoder.jp/contests/abc286/tasks/abc286_c
"""

import io
import sys

_INPUT = """\
8 1000000000 1000000000
bcdfcgaa
"""

sys.stdin = io.StringIO(_INPUT)

###################################

def check(cs):
    cnt=0
    for i in range(n):
        if cs[i] !=cs[n-1-i]:
            cnt+=1
    return cnt//2

n,a,b = map(int, input().split())
s     = input()
s    += s
ans   = 1 << 60

for i in range(n):
    cost  = a * i
    tmps  = s[i:n+i]

    cost += b * check(tmps)
    ans   = min(ans, cost)

print(ans)
