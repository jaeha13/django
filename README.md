# Django

> `파이썬` 으로 작성된 오픈 소스 웹 프레임워크
> `모델/뷰/컨트롤러` 패턴으로 이루어짐



## 시작하기

개발 환경 : Window

### 가상 환경 만들기

```cmd
C:\***> mkdir python_venv
C:\***> cd python_venv
C:\***\python_venv> python -m venv djangovenv	# djangovenv 라는 가상환경 생성
C:\***\python_venv> dir	# 생성 확인
Volume in drive C has no label.
Volume Serial Number is *******

Directory of C:\***\python_venv

07/23/2021  11:23 AM    <DIR>          .
07/23/2021  11:23 AM    <DIR>          ..
07/23/2021  11:23 AM    <DIR>          djangovenv
               0 File(s)              0 bytes
               3 Dir(s)  107,539,709,952 bytes free
```

### 가상 환경 활성화

```cmd
C:\***\python_venv> cd djangovenv\Scripts
C:\***\python_venv\djangovenv\Scripts> activate
(djangovenv)C:\***\python_venv\djangovenv\Scripts>_
```

### 가상환경에 장고 개발 환경 설치

```cmd
(djangovenv)C:\***\python_venv\djangovenv\Scripts> pip install django
"""장고 설치 과정............."""
"""WARNING: pip upgrade 관련 경고 뜨는 경우 아래 pip upgrade 실시 아니면 다음 과정을 넘어가도 됨"""
(djangovenv)C:\***\python_venv\djangovenv\Scripts> python -m pip install --upgrade pip
"""pip upgrade 과정............."""
(djangovenv)C:\***\python_venv\djangovenv\Scripts>_
```



### 장고 프로젝트 만들기

```cmd
(djangovenv)C:\***\python_venv\djangovenv\Scripts> mkdir \***\django_	# 장고 프로젝트 만들 디렉토리 생성
(djangovenv)C:\***\python_venv\djangovenv\Scripts> cd \***\django_
(djangovenv)C:\***\django_> django-admin startproject exerciseproject	# exerciseproject 이라는 main 프로젝트 생성
(djangovenv)C:\***\django_>_
```



### 장고 프로젝트 생성

```cmd
(djangovenv)C:\***\django_>cd exerciseproject
(djangovenv)C:\***\django_\exerciseproject> python manage.py runserver

```

![image-20210723150447972](C:/Users/hajae/OneDrive/%EB%B0%94%ED%83%95%20%ED%99%94%EB%A9%B4/TIL/images_file/image-20210723150447972.png)

http://localhost:8000/ 브라우저에서 접속

![image-20210723150555314](C:/Users/hajae/OneDrive/%EB%B0%94%ED%83%95%20%ED%99%94%EB%A9%B4/TIL/images_file/image-20210723150555314.png)

> 서버 종료하고 싶으면 cmd 창에서 `ctrl+c` .



### 앱 생성

> PyCharm terminal 창에서 진행

```python
(djangovenv) C:\django_\exerciseproject> python manage.py startapp workapp
```

