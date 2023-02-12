import re
# group 그룹
# # 매칭되는 문자열 한개
# str1= '010-2343-3333'
# result = re.match('\d{2,3}-\d{3,4}-(\d{4}$)',str1)
# print(result.group(1))

# # 매칭된 문자열 두개
# str2 = '010-2343-7888,010-2343-1234, 010-2343-5678,010-2343-9959, 010-2343-2222'
# results = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=,|$)',str2)

# for index,result in enumerate (results,1):
#     print(f'{index}. {result.group(1)}')

# 2.subtitution (교체)
str3 ='010-2343-3333'
result =re.sub('(?<=\d{3}-\d{4}-)\d{4}','****',str3)
print(result)