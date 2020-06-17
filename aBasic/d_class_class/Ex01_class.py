"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""
# class Simple:
#     data = "Hello"
#     def __init__(self):
#         self.age = 38
#         self.name = "홍길동"
#         print('__init__ 호출')
#     def __del__(self): # 소멸자
#         print('__del__ 호출')
# s = Simple()
#
# print(s.data)
# print(s.age)
# print(s.name)
# print(dir(s))

class Book:
    cnt = 0
    def __init__(self, title):
        self.title = title
    def output(self):
        print("제목:", self.title)
        self.cnt += 1
        print('1> 총 갯수 ', self.cnt)
    @staticmethod       #static메소드임을 알려줌 -> static메소드는 self를 사용할 수 없음
    def output2(self):
 #       pass
        print("제목:", self.title)
        self.cnt += 1
        print('2> 총 갯수 ', self.cnt)
    @classmethod
    def output3(cls):   #class의 약자 cls를 사용
        cls.cnt += 1
        print('3> 총 갯수 ', cls.cnt)
b = Book('자바란무엇인가')
z = Book('파이썬만세')

#Book.output2()
#Book.output2()
print("인스턴스 메소드 사용 시작 -------")
b.output()
z.output()
print("인스턴스 메소드 사용 끝 -------")
b.output3()
z.output3()
Book.output3()

"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""







'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:
    def move(self):
        print('동물은 움직인다')
class Wolf(Animal):
    def move(self):
        print("늑대는 네발로 움직인다")
class Human(Animal):
    def move(self):
        print("사람은 두발로 움직인다")
class WereWolf(Human, Wolf):
    def move(self):         # 상속받는 두곳에서 동일한 이름의 여러 메소드가 있어도 문제가 생기지 않음
        super().move()      # 먼저 상속받은 클래스의 메소드를 오버라이딩함
        print("늑대인간은 ---------")

w = WereWolf()
w.move()