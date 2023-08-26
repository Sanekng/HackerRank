n, m = map(int, input().split())
arr = list(map(int, input().split()))
liking_dict = {int(x): 1 for x in input().split()}
disliking_dict = {int(x): 1 for x in input().split()}
happiness = 0
for num in arr:
    if num in liking_dict:
        happiness += 1
    elif num in disliking_dict:
        happiness -= 1
print(happiness)