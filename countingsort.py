import os


def counting_sort(arr):
    # Write your code here
    res = [0] * 100
    for i in arr:
        res[i] += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = counting_sort(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
