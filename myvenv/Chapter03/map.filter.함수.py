# 1.map함수 사용이유
# 기존 리스트를 수정해서 새로운리스트를 만들고싶을때
# - 사용방법
# map(함수, 순서가있는자료형)
print(list(map(int,['3','4','5','6'])))
# 예제
# 리스트 모든 요소의 공백 제거 
item = ['  갤럭시  ','  아이폰  ']
# for 문을 사용한경우
# for word in range(len(item)):
#     item[word] = item[word].strip()
# print(item)
# map 사용
def strip_all(x):
    return x.strip()
item = list(map(strip_all,item))
print(item)
# 람다함수사용
item = list(map(lambda x:x.strip(),item))
#2. filter 함수
# 기존리스트에서 조건을 만족하는 요소만 뽑고싶을때 사용한다.
#filter(함수, 순서가있는자료형)
def func(x):
    return x<0
print(list(filter(func,[-4,-5,-3,-2,0,5,6,7])))
# filter 함수 
#1)리스트 길이가 3이하인 문자들만 필터링
animals = ['cat', 'tiger''dog','bird','monkey']
result =[]
# 1)for문 사용한경우
for word in animals:
    if len(word)<=3:
        result.append(word)
#2)filter 함수를 사용한경우
animals = ['cat', 'tiger''dog','bird','monkey']
def word_check(x):
    return len(x) <=3
result= list(filter(word_check, animals))
# 3)람다함수를 사용한경우
animals = ['cat', 'tiger''dog','bird','monkey']
result = list(filter(lambda x : len(x) <=3, animals))