# nの約数を列挙
def list_divisor(n: int) -> list:
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# エラトステネスの篩：x以下の素数を列挙
def eratosthenes(x: int) -> list:
    nums = [i for i in range(x + 1)]
    root = int(pow(x, 0.5))

    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    return sorted(list(set(nums)))[2:] # setで複数個ある0を1つに [2:]で0と1を除く素数を抽出

# 二分探索：ソートされた配列Aから値がx以上の要素のうち最小の要素のインデックスを求める
def binary_search(A: list, N:int, x:int) -> int:
    l = 0
    r = N - 1

    while r - l > 1:
        c = (l + r) // 2
        if A[c] < x:
            l = c
        else:
            r = c

    return r
