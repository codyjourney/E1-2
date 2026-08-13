# 퀴즈 게임

Python 입문자를 대상으로 만든 터미널 기반 퀴즈 게임입니다.

Python의 기본 문법과 객체 지향 프로그래밍을 직접 활용하여
퀴즈 출제, 퀴즈 등록, 퀴즈 목록 확인, 최고 점수 확인 기능을 구현했습니다.

또한 JSON 파일을 이용해 퀴즈와 최고 점수를 저장하고,
Git을 이용해 기능별 개발 이력을 관리하는 것을 목표로 합니다.

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


## 7. 설명
## 클래스 및 메서드 설명

이 프로젝트는 기능별 역할을 분리하기 위해 `Quiz`, `Storage`, `QuizGame` 3개의 클래스로 구성했습니다.

- `Quiz`: 하나의 퀴즈 데이터를 관리
- `Storage`: JSON 파일의 저장과 불러오기를 담당
- `QuizGame`: 메뉴, 퀴즈 진행, 퀴즈 추가, 점수 등 게임 전체 흐름을 관리

---

### 1. Quiz 클래스

`Quiz` 클래스는 하나의 퀴즈 문제를 객체로 표현합니다.

각 퀴즈는 다음 3개의 데이터를 가집니다.

- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호

#### 주요 속성

| 속성 | 자료형 | 설명 |
|---|---|---|
| `question` | `str` | 퀴즈 문제 |
| `choices` | `list` | 4개의 선택지 |
| `answer` | `int` | 정답 번호 (`1~4`) |

#### `__init__()`

```python
def __init__(self, question, choices, answer):
    self.question = question
    self.choices = choices
    self.answer = answer
```

퀴즈 객체가 생성될 때 문제, 선택지, 정답을 초기화합니다.

예를 들어:

```python
quiz = Quiz(
    "Python에서 문자열을 나타내는 자료형은?",
    ["str", "int", "list", "bool"],
    1
)
```

위 코드에서는 `question`, `choices`, `answer`가 해당 객체의 속성으로 저장됩니다.

---

#### `display()`

```python
def display(self, number=None):
```

퀴즈 문제와 4개의 선택지를 화면에 출력합니다.

`number`가 전달되면 현재 몇 번째 문제인지 함께 표시합니다.

실행 예시:

```text
[문제 1]
Python에서 문자열을 나타내는 자료형은?

1. str
2. int
3. list
4. bool
```

---

#### `check_answer()`

```python
def check_answer(self, user_answer):
    return user_answer == self.answer
```

사용자가 입력한 답과 실제 정답을 비교합니다.

정답이면 `True`, 오답이면 `False`를 반환합니다.

예:

```python
if quiz.check_answer(1):
    print("정답입니다!")
```

---

#### `to_dict()`

```python
def to_dict(self):
```

`Quiz` 객체를 JSON으로 저장할 수 있는 Dictionary 형태로 변환합니다.

예:

```python
{
    "question": "Python에서 문자열을 나타내는 자료형은?",
    "choices": ["str", "int", "list", "bool"],
    "answer": 1
}
```

객체 자체는 JSON으로 직접 저장할 수 없기 때문에 `to_dict()`를 사용하여 Dictionary로 변환한 후 저장합니다.

---

#### `from_dict()`

```python
@classmethod
def from_dict(cls, data):
```

JSON에서 불러온 Dictionary 데이터를 다시 `Quiz` 객체로 변환합니다.

저장된 데이터:

```python
{
    "question": "Python에서 문자열을 나타내는 자료형은?",
    "choices": ["str", "int", "list", "bool"],
    "answer": 1
}
```

을 다음과 같은 `Quiz` 객체로 변환합니다.

```python
Quiz(
    "Python에서 문자열을 나타내는 자료형은?",
    ["str", "int", "list", "bool"],
    1
)
```

`@classmethod`를 사용하여 클래스 자체를 통해 객체를 생성합니다.

---

### 2. Storage 클래스

`Storage` 클래스는 `state.json` 파일의 저장과 불러오기를 담당합니다.

게임 로직과 파일 입출력 로직을 분리하여 `QuizGame` 클래스가 JSON 파일의 세부적인 처리 방법을 직접 알 필요가 없도록 구성했습니다.

#### 주요 속성

| 속성 | 자료형 | 설명 |
|---|---|---|
| `file_path` | `Path` | `state.json` 파일의 경로 |

---

#### `__init__()`

```python
def __init__(self, file_path):
    self.file_path = Path(file_path)
```


JSON 파일의 경로를 저장합니다.

`Path`를 사용하여 운영체제에 맞는 파일 경로를 쉽게 처리할 수 있도록 했습니다.

---

#### `load()`

```python
def load(self):
```

`state.json` 파일을 읽고 저장된 데이터를 반환합니다.

주요 처리 과정:

```text
state.json 열기
    ↓
JSON 데이터 읽기
    ↓
Dictionary 형식인지 확인
    ↓
quizzes / best_score 확인
    ↓
데이터 반환
```

파일이 존재하지 않는 경우:

```text
📂 저장된 데이터가 없습니다. 기본 퀴즈를 사용합니다.
```

라는 메시지를 출력하고 `None`을 반환합니다.

JSON 파일이 손상되었거나 데이터 구조가 잘못된 경우에도 예외를 처리하고 `None`을 반환합니다.

사용한 주요 예외 처리:

- `FileNotFoundError`
- `json.JSONDecodeError`
- `ValueError`
- `KeyError`
- `TypeError`
- `OSError`

---

#### `save()`

```python
def save(self, quizzes, best_score):
```

현재 퀴즈 목록과 최고 점수를 `state.json`에 저장합니다.

저장하기 전에 각 `Quiz` 객체를 `to_dict()`를 통해 Dictionary로 변환합니다.

```text
Quiz 객체
    ↓
to_dict()
    ↓
Dictionary
    ↓
json.dump()
    ↓
state.json
```

`ensure_ascii=False` 옵션을 사용하여 한글이 Unicode 코드로 변환되지 않고 그대로 저장되도록 했습니다.

```python
json.dump(
    data,
    file,
    ensure_ascii=False,
    indent=4
)
```

또한 `encoding="utf-8"`을 사용하여 UTF-8 인코딩으로 데이터를 저장합니다.

---

### 3. QuizGame 클래스

`QuizGame` 클래스는 퀴즈 게임의 전체적인 흐름을 관리합니다.

메뉴 출력부터 퀴즈 진행, 퀴즈 추가, 목록 확인, 점수 확인, 데이터 저장 및 불러오기까지 게임에 필요한 주요 기능을 담당합니다.

#### 주요 속성

| 속성 | 자료형 | 설명 |
|---|---|---|
| `storage` | `Storage` | JSON 저장/불러오기를 담당하는 객체 |
| `quizzes` | `list` | 현재 등록된 `Quiz` 객체 목록 |
| `best_score` | `int` | 현재 최고 점수 |

---

#### `__init__()`

```python
def __init__(self, storage):
    self.storage = storage
    self.quizzes = []
    self.best_score = 0
    self.load_data()
```

게임 객체가 생성될 때 필요한 속성을 초기화하고 저장된 데이터를 불러옵니다.

실행 과정:

```text
QuizGame 생성
    ↓
Storage 연결
    ↓
quizzes 초기화
    ↓
best_score 초기화
    ↓
load_data() 실행
```

---

#### `get_default_quizzes()`

```python
def get_default_quizzes(self):
```

`state.json`이 처음부터 존재하지 않거나 손상된 경우 사용할 기본 퀴즈 데이터를 생성합니다.

현재 Python 입문자를 위한 기본 퀴즈 8개가 포함되어 있습니다.

예:

```python
Quiz(
    "Python에서 문자열(string)을 나타내는 자료형은?",
    ["str", "int", "list", "bool"],
    1,
)
```

각 문제는 `Quiz` 클래스의 객체로 생성됩니다.

---

#### `load_data()`

```python
def load_data(self):
```

`Storage` 클래스의 `load()` 메서드를 호출하여 `state.json`의 데이터를 불러옵니다.

저장된 데이터가 없는 경우:

```text
기본 퀴즈 생성
    ↓
최고 점수 0점 설정
    ↓
state.json 저장
```

저장된 데이터가 있는 경우:

```text
state.json 읽기
    ↓
Dictionary 데이터 확인
    ↓
Quiz.from_dict() 실행
    ↓
Quiz 객체 생성
    ↓
quizzes에 저장
    ↓
best_score 적용
```

이를 통해 프로그램을 다시 실행해도 기존 퀴즈와 최고 점수를 유지할 수 있습니다.

---

#### `save_data()`

```python
def save_data(self):
```

현재 게임 데이터를 `Storage` 객체에 전달하여 `state.json`에 저장합니다.

```python
self.storage.save(
    self.quizzes,
    self.best_score
)
```

파일 저장의 실제 처리는 `Storage` 클래스가 담당하기 때문에 `QuizGame`에서는 저장 과정만 요청합니다.

---

#### `display_menu()`

```python
def display_menu(self):
```

프로그램의 메인 메뉴를 출력합니다.

메뉴는 다음과 같이 구성됩니다.

```text
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

---

#### `get_number()`

```python
def get_number(self, prompt, min_value, max_value):
```

숫자 입력이 필요한 상황에서 사용자의 입력을 안전하게 처리하는 공통 메서드입니다.

다음과 같은 입력을 처리합니다.

- 정상적인 숫자 입력
- 빈 입력
- 숫자가 아닌 입력
- 허용 범위를 벗어난 숫자

예를 들어 메뉴에서는:

```python
choice = self.get_number(
    "선택: ",
    1,
    5,
)
```

를 사용하여 1~5 사이의 숫자만 입력받습니다.

사용자가 `abc`를 입력하면:

```text
⚠️ 숫자만 입력해주세요.
```

를 출력하고 다시 입력받습니다.

`9`를 입력하면:

```text
⚠️ 1-5 사이의 숫자를 입력해주세요.
```

를 출력하고 다시 입력받습니다.

---

#### `get_non_empty_input()`

```python
def get_non_empty_input(self, prompt):
```

문제나 선택지처럼 빈 문자열을 허용하지 않는 입력을 처리합니다.

입력값의 앞뒤 공백을 제거한 후 값이 비어 있으면 다시 입력받습니다.

예:

```text
문제를 입력하세요:
```

사용자가 아무것도 입력하지 않고 Enter를 누르면:

```text
⚠️ 빈 입력은 사용할 수 없습니다.
```

를 출력합니다.

---

#### `play_quiz()`

```python
def play_quiz(self):
```

등록된 퀴즈를 출제하고 사용자의 답을 확인하여 점수를 계산합니다.

주요 처리 과정:

```text
퀴즈 존재 여부 확인
    ↓
퀴즈 목록 복사
    ↓
random.shuffle()로 순서 섞기
    ↓
문제 출력
    ↓
사용자 답 입력
    ↓
정답 확인
    ↓
정답 개수 계산
    ↓
점수 계산
    ↓
최고 점수와 비교
    ↓
필요한 경우 최고 점수 저장
```

원본 퀴즈 목록을 변경하지 않기 위해:

```python
quiz_list = self.quizzes.copy()
```

를 사용합니다.

그 후:

```python
random.shuffle(quiz_list)
```

을 사용하여 문제 순서를 랜덤하게 변경합니다.

이를 통해 같은 퀴즈라도 매번 다른 순서로 출제될 수 있습니다.

점수는 다음과 같이 계산됩니다.

```text
정답 개수 ÷ 전체 문제 수 × 100
```

예를 들어 8문제 중 6문제를 맞히면 75점입니다.

---

#### `add_quiz()`

```python
def add_quiz(self):
```

사용자로부터 새로운 퀴즈 정보를 입력받아 `Quiz` 객체를 생성하고 등록합니다.

입력 과정:

```text
문제 입력
    ↓
선택지 1 입력
    ↓
선택지 2 입력
    ↓
선택지 3 입력
    ↓
선택지 4 입력
    ↓
정답 번호 입력
    ↓
Quiz 객체 생성
    ↓
quizzes 리스트에 추가
    ↓
state.json 저장
```

정답 번호는 `get_number()`를 사용하여 1~4 범위만 허용합니다.

---

#### `show_quizzes()`

```python
def show_quizzes(self):
```

현재 등록된 모든 퀴즈의 목록을 출력합니다.

각 퀴즈의 문제와 선택지를 함께 보여줍니다.

예:

```text
[1] Python에서 문자열을 나타내는 자료형은?
    1. str
    2. int
    3. list
    4. bool
```

등록된 퀴즈가 없는 경우에는 별도의 안내 메시지를 출력합니다.

---

#### `show_score()`

```python
def show_score(self):
```

현재 저장된 최고 점수를 화면에 출력합니다.

최고 점수가 0점인 경우에는:

```text
아직 퀴즈를 풀지 않았습니다.
```

라는 메시지를 출력합니다.

최고 점수가 있는 경우에는:

```text
최고 점수: 80점
```

과 같이 표시합니다.

---

#### `run()`

```python
def run(self):
```

게임의 메인 실행 루프입니다.

메뉴를 반복해서 출력하고 사용자가 선택한 기능을 실행합니다.

전체 흐름:

```text
메뉴 출력
    ↓
사용자 메뉴 선택
    ↓
┌───────────────────────┐
│ 1. 퀴즈 풀기           │
│ 2. 퀴즈 추가           │
│ 3. 퀴즈 목록           │
│ 4. 점수 확인           │
│ 5. 종료                │
└───────────────────────┘
    ↓
선택한 기능 실행
    ↓
다시 메뉴 출력
```

5번 종료를 선택하면 현재 데이터를 저장하고 프로그램을 종료합니다.

---

### 4. `main()` 함수

```python
def main():
```

프로그램을 시작하는 진입점 역할을 합니다.

먼저 현재 Python 파일의 위치를 기준으로 `state.json`의 경로를 생성합니다.

```python
base_dir = Path(__file__).resolve().parent
state_file = base_dir / "state.json"
```

그 다음 `Storage`와 `QuizGame` 객체를 생성하고 게임을 실행합니다.

```python
storage = Storage(state_file)
game = QuizGame(storage)

game.run()
```

이렇게 하면 `state.json`이 실행 위치에 따라 달라지는 것을 방지하고 프로젝트 루트의 `state.json`을 사용하게 됩니다.

---

### 5. 프로그램 실행 조건

```python
if __name__ == "__main__":
    main()
```

현재 파일이 직접 실행된 경우에만 `main()` 함수를 호출합니다.

따라서 `main.py`를 직접 실행하면 프로그램이 시작됩니다.

```bash
python main.py
```

---

## 클래스 간 관계

각 클래스는 서로 다른 역할을 담당하도록 구성했습니다.

```text
                    ┌───────────────┐
                    │    QuizGame   │
                    │  게임 전체 관리 │
                    └───────┬───────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
          ┌─────────────┐       ┌─────────────┐
          │    Quiz     │       │   Storage   │
          │ 퀴즈 데이터 관리 │       │ JSON 파일 관리 │
          └─────────────┘       └─────────────┘
                 │                     │
                 │                     │
                 ▼                     ▼
           문제/선택지/정답          state.json
```

### 역할 분리

| 클래스 | 주요 책임 |
|---|---|
| `Quiz` | 하나의 퀴즈 데이터와 정답 확인 |
| `Storage` | JSON 파일 저장 및 불러오기 |
| `QuizGame` | 메뉴, 게임 진행, 퀴즈 추가, 목록, 점수 관리 |

이와 같이 역할을 분리함으로써 하나의 클래스에 모든 기능을 작성하지 않고 각 클래스가 자신의 역할에 집중하도록 설계했습니다.

---

## 프로그램의 전체 실행 흐름

```text
main()
  ↓
Storage 객체 생성
  ↓
QuizGame 객체 생성
  ↓
state.json 불러오기
  ↓
기본 데이터 또는 저장 데이터 설정
  ↓
run()
  ↓
메뉴 출력
  ↓
사용자 선택
  ├── 1 → play_quiz()
  ├── 2 → add_quiz()
  ├── 3 → show_quizzes()
  ├── 4 → show_score()
  └── 5 → save_data() 후 종료
```

이 구조를 통해 **퀴즈 데이터 관리(`Quiz`)**, **파일 입출력(`Storage`)**, **게임 진행(`QuizGame`)**의 책임을 분리하고 객체 지향적인 구조로 프로그램을 구현했습니다.


## Git
```
% git log --oneline --graph --all
* a6a5fdb (HEAD -> main) Fix: 잘못된 입력과 JSON 파일 오류 처리
* 0046818 Feat: state.json 데이터 저장 및 불러오기 구현
* d452a7a Feat: 최고 점수 확인 및 갱신 기능 구현
* 9d9c197 Feat: 등록된 퀴즈 목록 조회 기능 구현
* 15fa49a Feat: 사용자 퀴즈 추가 기능 구현
* ed41239 Feat: 등록된 퀴즈 목록 조회 기능 구현
* e890cec Feat: 사용자 퀴즈 추가 기능 구현
* bb7645f (origin/feature/play-quiz, feature/play-quiz) Feat: 퀴즈 랜덤 출제와 점수 계산 
기능 추가
* bebf084 Feat: 퀴즈 출제 및 정답 확인 기능 구현
* 927164d Feat: 기본 퀴즈 데이터 추가
* 0afe520 Feat: Quiz 클래스와 정답 확인 기능 구현
* 462235b Feat: 메인 메뉴 및 종료 기능 구현
* 484a4f0 (origin/main) Init: 퀴즈 게임 프로젝트 초기 설정
* 107927e Chore: gitignore 설정
```


## 참고
https://chatgpt.com/share/6a7aed57-d258-83ea-8ed0-651915ea5410
