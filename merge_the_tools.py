def merge_the_tools(string, k):
    # your code goes here
    divid= [(string[i:i+k]) for i in range(0, len(string), k)]
    result = []
    for i in divid:
        time = []
        for j in i:
            if j not in time:
                time.append(j)
        result.append(time)
    for k in result:
        print(''.join(k))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)