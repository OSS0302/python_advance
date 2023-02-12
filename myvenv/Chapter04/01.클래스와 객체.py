class Unit:
    def __init__(self,name , hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield=shield
        self.demage = demage
        print(f"[{self.name}]이 생성되었습니다.")
    
    def __str__(self):
        return f"[{self.name}] 체력:{self.hp}  방어막:{self.shield} 공격력 {self.demage}"
# 인스턴스 객체 만들기

probe = Unit("프로브",20,20,5)       
zealot = Unit("질럿",100,60,16)
dragoon= Unit("드라군",200,60,20)

# 인스턴스 수정하기
probe.demage +=20 
probe.hp +=9979
print(probe)



