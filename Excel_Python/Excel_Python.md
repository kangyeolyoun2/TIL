# Using Excel in Python


## pre-setting


#### `openpyxl`  module Installation
- `pip install openpyxl`


---
## 1. 파일의 데이터를 읽어오기

```python
    import openpyxl
    import math

    def get_data_from_excel(filename):
        '''
        get_data_from_excel(filename) -> {'name1' : 'score1','name2' : 'score2', ...}
        import data from excel
        key = name, value = scores
        '''

        dic = {}
        wb = openpyxl.load_workbook("/Users/kangyeolyoun/Downloads/class_2_3.xlsx")
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        return dic
```
---
---
## 2. average, variance, standard deviation
```python
    def average(scores):
        s = 0
        for score in scores:
            s += score
        return round(s/len(scores), 1)

    def variance(scores, avrg):
        s = 0
        for score in scores:
            s += (score - avrg) ** 2
        return round(s/len(scores), 1)

    def std_dev(variance):
        return round(math.sqrt(variance), 1)
```
---
---
## 3. 평가하는 함수
```python
    def evaluateClass(avrg, total_avrg, std_dev, sd):
        '''
        evaluateClass(avrg, total_avrg, std_dev, sd) -> None
        avrg: class average
        total_avrg: total students average
        std_dev : standard deviation of class
        sd: desired standard deviation basis
        '''

        if avrg < total_avrg and std_dev > sd:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다")
        elif avrg > total_avrg and std_dev > sd:
            print("성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!")
        elif avrg < total_avrg and std_dev < sd:
            print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!")
        elif avrg > total_avrg and std_dev > sd:
            print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")
```

---

## reference
- 컴퓨터 사이언스 부트캠프 with 파이썬 by 양태환 지음
