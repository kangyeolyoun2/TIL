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
 61   3
Essential Linux Commands README.md                fundamental_of_CS
 kangyeolyoun  ~/Documents/github/TIL   master  cd fundamental_of_CS
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git add -A

 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "feat: added 5_function"
[master 7f616e4] feat: added 5_function
 2 files changed, 81 insertions(+)
 create mode 100644 fundamental_of_CS/5_function.md
 create mode 100644 fundamental_of_CS/Untitled.ipynb
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.22 KiB | 1.22 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
  3
  4 ## 1. 전역 변수와 지역 변수
  5 - 전역변수(global variable): 전체 영역에서 접근할 수 있는 변수, 함수안에서도
     접근가능
  6 - 지역변수(local vairable): 특정 지역(함수 내부) 안에서만 접근할 수 있는 변>    수
  7
  8
  9 ---
 10 ```python
 11 g_var = 10 #1
 12
 13 def func():
 14     global g_var #2
 15     g_var = 20
 16
 17 if __name__ == "__main__":
 18     print("g_var : {} before".format(g_var)) #3
 19     func()
 20     print("g_var : {} after".format(g_var))
 21 ```
 22     `g_var : 10 before`
 23     `g_var : 20 after` #4
 24 ---
 24 ---
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To https://github.com/kangyeolyoun2/TIL.git
   2891c03..7f616e4  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "feat: modified 5_function"
[master 5928d68] feat: modified 5_function
 2 files changed, 83 insertions(+), 25 deletions(-)
 rewrite fundamental_of_CS/5_function.md (100%)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.39 KiB | 203.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
  1 # 5장. Function
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   7f616e4..5928d68  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "feat: modified 5_Function"
[master 4c110e8] feat: modified 5_Function
 2 files changed, 27 insertions(+), 85 deletions(-)
 rewrite fundamental_of_CS/5_function.md (100%)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 645 bytes | 161.00 KiB/s, done.
 13
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   5928d68..4c110e8  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 ✘ kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master 3a80add] modified 5_function
 2 files changed, 10 insertions(+)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 756 bytes | 756.00 KiB/s, done.
 13
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   4c110e8..3a80add  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master 5d7f7bb] modified 5_function
 2 files changed, 15 insertions(+), 1 deletion(-)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 844 bytes | 844.00 KiB/s, done.
 13
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   3a80add..5d7f7bb  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "added 5_function"
[master 8904640] added 5_function
 1 file changed, 1 insertion(+), 1 deletion(-)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 379 bytes | 379.00 KiB/s, done.
 13
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   5d7f7bb..8904640  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master a6221db] modified 5_function
 2 files changed, 2 insertions(+), 2 deletions(-)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 434 bytes | 434.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
 26 - 전역변수 #1 선언후,
   8904640..a6221db  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master b15753b] modified 5_function
 5 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 fundamental_of_CS/.DS_Store
 create mode 100644 fundamental_of_CS/img/.DS_Store
 create mode 100644 fundamental_of_CS/img/5-4.png
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 4 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 64.50 KiB | 9.21 MiB/s, done.
Total 9 (delta 4), reused 0 (delta 0)
 41     def inner():
remote: Resolving deltas: 100% (4/4), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   a6221db..b15753b  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master 230cc38] modified 5_function
 6 files changed, 25 insertions(+), 2 deletions(-)
 create mode 100644 fundamental_of_CS/img/5-6.png
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 92.86 KiB | 8.44 MiB/s, done.
 94 #include <iostream>
Total 10 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   b15753b..230cc38  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "feat: modified 5_function"
[master d05d862] feat: modified 5_function
 2 files changed, 38 insertions(+), 2 deletions(-)
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 760 bytes | 760.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/kangyeolyoun2/TIL.git
 94 #include <iostream>
   230cc38..d05d862  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_funct133 {
ion.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ✚  git commit -m "modified 5_function"
[master 204ec3b] modified 5_function
 6 files changed, 118 insertions(+), 9 deletions(-)
 create mode 100644 fundamental_of_CS/img/5-2.png
 delete mode 100644 fundamental_of_CS/img/5-4.png
 delete mode 100644 fundamental_of_CS/img/5-6.png
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  git push
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 83.15 KiB | 13.86 MiB/s, done.
Total 8 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/kangyeolyoun2/TIL.git
   d05d862..204ec3b  master -> master
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master  vi 5_function.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  vi 5_fun133 {
ction.md
 kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -
fatal: pathspec '-' did not match any files
 ✘ kangyeolyoun  ~/Documents/github/TIL/fundamental_of_CS   master ●  git add -A
  1 # 5장. Function
  2 - 스택: 접시 쌓기, 마지막에 들어온 데이터가 가장 먼저 나가는 구조
  3
  4 ## 1. 전역 변수와 지역 변수
  5 - 전역변수(global variable): 전체 영역에서 접근할 수 있는 변수, 함수안에서도
     접근가능
  6 - 지역변수(local vairable): 특정 지역(함수 내부) 안에서만 접근할 수 있는 변>    수
  7
  8
  9 - `global` 키워드를 사용하여 함수안에서 전역변수를 변경할 수 있다.
 10 ---
 11 ```python
 12 g_var = 10 #1
 13
 14 def func():
 15     global g_var #2
 16     g_var = 20
 17
 18 if __name__ == "__main__":
 19     print("g_var : {} before".format(g_var)) #3
 20     func()
 21     print("g_var : {} after".format(g_var))
 22 ```
-- INSERT --
