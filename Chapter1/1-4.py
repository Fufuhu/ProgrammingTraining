import re

def replace_space(line):
    line_replaced = ""

    ch_replaced = "%20"
    line = re.sub(r'\s+$','',line)
    for ch in line:
        if ch == " ":
            line_replaced = line_replaced + ch_replaced
        else:
            line_replaced = line_replaced + ch
    return line_replaced
    



if __name__ == "__main__":
    line = input()
    print(replace_space(line))
