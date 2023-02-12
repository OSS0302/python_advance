#리스트 내포 컴프리헌즈
#for 문사용
num1 = [i for i in range(5)]
print("num1:",num1)

num2 = [100, 200, 300]
double_nums = [i * 2 for i in num2]
print("num2:",double_nums)

#if 문사용

num3 =[ i for i in range(10) if i % 2==0 ]
print("num3:",num3)

num4 = [100, 200, 300, 400, 500] 
double_nums = [i * 2 for i in num4 if i >= 300]
print("num4:",double_nums)