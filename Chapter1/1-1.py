def duplication_check(line):

    checker = {}
    for ch in line:
        if ch in checker:
            return True
        else:
            checker[ch] = True
    return False


if __name__ == "__main__":
    line = input()
    print(duplication_check(line))