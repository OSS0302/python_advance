import re
"""
1. 이메일은 ID 파트와 host 파트가 있다. (id@host)
2. 1D 파트는 영문 대소문자, 숫자, 특수문자(-_))가 쓸어갈 수 있다.
3. host 파트는 영문 대소문자, 숫자, 특수문자(-)
4. host 파트는 2개 이상의 도메인으로 구성 될 수 있다.
"""
datas=[
'startcoding@maver.com',
'start-coding@maver.com',
'start_coding@maver.co.kr',
'startcoding@k-mail.com',
'@maver.com',
'startcoding?@krnail.com',
'startcoding@k-mail',
'startcoding@maver',
]
regex ='^[a-zA-z0-9-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

for data in datas:
    match_email= re.match(regex ,data)
    result=(lambda x : True if x != None else False)(match_email)
    print(f'{data}:{result}')
