from random_words import LoremIpsum
rw = LoremIpsum()

def check_comment(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines_len = len(lines)

    with open(filename, mode="w+") as f:
        for i in range(lines_len):
            if lines[i] == "\n":
                continue
            f.write(lines[i])
            if (lines[i][len(lines[i]) - 2] == ";"):
                f.write(f"/*{rw.get_sentence()}*/\n")
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: {} <filename>".format(sys.argv[0]), file=sys.stderr)
        exit(-1)

    ret = check_comment(sys.argv[1])
    exit(0 if ret else 1)
