# 퀴즈 게임

Python 입문자를 대상으로 만든 터미널 기반 퀴즈 게임입니다.

Python의 기본 문법과 객체 지향 프로그래밍을 직접 활용하여
퀴즈 출제, 퀴즈 등록, 퀴즈 목록 확인, 최고 점수 확인 기능을 구현했습니다.

또한 JSON 파일을 이용해 퀴즈와 최고 점수를 저장하고,
Git을 이용해 기능별 개발 이력을 관리하는 것을 목표로 합니다.1

---

## 1. 프로젝트 개요

이 프로젝트는 Python을 처음 배우는 학습자가
Python 기본 문법을 실제 프로그램에 적용해 보는 것을 목적으로 합니다.

단순한 문법 실습에 그치지 않고 다음 기능을 하나의 프로그램으로 구성했습니다.

- 콘솔 메뉴
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록
- 최고 점수 확인
- JSON 데이터 저장 및 불러오기
- 예외 처리
- 클래스 기반 코드 구조
- Git 브랜치 및 병합

---

## 2. 퀴즈 주제 선정 이유

### 주제: Python · 프로그래밍 기초

이 프로젝트 자체가 Python으로 작성되기 때문에
Python 기초 문법을 퀴즈 주제로 선정했습니다.

특히 Python을 처음 배우는 학습자가
변수, 자료형, 조건문, 반복문, 함수, 딕셔너리, 클래스,
예외 처리 등의 개념을 복습할 수 있도록 입문자 수준으로 구성했습니다.

---

## 3. 개발 환경

- Python 3.12 이상
- Git
- GitHub
- 외부 라이브러리 없음
- Python 표준 라이브러리만 사용

---

## 4. 실행 방법

python main.py



## 5. 기능 목록

### 1. 퀴즈 풀기

등록된 Python 기초 퀴즈를 풀 수 있습니다.

- 등록된 퀴즈를 랜덤한 순서로 출제
- 각 문제마다 4개의 선택지 제공
- 1~4번 중 정답 입력
- 정답/오답 여부 즉시 확인
- 모든 문제를 푼 후 정답 개수와 점수 확인
- 기존 최고 점수보다 높은 점수를 획득하면 최고 점수 갱신
- 등록된 퀴즈가 없는 경우 안내 메시지 출력

### 2. 퀴즈 추가

사용자가 직접 새로운 Python 퀴즈를 등록할 수 있습니다.

- 문제 입력
- 선택지 4개 입력
- 정답 번호 입력
- 정답 번호는 1~4 범위로 제한
- 빈 입력 및 잘못된 숫자 입력 처리
- 추가한 퀴즈를 `state.json`에 자동 저장

### 3. 퀴즈 목록

현재 등록되어 있는 모든 퀴즈를 확인할 수 있습니다.

- 등록된 퀴즈의 전체 개수 표시
- 문제와 4개의 선택지 표시
- 등록된 퀴즈가 없는 경우 안내 메시지 출력

### 4. 점수 확인

현재까지 기록된 최고 점수를 확인할 수 있습니다.

- 퀴즈를 풀 때마다 기존 최고 점수와 비교
- 새로운 최고 점수 획득 시 자동 갱신
- 갱신된 최고 점수를 `state.json`에 저장
- 아직 퀴즈를 풀지 않은 경우 안내 메시지 출력

### 5. 입력 및 예외 처리

프로그램의 안정적인 실행을 위해 잘못된 입력과 예외 상황을 처리합니다.

- 숫자 입력 앞뒤 공백 제거
- 숫자가 아닌 입력 처리
- 허용 범위를 벗어난 숫자 처리
- 빈 입력 처리
- `Ctrl+C` 입력 시 안전하게 종료
- `EOFError` 발생 시 안전하게 종료
- `state.json` 파일이 없는 경우 기본 데이터 사용
- `state.json`이 손상된 경우 기본 데이터로 초기화
- JSON 파일 읽기/쓰기 오류 처리


## 6. 파일 구조

```text
E1-2/
├── main.py
├── state.json
├── README.md
├── .gitignore
└── screenshots/
    ├── git.png
    ├── menu.png
    ├── play.png
    ├── play2.png
    ├── play3.png
    ├── add_quiz.png
    └── score.png
```

## 7. 설명
# 🐍 Python 콘솔 퀴즈 게임

Python 입문자를 위한 **콘솔 기반 퀴즈 게임**입니다.

이 프로젝트에서는 Python의 기본 문법뿐만 아니라 다음과 같은 개념을 함께 학습할 수 있습니다.

- 클래스(Class)
- 객체(Object)
- 메서드(Method)
- 함수(Function)
- 리스트(List)
- 딕셔너리(Dictionary)
- 조건문(`if`, `elif`, `else`)
- 반복문(`for`, `while`)
- 예외 처리(`try`, `except`)
- 파일 입출력
- JSON 데이터 저장
- `pathlib.Path`
- `datetime`
- `random`
- 리스트 컴프리헨션
- `lambda`
- 백업 및 복구
- `KeyboardInterrupt`
- `EOFError`

---

# 📌 1. 프로그램의 전체 구조

이 프로그램은 크게 3개의 클래스와 1개의 함수로 구성되어 있습니다.

```text
Quiz
 └─ 하나의 퀴즈 문제를 관리

Storage
 └─ state.json 파일 저장/불러오기
 └─ 백업 및 복구 관리

QuizGame
 └─ 실제 게임의 전체 흐름 관리

main()
 └─ 프로그램 시작
```

전체적인 데이터 흐름은 다음과 같습니다.

```text
사용자
  │
  ▼
QuizGame
  │
  ├── Quiz 객체 사용
  │
  └── Storage 사용
          │
          ▼
      state.json
```

즉, 각각의 클래스가 서로 다른 역할을 담당합니다.

| 구성 요소 | 역할 |
|---|---|
| `Quiz` | 하나의 문제와 선택지, 정답 관리 |
| `Storage` | JSON 파일 저장/불러오기 및 백업 관리 |
| `QuizGame` | 실제 퀴즈 게임 진행 |
| `main()` | 프로그램 시작 및 종료 처리 |

이처럼 역할을 나누는 것을 **관심사의 분리(Separation of Concerns)**라고 볼 수 있습니다.

---

# 📌 2. 사용하는 Python 모듈

프로그램에서는 다음 모듈을 사용합니다.

```python
import json
import random
from pathlib import Path
from datetime import datetime
```

각각의 역할은 다음과 같습니다.

| 모듈 | 역할 |
|---|---|
| `json` | JSON 파일 읽기/저장 |
| `random` | 퀴즈 순서 무작위 섞기 |
| `pathlib.Path` | 파일 경로 관리 |
| `datetime` | 백업 파일의 날짜와 시간 생성 |

---

# 📌 3. `import`

## `import json`

```python
import json
```

Python의 `json` 모듈을 가져옵니다.

JSON은 데이터를 저장할 때 많이 사용하는 형식입니다.

예를 들어 Python 딕셔너리:

```python
data = {
    "name": "Python",
    "score": 100
}
```

이 데이터를 JSON 파일로 저장할 수 있습니다.

이 프로그램에서는 `state.json`에 다음과 같은 데이터를 저장합니다.

```json
{
    "quizzes": [],
    "best_score": 80
}
```

---

# 📌 4. `random`

```python
import random
```

무작위 값을 만들 때 사용하는 모듈입니다.

이 프로그램에서는:

```python
random.shuffle(quiz_list)
```

을 사용합니다.

`shuffle()`은 리스트의 순서를 무작위로 섞습니다.

예를 들어:

```python
quiz_list = [1, 2, 3, 4, 5]
```

다음과 같이 변경될 수 있습니다.

```python
[4, 1, 5, 2, 3]
```

따라서 게임을 실행할 때마다 문제가 다른 순서로 출제됩니다.

---

# 📌 5. `Path`

```python
from pathlib import Path
```

파일과 폴더의 경로를 쉽게 관리할 수 있게 해주는 클래스입니다.

예를 들어:

```python
Path("state.json")
```

은 `state.json`이라는 파일 경로를 나타냅니다.

문자열로 경로를 관리하는 것보다 `Path`를 사용하면 파일 관련 작업을 쉽게 처리할 수 있습니다.

예:

```python
self.file_path.exists()
```

파일이 존재하는지 확인합니다.

```python
self.file_path.open()
```

파일을 엽니다.

```python
self.file_path.parent
```

파일이 들어 있는 폴더를 가져옵니다.

---

# 📌 6. `datetime`

```python
from datetime import datetime
```

날짜와 시간을 다룰 때 사용하는 클래스입니다.

이 프로그램에서는 백업 파일 이름에 날짜와 시간을 넣기 위해 사용합니다.

```python
timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)
```

예를 들어 현재 시간이 다음과 같다면:

```text
2026년 8월 16일 10시 25분 30초
```

다음과 같은 문자열이 만들어집니다.

```text
20260816_102530
```

따라서 백업 파일은 다음과 같은 이름으로 만들어질 수 있습니다.

```text
state.json.20260816_102530.bak
```

---

# 🏗️ 7. `Quiz` 클래스

```python
class Quiz:
```

`Quiz` 클래스는 **하나의 퀴즈 문제**를 표현합니다.

하나의 퀴즈는 다음 세 가지 정보를 가집니다.

```text
문제
선택지
정답
```

예를 들어:

```python
Quiz(
    "Python에서 문자열 자료형은?",
    ["str", "int", "list", "bool"],
    1
)
```

은 다음과 같은 문제를 의미합니다.

```text
문제:
Python에서 문자열 자료형은?

1. str
2. int
3. list
4. bool

정답:
1번
```

---

# 📌 8. 클래스란?

클래스는 쉽게 말하면 **객체를 만들기 위한 설계도**입니다.

예를 들어 `Quiz`라는 설계도를 만들고:

```python
quiz1 = Quiz(...)
quiz2 = Quiz(...)
quiz3 = Quiz(...)
```

여러 개의 퀴즈 객체를 만들 수 있습니다.

```text
Quiz 클래스
     │
     ├── quiz1
     ├── quiz2
     └── quiz3
```

각 객체는 서로 다른 문제를 가질 수 있습니다.

---

# 📌 9. `__init__()` 메서드

```python
def __init__(self, question, choices, answer):
```

`__init__()`은 객체가 생성될 때 자동으로 실행되는 특별한 메서드입니다.

예:

```python
quiz = Quiz(
    "2 + 2 = ?",
    ["1", "2", "3", "4"],
    4
)
```

객체가 만들어질 때 자동으로:

```python
__init__(
    self,
    "2 + 2 = ?",
    ["1", "2", "3", "4"],
    4
)
```

가 실행됩니다.

---

# 📌 10. `self`

Python 클래스에서 매우 중요한 개념입니다.

```python
self
```

는 **현재 객체 자기 자신**을 의미합니다.

예를 들어:

```python
self.question = question
```

은

> 현재 Quiz 객체의 `question`에 전달받은 `question`을 저장한다.

라는 뜻입니다.

예:

```python
quiz = Quiz(
    "2 + 2 = ?",
    ["1", "2", "3", "4"],
    4
)
```

그러면:

```python
quiz.question
```

의 값은:

```text
2 + 2 = ?
```

가 됩니다.

그리고:

```python
quiz.choices
```

는:

```python
["1", "2", "3", "4"]
```

가 됩니다.

```python
quiz.answer
```

는:

```text
4
```

가 됩니다.

---

# 📌 11. `self.question`

```python
self.question = question
```

현재 객체에 문제를 저장합니다.

```text
question
   ↓
self.question
```

즉:

```python
quiz.question
```

으로 문제 내용을 가져올 수 있습니다.

---

# 📌 12. `self.choices`

```python
self.choices = choices
```

선택지 목록을 객체에 저장합니다.

예:

```python
[
    "str",
    "int",
    "list",
    "bool"
]
```

---

# 📌 13. `self.answer`

```python
self.answer = answer
```

정답 번호를 저장합니다.

예:

```python
self.answer = 1
```

이면 1번이 정답입니다.

---

# 📌 14. `display()` 메서드

```python
def display(self, number=None):
```

문제와 선택지를 화면에 출력하는 메서드입니다.

예:

```text
[문제 1]

Python에서 문자열 자료형을 나타내는 것은?

1. str
2. int
3. list
4. bool
```

---

# 📌 15. 기본값 `number=None`

```python
def display(self, number=None):
```

`number`의 기본값을 `None`으로 설정했습니다.

따라서 다음과 같이 호출할 수 있습니다.

```python
quiz.display()
```

또는:

```python
quiz.display(1)
```

`number`가 전달되지 않으면:

```python
number = None
```

이 됩니다.

---

# 📌 16. `is not None`

```python
if number is not None:
```

`number`에 값이 들어 있는지 확인합니다.

예:

```python
number = 1
```

이면:

```python
number is not None
```

은 `True`입니다.

반면:

```python
number = None
```

이면 `False`입니다.

`None`인지 확인할 때는 일반적으로 다음과 같이 작성합니다.

```python
is None
is not None
```

---

# 📌 17. `print()`

```python
print(self.question)
```

화면에 값을 출력합니다.

예:

```python
print("Hello")
```

결과:

```text
Hello
```

---

# 📌 18. f-string

코드에서 다음과 같은 문법이 사용됩니다.

```python
print(f"[문제 {number}]")
```

앞에 `f`를 붙이면 문자열 안에 변수를 쉽게 넣을 수 있습니다.

예:

```python
number = 3

print(f"[문제 {number}]")
```

결과:

```text
[문제 3]
```

---

# 📌 19. `enumerate()`

선택지 출력 부분:

```python
for index, choice in enumerate(
    self.choices,
    start=1
):
```

`enumerate()`는 리스트의 **순서와 값**을 동시에 가져올 때 사용합니다.

예:

```python
choices = ["A", "B", "C"]
```

일반적인 반복:

```python
for choice in choices:
    print(choice)
```

결과:

```text
A
B
C
```

`enumerate()`를 사용하면:

```python
for index, choice in enumerate(
    choices,
    start=1
):
    print(index, choice)
```

결과:

```text
1 A
2 B
3 C
```

`start=1`은 번호를 1부터 시작하라는 의미입니다.

---

# 📌 20. `check_answer()` 메서드

```python
def check_answer(self, user_answer):
```

사용자가 입력한 답이 실제 정답인지 확인합니다.

핵심 코드는:

```python
return user_answer == self.answer
```

입니다.

예:

```python
self.answer = 2
user_answer = 2
```

이면:

```python
2 == 2
```

결과:

```python
True
```

반대로:

```python
user_answer = 3
```

이면:

```python
3 == 2
```

결과:

```python
False
```

---

# 📌 21. `return`

```python
return user_answer == self.answer
```

`return`은 함수나 메서드의 결과를 호출한 곳으로 돌려줍니다.

예:

```python
def add(a, b):
    return a + b
```

사용:

```python
result = add(10, 20)
```

그러면:

```text
result = 30
```

이 됩니다.

---

# 📌 22. `to_dict()` 메서드

```python
def to_dict(self):
```

Quiz 객체를 Python 딕셔너리로 변환합니다.

왜 필요한가요?

JSON은 Python의 `Quiz` 객체 자체를 바로 저장할 수 없기 때문입니다.

따라서:

```text
Quiz 객체
   ↓
딕셔너리
   ↓
JSON
```

과정을 거칩니다.

예:

```python
{
    "question": "2 + 2 = ?",
    "choices": ["1", "2", "3", "4"],
    "answer": 4
}
```

---

# 💾 23. `Storage` 클래스

```python
class Storage:
```

`Storage`는 파일 저장과 관련된 작업을 담당합니다.

주요 역할은 다음과 같습니다.

```text
state.json 읽기
state.json 저장
백업 만들기
백업 확인
손상된 데이터 복구
```

즉:

```text
QuizGame
   │
   ▼
Storage
   │
   ├── 읽기
   ├── 저장
   ├── 백업
   └── 복구
```

게임 로직과 파일 처리 로직을 분리하기 위한 클래스입니다.

---

# 📌 24. `Storage.__init__()`

```python
def __init__(self, file_path):
```

저장할 파일 경로를 전달받습니다.

예:

```python
storage = Storage("state.json")
```

그러면:

```python
self.file_path
```

에는 `state.json`의 경로가 저장됩니다.

---

# 📌 25. `Path(file_path)`

```python
self.file_path = Path(file_path)
```

문자열로 받은 파일 경로를 `Path` 객체로 변환합니다.

예:

```python
file_path = "state.json"
```

을:

```python
Path("state.json")
```

으로 변환합니다.

---

# 📌 26. `.suffix`

```python
self.file_path.suffix
```

파일의 확장자를 가져옵니다.

예:

```python
Path("state.json").suffix
```

결과:

```text
.json
```

---

# 📌 27. `.with_suffix()`

```python
self.file_path.with_suffix(
    self.file_path.suffix + ".bak"
)
```

파일의 확장자를 변경합니다.

예:

```text
state.json
```

의 suffix는:

```text
.json
```

입니다.

여기에 `.bak`을 붙이면:

```text
.json.bak
```

이 됩니다.

따라서 결과는:

```text
state.json.bak
```

입니다.

---

# 📌 28. `_load_file()` 메서드

```python
def _load_file(self, file_path):
```

JSON 파일 하나를 읽는 내부용 메서드입니다.

메서드 이름 앞에 `_`가 붙어 있습니다.

```python
_load_file()
```

Python에서 `_`는 일반적으로:

> 이 메서드는 클래스 내부에서 사용하는 메서드입니다.

라는 의도를 표현할 때 사용합니다.

Python이 강제로 접근을 막는 것은 아닙니다.

---

# 📌 29. `with`

파일을 열 때 다음과 같이 작성합니다.

```python
with file_path.open(
    "r",
    encoding="utf-8"
) as file:
```

`with`를 사용하면 작업이 끝난 후 파일을 자동으로 닫아줍니다.

일반적으로 파일을 직접 열고 닫으면:

```python
file = open("state.json", "r")
data = file.read()
file.close()
```

처럼 작성해야 합니다.

하지만 `with`를 사용하면:

```python
with open("state.json", "r") as file:
    data = file.read()
```

처럼 사용할 수 있습니다.

파일을 사용한 후 자동으로 정리되므로 더 안전하고 편리합니다.

---

# 📌 30. 파일 모드 `"r"`

```python
file_path.open("r")
```

`r`은 `read`의 약자로 **읽기 모드**입니다.

대표적인 파일 모드는 다음과 같습니다.

| 모드 | 의미 |
|---|---|
| `r` | 읽기 |
| `w` | 쓰기 |
| `a` | 이어쓰기 |
| `x` | 새 파일 생성 |

이 프로그램에서는:

```python
"r"
```

은 JSON 읽기에 사용하고:

```python
"w"
```

는 JSON 저장에 사용합니다.

---

# 📌 31. `encoding="utf-8"`

```python
encoding="utf-8"
```

한글과 같은 문자를 정상적으로 읽고 저장하기 위해 사용합니다.

예:

```python
with open(
    "state.json",
    "r",
    encoding="utf-8"
) as file:
    ...
```

한글 데이터가 포함된 파일을 다룰 때 매우 중요합니다.

---

# 📌 32. `json.load()`

```python
data = json.load(file)
```

JSON 파일의 내용을 읽어서 Python 객체로 변환합니다.

예를 들어 JSON 파일:

```json
{
    "best_score": 80
}
```

을 읽으면 Python에서는:

```python
{
    "best_score": 80
}
```

이라는 딕셔너리가 됩니다.

즉:

```text
JSON 파일
   ↓
json.load()
   ↓
Python 객체
```

---

# 📌 33. `isinstance()`

코드에서는:

```python
isinstance(data, dict)
```

와 같이 사용합니다.

`isinstance()`는 값이 특정 자료형인지 확인합니다.

예:

```python
data = {}
```

이라면:

```python
isinstance(data, dict)
```

결과는:

```python
True
```

입니다.

예:

```python
data = []
```

이면:

```python
isinstance(data, dict)
```

결과는:

```python
False
```

입니다.

이 프로그램에서는 저장된 JSON 데이터가 올바른 자료형인지 확인하는 데 사용합니다.

---

# 📌 34. `raise ValueError`

예:

```python
raise ValueError(
    "데이터 형식이 올바르지 않습니다."
)
```

`raise`는 직접 예외를 발생시킬 때 사용합니다.

즉:

> 이 데이터는 정상적인 형태가 아니므로 오류로 처리하겠다.

라는 의미입니다.

---

# 📌 35. `ValueError`

`ValueError`는 값의 형태가 적절하지 않을 때 사용하는 예외입니다.

예를 들어:

```python
int("hello")
```

처럼 숫자가 아닌 문자열을 숫자로 변환하려고 하면 `ValueError`가 발생합니다.

이 프로그램에서는 잘못된 JSON 데이터 구조를 발견했을 때도 사용합니다.

---

# 📌 36. `_get_backup_files()`

```python
def _get_backup_files(self):
```

사용 가능한 백업 파일 목록을 찾습니다.

이 프로그램에서 찾는 백업은 다음과 같습니다.

```text
state.json.bak

state.json.20260816_101500.bak

state.json.20260816_102000.bak
```

---

# 📌 37. `exists()`

```python
self.backup_file_path.exists()
```

파일이나 폴더가 실제로 존재하는지 확인합니다.

결과는 `True` 또는 `False`입니다.

예:

```python
Path("state.json").exists()
```

파일이 있으면:

```python
True
```

없으면:

```python
False
```

---

# 📌 38. `glob()`

```python
self.file_path.parent.glob(
    f"{self.file_path.name}.*.bak"
)
```

특정 패턴에 맞는 파일들을 찾습니다.

예를 들어:

```text
state.json.20260816_101500.bak
state.json.20260816_102000.bak
state.json.20260816_103000.bak
```

같은 파일을 찾을 수 있습니다.

`*`는 여러 문자열을 의미합니다.

---

# 📌 39. `extend()`

```python
backup_files.extend(
    timestamp_backups
)
```

리스트에 여러 개의 값을 추가합니다.

예:

```python
numbers = [1, 2]

numbers.extend([3, 4])
```

결과:

```python
[1, 2, 3, 4]
```

---

# 📌 40. `sorted()`

```python
return sorted(
    backup_files,
    key=lambda path: path.stat().st_mtime,
    reverse=True
)
```

리스트를 정렬합니다.

여기서는 파일의 수정 시간을 기준으로 정렬합니다.

---

# 📌 41. `lambda`

```python
lambda path: path.stat().st_mtime
```

`lambda`는 간단한 함수를 한 줄로 만드는 문법입니다.

위 코드는 사실상 다음과 비슷합니다.

```python
def get_modified_time(path):
    return path.stat().st_mtime
```

즉:

```python
lambda path: path.stat().st_mtime
```

은

> path를 받아서 파일 수정 시간을 반환하는 간단한 함수

입니다.

---

# 📌 42. `stat().st_mtime`

```python
path.stat().st_mtime
```

파일의 마지막 수정 시간을 가져옵니다.

따라서:

```python
sorted(
    backup_files,
    key=lambda path: path.stat().st_mtime,
    reverse=True
)
```

는:

> 파일 수정 시간이 최신인 백업부터 정렬

한다는 의미입니다.

---

# 📌 43. `reverse=True`

```python
reverse=True
```

정렬 순서를 뒤집습니다.

기본적으로:

```python
sorted([1, 3, 2])
```

결과:

```python
[1, 2, 3]
```

하지만:

```python
sorted(
    [1, 3, 2],
    reverse=True
)
```

결과:

```python
[3, 2, 1]
```

이 프로그램에서는 최신 백업을 먼저 확인하기 위해 사용합니다.

---

# 📌 44. `_restore_from_backup()`

```python
def _restore_from_backup(self):
```

손상되거나 없는 `state.json`을 백업 파일로 복구합니다.

처리 순서는:

```text
백업 목록 확인
     ↓
최신 백업 확인
     ↓
JSON 정상 여부 확인
     ↓
정상이라면 복구
     ↓
문제가 있으면 다음 백업 확인
```

---

# 📌 45. `for`

```python
for backup_file in backup_files:
```

리스트의 값을 하나씩 꺼내 반복합니다.

예:

```python
backup_files = [
    "backup1",
    "backup2",
    "backup3"
]
```

이라면:

```text
backup1
backup2
backup3
```

순서대로 처리합니다.

---

# 📌 46. `try`

```python
try:
    ...
```

오류가 발생할 수 있는 코드를 감싸는 데 사용합니다.

예:

```python
try:
    data = self._load_file(backup_file)
```

JSON 파일을 읽다가 오류가 발생할 수 있기 때문입니다.

---

# 📌 47. `except`

```python
except ValueError:
    ...
```

`try` 안에서 특정 오류가 발생했을 때 실행됩니다.

즉:

```text
try
 ↓
코드 실행
 ↓
오류 발생?
 ├─ 아니오 → 계속 진행
 └─ 예 → except 실행
```

---

# 📌 48. 여러 예외를 한 번에 처리

```python
except (
    json.JSONDecodeError,
    ValueError,
    KeyError,
    TypeError,
    OSError
):
```

여러 종류의 예외를 한 번에 처리할 수 있습니다.

각 예외의 의미는 대략 다음과 같습니다.

| 예외 | 의미 |
|---|---|
| `JSONDecodeError` | JSON 문법 오류 |
| `ValueError` | 값이 올바르지 않음 |
| `KeyError` | 딕셔너리에 없는 키 접근 |
| `TypeError` | 자료형 사용이 잘못됨 |
| `OSError` | 파일/운영체제 관련 오류 |

---

# 📌 49. `continue`

```python
continue
```

현재 반복을 중단하고 다음 반복으로 넘어갑니다.

예:

```python
for number in numbers:

    if number < 0:
        continue

    print(number)
```

음수는 건너뛰고 다음 값으로 넘어갑니다.

이 프로그램에서는 손상된 백업을 발견하면:

```python
continue
```

하여 다음 백업 파일을 확인합니다.

---

# 📌 50. `replace()`

```python
backup_file.replace(
    self.file_path
)
```

백업 파일을 `state.json`으로 이동/이름 변경합니다.

예:

```text
state.json.20260816_102530.bak
```

을:

```text
state.json
```

으로 복구합니다.

---

# 📌 51. `load()` 메서드

```python
def load(self):
```

게임 데이터를 불러오는 가장 중요한 메서드입니다.

처리 순서는 다음과 같습니다.

```text
state.json 존재?
       │
   ┌───┴───┐
   │       │
  없음     있음
   │       │
   ▼       ▼
백업 확인  JSON 읽기
   │       │
   ▼       ▼
복구 성공? 정상?
   │       │
   ▼       ▼
데이터 반환
```

---

# 📌 52. `json.JSONDecodeError`

JSON 파일 자체가 문법적으로 잘못되어 있을 때 발생합니다.

예를 들어 잘못된 JSON:

```json
{
    "name": "Python",
```

처럼 닫는 `}`가 없다면 JSON을 정상적으로 읽을 수 없습니다.

이때:

```python
json.JSONDecodeError
```

가 발생할 수 있습니다.

---

# 💾 53. `save()` 메서드

```python
def save(self, quizzes, best_score):
```

퀴즈와 최고 점수를 `state.json`에 저장합니다.

저장 과정은 다음과 같습니다.

```text
현재 state.json 존재?
       │
       ▼
기존 파일 백업
       │
       ├── state.json.bak
       │
       └── state.json.YYYYMMDD_HHMMSS.bak
       │
       ▼
새로운 state.json 저장
```

---

# 📌 54. 리스트 컴프리헨션

다음 코드가 사용됩니다.

```python
"quizzes": [
    quiz.to_dict()
    for quiz in quizzes
],
```

이것은 **리스트 컴프리헨션(List Comprehension)**입니다.

일반적인 `for`문으로 작성하면:

```python
quiz_data = []

for quiz in quizzes:
    quiz_data.append(
        quiz.to_dict()
    )
```

리스트 컴프리헨션으로 작성하면:

```python
quiz_data = [
    quiz.to_dict()
    for quiz in quizzes
]
```

훨씬 짧게 표현할 수 있습니다.

---

# 📌 55. `json.dump()`

```python
json.dump(
    data,
    file,
    ensure_ascii=False,
    indent=4
)
```

Python 데이터를 JSON 파일에 저장합니다.

구조는:

```text
Python 데이터
      ↓
json.dump()
      ↓
JSON 파일
```

---

# 📌 56. `ensure_ascii=False`

```python
ensure_ascii=False
```

한글을 그대로 저장하도록 합니다.

예를 들어:

```json
{
    "question": "Python이란?"
}
```

처럼 한글을 사람이 읽기 좋은 형태로 저장할 수 있습니다.

---

# 📌 57. `indent=4`

```python
indent=4
```

JSON을 보기 좋게 들여쓰기합니다.

예:

```json
{
    "quizzes": [
        {
            "question": "2 + 2 = ?",
            "choices": [
                "1",
                "2",
                "3",
                "4"
            ],
            "answer": 4
        }
    ],
    "best_score": 100
}
```

---

# 📌 58. `shutil`

코드에서는 필요한 시점에:

```python
import shutil
```

을 실행합니다.

`shutil`은 파일 복사와 같은 작업에 사용할 수 있습니다.

이 프로그램에서는:

```python
shutil.copy2(
    self.file_path,
    self.backup_file_path
)
```

을 사용하여 파일을 백업합니다.

---

# 📌 59. `copy2()`

```python
shutil.copy2(
    source,
    destination
)
```

파일을 복사합니다.

예:

```text
state.json
   ↓
state.json.bak
```

파일의 메타데이터도 가능한 범위에서 함께 보존합니다.

---

# 📌 60. `datetime.now()`

```python
datetime.now()
```

현재 날짜와 시간을 가져옵니다.

예:

```text
2026-08-16 10:25:30
```

---

# 📌 61. `strftime()`

```python
datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)
```

날짜와 시간을 원하는 문자열 형식으로 변환합니다.

주요 형식은 다음과 같습니다.

| 형식 | 의미 |
|---|---|
| `%Y` | 4자리 연도 |
| `%m` | 월 |
| `%d` | 일 |
| `%H` | 시간 |
| `%M` | 분 |
| `%S` | 초 |

따라서:

```python
"%Y%m%d_%H%M%S"
```

는:

```text
20260816_102530
```

형태가 됩니다.

---

# 🎮 62. `QuizGame` 클래스

```python
class QuizGame:
```

실제 게임의 전체 흐름을 관리합니다.

주요 기능:

```text
기본 퀴즈 생성
저장 데이터 불러오기
데이터 저장
메뉴 출력
사용자 입력
퀴즈 풀기
퀴즈 추가
퀴즈 목록 보기
최고 점수 보기
게임 실행
```

즉, 프로그램의 **중앙 관리자 역할**을 합니다.

---

# 📌 63. `QuizGame.__init__()`

```python
def __init__(self, storage):
```

게임 객체가 생성될 때 실행됩니다.

가장 먼저:

```python
self.storage = storage
```

를 통해 `Storage` 객체를 저장합니다.

그리고:

```python
self.quizzes = []
```

로 퀴즈 목록을 초기화하고:

```python
self.best_score = 0
```

으로 최고 점수를 초기화합니다.

마지막으로:

```python
self.load_data()
```

를 실행하여 저장된 데이터를 불러옵니다.

---

# 📌 64. 객체를 다른 객체에 전달하기

다음 코드가 있습니다.

```python
game = QuizGame(storage)
```

여기서 `storage` 객체를 `QuizGame` 객체에게 전달합니다.

즉:

```text
Storage 객체
    │
    ▼
QuizGame
```

이 구조를 사용하면 `QuizGame`이 파일을 직접 다루지 않고 `Storage`에게 파일 작업을 맡길 수 있습니다.

이런 구조는 객체지향 프로그래밍에서 매우 중요한 개념입니다.

---

# 📌 65. `get_default_quizzes()`

```python
def get_default_quizzes(self):
```

프로그램을 처음 실행했을 때 사용할 기본 퀴즈를 생성합니다.

반환값은 `Quiz` 객체의 리스트입니다.

```python
return [
    Quiz(...),
    Quiz(...),
    Quiz(...),
]
```

---

# 📌 66. `return []`

```python
return [
    Quiz(...),
    Quiz(...),
]
```

리스트를 생성해서 호출한 곳으로 반환합니다.

따라서:

```python
self.quizzes = self.get_default_quizzes()
```

라고 하면 기본 퀴즈들이 `self.quizzes`에 저장됩니다.

---

# 📌 67. `load_data()`

```python
def load_data(self):
```

저장된 게임 데이터를 불러옵니다.

처음에는:

```python
data = self.storage.load()
```

을 실행합니다.

그리고 결과에 따라 처리합니다.

### 저장 데이터가 없는 경우

```python
if data is None:
```

기본 퀴즈를 사용합니다.

```python
self.quizzes = self.get_default_quizzes()
self.best_score = 0
self.save_data()
```

### 저장 데이터가 있는 경우

JSON의 데이터를 Quiz 객체로 변환합니다.

---

# 📌 68. JSON 딕셔너리를 Quiz 객체로 변환

JSON에서는 다음처럼 저장됩니다.

```json
{
    "question": "2 + 2 = ?",
    "choices": ["1", "2", "3", "4"],
    "answer": 4
}
```

게임에서는 `Quiz` 객체가 필요합니다.

따라서:

```python
quiz = Quiz(
    item["question"],
    item["choices"],
    item["answer"]
)
```

를 사용합니다.

즉:

```text
JSON 딕셔너리
      ↓
Quiz()
      ↓
Quiz 객체
```

로 변환합니다.

---

# 📌 69. 딕셔너리 접근

```python
item["question"]
```

딕셔너리에서 특정 키의 값을 가져옵니다.

예:

```python
item = {
    "question": "2 + 2 = ?",
    "answer": 4
}
```

이면:

```python
item["question"]
```

결과:

```text
2 + 2 = ?
```

그리고:

```python
item["answer"]
```

결과:

```text
4
```

---

# 📌 70. `append()`

```python
self.quizzes.append(quiz)
```

리스트의 마지막에 값을 추가합니다.

예:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

결과:

```python
[1, 2, 3, 4]
```

이 프로그램에서는 새롭게 만든 `Quiz` 객체를 퀴즈 목록에 추가할 때 사용합니다.

---

# 📌 71. `save_data()`

```python
def save_data(self):
```

현재 게임 데이터를 저장합니다.

실제 파일 작업은 직접 하지 않고:

```python
self.storage.save(
    self.quizzes,
    self.best_score
)
```

를 호출합니다.

즉:

```text
QuizGame
    │
    │ save_data()
    ▼
Storage
    │
    │ save()
    ▼
state.json
```

역할을 분리한 것입니다.

---

# 🖥️ 72. `display_menu()`

```python
def display_menu(self):
```

메인 메뉴를 출력합니다.

결과는 대략 다음과 같습니다.

```text
==================================================
               퀴즈 게임
==================================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==================================================
```

---

# 📌 73. 문자열 곱셈

다음 코드가 있습니다.

```python
"=" * 50
```

문자열도 숫자와 곱셈 연산을 할 수 있습니다.

결과:

```text
==================================================
```

즉:

```python
"abc" * 3
```

은:

```text
abcabcabc
```

가 됩니다.

---

# 🔢 74. `get_number()`

```python
def get_number(
    self,
    prompt,
    min_value,
    max_value
):
```

사용자에게 숫자를 입력받고 올바른 범위인지 검사하는 메서드입니다.

예:

```python
self.get_number(
    "선택: ",
    1,
    5
)
```

이면:

```text
1~5
```

사이의 숫자만 허용합니다.

---

# 📌 75. `input()`

```python
user_input = input(prompt)
```

사용자로부터 키보드 입력을 받습니다.

중요한 점은 `input()`의 반환값은 항상 **문자열**이라는 것입니다.

예:

```python
age = input("나이: ")
```

사용자가:

```text
20
```

을 입력해도:

```python
age
```

의 실제 자료형은:

```python
str
```

입니다.

---

# 📌 76. `strip()`

```python
input(prompt).strip()
```

문자열 앞뒤의 공백을 제거합니다.

예:

```python
"   hello   ".strip()
```

결과:

```text
hello
```

사용자 입력을 받을 때 유용합니다.

---

# 📌 77. `not`

```python
if not user_input:
```

`not`은 논리값을 반대로 바꿉니다.

예:

```python
user_input = ""
```

이면 빈 문자열은 거짓처럼 취급되므로:

```python
not user_input
```

은 `True`가 됩니다.

따라서 빈 입력을 검사할 수 있습니다.

---

# 📌 78. `int()`

```python
number = int(user_input)
```

문자열을 정수로 변환합니다.

예:

```python
"123"
```

을:

```python
123
```

으로 변환합니다.

`input()`은 문자열을 반환하기 때문에 숫자 계산이나 숫자 비교를 하려면 `int()`가 필요합니다.

---

# 📌 79. `or`

다음 코드:

```python
if (
    number < min_value
    or number > max_value
):
```

`or`는 **둘 중 하나라도 참이면 참**입니다.

예:

```python
number = 10

number < 1
```

은 `False`지만:

```python
number > 5
```

는 `True`입니다.

따라서:

```python
False or True
```

는:

```python
True
```

가 됩니다.

---

# 📌 80. `while True`

```python
while True:
```

조건이 항상 `True`이기 때문에 무한 반복합니다.

예:

```python
while True:
    print("반복")
```

계속 실행됩니다.

따라서 반드시 적절한 시점에:

```python
break
```

가 필요합니다.

---

# 📌 81. `break`

```python
break
```

반복문을 즉시 종료합니다.

예:

```python
while True:

    number = input("종료하려면 q: ")

    if number == "q":
        break
```

`q`를 입력하면 반복문이 종료됩니다.

이 프로그램에서는 메뉴에서 `5. 종료`를 선택하면 `break`가 실행됩니다.

---

# 🎯 82. `play_quiz()`

```python
def play_quiz(self):
```

실제 퀴즈를 진행하는 핵심 메서드입니다.

전체 흐름:

```text
퀴즈가 있는지 확인
      ↓
퀴즈 목록 복사
      ↓
문제 순서 섞기
      ↓
문제 하나씩 출력
      ↓
사용자 답 입력
      ↓
정답 확인
      ↓
점수 계산
      ↓
최고 점수 갱신
      ↓
저장
```

---

# 📌 83. `copy()`

```python
quiz_list = self.quizzes.copy()
```

현재 리스트를 복사합니다.

왜 복사할까요?

다음 코드를 사용하면:

```python
random.shuffle(self.quizzes)
```

실제 등록된 퀴즈 목록의 순서가 바뀝니다.

하지만:

```python
quiz_list = self.quizzes.copy()
random.shuffle(quiz_list)
```

를 사용하면 원본:

```python
self.quizzes
```

는 그대로 유지됩니다.

---

# 📌 84. `random.shuffle()`

```python
random.shuffle(quiz_list)
```

리스트의 순서를 무작위로 섞습니다.

예:

```python
[1, 2, 3, 4]
```

가:

```python
[3, 1, 4, 2]
```

처럼 바뀔 수 있습니다.

---

# 📌 85. `correct_count`

```python
correct_count = 0
```

맞힌 문제의 개수를 저장하는 변수입니다.

정답을 맞히면:

```python
correct_count += 1
```

을 실행합니다.

---

# 📌 86. `+=`

```python
correct_count += 1
```

다음 코드와 동일합니다.

```python
correct_count = correct_count + 1
```

즉, 현재 값에 1을 더합니다.

---

# 📌 87. `for index, quiz in enumerate()`

```python
for index, quiz in enumerate(
    quiz_list,
    start=1
):
```

퀴즈를 하나씩 가져오면서 문제 번호도 함께 가져옵니다.

예:

```text
index = 1
quiz = 첫 번째 Quiz 객체

index = 2
quiz = 두 번째 Quiz 객체
```

---

# 📌 88. `if / else`

정답 확인:

```python
if quiz.check_answer(user_answer):

    print("정답입니다!")

else:

    print("오답입니다.")
```

조건이 참이면 `if` 부분을 실행합니다.

조건이 거짓이면 `else` 부분을 실행합니다.

---

# 📌 89. 점수 계산

```python
score = int(
    (correct_count / total_count) * 100
)
```

예를 들어:

```text
총 8문제
정답 6문제
```

이면:

```text
6 / 8 × 100
= 75
```

따라서:

```python
score = 75
```

가 됩니다.

---

# 📌 90. `/`

```python
correct_count / total_count
```

나눗셈 연산입니다.

예:

```python
6 / 8
```

결과:

```python
0.75
```

---

# 📌 91. `int()`

점수 계산 결과가 소수일 수도 있기 때문에:

```python
int(...)
```

로 정수로 변환합니다.

예:

```python
int(87.5)
```

결과:

```python
87
```

소수점 이하를 버립니다.

---

# 🏆 92. 최고 점수 갱신

```python
if score > self.best_score:
```

현재 점수가 기존 최고 점수보다 높은지 확인합니다.

예:

```text
현재 점수: 90
최고 점수: 80
```

이면:

```python
90 > 80
```

이므로 새로운 최고 점수가 됩니다.

```python
self.best_score = score
```

---

# ➕ 93. `add_quiz()`

```python
def add_quiz(self):
```

사용자가 직접 새로운 퀴즈를 추가하는 메서드입니다.

입력 순서는:

```text
문제
선택지 1
선택지 2
선택지 3
선택지 4
정답 번호
```

입니다.

---

# 📌 94. 빈 리스트

```python
choices = []
```

선택지를 저장할 빈 리스트를 만듭니다.

이후:

```python
choices.append(choice)
```

를 사용하여 하나씩 추가합니다.

결과:

```python
[
    "선택지 1",
    "선택지 2",
    "선택지 3",
    "선택지 4"
]
```

---

# 📌 95. `range()`

```python
for index in range(1, 5):
```

`range()`는 일정한 숫자 범위를 만들어줍니다.

```python
range(1, 5)
```

은:

```text
1
2
3
4
```

를 의미합니다.

주의할 점은 마지막 숫자 `5`는 포함되지 않는다는 것입니다.

즉:

```python
range(1, 5)
```

은:

```text
1 이상 5 미만
```

입니다.

---

# 📋 96. `show_quizzes()`

```python
def show_quizzes(self):
```

현재 등록된 모든 퀴즈를 화면에 보여줍니다.

예:

```text
==================================================
📋 등록된 퀴즈 목록 (총 2개)
==================================================

[1] Python에서 문자열 자료형은?
    1. str
    2. int
    3. list
    4. bool

[2] Python에서 리스트를 만드는 방법은?
    1. []
    2. {}
    3. ()
    4. <>
```

---

# 🏆 97. `show_score()`

```python
def show_score(self):
```

현재 저장된 최고 점수를 보여줍니다.

```text
==================================================
🏆 최고 점수
==================================================
최고 점수: 90점
```

---

# 🎮 98. `run()`

```python
def run(self):
```

게임의 메인 루프입니다.

메뉴를 계속 보여주고 사용자의 선택에 따라 기능을 실행합니다.

전체 구조:

```text
while True
   │
   ├── 메뉴 출력
   │
   ├── 1 → 퀴즈 풀기
   │
   ├── 2 → 퀴즈 추가
   │
   ├── 3 → 퀴즈 목록
   │
   ├── 4 → 점수 확인
   │
   └── 5 → 저장 후 종료
```

---

# 📌 99. `elif`

```python
if choice == 1:
    ...

elif choice == 2:
    ...

elif choice == 3:
    ...
```

`elif`는 **else if**의 줄임말입니다.

앞의 `if`가 거짓일 때 다른 조건을 검사합니다.

이 프로그램에서는 메뉴 선택을 처리할 때 사용합니다.

---

# 🛑 100. 메뉴 종료

사용자가:

```text
5
```

를 입력하면:

```python
elif choice == 5:
```

가 실행됩니다.

그리고:

```python
self.save_data()
```

로 데이터를 저장한 후:

```python
break
```

로 메인 반복문을 종료합니다.

---

# 🚀 101. `main()` 함수

```python
def main():
```

프로그램의 시작점 역할을 하는 함수입니다.

주요 역할:

```text
프로그램 위치 확인
      ↓
state.json 경로 생성
      ↓
Storage 생성
      ↓
QuizGame 생성
      ↓
게임 실행
      ↓
예외 발생 시 저장 후 종료
```

---

# 📌 102. `__file__`

```python
Path(__file__)
```

`__file__`은 현재 실행 중인 Python 파일의 경로를 나타냅니다.

예:

```text
/home/user/quiz/main.py
```

---

# 📌 103. `resolve()`

```python
Path(__file__).resolve()
```

파일의 경로를 절대 경로 형태로 가져옵니다.

예:

```text
/home/user/quiz/main.py
```

---

# 📌 104. `parent`

```python
Path(__file__).resolve().parent
```

현재 파일이 들어 있는 폴더를 가져옵니다.

예:

```text
/home/user/quiz/main.py
```

의 `parent`는:

```text
/home/user/quiz
```

입니다.

---

# 📌 105. `Path / "파일명"`

다음과 같은 코드가 있습니다.

```python
state_file = base_dir / "state.json"
```

`Path` 객체에서는 `/` 연산자를 이용해 경로를 쉽게 연결할 수 있습니다.

예:

```text
base_dir
   +
state.json
```

→

```text
/home/user/quiz/state.json
```

이 됩니다.

---

# 🛡️ 106. `KeyboardInterrupt`

```python
except KeyboardInterrupt:
```

사용자가 `Ctrl+C`를 누르면 발생하는 예외입니다.

일반적으로 프로그램을 강제로 종료하려는 상황입니다.

이 프로그램에서는 갑자기 종료하는 대신:

```text
Ctrl+C
  ↓
현재 데이터 저장
  ↓
안전하게 종료
```

하도록 만들었습니다.

---

# 📌 107. `EOFError`

```python
except EOFError:
```

입력 스트림이 종료되었을 때 발생할 수 있는 예외입니다.

터미널 환경에서는 `Ctrl+D` 등의 상황에서 발생할 수 있습니다.

이 프로그램에서는 `EOFError`가 발생해도:

```text
현재 데이터 저장
      ↓
안전하게 종료
```

합니다.

---

# 📌 108. 예외 처리 전체 구조

`main()`의 핵심 구조는 다음과 같습니다.

```python
try:
    game.run()

except KeyboardInterrupt:
    game.save_data()

except EOFError:
    game.save_data()
```

즉:

```text
게임 실행
   │
   ├── 정상 종료
   │
   ├── Ctrl+C
   │      ↓
   │   데이터 저장
   │
   └── EOFError
          ↓
       데이터 저장
```

---

# 📌 109. `if __name__ == "__main__"`

프로그램 마지막에 다음 코드가 있습니다.

```python
if __name__ == "__main__":
    main()
```

Python에서 매우 자주 사용하는 패턴입니다.

현재 파일을 직접 실행하면:

```python
__name__ == "__main__"
```

이 됩니다.

따라서:

```python
main()
```

이 실행됩니다.

---

# 📌 110. 직접 실행과 `import`의 차이

예를 들어 파일 이름이:

```text
main.py
```

라고 합시다.

터미널에서:

```bash
python main.py
```

으로 직접 실행하면:

```python
__name__ == "__main__"
```

입니다.

따라서:

```python
main()
```

이 실행됩니다.

하지만 다른 파일에서:

```python
import main
```

하면:

```python
__name__
```

은 `"main"`과 같은 모듈 이름이 됩니다.

따라서:

```python
if __name__ == "__main__":
```

조건이 거짓이 되어 `main()`이 자동 실행되지 않습니다.

이 구조 덕분에 이 파일을 다른 Python 파일에서 모듈처럼 가져와 사용할 수도 있습니다.

---

# 🧩 111. 프로그램 전체 실행 과정

프로그램을 실행하면 다음과 같은 과정이 진행됩니다.

```text
python main.py
      │
      ▼
main()
      │
      ▼
현재 파일 위치 확인
      │
      ▼
state.json 경로 생성
      │
      ▼
Storage 객체 생성
      │
      ▼
QuizGame 객체 생성
      │
      ▼
load_data()
      │
      ├── state.json 있음
      │       ↓
      │     데이터 읽기
      │
      └── state.json 없음
              ↓
          백업 확인
              ↓
          백업도 없음
              ↓
          기본 퀴즈 생성
      │
      ▼
game.run()
      │
      ▼
메뉴 출력
      │
      ├── 1. 퀴즈 풀기
      │
      ├── 2. 퀴즈 추가
      │
      ├── 3. 퀴즈 목록
      │
      ├── 4. 점수 확인
      │
      └── 5. 종료
```

---

# 💾 112. `state.json`의 역할

프로그램을 종료하면 일반적으로 Python 프로그램의 변수는 사라집니다.

예:

```python
self.best_score = 90
```

프로그램이 종료되면 메모리에서 사라집니다.

그래서 파일에 저장해야 합니다.

이 프로그램에서는:

```text
state.json
```

파일에 데이터를 저장합니다.

예:

```json
{
    "quizzes": [
        {
            "question": "Python에서 문자열 자료형은?",
            "choices": [
                "str",
                "int",
                "list",
                "bool"
            ],
            "answer": 1
        }
    ],
    "best_score": 90
}
```

프로그램을 다시 실행하면 이 데이터를 읽어서 다시 객체로 만듭니다.

---

# 🔄 113. 저장과 복원의 구조

저장할 때:

```text
Quiz 객체
   ↓
to_dict()
   ↓
Python 딕셔너리
   ↓
json.dump()
   ↓
state.json
```

불러올 때:

```text
state.json
   ↓
json.load()
   ↓
Python 딕셔너리
   ↓
Quiz()
   ↓
Quiz 객체
```

즉, 저장과 불러오기는 서로 반대 방향으로 동작합니다.

---

# 🛡️ 114. 백업 시스템

이 프로그램은 데이터를 저장하기 전에 기존 `state.json`을 백업합니다.

예:

```text
state.json
state.json.bak
state.json.20260816_101500.bak
state.json.20260816_102000.bak
state.json.20260816_103000.bak
```

이렇게 여러 개의 백업을 남길 수 있습니다.

---

# 🔧 115. 백업 복구 과정

만약 `state.json`이 손상되었다면:

```text
state.json
     ↓
JSON 읽기 실패
     ↓
백업 파일 검색
     ↓
최신 백업 확인
     ↓
정상적인 JSON인가?
     │
   ┌─┴─┐
   │   │
  YES  NO
   │   │
   ▼   ▼
복구   다음 백업 확인
```

따라서 최신 백업이 손상되어 있어도 다음 백업을 확인할 수 있습니다.

---

# 🧱 116. 객체지향 관점에서 보기

이 프로그램의 가장 중요한 구조는 **역할 분리**입니다.

## `Quiz`

```text
"퀴즈 하나를 어떻게 표현할 것인가?"
```

를 담당합니다.

---

## `Storage`

```text
"데이터를 어떻게 저장하고 불러올 것인가?"
```

를 담당합니다.

---

## `QuizGame`

```text
"게임을 어떻게 진행할 것인가?"
```

를 담당합니다.

---

## `main()`

```text
"프로그램을 어떻게 시작할 것인가?"
```

를 담당합니다.

---

# 📊 117. 클래스 간 관계

```text
                    ┌───────────────┐
                    │     Quiz      │
                    │───────────────│
                    │ question      │
                    │ choices       │
                    │ answer        │
                    └───────▲───────┘
                            │
                            │ 여러 개 사용
                            │
                    ┌───────┴───────┐
                    │   QuizGame    │
                    │───────────────│
                    │ quizzes       │
                    │ best_score    │
                    │ play_quiz()   │
                    │ add_quiz()    │
                    │ run()         │
                    └───────┬───────┘
                            │
                            │ 사용
                            ▼
                    ┌───────────────┐
                    │    Storage    │
                    │───────────────│
                    │ load()        │
                    │ save()        │
                    │ backup        │
                    │ restore       │
                    └───────┬───────┘
                            │
                            ▼
                      ┌───────────┐
                      │state.json │
                      └───────────┘
```

---

# 📚 118. 사용된 Python 문법 정리

이 프로그램에 사용된 주요 Python 문법을 정리하면 다음과 같습니다.

| 문법 | 의미 |
|---|---|
| `import` | 모듈 가져오기 |
| `from ... import ...` | 특정 클래스/함수 가져오기 |
| `class` | 클래스 정의 |
| `def` | 함수/메서드 정의 |
| `self` | 현재 객체 자신 |
| `__init__` | 객체 초기화 메서드 |
| `return` | 결과 반환 |
| `if` | 조건문 |
| `elif` | 추가 조건 |
| `else` | 그 외 조건 |
| `for` | 반복문 |
| `while` | 조건 반복문 |
| `break` | 반복문 종료 |
| `continue` | 현재 반복 건너뛰기 |
| `try` | 예외가 발생할 수 있는 코드 실행 |
| `except` | 예외 처리 |
| `raise` | 직접 예외 발생 |
| `is` | 객체 동일성 비교 |
| `is not` | 객체 동일성이 아님 |
| `==` | 값이 같은지 비교 |
| `>` | 큰지 비교 |
| `<` | 작은지 비교 |
| `or` | 논리 OR |
| `not` | 논리 NOT |
| `+=` | 값에 더하기 |
| `[]` | 리스트/딕셔너리 접근 |
| `{}` | 딕셔너리 |
| `None` | 값이 없음을 나타냄 |
| `lambda` | 익명 함수 |
| `enumerate()` | 순서와 값을 함께 반복 |
| `range()` | 숫자 범위 생성 |
| `isinstance()` | 자료형 확인 |
| `sorted()` | 정렬 |
| `append()` | 리스트에 하나 추가 |
| `extend()` | 리스트에 여러 개 추가 |
| `copy()` | 리스트 복사 |
| `strip()` | 문자열 앞뒤 공백 제거 |

---

# 🧠 119. 핵심 개념 한 번에 정리

이 프로젝트를 공부할 때는 다음 순서로 이해하면 좋습니다.

```text
① 변수
   ↓
② 리스트 / 딕셔너리
   ↓
③ if / elif / else
   ↓
④ for / while
   ↓
⑤ 함수
   ↓
⑥ 클래스
   ↓
⑦ 객체
   ↓
⑧ 메서드
   ↓
⑨ 예외 처리
   ↓
⑩ 파일 입출력
   ↓
⑪ JSON
   ↓
⑫ 클래스 간 역할 분리
   ↓
⑬ 백업 / 복구
```

---

# 🎯 120. 이 프로젝트에서 배울 수 있는 핵심

## ① 클래스

```python
class Quiz:
```

데이터와 기능을 하나의 객체로 묶는 방법을 배울 수 있습니다.

---

## ② 객체

```python
quiz = Quiz(...)
```

클래스를 이용하여 실제 객체를 생성합니다.

---

## ③ 메서드

```python
quiz.display()
quiz.check_answer()
```

객체가 수행할 수 있는 동작을 정의합니다.

---

## ④ 리스트

```python
self.quizzes = []
```

여러 개의 데이터를 저장합니다.

---

## ⑤ 딕셔너리

```python
{
    "question": "...",
    "choices": [...],
    "answer": 1
}
```

키와 값의 형태로 데이터를 관리합니다.

---

## ⑥ 반복문

```python
for quiz in quiz_list:
```

여러 개의 퀴즈를 하나씩 처리합니다.

---

## ⑦ 조건문

```python
if quiz.check_answer(user_answer):
```

정답과 오답을 판단합니다.

---

## ⑧ 예외 처리

```python
try:
    ...
except ValueError:
    ...
```

잘못된 사용자 입력이나 파일 오류에 대응합니다.

---

## ⑨ JSON

```python
json.load()
json.dump()
```

프로그램의 데이터를 파일에 저장하고 다시 불러옵니다.

---

## ⑩ 파일 관리

```python
Path(...)
```

파일 경로를 관리합니다.

---

## ⑪ 백업

```python
shutil.copy2(...)
```

기존 데이터를 백업합니다.

---

## ⑫ 복구

```python
_restore_from_backup()
```

손상된 데이터를 백업으로 복구합니다.

---

# 📝 121. 프로그램 실행 예시

프로그램을 실행하면:

```text
==================================================
               퀴즈 게임
==================================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==================================================
선택:
```

예를 들어 `1`을 입력하면:

```text
==================================================
📝 퀴즈를 시작합니다! (총 8문제)
==================================================

--------------------------------------------------

[문제 1]

Python에서 함수를 정의할 때 사용하는 키워드는?

1. func
2. function
3. def
4. method

정답 입력 (1-4):
```

정답을 입력하면:

```text
✅ 정답입니다!
```

또는:

```text
❌ 오답입니다. 정답은 3번입니다.
```

모든 문제를 풀면:

```text
==================================================
🏆 결과: 8문제 중 7문제 정답! (87점)
==================================================
```

기존 최고 점수보다 높으면:

```text
🎉 새로운 최고 점수입니다!
```

가 출력됩니다.

---

# 📁 122. 프로젝트 파일 구조

권장 프로젝트 구조는 다음과 같습니다.

```text
quiz-game/
│
├── main.py
│
├── state.json
│
├── state.json.bak
│
├── state.json.20260816_101500.bak
│
├── state.json.20260816_102000.bak
│
└── README.md
```

각 파일의 역할:

| 파일 | 역할 |
|---|---|
| `main.py` | Python 퀴즈 게임 프로그램 |
| `state.json` | 현재 퀴즈와 최고 점수 |
| `state.json.bak` | 최근 백업 |
| `state.json.*.bak` | 시간별 백업 |
| `README.md` | 프로젝트 설명 |

---

# ▶️ 123. 실행 방법

Python이 설치되어 있다면 터미널에서 프로젝트 폴더로 이동한 뒤:

~~~~bash
python main.py
~~~~

또는 운영체제 환경에 따라:

~~~~bash
python3 main.py
~~~~

로 실행할 수 있습니다.

---

# 🧪 124. 프로그램 사용 방법

## 1. 퀴즈 풀기

메뉴에서:

```text
1
```

을 선택합니다.

등록된 퀴즈가 무작위 순서로 출제됩니다.

---

## 2. 새로운 퀴즈 추가

메뉴에서:

```text
2
```

를 선택합니다.

다음 순서로 입력합니다.

```text
문제
선택지 1
선택지 2
선택지 3
선택지 4
정답 번호
```

입력이 완료되면 `state.json`에 저장됩니다.

---

## 3. 퀴즈 목록

메뉴에서:

```text
3
```

을 선택합니다.

현재 등록된 모든 퀴즈를 확인할 수 있습니다.

---

## 4. 최고 점수

메뉴에서:

```text
4
```

를 선택합니다.

현재까지 기록된 최고 점수를 확인할 수 있습니다.

---

## 5. 종료

메뉴에서:

```text
5
```

를 선택하면 데이터를 저장하고 프로그램을 종료합니다.

---

# 🛡️ 125. 잘못된 입력 처리

이 프로그램은 사용자가 잘못된 값을 입력해도 프로그램이 바로 종료되지 않도록 만들어져 있습니다.

예를 들어 메뉴에서:

```text
abc
```

를 입력하면:

```text
⚠️ 숫자만 입력해주세요.
```

가 출력됩니다.

범위를 벗어난 숫자를 입력하면:

```text
10
```

다음과 같이 안내합니다.

```text
⚠️ 1-5 사이의 숫자를 입력해주세요.
```

빈 입력도 처리합니다.

```text
⚠️ 입력값이 없습니다. 숫자를 입력해주세요.
```

---

# 🔐 126. 데이터 안정성

이 프로그램은 단순히 JSON 파일에 저장하는 것에서 끝나지 않습니다.

다음과 같은 상황까지 고려합니다.

```text
① state.json이 없음
        ↓
   백업 확인

② state.json이 손상됨
        ↓
   백업 확인

③ 최신 백업도 손상됨
        ↓
   다음 백업 확인

④ 백업도 없음
        ↓
   기본 데이터 사용

⑤ Ctrl+C
        ↓
   데이터 저장 후 종료

⑥ EOFError
        ↓
   데이터 저장 후 종료
```

따라서 단순한 콘솔 게임이지만 파일 데이터의 안정성까지 고려한 구조입니다.

---

# 🧩 127. 이 코드에서 특히 중요한 Python 개념

이 프로젝트를 통해 다음 네 가지 개념을 집중적으로 공부하면 좋습니다.

## 1. 객체지향 프로그래밍

```python
class Quiz:
class Storage:
class QuizGame:
```

각 객체가 자신의 책임을 가지도록 구성했습니다.

---

## 2. 데이터 직렬화

```text
Quiz 객체
    ↓
dict
    ↓
JSON
```

객체 데이터를 파일에 저장할 수 있는 형태로 변환하는 과정입니다.

---

## 3. 예외 처리

```python
try:
    ...
except:
    ...
```

프로그램 실행 중 발생할 수 있는 문제에 대응합니다.

---

## 4. 파일 영속성

프로그램이 종료되어도:

```text
state.json
```

에 데이터가 남기 때문에 다음 실행에서도 이전 상태를 복원할 수 있습니다.

이를 **영속성(Persistence)**이라고 합니다.

---

# 📌 128. 핵심 메서드 요약

## `Quiz`

| 메서드 | 역할 |
|---|---|
| `__init__()` | 퀴즈 객체 초기화 |
| `display()` | 문제와 선택지 출력 |
| `check_answer()` | 정답 여부 확인 |
| `to_dict()` | Quiz 객체를 딕셔너리로 변환 |

---

## `Storage`

| 메서드 | 역할 |
|---|---|
| `__init__()` | 파일 경로 초기화 |
| `_load_file()` | JSON 파일 하나 읽기 |
| `_get_backup_files()` | 백업 목록 가져오기 |
| `_restore_from_backup()` | 백업으로 데이터 복구 |
| `load()` | 저장 데이터 불러오기 |
| `save()` | 데이터 저장 및 백업 |

---

## `QuizGame`

| 메서드 | 역할 |
|---|---|
| `__init__()` | 게임 초기화 |
| `get_default_quizzes()` | 기본 퀴즈 생성 |
| `load_data()` | 저장 데이터 불러오기 |
| `save_data()` | 게임 데이터 저장 |
| `display_menu()` | 메뉴 출력 |
| `get_number()` | 숫자 입력 및 검증 |
| `get_non_empty_input()` | 빈 문자열이 아닌 입력 받기 |
| `play_quiz()` | 퀴즈 진행 |
| `add_quiz()` | 새로운 퀴즈 추가 |
| `show_quizzes()` | 퀴즈 목록 출력 |
| `show_score()` | 최고 점수 출력 |
| `run()` | 메인 게임 루프 |

---

# 🎓 129. 전체 코드에서 기억해야 할 핵심

이 프로그램을 이해할 때 모든 코드를 한 번에 외울 필요는 없습니다.

다음 흐름을 먼저 이해하는 것이 중요합니다.

```text
Quiz
│
├── 문제를 저장한다.
├── 선택지를 저장한다.
├── 정답을 저장한다.
├── 문제를 출력한다.
└── 정답을 확인한다.


Storage
│
├── JSON을 읽는다.
├── JSON을 저장한다.
├── 기존 데이터를 백업한다.
└── 문제가 생기면 백업에서 복구한다.


QuizGame
│
├── Quiz를 여러 개 관리한다.
├── Storage를 사용한다.
├── 사용자의 입력을 받는다.
├── 퀴즈를 진행한다.
├── 점수를 계산한다.
└── 메뉴를 관리한다.


main()
│
├── Storage 생성
├── QuizGame 생성
└── 게임 실행
```

결국 이 프로그램의 핵심 구조는 다음 한 문장으로 정리할 수 있습니다.

> **`Quiz`는 문제를 관리하고, `Storage`는 데이터를 관리하며, `QuizGame`은 게임을 관리하고, `main()`은 프로그램을 시작한다.**

이렇게 각 클래스와 함수가 자신의 역할을 나누어 담당하기 때문에 코드가 길어져도 전체 구조를 이해하고 유지보수하기 쉬워집니다.


## Git
```
% git log --oneline --graph --all
* a401847 Fix
* 4e0ef1a Fix
* a1e3103 Fix
*   abb363f Fix
|\  
| *   ef12e8d Merge pull request #1 from codyjourney/feature/play-quiz
| |\  
* | | 73acf10 Fix
* | | bb1be64 README
* | | a6a5fdb Fix: 잘못된 입력과 JSON 파일 오류 처리
* | | 0046818 Feat: state.json 데이터 저장 및 불러오기 구현
* | | d452a7a Feat: 최고 점수 확인 및 갱신 기능 구현
* | | 9d9c197 Feat: 등록된 퀴즈 목록 조회 기능 구현
* | | 15fa49a Feat: 사용자 퀴즈 추가 기능 구현
* | | ed41239 Feat: 등록된 퀴즈 목록 조회 기능 구현
* | | e890cec Feat: 사용자 퀴즈 추가 기능 구현
| |/  
|/|   
* | bb7645f (origin/feature/play-quiz) Feat: 퀴즈 랜덤 출제와 점수 계산 기능 추가
* | bebf084 Feat: 퀴즈 출제 및 정답 확인 기능 구현
* | 927164d Feat: 기본 퀴즈 데이터 추가
* | 0afe520 Feat: Quiz 클래스와 정답 확인 기능 구현
* | 462235b Feat: 메인 메뉴 및 종료 기능 구현
|/  
* 484a4f0 Init: 퀴즈 게임 프로젝트 초기 설정
* 107927e Chore: gitignore 설정
~
```


# Git Commit Type 설명

Git 커밋 메시지에서 사용하는 `fix`, `feat`, `init`, `chore`는  
**커밋에서 어떤 작업을 했는지 나타내는 접두어**입니다.

## 1. `feat` — 새로운 기능 추가

**Feature**의 줄임말입니다.

새로운 기능을 구현했을 때 사용합니다.

```text
Feat: 사용자 퀴즈 추가 기능 구현
Feat: 퀴즈 랜덤 출제 기능 추가
Feat: 최고 점수 확인 기능 구현
```

### 예시

```text
feat: 로그인 기능 추가
```

→ 기존에는 없던 로그인 기능을 새롭게 추가했다는 의미입니다.

---

## 2. `fix` — 버그 수정

**Fix**의 줄임말입니다.

기존 기능에 문제가 있어서 수정했을 때 사용합니다.

```text
Fix: 잘못된 입력 처리
Fix: JSON 파일 오류 처리
Fix: 점수가 제대로 저장되지 않는 문제 수정
```

### 예시

```text
fix: 잘못된 입력으로 프로그램이 종료되는 문제 수정
```

→ 기존에 있던 기능의 오류를 고쳤다는 의미입니다.

### `feat`와 `fix`의 차이

```text
새로운 기능을 추가했다 → feat

기존 기능의 문제를 수정했다 → fix
```

---

## 3. `init` — 프로젝트 초기 설정

**Initialize**의 줄임말입니다.

프로젝트를 처음 만들면서 기본적인 환경이나 구조를 설정할 때 사용합니다.

```text
Init: 퀴즈 게임 프로젝트 초기 설정
```

예를 들어:

```text
init: 프로젝트 초기 설정
init: 기본 디렉터리 구조 생성
init: 기본 설정 파일 추가
```

> `init`은 Conventional Commits의 필수/표준 타입이라기보다는  
> 프로젝트에서 관습적으로 사용하는 표현입니다.

---

## 4. `chore` — 기타 관리 작업

기능 추가나 버그 수정에는 해당하지 않지만  
프로젝트 관리에 필요한 작업을 의미합니다.

```text
Chore: gitignore 설정
Chore: 의존성 업데이트
Chore: 개발 환경 설정 변경
```

### 예시

```text
chore: .gitignore 파일 추가
```

→ 사용자 기능이나 버그 수정과는 관계없이 프로젝트 설정을 변경한 것입니다.

---

## 한눈에 비교

| Type | 의미 | 예시 |
|---|---|---|
| `feat` | 새로운 기능 | `feat: 로그인 기능 추가` |
| `fix` | 버그 수정 | `fix: 로그인 오류 수정` |
| `init` | 프로젝트 초기 설정 | `init: 프로젝트 초기 설정` |
| `chore` | 기타 관리 작업 | `chore: .gitignore 추가` |

---

## 자주 사용하는 다른 타입

Conventional Commits에서는 다음과 같은 타입도 많이 사용합니다.

```text
feat      새로운 기능 추가
fix       버그 수정
docs      문서 수정
style     코드 스타일 수정
refactor  코드 구조 개선
test      테스트 추가/수정
chore     기타 관리 작업
```

### 쉽게 기억하기

```text
feat     → 기능 만들기
fix      → 문제 고치기
docs     → 문서 수정하기
refactor → 코드 정리하기
test     → 테스트하기
chore    → 기타 작업하기
init     → 프로젝트 시작하기
```


## JSON을 사용하는 이유

JSON은 구조가 단순하고 경량인 데이터 포맷이며, 사람이 읽고 수정하기 쉬워 설정값이나 소규모 데이터를 저장하고 교환하는 데 적합하다.

### JSON과 XML 비교

JSON은 XML에 비해 문법이 간결하고 불필요한 태그가 적어 같은 데이터를 표현할 때 데이터 크기가 작다. 또한 JavaScript 등 다양한 프로그래밍 언어에서 쉽게 처리할 수 있다. 반면 XML은 속성, 네임스페이스, 스키마 등을 활용해 복잡하고 정형화된 문서 구조를 표현하는 데 유리하다.

### JSON과 DB의 속도 차이

소규모 데이터에서는 JSON 파일을 사용하는 것이 간단하고 충분히 빠를 수 있지만, 데이터가 많아지면 데이터베이스보다 느려질 수 있다.

JSON 파일은 특정 데이터를 검색하거나 수정할 때 파일 전체를 읽어야 하는 경우가 많다. 또한 수정 후에는 전체 파일을 다시 저장해야 할 수 있어 데이터가 커질수록 디스크 I/O와 처리 시간이 증가한다.

반면 데이터베이스는 인덱스를 이용해 필요한 데이터만 빠르게 검색할 수 있고, 데이터를 페이지 단위로 관리하며 쿼리 최적화와 캐싱 등의 기능을 제공한다. 따라서 대량의 데이터를 반복적으로 검색·수정해야 하는 경우에는 JSON 파일보다 DB가 일반적으로 효율적이다.

즉, **JSON은 가볍고 사용하기 쉬운 소규모 데이터 저장에 적합하고, 대량 데이터의 빠른 검색과 관리를 위해서는 데이터베이스를 사용하는 것이 적합하다.**



## 브랜치와 병합

브랜치는 하나의 프로젝트에서 기능별로 작업을 분리하여 개발하기 위해 사용한다. 각 기능을 독립적인 브랜치에서 작업하면 기존 코드에 영향을 최소화하면서 개발하고 테스트할 수 있다.

병합(Merge)은 기능 개발이 완료된 브랜치의 변경 사항을 다른 브랜치(예: `main`)에 합치는 과정이다. 즉, **브랜치는 기능을 독립적으로 개발하기 위한 수단이고, 병합은 완료된 기능을 하나의 프로젝트에 통합하는 과정**이다.



## JSON 데이터 백업 및 복원

프로그램에서는 `state.json`을 저장할 때 기존 데이터를 바로 덮어쓰지 않고 백업하여 데이터 손실에 대비합니다.

### 백업 정책

`state.json`을 새 데이터로 저장하기 전에 기존 파일을 다음과 같이 백업합니다.

- `state.json.bak`
  - 가장 최근의 정상 데이터를 저장하는 백업 파일입니다.
- `state.json.YYYYMMDD_HHMMSS.bak`
  - 저장 시점의 날짜와 시간을 포함한 백업 파일입니다.
  - 예: `state.json.20260815_160300.bak`

따라서 새로운 데이터를 저장하는 과정에서 문제가 발생하더라도 이전 데이터를 이용하여 복원할 수 있습니다.

### 손상 데이터 복원 절차

`state.json`을 불러오는 과정에서 JSON 형식 오류나 필수 데이터 누락이 발견되면 다음 순서로 복구합니다.

1. `state.json`의 손상 여부를 확인합니다.
2. 손상된 경우 백업 파일 목록을 확인합니다.
3. 가장 최근의 백업 파일부터 JSON 형식이 정상인지 검사합니다.
4. 정상적인 백업 파일을 찾으면 해당 데이터를 `state.json`으로 복원합니다.
5. 사용할 수 있는 백업이 하나도 없는 경우 기본 퀴즈 데이터로 초기화합니다.

즉, **`state.json` → 최신 백업 → 이전 타임스탬프 백업 → 기본 데이터** 순서로 복구를 시도합니다.

이러한 백업 정책을 통해 JSON 파일이 손상되더라도 기존 퀴즈와 최고 점수를 최대한 보존할 수 있습니다.

```text
state.json 손상
    ↓
state.json.bak 확인
    ↓
타임스탬프 백업 확인
    ↓
정상 백업 발견 → state.json 복원
    ↓
모든 백업 손상/없음
    ↓
기본 데이터로 초기화
```


### Git 10
```text
git rev-list --all --count
38
```




# Python 코드에 사용된 클래스, 메소드, 문법 및 명령어 설명

이 문서는 Python 코드에 등장하는 주요 클래스, 메소드, 문법 및 명령어를 처음 Python을 배우는 사람도 이해할 수 있도록 쉽게 설명합니다.

## 1\. `pathlib.Path`

`pathlib.Path`는 ****파일이나 폴더의 경로를 다루기 위한 클래스****입니다.

Python에서는 파일 경로를 문자열로 직접 다룰 수도 있습니다.

file\_path = "data/state.json"  

하지만 `pathlib.Path`를 사용하면 파일과 폴더를 훨씬 편리하게 다룰 수 있습니다.

from pathlib import Path  
  
file\_path = Path("data/state.json")  

이제 `file_path`는 단순한 문자열이 아니라 ****파일 경로를 다루는 Path 객체****가 됩니다.

### 예시

from pathlib import Path  
  
file\_path = Path("data/state.json")  
  
print(file\_path)  

결과:

data/state.json  

### 폴더와 파일을 합치기

data\_dir = Path("data")  
file\_path = data\_dir / "state.json"  

결과적으로:

data/state.json  

가 됩니다.

`/` 연산자를 사용해서 경로를 연결할 수 있다는 것이 `Path`의 큰 장점입니다.

문자열로 작성하면:

file\_path = "data/" + "state.json"  

처럼 작성해야 하지만, `Path`를 사용하면:

file\_path = Path("data") / "state.json"  

처럼 작성할 수 있습니다.

### 자주 사용하는 `Path` 메소드

#### `exists()`

파일이나 폴더가 실제로 존재하는지 확인합니다.

file\_path.exists()  

존재하면:

True  

존재하지 않으면:

False  

를 반환합니다.

#### `is_file()`

해당 경로가 파일인지 확인합니다.

file\_path.is\_file()  

#### `is_dir()`

해당 경로가 폴더인지 확인합니다.

file\_path.is\_dir()  

#### `mkdir()`

폴더를 생성합니다.

data\_dir.mkdir()  

부모 폴더까지 함께 만들고 싶다면:

data\_dir.mkdir(parents=True, exist\_ok=True)  

-   `parents=True` : 필요한 상위 폴더도 함께 생성
-   `exist_ok=True` : 이미 폴더가 있어도 오류를 발생시키지 않음

# 2\. 리스트 컴프리헨션(List Comprehension)

리스트 컴프리헨션은 ****반복문을 사용해서 새로운 리스트를 간단하게 만드는 Python 문법****입니다.

일반적인 `for`문으로 작성하면:

numbers = \[\]  
  
for i in range(5):  
    numbers.append(i)  

결과:

\[0, 1, 2, 3, 4\]  

리스트 컴프리헨션을 사용하면 훨씬 짧게 작성할 수 있습니다.

numbers = \[i for i in range(5)\]  

결과는 동일합니다.

\[0, 1, 2, 3, 4\]  

## 조건을 사용할 수도 있습니다.

예를 들어 짝수만 가져오고 싶다면:

numbers = \[i for i in range(10) if i % 2 == 0\]  

결과:

\[0, 2, 4, 6, 8\]  

구조를 이해하면 다음과 같습니다.

\[표현식 for 변수 in 반복할\_대상 if 조건\]  

예:

\[i for i in range(10) if i % 2 == 0\]  

의 의미는:

> `0`부터 `9`까지 반복하면서 짝수인 값만 리스트에 넣어라.

입니다.

# 3\. `lambda`

`lambda`는 ****이름이 없는 간단한 함수를 한 줄로 만드는 문법****입니다.

일반적인 함수를 만들면:

def add(a, b):  
    return a + b  

`lambda`를 사용하면:

add = lambda a, b: a + b  

처럼 작성할 수 있습니다.

두 코드 모두 다음과 같이 사용할 수 있습니다.

print(add(10, 20))  

결과:

30  

## `lambda`의 기본 구조

lambda 매개변수: 반환할\_값  

예:

lambda x: x \* 2  

의 의미는:

> x를 전달받아서 x × 2를 반환하는 작은 함수

입니다.

## `sorted()`에서 사용하는 `lambda`

다음 코드를 살펴보겠습니다.

return sorted(  
    backup\_files,  
    key=lambda path: path.stat().st\_mtime,  
    reverse=True  
)  

여기서:

key=lambda path: path.stat().st\_mtime  

는 각 파일의 ****수정 시간****을 기준으로 정렬하겠다는 의미입니다.

즉:

파일 A → 수정 시간 확인  
파일 B → 수정 시간 확인  
파일 C → 수정 시간 확인  
...  

한 후 수정 시간을 기준으로 정렬합니다.

`reverse=True`이므로 큰 값부터 정렬합니다.

따라서 결과적으로 ****가장 최근에 수정된 파일이 먼저 나오게 됩니다.****

# 4\. `KeyboardInterrupt`

`KeyboardInterrupt`는 사용자가 프로그램을 실행하는 도중 ****키보드로 강제 중단했을 때 발생하는 예외****입니다.

일반적으로 터미널에서:

Ctrl + C  

를 누르면 발생합니다.

예를 들어:

while True:  
    print("실행 중...")  

이 프로그램은 계속 실행됩니다.

사용자가 `Ctrl + C`를 누르면 Python은:

KeyboardInterrupt  

를 발생시킵니다.

이를 `try-except`로 처리할 수도 있습니다.

try:  
    while True:  
        print("실행 중...")  
except KeyboardInterrupt:  
    print("프로그램을 종료합니다.")  

이렇게 하면 사용자가 `Ctrl + C`를 눌렀을 때 프로그램을 깔끔하게 종료할 수 있습니다.

# 5\. `EOFError`

`EOFError`는 주로 `input()`을 사용하고 있을 때 ****입력의 끝(EOF)을 만났을 경우 발생하는 예외****입니다.

EOF는:

End Of File  

의 약자입니다.

쉽게 말하면:

> 더 이상 입력할 데이터가 없는데 프로그램이 입력을 기다리고 있는 상황

이라고 이해하면 됩니다.

예를 들어:

try:  
    value = input("입력하세요: ")  
except EOFError:  
    print("입력이 종료되었습니다.")  

이런 방식으로 처리할 수 있습니다.

특히 터미널에서 입력을 받는 프로그램이나, 파일/파이프 등을 통해 입력을 전달받는 프로그램에서 발생할 수 있습니다.

# 6\. `datetime.now().strftime()`

다음 코드를 살펴보겠습니다.

timestamp = datetime.now().strftime(  
    "%Y%m%d\_%H%M%S"  
)  

이 코드는 ****현재 날짜와 시간을 가져와서 원하는 형식의 문자열로 만드는 코드****입니다.

먼저:

datetime.now()  

는 현재 날짜와 시간을 가져옵니다.

예를 들어:

2026-08-16 11:30:25.123456  

와 같은 값이 될 수 있습니다.

그 다음:

.strftime(...)  

를 사용하면 날짜와 시간의 표시 형식을 원하는 형태로 바꿀 수 있습니다.

예:

datetime.now().strftime("%Y%m%d\_%H%M%S")  

결과:

20260816\_113025  

이런 형태의 문자열을 만들 수 있습니다.

## 자주 사용하는 형식

| 코드 | 의미     | 예    |
| -- | ------ | ---- |
| %Y | 4자리 연도 | 2026 |
| %m | 2자리 월  | 08   |
| %d | 2자리 일  | 16   |
| %H | 시      | 11   |
| %M | 분      | 30   |
| %S | 초      | 25   |

예를 들어:

strftime("%Y-%m-%d %H:%M:%S")  

결과:

2026-08-16 11:30:25  

이런 방식으로 백업 파일 이름에 날짜와 시간을 넣을 때 매우 유용합니다.

예:

backup\_20260816\_113025.json  

# 7\. Python에서 `_`의 의미

Python에서 `_`는 여러 가지 용도로 사용됩니다.

특히 클래스나 메소드 이름 앞에 `_`가 붙는 경우가 중요합니다.

예:

def \_load\_state(self):  
    ...  

이 메소드 이름 앞의 `_`는 일반적으로:

> 이 메소드는 클래스 내부에서 주로 사용하는 메소드입니다.

라는 의도를 표현합니다.

즉:

\_load\_state  

라고 이름을 지으면 다른 개발자에게:

> 이 메소드는 외부에서 직접 사용하기보다는 클래스 내부에서 사용하는 것이 좋습니다.

라는 의미를 전달합니다.

### 중요한 점

Python이 `_`가 붙은 메소드에 대한 접근을 ****강제로 막는 것은 아닙니다.****

예를 들어:

class Example:  
    def \_hello(self):  
        print("Hello")  

다음과 같이 호출할 수도 있습니다.

example = Example()  
example.\_hello()  

실제로 실행됩니다.

따라서 `_`는:

접근 금지  

가 아니라:

내부적으로 사용하는 메소드라는 개발자 간의 약속  

에 가깝습니다.

# 8\. `with`

`with`는 파일이나 기타 자원을 사용할 때 ****사용이 끝난 후 자동으로 정리하도록 해주는 문법****입니다.

파일을 직접 열고 닫으면:

file = open("state.json", "r")  
  
data = file.read()  
  
file.close()  

처럼 작성해야 합니다.

하지만 `with`를 사용하면:

with open("state.json", "r") as file:  
    data = file.read()  

처럼 작성할 수 있습니다.

파일을 사용한 후 Python이 파일을 자동으로 닫아줍니다.

## `Path.open()`과 함께 사용하는 경우

다음과 같은 코드도 자주 사용합니다.

with file\_path.open(  
    "r",  
    encoding="utf-8"  
) as file:  
    data = file.read()  

여기서:

file\_path.open()  

은 해당 경로의 파일을 여는 메소드입니다.

"r"  

은 읽기 모드입니다.

encoding="utf-8"  

은 파일을 UTF-8 방식으로 읽겠다는 의미입니다.

그리고:

as file  

을 통해 열린 파일을 `file`이라는 변수로 사용할 수 있습니다.

# 9\. 파일을 닫지 않으면 어떻게 될까?

파일을 열었다면 사용이 끝난 후 닫아주는 것이 중요합니다.

file = open("state.json", "r")  
  
data = file.read()  
  
file.close()  

파일을 닫지 않으면 다음과 같은 문제가 발생할 수 있습니다.

-   사용하지 않는 파일 핸들이 계속 남을 수 있습니다.
-   많은 파일을 열면 시스템의 파일 리소스를 소모할 수 있습니다.
-   쓰기 작업의 경우 데이터가 제대로 저장되지 않는 문제가 발생할 수 있습니다.
-   프로그램이 예상하지 못한 상태로 동작할 수 있습니다.

따라서 가능하면 다음처럼 `with`를 사용하는 것이 좋습니다.

with open("state.json", "r", encoding="utf-8") as file:  
    data = file.read()  

`with`를 사용하면 예외가 발생하더라도 파일을 정리하는 데 유리합니다.

# 10\. `raise ValueError()`

`raise`는 ****개발자가 직접 예외를 발생시키는 명령어****입니다.

예를 들어:

raise ValueError("잘못된 값입니다.")  

라고 작성하면 Python이 의도적으로 `ValueError`를 발생시킵니다.

## `ValueError`란?

`ValueError`는 ****자료형 자체는 올바르지만 값이 잘못되었을 때 사용하는 예외****입니다.

예:

age = -10  
  
if age < 0:  
    raise ValueError("나이는 0보다 작을 수 없습니다.")  

여기서 `age`는 숫자이므로 자료형은 문제가 없습니다.

하지만:

\-10  

이라는 값은 프로그램에서 허용하지 않으므로 `ValueError`를 발생시키는 것입니다.

## `raise`를 사용하는 이유

프로그램에서 문제가 발생했는데도 계속 실행하도록 놔두면 나중에 더 큰 문제가 발생할 수 있습니다.

따라서:

if not valid:  
    raise ValueError("잘못된 데이터입니다.")  

처럼 ****문제가 발생한 지점에서 즉시 알려주는 것****이 좋습니다.

# 11\. `glob()`

`glob()`은 특정 패턴에 맞는 ****파일들을 찾아주는 기능****입니다.

`pathlib.Path`에서도 사용할 수 있습니다.

예:

backup\_files = list(data\_dir.glob("\*.json"))  

여기서:

\*.json  

은:

> 확장자가 `.json`인 모든 파일

이라는 의미입니다.

예를 들어 폴더에:

state.json  
backup.json  
config.json  
readme.txt  

가 있다면:

data\_dir.glob("\*.json")  

은 다음 파일들을 찾습니다.

state.json  
backup.json  
config.json  

하지만:

readme.txt  

는 찾지 않습니다.

## `*`의 의미

`*`는 여러 문자를 의미합니다.

\*.json  

은:

아무 이름.json  

이라는 의미입니다.

예:

a.json  
state.json  
backup\_20260816.json  

모두 해당합니다.

# 12\. `append()`와 `extend()`의 차이

둘 다 리스트에 데이터를 추가하는 메소드지만 ****추가하는 방식이 다릅니다.****

## `append()`

`append()`는 ****하나의 항목을 리스트의 마지막에 추가****합니다.

numbers = \[1, 2, 3\]  
  
numbers.append(4)  

결과:

\[1, 2, 3, 4\]  

리스트 자체를 추가할 수도 있습니다.

numbers = \[1, 2, 3\]  
  
numbers.append(\[4, 5\])  

결과:

\[1, 2, 3, \[4, 5\]\]  

즉, 리스트 `[4, 5]` 자체가 하나의 항목으로 추가됩니다.

## `extend()`

`extend()`는 다른 리스트의 ****각 항목을 하나씩 꺼내서 추가****합니다.

numbers = \[1, 2, 3\]  
  
numbers.extend(\[4, 5\])  

결과:

\[1, 2, 3, 4, 5\]  

### 비교

numbers = \[1, 2, 3\]  
  
numbers.append(\[4, 5\])  

결과:

\[1, 2, 3, \[4, 5\]\]  

반면:

numbers = \[1, 2, 3\]  
  
numbers.extend(\[4, 5\])  

결과:

\[1, 2, 3, 4, 5\]  

### 쉽게 기억하기

append  → 리스트 안에 하나 추가  
extend  → 리스트의 내용을 펼쳐서 추가  

# 13\. `sorted()`

`sorted()`는 데이터를 ****정렬해서 새로운 리스트로 반환하는 Python 내장 함수****입니다.

예:

numbers = \[3, 1, 5, 2\]  
  
result = sorted(numbers)  

결과:

\[1, 2, 3, 5\]  

원래 리스트는 그대로 유지됩니다.

numbers = \[3, 1, 5, 2\]  
  
result = sorted(numbers)  
  
print(numbers)  
print(result)  

결과:

\[3, 1, 5, 2\]  
\[1, 2, 3, 5\]  

# 14\. `sorted()`의 `key`

`sorted()`에서 `key`를 사용하면 ****무엇을 기준으로 정렬할지 지정할 수 있습니다.****

예:

sorted(  
    backup\_files,  
    key=lambda path: path.stat().st\_mtime  
)  

여기서는 파일 자체를 직접 비교하는 것이 아니라:

path.stat().st\_mtime  

값을 기준으로 정렬합니다.

즉:

파일 → 수정 시간 가져오기 → 수정 시간을 기준으로 정렬  

이라는 과정입니다.

# 15\. `path.stat()`

`Path` 객체에서:

path.stat()  

을 호출하면 해당 파일의 \*\*파일 정보(metadata)\*\*를 가져옵니다.

예를 들어 파일 크기나 수정 시간 등의 정보를 확인할 수 있습니다.

info = path.stat()  

그 결과에서:

info.st\_size  

는 파일 크기를 의미합니다.

그리고:

info.st\_mtime  

는 파일이 마지막으로 수정된 시간을 나타냅니다.

# 16\. `st_mtime`

`st_mtime`은 ****파일이 마지막으로 수정된 시각****을 나타냅니다.

예:

path.stat().st\_mtime  

이 값을 사용하면 여러 파일을:

가장 오래된 파일  
↓  
...  
↓  
가장 최근에 수정된 파일  

순서로 정렬할 수 있습니다.

# 17\. `reverse=True`

`sorted()`는 기본적으로 오름차순으로 정렬합니다.

sorted(\[3, 1, 2\])  

결과:

\[1, 2, 3\]  

반대로 큰 값부터 정렬하고 싶다면:

sorted(\[3, 1, 2\], reverse=True)  

결과:

\[3, 2, 1\]  

따라서:

return sorted(  
    backup\_files,  
    key=lambda path: path.stat().st\_mtime,  
    reverse=True  
)  

는:

> 백업 파일들을 마지막 수정 시간을 기준으로 정렬하되, 가장 최근 파일부터 반환한다.

라는 의미입니다.

# 18\. `json.dump()`

`json.dump()`는 ****Python 데이터를 JSON 형식으로 파일에 저장할 때 사용하는 함수****입니다.

예:

json.dump(  
    data,  
    file,  
    ensure\_ascii=False,  
    indent=4  
)  

여기서 각각의 의미는 다음과 같습니다.

## `data`

저장할 Python 데이터입니다.

예:

data = {  
    "name": "홍길동",  
    "age": 20  
}  

## `file`

JSON을 저장할 파일 객체입니다.

예:

with open("state.json", "w", encoding="utf-8") as file:  
    json.dump(data, file)  

## `ensure_ascii=False`

한글과 같은 Unicode 문자를 그대로 저장하기 위한 옵션입니다.

ensure\_ascii=False  

를 사용하면:

{  
    "name": "홍길동"  
}  

처럼 한글을 그대로 저장할 수 있습니다.

반대로 설정하지 않으면 Unicode 문자가 escape 형태로 저장될 수 있습니다.

ensure_ascii=False → 한글, 일본어, 이모지 등의 유니코드 문자를 \uXXXX로 바꾸지 않고 그대로 표시

## `indent=4`

JSON 파일을 보기 좋게 들여쓰기합니다.

indent=4  

를 사용하면:

{  
    "name": "홍길동",  
    "age": 20  
}  

처럼 사람이 읽기 편하게 저장됩니다.

# 19\. `shutil.copy2()`

`shutil.copy2()`는 ****파일을 다른 위치로 복사하는 함수****입니다.

예:

shutil.copy2(  
    source,  
    destination  
)  

의 의미는:

> source 파일을 destination 위치로 복사해라.

입니다.

예:

import shutil  
  
shutil.copy2(  
    "state.json",  
    "backup/state.json"  
)  

이렇게 하면:

state.json  

파일을:

backup/state.json  

으로 복사합니다.

## `copy()`와 `copy2()`의 차이

둘 다 파일을 복사하지만 `copy2()`는 파일의 ****메타데이터도 가능한 범위에서 함께 보존****합니다.

따라서 백업 프로그램에서는 `copy2()`가 유용할 수 있습니다.

# 20\. `strftime()`

`strftime()`은 날짜와 시간 객체를 ****문자열로 변환하면서 원하는 형식으로 표시하는 메소드****입니다 string format time.

예:

now.strftime("%Y-%m-%d")  

결과:

2026-08-16  

시간까지 포함하면:

now.strftime("%Y-%m-%d %H:%M:%S")  

결과:

2026-08-16 11:30:25  

특히 파일 이름을 만들 때 유용합니다.

예:

timestamp = datetime.now().strftime("%Y%m%d\_%H%M%S")  

결과:

20260816\_113025  

따라서:

backup\_filename = f"backup\_{timestamp}.json"  

처럼 사용하면:

backup\_20260816\_113025.json  

같은 파일 이름을 만들 수 있습니다.

# 21\. `f-string`

위의 예제에서 사용한:

f"backup\_{timestamp}.json"  

은 Python의 ****f-string**** 문법입니다.

문자열 앞에:

f  

를 붙이면 문자열 안에 변수의 값을 쉽게 넣을 수 있습니다.

예:

name = "홍길동"  
  
message = f"안녕하세요, {name}님"  

결과:

안녕하세요, 홍길동님  

따라서:

timestamp = "20260816\_113025"  
  
filename = f"backup\_{timestamp}.json"  

결과:

backup\_20260816\_113025.json  

이 됩니다.

# 22\. 전체 코드에서 서로 어떻게 연결되는가?

지금까지 설명한 기능들은 파일 백업 프로그램에서 서로 연결해서 사용할 수 있습니다.

예를 들어:

from datetime import datetime  
from pathlib import Path  
import shutil  
  
data\_dir = Path("data")  
backup\_dir = Path("backup")  
  
backup\_dir.mkdir(parents=True, exist\_ok=True)  
  
backup\_files = list(data\_dir.glob("\*.json"))  
  
timestamp = datetime.now().strftime("%Y%m%d\_%H%M%S")  
  
for file\_path in backup\_files:  
    backup\_path = backup\_dir / f"{file\_path.stem}\_{timestamp}.json"  
  
    shutil.copy2(  
        file\_path,  
        backup\_path  
    )  

이 코드를 순서대로 해석하면 다음과 같습니다.

### ① `Path`

data\_dir = Path("data")  
backup\_dir = Path("backup")  

`data`와 `backup`이라는 폴더의 경로를 만듭니다.

### ② `mkdir()`

backup\_dir.mkdir(parents=True, exist\_ok=True)  

백업 폴더가 없으면 생성합니다.

### ③ `glob()`

backup\_files = list(data\_dir.glob("\*.json"))  

`data` 폴더 안에서 `.json` 파일을 찾습니다. global.

### ④ `datetime.now()`

datetime.now()  

현재 날짜와 시간을 가져옵니다.

### ⑤ `strftime()`

strftime("%Y%m%d\_%H%M%S")  

현재 시간을 파일 이름에 넣기 좋은 문자열로 변환합니다.

예:

20260816\_113025  

### ⑥ `for`

for file\_path in backup\_files:  

찾은 JSON 파일들을 하나씩 처리합니다.

### ⑦ `shutil.copy2()`

shutil.copy2(  
    file\_path,  
    backup\_path  
)  

원본 파일을 백업 폴더로 복사합니다.

# 23\. 핵심 문법 한눈에 보기

| 문법 / 기능            | 쉽게 말하면                      |
| ------------------ | --------------------------- |
| Path               | 파일과 폴더의 경로를 다루는 객체          |
| glob()             | 특정 패턴의 파일을 찾기               |
| mkdir()            | 폴더 만들기                      |
| exists()           | 파일/폴더가 존재하는지 확인             |
| is_file()          | 파일인지 확인                     |
| is_dir()           | 폴더인지 확인                     |
| 리스트 컴프리헨션          | 반복문으로 리스트를 간단하게 만들기         |
| lambda             | 이름 없는 간단한 함수 만들기            |
| KeyboardInterrupt  | Ctrl + C 등으로 프로그램을 중단할 때 발생 |
| EOFError           | 입력의 끝(EOF)을 만났을 때 발생        |
| datetime.now()     | 현재 날짜와 시간 가져오기              |
| strftime()         | 날짜/시간을 원하는 문자열로 변환          |
| _                  | 내부용이라는 의도를 나타내는 관례          |
| with               | 작업이 끝난 후 자원을 자동으로 정리        |
| raise              | 의도적으로 예외 발생시키기              |
| ValueError         | 값이 잘못되었을 때 발생하는 예외          |
| append()           | 리스트에 항목 하나 추가               |
| extend()           | 다른 리스트의 항목들을 하나씩 추가         |
| sorted()           | 데이터를 정렬해서 새로운 리스트 반환        |
| key                | 정렬할 때 어떤 값을 기준으로 할지 지정      |
| reverse=True       | 내림차순으로 정렬                   |
| stat()             | 파일의 정보 가져오기                 |
| st_mtime           | 파일의 마지막 수정 시간               |
| json.dump()        | Python 데이터를 JSON 파일로 저장     |
| ensure_ascii=False | 한글 등을 그대로 저장                |
| indent=4           | JSON을 보기 좋게 들여쓰기            |
| shutil.copy2()     | 파일을 복사하면서 메타데이터도 보존         |
| f-string           | 문자열 안에 변수 값을 쉽게 넣기          |

# 24\. 가장 중요한 부분만 쉽게 기억하기

Python 파일 처리 코드를 볼 때 다음 정도를 기억하면 코드를 이해하는 데 큰 도움이 됩니다.

Path  

→ 파일이나 폴더의 위치를 다룬다.

glob()  

→ 원하는 파일을 찾는다.

with  

→ 파일을 안전하게 사용한다.

append()  

→ 하나를 추가한다.

extend()  

→ 여러 개를 펼쳐서 추가한다.

lambda  

→ 간단한 함수를 한 줄로 만든다.

sorted()  

→ 정렬한다.

key=lambda ...  

→ 무엇을 기준으로 정렬할지 정한다.

reverse=True  

→ 큰 값부터 정렬한다.

stat().st\_mtime  

→ 파일이 마지막으로 수정된 시간을 가져온다.

json.dump()  

→ 데이터를 JSON 파일에 저장한다.

shutil.copy2()  

→ 파일을 복사한다.

strftime()  

→ 날짜와 시간을 원하는 문자열로 만든다.

raise ValueError()  

→ 잘못된 값이라고 판단하면 직접 오류를 발생시킨다.

KeyboardInterrupt  

→ 사용자가 프로그램을 강제로 중단했을 때 처리한다.

EOFError  

→ 입력이 끝났을 때 발생하는 오류를 처리한다.

그리고 메소드 이름 앞의:

\_  

는 보통:

> "이것은 클래스 내부에서 사용하는 용도의 메소드입니다."

라는 개발자의 의도를 나타내는 ****관례****이며, Python이 접근 자체를 강제로 차단하는 것은 아닙니다.


## `path.stat()`

`pathlib.Path`의 `stat()` 메서드를 호출하면 해당 파일의 **파일 정보(metadata)**를 가져옵니다.

예를 들어 파일 크기나 수정 시간 등의 정보를 확인할 수 있습니다.

```python
from pathlib import Path

path = Path("test.txt")

info = path.stat()

print(info.st_size)   # 파일 크기
print(info.st_mtime)  # 마지막 수정 시각
```

### `st_size`

`info.st_size`는 **파일 크기**를 의미합니다.

```python
info = path.stat()

print(info.st_size)
```

### `st_mtime`

`st_mtime`은 **파일이 마지막으로 수정된 시각**을 나타냅니다.

```python
path.stat().st_mtime
```

이 값을 사용하면 여러 파일을 **수정된 시각을 기준으로 정렬**할 수 있습니다.

```python
files = sorted(files, key=lambda path: path.stat().st_mtime)
```

이렇게 하면:

```text
가장 오래된 파일
↓
...
↓
가장 최근에 수정된 파일
```

순서로 정렬됩니다.

---

## `pathlib.Path`에만 해당하는가?

아닙니다.

**`st_mtime` 자체는 `pathlib.Path`에만 해당하는 것이 아닙니다.**

`Path.stat()`은 운영체제의 **파일 상태 정보(stat result)**를 가져오는 방법 중 하나입니다.

### `pathlib.Path`에서 사용

```python
from pathlib import Path

path = Path("test.txt")

info = path.stat()

print(info.st_size)
print(info.st_mtime)
```

### `os`에서도 사용

Python의 `os` 모듈에서도 동일한 파일 정보를 가져올 수 있습니다.

```python
import os

info = os.stat("test.txt")

print(info.st_size)
print(info.st_mtime)
```

### 정리

| 표현 | 의미 |
|---|---|
| `path.stat()` | `Path` 객체를 통해 파일 정보 가져오기 |
| `os.stat(path)` | `os` 모듈을 통해 파일 정보 가져오기 |
| `.st_size` | 파일 크기 |
| `.st_mtime` | 마지막 수정 시각 |

따라서 **`stat()`은 `pathlib`만의 개념이 아닙니다.**

`Path.stat()`은 파일의 상태 정보를 가져오는 기능을 `pathlib.Path` 객체에서 사용할 수 있도록 제공하는 메서드입니다.

> **`st_mtime` → 파일 정보(metadata)에 들어 있는 값**
>
> **`Path.stat()` → 해당 파일의 metadata를 가져오는 `Path` 객체의 메서드**

즉,

```python
path.stat().st_mtime
```

은 **"Path 객체가 가리키는 파일의 마지막 수정 시각을 가져온다"**는 뜻입니다.