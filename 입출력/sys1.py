import sys

sum = 0
args = sys.argv[1:]
for i in args:
    print(i)
    sum = sum + int(i)
    print(sum)
print(sum)