### 사전작업
- python3.6 설치
- mongoDB(3.6.0) 설치
> db.articles.insert({title:'Hello world'})

## Getting Started

### git clone

git clone it once globally:

```sh
git clone https://github.com/elle510/venv-note.git
```

### virtualenv 생성

```sh
virtualenv venv-note
cd venv-note

// windows
Scripts\activate

// linux/osx
bin/activate
```

### Install Library

```sh
pip install -r requirements.txt
```

### Run Server

```sh
python manage.py runserver
```

### 웹 브라우저에서 확인
http://localhost:8000/memo 로 확인한다.
