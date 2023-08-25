def mini_max_sum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))


if __name__ == '__main__':
    rg = list(map(int, input().rstrip().split()))

    mini_max_sum(rg)
