time = input("시간을 입력해주세요>>>")

# 1.  분만 있는 경우 ex)30분
# 2. 시간만 있는경우 
# 3. 시간과 분이 있는경우

if time.find('시간') == -1:
    # 분만 있는경우
    result = int(time.split('분')[0])
else:
    if time.find('분') ==-1:
        result = int(time.split('시간')[0])* 60
    else:
        # 시간과 분이 있는경우
        sub = time.split('시간')
        result =int(sub[0])*60 + int(sub[1].split('분')[0])
print(result)