# 🌏환장Test(환경장인 Test)

## Our Service
the test for environmental proffessional for Likelion hackerton 9th A-heung Olympic

## 👨‍👨‍👦‍👦Contributor

- Likelion 9th
- 김하은(PM)
- 박은지(Back-end)
- 정우진(Front-end)
- 최윤한(Front-end)

## Branch structure

### Main branch

- Main branch : It is Manage only the state that can be distributed
- Develop branch : It is Used to merge branches for feature development

### Secondary branch
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

## Merge Rule

- merge는 확실하게 된 pull request만 할 것
- 에러나 convention이 잘 지켜지지 않았을 경우 코드리뷰를 하거나 보고 수정을 할 것
