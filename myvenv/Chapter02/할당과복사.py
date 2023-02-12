# 리스트 할당 방식

# x =[1,2,3,4,5]
# y=x
# y[2]=0
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# # 리스트 복사방식
# a =[5,6,7,8,9]
# b =a.copy()
# b[2]=0
# print(a)
# print(b)
# print(id(a))
# print(id(b))
#다차원 리스트 복사 방식
import copy
x=[[1,2],[3,4,5]]
d = copy.deepcopy(x)
d[0][0] =0
print(x)
print(d)





# #파이썬 리스트 객체주소 확인하기
# a =[5,6,7,8,9]
# b =a.copy() 
# print(id(a))
# print(id(b))
