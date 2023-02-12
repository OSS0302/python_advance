# 문자열 포매팅 
# 기주님 수강기간이 8일 남았습니다.

name = '기준'
duration = 7
message = name +'님 수강기간이' +str(duration)+ '일  남았습니다.'
print(message)

# 문지얄 포메팅 사용시 !!!
message_format = f'{name}님 수강기간이{duration}일 남았습니다.'
print(message_format)
# 문자열 포매팅 2가지 방법에 대해서 학습하기 
#format(메서드) 값이 한개인경우
d='Hello{0}'.format('startcoding')
#format(메서드) 값이 여러개인경우
c= 'hello {0} {1} {2}'.format('apple','pinapple','pen')

print(d)
print(c)
# f-string
name1 = 'apple'
name2 ='ipone'
name3 ='mac book air'
msg = f'뭐살래 {name1} {name2} {name3} 나한테 알려줘'
print(msg)

