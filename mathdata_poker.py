n = int(input())

string = input()

A = 0
F = 0
I = 0

for c in string:
    if c == 'A':
        A += 1
    if c == 'F':
        F += 1
    if I == 'I':
        I += 1

if I == 0:
    print(A)
elif I == 1:
    print(1)
else:
    print(0)
