import sys

input = sys.stdin.readline

students = [input().strip().split() for _ in range(int(input()))]
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in students:
    print(student[0])
