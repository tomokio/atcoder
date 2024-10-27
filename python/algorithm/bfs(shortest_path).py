import io
import sys

_INPUT = """\
6 9
6 1
1 5
2 6
2 1
3 6
4 2
6 4
3 5
5 4
"""

sys.stdin = io.StringIO(_INPUT)

###################################

from collections import deque, defaultdict

# 入力の受取り
g = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)

# 幅優先探索の準備
d = [-1] * n # 各頂点を訪問する際の最短経路を格納するためのリスト
d[0] = 0
q = deque()
q.append(0)

# 幅優先探索の実施
while len(q) > 0:
    cur = q.popleft()
    for nex in g[cur]:
        # 再び頂点1に戻ってきた場合、グラフは閉路であり、最初に到達した場合が最も短い辺数である
        if nex == 0:
            print(d[cur] + 1)
            exit(0)

        # 訪問したことのない頂点の場合、d[nex]を更新し、頂点をdequeに追加する
        if d[nex] == -1:
            d[nex] = d[cur] + 1
            q.append(nex)

# 頂点1を含めた閉路が存在しない場合、-1を表示する
print(-1)
