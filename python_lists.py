if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0, n):
        user_input = input().split()
        if len(user_input) == 1:
            if user_input[0] == "print":
                print(arr)
            elif user_input[0] == "sort":
                arr.sort()
            elif user_input[0] == "pop":
                arr.pop(-1)
            elif user_input[0] == "reverse":
                arr.reverse()
        if len(user_input) == 2:
            if user_input[0] == "remove":
                arr.remove(int(user_input[1]))
            elif user_input[0] == "append":
                arr.append(int(user_input[1]))
        if len(user_input) == 3:
            arr.insert(int(user_input[1]), int(user_input[2]))

