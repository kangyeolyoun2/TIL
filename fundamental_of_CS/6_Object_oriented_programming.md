# 6장. Object-oriented programming
- 프로그래밍 패러다임의 한 종류
- 패러다임: 사물을 바라보는 사고의 틀

## 1. 절차 지향 프로그래밍(procedure)
- 프로그램이 어떤 일을 하는가? 에 대한 질문에 쉽게 답할 수 있도록 함수를 사용
- 절차에 의해 만들어 졌기 때문에, 중간 과정의 하나만 작동이 안할 경우 전체적으로 문제를 일으킴.
- 다른 프로그래머가 봐도 프로그램의 실행 흐름을 매우 쉽게 파악할 수 있음

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


## 2. 객체 지향 프로그래밍(object-oriented)
- 짧게 `OOP`(Object Oriented Programing)라고 불림
- 절차에 있어 순서적이지 않아도 됨
- 현실 세계에 존재하는 객체를 어떻게 모델링 할것인가?


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
- `클래스` : 객체를 생성해 내는 템플릿
- `객체` : 클래스를 이용해 만들어진 변수와 함수를 가진 메모리 공간
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


    static method
    A
- #1 정적 메서드: 인자로 클래스나 객체를 받지 않음. 전역 함수를 대체
- #2 첫번째 인자로 클래스 A를 받습니다.
---

### 3.5.1 정보 은닉(c++)
- 특정 멤버와 메서드를 숨겨 유저 프로그래머가 접근할 수 없도록 정하는것

---
```c++
class Account{
public: // #1
    // 생성자: 파이썬 클래스의 __init__()과 같다
    Account(string name, int money){
        user = name;
        balance = money;
    }
    // 인스턴스 메서드(멤버 함수)
    int get_balance() {
        return balance;
    }
    
    // 인스턴스 메서드(멤버 함수)
    void set_balance(int money){
        if (money < 0) {
            return;
        }
        
        balance = money;
    }
private: // #2
    // 인스턴스 멤버(멤버 변수)
    string user;
    int balance; // #3
};
```

- #1 public: 유저 프로그래머가 접근하거나 호출 가능
- #2 private: 클래스 안에서만 사용가능, 객체 안에서는 접근, 호출 x
- 숨겨진 balance 멤버에 접근하기 위한 get_balance, set_balance 등이 액세스 함수
---

### 3.5.2 정보 은닉(python)
- 파이썬은 정보은닉을 기본적으로 지원 x
- 대체방안으로 1) 숨기려는 멤버앞 `__` 붙이기 2) 프로퍼티 기법 사용

---
```python
# property 기법

class Account:
    def __init__(self, name, money):
        self.user = name
        # #3의 setter메서드를 호출
        self.balance = money #1
        
    @property
    def balance(self):
        return self._balance #2 (def get_balance 대신사용)
    
    @balance.setter
    def balance(self, money): #3 (def set_balance 대신 사용)
        if money < 0:
            return
        
        #실제 인스턴스 멤버 선언이 일어나는 부분(#1)
        self._balance = money
        
if __name__ == "__main__":
    my_acnt = Account("greg", 5000)
    my_acnt.balance = -3000 #4
    
    print(my_acnt.balance) #5

```
- 유저 프로그래머가 실제 멤버인 _balance에 접근
- #4 setter 함수인 balance()메서드를 호출. setter 함수를 통해 변경 시도하므로 _balance멤버의 값은 음수로 변경되지 않음
- 파이썬은 완벽한 정보 은닉 제공x (my_acnt._balance = -3000 등으로 접근시, my_acnt.balance 값은 -3000 이 됨)
- 숨기려는 멤버 앞에 `__` 붙이기
---

## 4. DataHandler 클래스 만들기
- cache(일종의 저장 장소)를 두어 연산 결과를 저장하고, 필요한 만큼만 연산

---
```python
#DataHandler 클래스 만들기
import os, stat
from statistics import *
import openpyxl

class DataHandler:
    evaluator = Stat() #1
    @classmethod
    def get_data_from_excel(cls, filename): #2
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows
        
        for name, score in g:
            dic[name.value] = score.value
            
        return dic
    
    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.year_class = year_class
        #연산할 값을 저장해 두는 저장소
        # 필요할 떄 연산하되
        # 이미 연산된 값이면 연산 없이 저장된 값을 반환
        self.cache = {} #3
        
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
            
        return self.cache.get('scores')
    
    def get_average(self): #4
        if 'average' not in self.cache: #5
            self.cache['average'] = self.evaluator.average(self.get_scores())
            
        return self.cache.get('average')
    
    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(self.get_scores(), self.get_average())
            
        return self.cache.get('variance')

    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation'] = self.evaluator.std_dev(self.get_variance())            
            
        return self.cache.get('standard_deviation')
    
    def evaluate_class(self, total_avrg, sd): #7
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()
        
        
        if avrg < total_avrg and std_dev > sd:
            print("성적 너무 저조, 학생들 실력차 큼")
        elif avrg > total_avrg and std_dev > sd:
            print("성적 평균 이상, 학생들 실력차 큼, 주의요망!")
        elif avrg < total_avrg and std_dev < sd:
            print("실력차이는 크지않음. 성적이 너무 저조! 주의요망")
        elif avrg > total_avrg and std_dev < sd:
            print("성적 평균이상, 실력차도 크지 않음")
            
    def get_evaluation(self, total_avrg, sd = 20): #8
        print("*" * 50)
        print("{} 반 성적 분석 결과".format(self.year_class))
        print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며 따라서 표준편차는 {3}이다.".format(
            self.year_class,
            self.get_average(),
            self.getvariance(),
            self.get_standard_deviation()))
        print("*" * 50)
        print("{} 반 종합 평가".format(self.year_class))
        print("*" * 50)
        self.evaluate_class(total_avrg, sd)
    
```


    #실행
    from datahandler import *

    dh = DataHandler("class_2_3.xlsx", "2-3")
    dh.get_evaluation(50)


---
