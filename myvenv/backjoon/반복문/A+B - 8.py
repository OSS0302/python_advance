import sys
count_num=0
count = int(input())
for i in range(count):
    num1,num2 = map(int, sys.stdin.readline().split())
    count_num+=1
    print(f"Case #{count_num}: {num1} + {num2} = {num1+num2}")