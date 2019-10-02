# Installing Aparche Spark version 2.4.4

## requirements
#### 1. Java version 8
- `brew cask install homebrew/cas-versions/adoptopenjdk8`

2. environment path setting
- vi ~/.bash_profile

#insert contexts below
---



JAVA_HOME=/Library/Java?javaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
PATH=$PATH:$JAVA_HOME/bin
export JAVA_HOME
export PATH
---

## setup apache-spark
- brew install apache-spark

## reference
- https://bit.ly/2QKoyM6
