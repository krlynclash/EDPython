import sys

lines = sys.stdin.readlines()

w = int(lines[0].strip())


if w <=2:
    print("NO")
    sys.exit(0)
if w % 2==0:
    print("YES")
else:    
    print("NO")