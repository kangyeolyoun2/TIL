# Installing Aparche Spark version 2.4.4

## requirements
#### 1. Java version 8
- `brew cask install homebrew/cas-versions/adoptopenjdk8`

#### 2. scala
- `brew install scala`

#### 3. py4j
- `pip install py4j`

#### 4. environment path setting
- `vi ~/.bash_profile`



- Add contexts below
---
```
JAVA_HOME=/Library/Java?javaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
PATH=$PATH:$JAVA_HOME/bin
export JAVA_HOME
export PATH
```
---

## setup apache-spark

#### 1. install apache-spark
-`brew install apache-spark`

#### 2. environment path setting
- `vi ~/.bash_profile`


- Add contexts below
---
```
# Setting PATH for spark
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.4/libexec
export PATH = $SPARK_HOME

# Setting PATH for python on pySpark
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-.0.10.4-src.zip:$PYTHONPATH
```
---

## Pyspark on Jupyter notebook
#### 1. Use findspark

---
```
import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
```
---


#### 2. setting path on jupyter for python3

---
```
import os
exec(open(os.path.join(os.environ["SPARK_HOME"], 'python/pyspark/shell.py')).read())
```
---




## reference
- https://bit.ly/2QKoyM6
- http://sanghun.xyz/2017/12/mac-apche-spark-%EC%84%A4%EC%B9%98/#pyspark%EB%A5%BC-%EC%9C%84%ED%95%9C-%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95
