def print_door_mat(rows, columns):
    pattern = [('.|.' * (2 * i + 1)).center(columns, '-') for i in range(rows // 2)]
    welcome = 'WELCOME'.center(columns, '-')
    pattern = '\n'.join(pattern + [welcome] + pattern[::-1])
    print(pattern)

# Read input from the user
rows, columns = map(int, input().split())
print_door_mat(rows, columns)
