
def compress(line):
    
    ch_prev = line[0]
    i = 1
    count = 1
    compressed_line = ""
    while i < len(line):
        ch = line[i]
        if ch == ch_prev:
            count += 1
        else:
            compressed_line = compressed_line + ch_prev + str(count)
            ch_prev = ch
            count = 1
        i += 1
    compressed_line = compressed_line + ch_prev + str(count)

    if len(compressed_line) >= len(line):
        return line
    else:
        return compressed_line


if __name__ == "__main__":
    line = input()
    print(compress(line))