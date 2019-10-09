# 6장. Object-oriented programming
- 프로그래밍 패러다임의 한 종류
- 패러다임: 사물을 바라보는 사고의 틀

## 1. 절차 지향 프로그래밍(procedure)
- 프로그램이 어떤 일을 하는가? 에 대한 질문에 쉽게 답할 수 있도록 함수를 사용

---
```python
    from functions import *

if __name__ == "__main__":
    raw_data = get_data_from_excel("class_2_3.xlsx") #1
    scores = list(raw_data.values())

    avrg = average(scores) #2
    variance = variance(scores, avrg) #3
    standard_deviation = std_dev(variance) #4

    print("평균: {}, 분산: {1}, 표준편차: {2}".format(avrg, variance, standard_deviation))
    evaluateClass(avrg, 50, standard_deviation, 20) #5

```
- 다음 #1 ~ #5까지 코드들을 볼때 이름만 봐도 이 프로그램이 무슨일을 하는지 알 수 있는것
- 인터페이스만 알면 필요 함수를 가져다 쓰면 되는것

---

## 2. 객체 지향 프로그래밍(object-oriented)
- 짧게 OOP(Object Oriented Programing)라고 불림
- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. (출처: https://tenlie10.tistory.com/1 [유니티 게임 개발자])

### 2.1 캡슐화(encapsulation)
- 연관 있는 변수(데이터)와 함수를 하나의 단위(클래스 등)으로 묶는것
- 정보은닉 포함하는 개념
---
```python
def person_init(name, money):
    obj = {"name" : name, "money" : money} #1
    obj["give_money"] = Person[1] #2
    obj["get_money"] = Person[2]
    obj["show"] = Person[3]
    
    
def give_money(self, other, money): #3
    self["money"] -= money
    other["get_money"](other, money) #4
    
def get_money(self, money):
    self["money"] += money
    
def show(self):
    print("{} : {}".format(self["name"], self["money"]))
```
- #1 두개의 변수(데이터)
- #2 세개의 함수를 가진 객체
- #3 처럼 다른 특정 함수 #4를 호출하여 상호작용하여 변하는것을 `message passing`이라고 함
---

### 2.2 클래스를 사용해 객체 만들기
- 클래스는 객체를 생성해 내는 템플릿
---
```python
class Person: #1
    def __init__(self, name, money): #2
        self.name = name #3
        self.money = money
        
    def give_money(self, other, money) #4
        self.money -= money
        other.get_money(money)
        
    def get_money(self, money):
        self.money += money
    
    def show(self):
        print("{} : {}".format(self.name, self.money))

```
- #2 클래스로 묶이는 변수를 멤버 
- #2 __init__()은 `생성자`: 인스턴스 멤버를 초기화
- #4 부터 인스턴스가 갖게 될 메서드
---

### 3.3 클래스 멤버와 메서드
---
```python
class A:
    c_mem = 10 #1
    
    @classmethod
    def cls_f(cls): #2
        print(cls.c_mem)
        
    def __init__(self, num):
        self.i_mem = num #3
        
    def ins_f(self):
        print(self.i_mem)
        
if __name__ == "__main__":
    print(A.c_mem) #4
    A.cls_f() #5
```
- #1 클래스 멤버, #4 클래스 메서드 : 객체가 없어도 클래스를 통해 접근하거나 호출가능. 
- 전역변수, 전역 함수를 클래스 멤버, 메서드를 통해 대체할 수 있다.
- 모든 객체가 클래스 멤버를 공유
---

### 3.4 클래스 메서드, 정적 메서드
---
```python
class A:
    @staticmethod
    def f(): #1
        print("static method")
        
    @classmethod
    
    def g(cls): #2
        print(cls.__name__)
        
if __name__ == "__main__":
    a = A()
    a.f()
    a.g()
```


    `static method`
    `A`
- #1 정적 메서드: 인자로 클래스나 객체를 받지 않음. 전역 함수를 대체
- #2 첫번째 인자로 클래스 A를 받습니다.
---

### 3.5 정보 은닉
- 특정 멤버와 메서드를 숨겨 유저 프로그래머가 접근할 수 없도록 정하는것


