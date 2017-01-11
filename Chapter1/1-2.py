def reverse_string(line):
    length = len(line)

    i = length - 1
    reversed_line = ""
    while i >=0:
        reversed_line = reversed_line + line[i]
        i -= 1
    return reversed_line



if __name__ == "__main__":
    line = input()
    print(reverse_string(line))