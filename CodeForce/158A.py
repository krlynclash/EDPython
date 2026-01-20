import sys

lines = sys.stdin.readlines()

line1 = list(map(int, lines[0].split()))

contestant_number = line1[0]

k_position = line1[1]

line2 = list(map(int, lines[1].split()))

k_score = line2[k_position - 1]
x = 0
for i in range(contestant_number):
    if line2[i] >= k_score and line2[i] > 0:
        x += 1
print(x)