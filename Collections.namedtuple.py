from collections import namedtuple

studentNum = int(input())
#columns = input().split()
students = namedtuple('student',input())
total = 0

for _ in range(studentNum):
    student = students(*input().split())
    total += int(student.MARKS)

print(f'{total/studentNum:2f}')

