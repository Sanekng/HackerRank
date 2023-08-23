if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    key, values = zip(*student_marks.items())
    for i in str(key):
        if i == query_name:
            print(1)


# Solve this later!
