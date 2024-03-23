"""
E - Insert or Erase
https://atcoder.jp/contests/abc344/tasks/abc344_e
"""

import io
import sys

_INPUT = """\
6
3 1 4 5 9 2
7
2 5
1 3 5
1 9 7
2 9
2 3
1 2 3
2 4
"""

sys.stdin = io.StringIO(_INPUT)

###################################

from collections import defaultdict

# 入力の受取
n = int(input())
a = [0] + list(map(int, input().split())) + [-1]
q = int(input())
# NOTE: 辞書のキーに文字列を指定すると遅い（TLEになる例）
# a = ["head"] + list(map(int, input().split())) + ["tail"]

# 双方向リストの初期化
front = defaultdict(int)
back  = defaultdict(int)

for i in range(len(a)-1):
    back[a[i]]      = a[i + 1]
    front[a[i + 1]] = a[i]

# クエリの個数分繰り返す
for _ in range(q):
    t, *p = map(int, input().split())

    # クエリ1の処理
    if t == 1:
        x, y = p

        # xおよびxの後ろに対して更新をかける
        back_x = back[x]
        front[back_x] = y
        back[x] = y

        # yに対して更新をかける
        front[y] = x
        back[y]  = back_x

    # クエリ2の処理
    else:
        x = p[0]

        # xの前後に対して更新をかける
        front_x = front[x]
        back_x  = back[x]

        front[back_x] = front_x
        back[front_x] = back_x

        # xを辞書から削除する
        del front[x]
        del back[x]


# 結果の出力
ans = list()
key = back[0]
while key != -1:
    ans.append(key)
    key = back[key]
print(*ans)
