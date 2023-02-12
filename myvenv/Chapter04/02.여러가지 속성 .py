class Unit:
    def __init__(self, name, hp, shield , demage):
        self. name = name 
        self.hp = hp 
        self. shield = shield 
        self.demage =demage 
    print


probe = Unit("프로브",20,20,5)
zealot = Unit("질럿",100,60,16)
dragoon = Unit("드라군",100,80,20)
print(probe)

def __init__(self, name, hp, shield , demage):
    self. name = name 
    self.hp = hp 
    self. shield = shield 
    self.demage =demage 

def __str__(self):
    return(f"[{self.name}체력: {self.hp}실드 :{self.shield} 공격력:{self.damage}]")

# 클래스 안: self: 속성명
# 클래스 밖 객체명,속성명
#모든 객체가 공유하는 속성
# 비공개 속성
# 클래스 안에서만 접근 가능한 속성

