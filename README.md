# 🌏환장Test(환경장인 Test)

## Our Service
the test for environmental proffessional for Likelion hackerton 9th A-heung Olympic

## 👨‍👨‍👦‍👦Contributor

- Likelion 9th

## Branch structure

### Main branch

- Master branch : It is Manage only the state that can be distributed
- Develop branch : It is Used to merge branches for feature development

### Secondary branch

- Feature branch : Branch to develop the function ex)feature/profile
- Fix branch : Branch to fix the function ex)fix/profile

## Guide

```
$ git clone
$ git pull origin develop
$ python -m venv myvenv
$ source myvenv/scripts/activate  mac) source myvenv/bin/activate
$ cd 
$ pip install -r requirements.txt
필요한 모듈들을 적어놓으면, 알아서 설치해줌.
manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver

```

## Commit rule

```
git commit -m "text"

```

[제목 없음](https://www.notion.so/3d949852d4fe43709a6c47163f02872d)

## Convention

### 1. [test.py](http://test.py/) 작성

- 기능에 대한 validation을 할 수 있는 test code를 작성
- 기능에 대한 문제가 날만한 test code를 작성

### 2. method

- CRUD 순서로 함수 작성

### 3. import

- module을 import 해야될 때는 무조건 알파벳 순서로 정리

### 4. python

- class, function 간의 간격은 무조건 2줄
- def (method)의 경우에 간격은 무조건 1줄

### 5. comments

- 로직, class, function에 대한 설명의 주석 작성
- 사용이 안되는 코드의 주석은 무조건 삭제하고 pull request

## Merge Rule

- merge는 확실하게 된 pull request만 할 것
- 에러나 convention이 잘 지켜지지 않았을 경우 코드리뷰를 하거나 보고 수정을 할 것
