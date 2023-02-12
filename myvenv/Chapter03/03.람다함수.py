# 기존함수
def mins_one(a):
    return a-1
#람다함수
lambda a : a-1
# 람다함수 호출방법 1. 함수 자체를 호출
print((lambda a : a-1)(10))
# 람다함수 호출방법 2. 변수에 담아서 호출
mins_one_2 =lambda a: a-1
print(mins_one_2(100))
# 람다함수에서 if문

lambda a : True if a>0 else False
#람다함수 호출(1)
print((lambda a : True if a >0 else False)(-2))
#람다함수 호출(2)
is_positive_number = lambda a : True if a>0 else False
print(is_positive_number(2))

# 람다함수 
print((lambda a : a-1 )(10))