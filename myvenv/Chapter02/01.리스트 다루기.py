# 리스트 메서드 
fruits = ['apple','banana','mango','orange']
# 리스트 데이터 삭제 
fruits.remove('apple')
print(fruits)
fruits.pop(2) 
# 리스트 형태 추가하기
fruits.append('strawberry')
print(fruits)
# 리스트 형태 특정 값의 갯 수 구하기 
count=fruits.count('strawberry')
print(count)
# 리스트 특정 값의 인덱스 구하기 입니다.
index=fruits.index('strawberry')
print(index)
#리스트 숫자 정렬하기 
numbers = [2,5,4,10,9,12]
numbers.sort()
print(numbers)
# for in 반복문 사용할때 인덱스 같이 출력하는 방법(enumerate)
numbers =[5,4,1,6,19]
for index, numbers in enumerate(numbers):
    print(index,numbers)
# enumerate
titles= ['출석!','출석인증합니다.','출석이다']
for index,title in enumerate( titles):
    print(index+1,title)
fruits = ['apple', 'orange', 'mango']
fruits.pop(1)
print(fruits)
