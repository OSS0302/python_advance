class Unit:
    def __init__(self,name,mineral, gas , hp, shield , demage):
        self. name = name
        self.mineral = mineral 
        self.gas = gas 
        self.hp = hp 
        self. shield = shield 
        self.demage =demage 
   
        if mineral > 100:
            print("유닛객체 생성")
        else:
            print("미네랄이 부족합니다.")
        if mineral >125:
            if   

    def __str__(self):
        return(f"[{self.name}체력: {self.hp}실드 :{self.shield} 공격력:{self.demage}]")


probe = Unit("프로브",50,0,20,20,5)
zealot = Unit("질럿",100,0,100,60,16)
dragoon = Unit("드라군",125,50,100,80,20)



