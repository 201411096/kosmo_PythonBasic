#클래스 개념
#1. ... ->
#2. ... -> korean \n english \n I'm Groot!
#3. 720
#4. 10, 5
#5.
#6.
#7.

class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):
        return "My name is {0} and my weapon is {1}.".format(self.name, self.characteristic)
class Villain(Marvel):
    pass
first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)


"""
--문제 1--
1.파이썬의 클래스와객체 지향 프로그래밍에 대한 설명으로 틀린 것은?
① 클래스에서 상속은 부모 클래스로부터 속성과 메서드를 물려받은 자식 클래스를 생성하는것을 말한다.
② 클래스에서 __init_ _( ) 함수는 객체 초기화예약 함수이다.
③ 객체 지향 프로그래밍에서 속성은 값(variable)으로, 행동은 메서드(method)로 표현된다.
④ 클래스에서 함수(function) 추가는 기존 함수의사용법과 동일하다.
⑤ 다형성은 같은 이름의 메서드의 내부 로직을 다르게 작성하는 것을 말하며, 같은 부모 클래스를 상속하는 과정에서 주로 발생한다.

--문제 2--
class Person(object):
    def __init__(self, name):
        self.name = name
    def language(self):
        pass
class Earthling(Person):
    def language(self, language):
        return language
class Groot(Person):
    def language(self, language):
        return "I'm Groot!"
name = ['Gachon', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', 'Galaxy']
language = ['Korean', 'English', 'Groot']
for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))
    else:
       groot = Groot(name)
       print(groot.language(language[idx]))

--문제 3--
factorial_calculator.py
def factorial(n):
    if n == 0:
        return 1
    else:
        return ( n * factorial(n-1))
main.py
from factorial_calculator import factorial
print(factorial_calculator.factorial(6))

--문제 4--
class SoccerPlayer(object):
    def  __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def  change_back_number(self, back_number):
        self.back_number = back_number
jinhyun = SoccerPlayer("jinhyun", "MF", 10)
print("현재 선수의 등번호는:",jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는:", jinhyun.back_number)

--문제 5--
class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):
        return "My name is {0} and my weapon is {1}.".format(self.name, self.characteristic)
class Villain(Marvel):
    pass
first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)

"""