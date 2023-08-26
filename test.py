n = int(input())
a = []
for i in range(n):
    more = input()
    a.append(more)
a = list(dict.fromkeys(a))
print(a)