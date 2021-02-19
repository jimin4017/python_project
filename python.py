class unit :     
    def __init__(self,name,hp,speed) :
        self.name = name
        self.hp = hp
        self.speed= speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    def move(self,location) :
        print("[지상 유닛 이동 ]")
        print("{0}: {1} 방향으로 이동합니다. ".format(self.name,location))
    
    def damaged(self,damage) :
        self.hp -=damage
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))

        if self.hp <=0:
            print("{0}: 파괴되었습니다.".format(self.name))

class AttackUnit(unit) : # 이름 체력 스피드 데미지
    def __init__(self, name, hp ,speed,damage) :

        unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location) :
        print("{0}: {1} 방향으로 적군을 공격 합니다.[공격력 {2} ] "
        .format(self.name,location,self.damage))
    
# 마린

class Marine(AttackUnit) :
    def __init__(self) :
        AttackUnit.__init__(self,"마린",40,1,5)
    #스팀팩 : 일정 시간동안 이속 공속 증가, 체력 -10

    def stimpck(self):
        if self.hp> 10 :
            self.hp>10 
            print("{0}: 스팀팩을 사용 합니다.(HP 10감소))".format(self.name))
        else :
            print("{0}: 체력이 부족하여 사용할수가 없습니다.") 

class Tank(AttackUnit) :
    seize_devlope = False
    def __init__(self) :
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode =False
    # 시즈 탱크

    def set_size_mode (self) :
        if Tank.seize_devlope == False :
            return  False

        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다. ".format(self.name))
            self.damage *=2
            self.seize_mode = True
        else :
             print("{0} : 시즈모드로 전환합니다. ".format(self.name))
             self.damage /=2
             self.seize_mode = False



def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over() :
    print("player : gg")
    print("[player] 님이 퇴장하셨습니다. ")


class Flyable :
    def __init__(self,flying_speed):
        self.flying_speed =flying_speed
    
    def fly(self,name,location) :
        print("{0} : {1} 방향으로 날아갑니다.[속도{2}]"
             .format(name,location,self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable) :
    def __init__(self,name,hp,damage,flying_speed) :
        AttackUnit.__init__(self,name,hp,0,damage) #지상 스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self,location) :
        print("[공중유닛 이동]")

class Wraith(FlyableAttackUnit) :
    def __init__(self) :
        FlyableAttackUnit.__init__("레이스",80,1,20,5)
        self.clocked = False
    
    def clocking(self) :
        if self.clocked == False :
            print("{0} : 클로킹 모드를  실행합니다.".format(self.name))
            self.clocked = True
        else :
            print("{0}: 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
# 발키리 생성  : 지상유닛
valture = AttackUnit("벌처",80,10,20)
#배틀 크루저 :    공중유닛


battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

valture.move("11시")

battlecruiser.move("9시")
# 건물

#class BuildingUnit(Unit) :
    ##def __init__(self,namemhp,0)   비교
   ## super().__init__(name)
   
#
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

T1 = Tank()
T2 = Tank()
T3 = Tank()

w1 = Wraith()

attack_unit = []

attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(T1)
attack_unit.append(T2)
attack_unit.append(w1)

# 전군 이동

for unit in attack_unitㄴ :
    unit.move("1시")

# 태크 시즈 모드 개발 
Tank.seize_devlope = True
print("")

for unit in attack_units :
    if isinstance(unit,Marine) :   #인스턴스 확인 ex) unit 안의 Marine 찾기
        unit.stimpck()
    elif isinstance(unit,Tank) :
        unit.set_size_mode()
    elif isinstance(unit,Wraith) :
        unit.clocking()




 
'''
try :
    print("나누기 전용 계산기 입니다.")
    num1 =int(input("첫 번째 숫자를 입력하세요:"))
    num2 =int(input("두 번째 숫자를 입력하세요:"))
    print("{0}/{1}= {2}".format(num1,num2,int(num1/num2)))
except ValueError :
    print("에러! 잘못된 값을 입력하였습니다.")
'''