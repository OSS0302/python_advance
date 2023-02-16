import sys as s
while True:
    try:
        num1,num2 = map(int, s.stdin.readline().split())        
        print(num1+num2)
    except:
        break
   