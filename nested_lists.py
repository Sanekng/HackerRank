if __name__ == '__main__':
    people = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        people.append([name, grade])
    people.sort(key=lambda x: x[1])
    small_record = people[0][1]
    second_record = 0
    for i in range(0, len(people)):
        if people[i][1] > small_record:
            second_record = people[i][1]
            break
    second_best = []
    for j in range(0, len(people)):
        if people[j][1] == second_record:
            second_best.append(people[j])
    second_best.sort()
    for i in range(0, len(second_best)):
        print(second_best[i][0])
