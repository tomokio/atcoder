"""
C - Divide and Divide
https://atcoder.jp/contests/abc340/tasks/abc340_c
"""

import io
import sys

_INPUT = """\
100000000000000000
"""

sys.stdin = io.StringIO(_INPUT)

###################################

from functools import cache

@cache
def f(n):
    return 0 if n == 1 else f(n // 2) + f((n + 1) // 2) + n

n = int(input())
print(f(n))
