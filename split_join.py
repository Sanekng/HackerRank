def split_and_join(line):
    text = line.split(" ")
    text = "-".join(text)
    return text


if __name__ == '__main__':
    quest = input()
    result = split_and_join(quest)
    print(result)
