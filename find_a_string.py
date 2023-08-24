def count_substring(string, sub_string):
    x = 0
    for i in range(0, len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            x += 1
    return x


if __name__ == '__main__':
    g = input().strip()
    h = input().strip()

    count = count_substring(g, h)
    print(count)
