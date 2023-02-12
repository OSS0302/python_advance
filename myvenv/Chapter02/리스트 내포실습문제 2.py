list=['오메가',None,'비타민500',None,'홍삼절편']
list1=[]
#내포 사용안한경우
for word in list:
        if  word != None:
                list1.append(word)
        else:
                list1.append('')
print(list1)
#내포 사용한경우
result =[i if i != None else '' for i in list]
print(result)
#  리스트 컨프리헨션 에서 조건문 if -else를 쓰고 싶다면 for문을 뒤에 조건문을 앞에쓴다



