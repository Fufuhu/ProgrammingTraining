def is_rearranged(kou, otsu):
    if len(kou) != len(otsu):
        return False
    
    kou_counter = character_count(kou)
    otsu_counter = character_count(otsu)

    result = True
    if len(kou_counter.keys()) == len(otsu_counter.keys()):
        keys = kou_counter.keys()
        for key in keys:
            if not key in otsu_counter:
                result = False
                break
            if kou_counter[key] != otsu_counter[key]:
                result = False
                break
    else:
        result = False
    return result


def character_count(line):
    counter = {}
    for ch in line:
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 1
    return counter

if __name__ == "__main__":
    kou = input()
    otsu = input()
    print(is_rearranged(kou, otsu))
