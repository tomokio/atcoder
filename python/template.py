#!/usr/bin/env python3

import io, sys
from icecream import ic

_INPUT = """\
3
1 2 3
"""

sys.stdin = io.StringIO(_INPUT)

###################################

n = int(input())
a = list(map(int, input().split()))

print(n)
print(a)
