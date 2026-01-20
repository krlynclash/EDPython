import sys

lines = sys.stdin.readlines()

w = int(lines[0].strip())
x=0
for line in range(0, w):
    math = lines[line+1].strip()

    if math == "++X" or math == "X++":
         x += 1
    elif math == "--X" or math == "X--":
         x -= 1

print(x)