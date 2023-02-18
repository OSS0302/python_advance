import sys

count = int(input())
for i in range(count):
    num1,num2 = map(int, sys.stdin.readline().split())
    print(num1+num2)
# 입출력 방식 input 이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다. 그래서 sys.stdin.readine()쓰면 된다.