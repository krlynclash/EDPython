import sys

lines = sys.stdin.readlines()
count = 0
for line in range(0, int(lines[0].strip())):
    questions = lines[line+1].strip()
    if (sum(list(map(int, questions.split()))) >= 2):
        count += 1
print(count)