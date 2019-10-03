Last login: Thu Oct  3 13:05:19 on ttys000
ls
l%                                                                               kangyeolyoun  ~  ls
Applications                Practice!
Coding                      Public
Desktop                     custom
Documents                   derby.log
Downloads                   iCloud Drive(아카이브)
Google 드라이브             metastore_db
Library                     movienaver
Movies                      nltk_data
Music                       scikit_learn_data
Myproject                   seaborn-data
Pictures
 kangyeolyoun  ~  ls
Applications                Practice!
Coding                      Public
Desktop                     custom
Documents                   derby.log
Downloads                   iCloud Drive(아카이브)
Google 드라이브             metastore_db
Library                     movienaver
Movies                      nltk_data
Music                       scikit_learn_data
Myproject                   seaborn-data
Pictures
 kangyeolyoun  ~  cd Documents
 kangyeolyoun  ~/Documents  ls
04_crawling_on_server.ipynb
04_crawling_on_server_solution-Copy1.ipynb
04_crawling_on_server_solution.ipynb
04_crawling_on_server_김인중.ipynb
Untitled.ipynb
crawling_server_test
exchange
github
king's county
  3
logging
naver_crawling
notebook
prescious
 kangyeolyoun  ~/Documents  cd github
 kangyeolyoun  ~/Documents/github  ls
TIL            Untitled.ipynb
 kangyeolyoun  ~/Documents/github  cd TIL
 kangyeolyoun  ~/Documents/github/TIL   master  ls
Customizing Terminal_ZSH LICENSE                  apache_spark
Essential Linux Commands README.md                fundamental_of_CS
 kangyeolyoun  ~/Documents/github/TIL   master  cd apache_spark
 kangyeolyoun  ~/Documents/github/TIL/apache_spark   master  ls
setup.md
 kangyeolyoun  ~/Documents/github/TIL/apache_spark   master  vi setup.md
 kangyeolyoun  ~/Documents/github/TIL/apache_spark   master  ls
setup.md
 kangyeolyoun  ~/Documents/github/TIL/apache_spark   master  cd ..
 kangyeolyoun  ~/Documents/github/TIL   master  ls
Customizing Terminal_ZSH LICENSE                  apache_spark
  1 # 5장. Function
  2 - 스택: 접시 쌓기, 마지막에 들어온 데이터가 가장 먼저 나가는 구조
  3
  4 ## 1. 전역 변수와 지역 변수
  5 - 전역변수(global variable): 전체 영역에서 접근할 수 있는 변수, 함수안에서도
     접근가능
  6 - 지역변수(local vairable): 특정 지역(함수 내부) 안에서만 접근할 수 있는 변>    수
  7
  8
  9 ---
 10 ```python
 11 g_var = 10
 12
 13 def func():
 14     global g_var
 15     g_var = 20
 16
 17 if __name__ == "__main__":
 18     print("g_var : {} before".format(g_var))
 19     func()
 20     print("g_var : {} after".format(g_var))
 21 ```
 22     `g_var : 10 before`
-- INSERT --
