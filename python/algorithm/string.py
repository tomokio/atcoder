# 文字列操作

# A - Treasure Chest
# https://atcoder.jp/contests/abc299/tasks/abc299_a
S     = '.|..*...|.'
start = S.index('|')  # | が最初に出現したインデックスを求める
end   = S.rindex('|') # | が最後に出現したインデックスを求める
print(start, end)

# C - Dango
# https://atcoder.jp/contests/abc299/tasks/abc299_c
S = '-o-o-oooo-oo-o-ooooooo--oooo-o'
print(max(map(len, S.split('-')))) # -を区切り文字とした場合の連続するoの最大文字数を求める
