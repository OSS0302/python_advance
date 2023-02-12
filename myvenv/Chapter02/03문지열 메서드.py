# 소문자를 대문자로 바꾸는 방법
print("be pround of yourself".upper())
# 대문자를 소문자로 바꾸는 방법
print("BE PROUND OF YOURSELF".lower())
# 문자열 바꾸는 방법 중요
print("오늘 날씨는 흐림 입니다. ".replace("흐림","맑음"))
# 문자열 위치 찾는 방벙
print("Hello world!".find("world!"))
# 문자열 갯수 찾는 방법
print("This cat my cat".count("cat"))
# 문자열 분리하는 방법
print("나이키신발 265X2421 78000".split())# 리스트 형태로 구분함
print("------------------------------")
print("나이키신발:265X2421:78000".split(":"))
# 문자열 연결하는 방법
print(''.join(['나이키신발','265X2421','78000']))
print(':'.join(['나이키신발','265X2421','78000']))
# 공백 삭제 하는 방법
#왼쪽 공백 삭제 
print('       yeah    '.lstrip())
# 오른 쪽 공백 삭제 
print('       yeah    '.rstrip())
# 양쪽 공백 삭제
print('       yeah    '.strip())
word = []
word_list = ['apple','watch','apolo','star','abpcado']
for word in word_list:
    if word[0] == "a":
        word_list.append(word)
