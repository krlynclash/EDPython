import sys

lines = sys.stdin.readlines()

for line in range(0, int(lines[0].strip())):
    word = lines[line+1].strip()
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)