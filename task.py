import random

# task a
A1 = []
sum = 0

print("Array:")
for i in range(20):
    A1.append(random.randint(-10, 10))
    print("{:4d}".format(A[i]), end=" ")
print("\n")

print("Changed array:")
for i in range(20):
    if A1[i] >= 0:
        print("{:4d}".format(A1[i]), end=" ")
for i in range(20):
    if A1[i] < 0:
        print("{:4d}".format(A1[i]), end=" ")
print("\n")

# task b
M = [[random.randint(-10, 10) for j in range(10)] for i in range(10)]

print("Matrix:")
for i in range(10):
    for j in range(10):
        print("{:6d}".format(M[i][j]), end=" ")
    print("")

print("Summ:")
for j in range(10):
    sum = 0
    for i in range(10):
        sum += M[i][j]
    print("{:6.1f}".format(float(sum) / 10), end=" ")
print("\n")
