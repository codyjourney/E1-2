# ============================================================
# 퀴즈 게임
# ============================================================
#
# 이 프로그램은 Python 입문자를 위한 콘솔 퀴즈 게임입니다.
#
# 주요 기능
# 1. 퀴즈 풀기
# 2. 새로운 퀴즈 추가
# 3. 등록된 퀴즈 목록 확인
# 4. 최고 점수 확인
# 5. 프로그램 종료
#
# 추가 기능
# - 퀴즈 문제 랜덤 출제
# - JSON 파일(state.json)을 이용한 데이터 저장
# - 프로그램을 다시 실행해도 퀴즈와 최고 점수 유지
# - 잘못된 입력 처리
# - Ctrl+C / EOFError 안전 종료
#
# 클래스 구성
# Quiz      : 하나의 퀴즈 문제를 관리
# Storage   : state.json 파일 저장/불러오기 담당
# QuizGame  : 실제 게임의 전체 흐름 담당
# ============================================================


# ------------------------------------------------------------
# 1. 필요한 모듈 가져오기
# ------------------------------------------------------------

import json
# JSON 데이터를 읽고 쓰기 위한 Python 표준 라이브러리입니다.
#
# 이 프로그램에서는 state.json 파일에
# 퀴즈 목록과 최고 점수를 저장할 때 사용합니다.


import random
# 퀴즈의 출제 순서를 랜덤하게 섞기 위해 사용합니다.
#
# random.shuffle()을 사용하면
# 퀴즈가 매번 다른 순서로 출제될 수 있습니다.


from pathlib import Path
# 파일 경로를 운영체제에 맞게 안전하게 처리하기 위한 클래스입니다.
#
# 문자열로 파일 경로를 직접 다루는 것보다
# Path를 사용하면 파일의 위치를 쉽게 관리할 수 있습니다.

from datetime import datetime

# ============================================================
# 2. Quiz 클래스
# ============================================================

class Quiz:
    """
    하나의 퀴즈 문제를 표현하는 클래스입니다.

    하나의 Quiz 객체는 다음 세 가지 정보를 가지고 있습니다.

    question
        퀴즈 문제

    choices
        4개의 선택지

    answer
        정답 번호
        1~4 중 하나의 숫자로 저장합니다.

    예:
        Quiz(
            "Python의 창시자는?",
            ["Guido", "Linus", "Bjarne", "James"],
            1
        )
    """

    # --------------------------------------------------------
    # Quiz 객체 생성
    # --------------------------------------------------------

    def __init__(self, question, choices, answer):
        """
        Quiz 객체를 생성할 때 실행되는 초기화 메서드입니다.

        매개변수
        ----------
        question : str
            퀴즈 문제

        choices : list
            4개의 선택지를 저장한 리스트

        answer : int
            정답 번호(1~4)
        """

        # self.question
        # 현재 Quiz 객체의 문제를 저장합니다.
        self.question = question

        # self.choices
        # 현재 Quiz 객체의 선택지를 저장합니다.
        self.choices = choices

        # self.answer
        # 현재 Quiz 객체의 정답 번호를 저장합니다.
        self.answer = answer

    # --------------------------------------------------------
    # 퀴즈 출력
    # --------------------------------------------------------

    def display(self, number=None):
        """
        퀴즈 문제와 선택지를 화면에 출력합니다.

        number가 전달되면
        [문제 1], [문제 2]와 같은 문제 번호도 함께 출력합니다.
        """

        # number가 None이 아니라면 문제 번호를 출력합니다.
        #
        # 예:
        # [문제 1]
        if number is not None:
            print(f"\n[문제 {number}]")

        # 문제 내용을 출력합니다.
        print(self.question)

        # 선택지를 하나씩 출력합니다.
        #
        # enumerate(..., start=1)을 사용하면
        # 리스트의 인덱스를 1부터 시작할 수 있습니다.
        #
        # 예:
        # 1. str
        # 2. int
        # 3. list
        # 4. bool
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    # --------------------------------------------------------
    # 정답 확인
    # --------------------------------------------------------

    def check_answer(self, user_answer):
        """
        사용자가 입력한 답이 정답인지 확인합니다.

        반환값
        ----------
        True
            정답인 경우

        False
            오답인 경우
        """

        # 사용자의 답과 저장된 정답 번호를 비교합니다.
        #
        # 예:
        # self.answer = 2
        # user_answer = 2
        #
        # 결과:
        # True
        return user_answer == self.answer

    # --------------------------------------------------------
    # Quiz 객체 → 딕셔너리
    # --------------------------------------------------------

    def to_dict(self):
        """
        Quiz 객체를 JSON으로 저장할 수 있는 딕셔너리 형태로 변환합니다.

        Python 객체 자체를 JSON 파일에 바로 저장할 수 없기 때문에
        딕셔너리로 변환한 후 json.dump()를 사용합니다.
        """

        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    # --------------------------------------------------------
    # 딕셔너리 → Quiz 객체
    # --------------------------------------------------------

    @classmethod
    def from_dict(cls, data):
        """
        딕셔너리 형태의 데이터를 Quiz 객체로 변환합니다.

        state.json에서 데이터를 읽으면
        Python 딕셔너리 형태로 가져오게 됩니다.

        따라서 다시 Quiz 객체로 만들어야
        display(), check_answer() 등의 메서드를 사용할 수 있습니다.
        """

        return cls(
            data["question"],
            data["choices"],
            data["answer"],
        )


# ============================================================
# 3. Storage 클래스
# ============================================================

class Storage:
    """
    퀴즈와 최고 점수를 JSON 파일에 저장하고 불러오는 클래스입니다.

    백업 정책
    ----------
    1. state.json을 저장하기 전에 기존 파일을 state.json.bak으로 백업합니다.
    2. 동시에 타임스탬프가 포함된 백업 파일도 생성합니다.
       예: state.json.20260815_160300.bak
    3. state.json이 손상된 경우 최신 백업 파일을 찾아 복원합니다.
    """

    def __init__(self, file_path):
        """
        저장할 파일의 경로를 전달받습니다.
        """

        self.file_path = Path(file_path)

        # 가장 최근 백업 파일
        self.backup_file_path = self.file_path.with_suffix(
            self.file_path.suffix + ".bak"
        )

    # --------------------------------------------------------
    # JSON 파일 하나 읽기
    # --------------------------------------------------------

    def _load_file(self, file_path):
        """
        지정된 JSON 파일을 읽고 데이터 형식을 검증합니다.

        문제가 있으면 예외를 발생시킵니다.
        """

        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError(
                "데이터 형식이 올바르지 않습니다."
            )

        if "quizzes" not in data or "best_score" not in data:
            raise ValueError(
                "필수 데이터가 없습니다."
            )

        if not isinstance(data["quizzes"], list):
            raise ValueError(
                "퀴즈 데이터가 올바르지 않습니다."
            )

        if not isinstance(data["best_score"], int):
            raise ValueError(
                "최고 점수 데이터가 올바르지 않습니다."
            )

        return data

    # --------------------------------------------------------
    # 백업 파일 목록 가져오기
    # --------------------------------------------------------

    def _get_backup_files(self):
        """
        state.json의 백업 파일을 최신 순서로 반환합니다.

        예:
            state.json.bak
            state.json.20260815_160300.bak
        """

        backup_files = []

        # 일반 백업 파일
        if self.backup_file_path.exists():
            backup_files.append(self.backup_file_path)

        # 타임스탬프 백업 파일
        timestamp_backups = self.file_path.parent.glob(
            f"{self.file_path.name}.*.bak"
        )

        backup_files.extend(timestamp_backups)

        # 수정 시간이 최신인 순서로 정렬합니다.
        return sorted(
            backup_files,
            key=lambda path: path.stat().st_mtime,
            reverse=True
        )

    # --------------------------------------------------------
    # 백업을 이용한 복원
    # --------------------------------------------------------

    def _restore_from_backup(self):
        """
        최신 백업 파일부터 확인하여 정상적인 JSON을 찾습니다.

        정상적인 백업을 찾으면 state.json으로 복원합니다.

        반환값
        ----------
        dict
            복원된 데이터

        None
            사용할 수 있는 백업이 없는 경우
        """

        backup_files = self._get_backup_files()

        for backup_file in backup_files:

            try:
                # 백업 파일의 데이터가 정상인지 먼저 확인합니다.
                data = self._load_file(backup_file)

                # 정상적인 백업을 찾으면 state.json으로 복원합니다.
                backup_file.replace(
                    self.file_path
                )

                print(
                    f"🔄 백업 파일을 이용해 데이터를 복원했습니다: "
                    f"{backup_file.name}"
                )

                return data

            except (
                json.JSONDecodeError,
                ValueError,
                KeyError,
                TypeError,
                OSError
            ):
                # 백업 파일도 손상되었다면
                # 다음 백업 파일을 확인합니다.
                continue

        return None

    # --------------------------------------------------------
    # JSON 파일 불러오기
    # --------------------------------------------------------

    def load(self):
        """
        state.json 파일을 읽어서 데이터를 반환합니다.

        state.json이 없거나 손상된 경우
        백업 파일을 이용하여 복원을 시도합니다.
        """

        # ----------------------------------------------------
        # 원본 파일이 없는 경우
        # ----------------------------------------------------

        if not self.file_path.exists():

            print(
                "📂 state.json이 없습니다. "
                "백업 파일을 확인합니다."
            )

            restored_data = self._restore_from_backup()

            if restored_data is not None:
                return restored_data

            print(
                "📂 사용할 수 있는 백업도 없습니다. "
                "기본 퀴즈를 사용합니다."
            )

            return None

        # ----------------------------------------------------
        # 원본 파일 읽기
        # ----------------------------------------------------

        try:

            data = self._load_file(
                self.file_path
            )

            return data

        # ----------------------------------------------------
        # JSON 파일이 손상된 경우
        # ----------------------------------------------------

        except (
            json.JSONDecodeError,
            ValueError,
            KeyError,
            TypeError
        ):

            print(
                "⚠️ state.json이 손상되었습니다."
            )

            print(
                "🔍 백업 파일을 이용한 복원을 시도합니다."
            )

            restored_data = self._restore_from_backup()

            if restored_data is not None:
                return restored_data

            print(
                "⚠️ 복원 가능한 백업이 없습니다. "
                "기본 데이터로 초기화합니다."
            )

            return None

        # ----------------------------------------------------
        # 파일을 읽는 과정에서 운영체제 오류가 발생한 경우
        # ----------------------------------------------------

        except OSError as error:

            print(
                f"⚠️ 데이터 파일을 읽는 중 오류가 발생했습니다: "
                f"{error}"
            )

            print(
                "🔍 백업 파일을 이용한 복원을 시도합니다."
            )

            restored_data = self._restore_from_backup()

            if restored_data is not None:
                return restored_data

            return None

    # --------------------------------------------------------
    # 기존 state.json 백업
    # --------------------------------------------------------

    def _backup_current_file(self):
        """
        기존 state.json을 저장하기 전에 백업합니다.

        백업 파일
        ----------
        state.json.bak
            가장 최근 백업

        state.json.YYYYMMDD_HHMMSS.bak
            타임스탬프가 포함된 백업
        """

        if not self.file_path.exists():
            return

        try:
            # 가장 최근 백업 파일 생성
            self.file_path.replace(
                self.backup_file_path
            )

            # 방금 만든 백업을 다시 원래 위치로 복원합니다.
            #
            # replace()만 사용하면 원본이 사라지기 때문에
            # shutil.copy2()를 사용합니다.
            import shutil

            shutil.copy2(
                self.backup_file_path,
                self.file_path
            )

            # 타임스탬프 백업 생성
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            timestamp_backup = self.file_path.parent / (
                f"{self.file_path.name}."
                f"{timestamp}.bak"
            )

            shutil.copy2(
                self.file_path,
                timestamp_backup
            )

            print(
                f"💾 기존 데이터를 백업했습니다: "
                f"{timestamp_backup.name}"
            )

        except OSError as error:

            print(
                f"⚠️ 데이터 백업 중 오류가 발생했습니다: "
                f"{error}"
            )

    # --------------------------------------------------------
    # JSON 파일 저장
    # --------------------------------------------------------

    def save(self, quizzes, best_score):
        """
        현재 퀴즈 목록과 최고 점수를 state.json에 저장합니다.

        저장 전에 기존 state.json을 백업합니다.
        """

        data = {
            "quizzes": [
                quiz.to_dict()
                for quiz in quizzes
            ],
            "best_score": best_score,
        }

        try:
            # ------------------------------------------------
            # 기존 파일 백업
            # ------------------------------------------------

            if self.file_path.exists():

                import shutil

                # state.json.bak 생성
                shutil.copy2(
                    self.file_path,
                    self.backup_file_path
                )

                # 타임스탬프 백업 생성
                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                timestamp_backup = self.file_path.parent / (
                    f"{self.file_path.name}."
                    f"{timestamp}.bak"
                )

                shutil.copy2(
                    self.file_path,
                    timestamp_backup
                )

                print(
                    f"💾 백업 생성: "
                    f"{timestamp_backup.name}"
                )

            # ------------------------------------------------
            # 새로운 데이터 저장
            # ------------------------------------------------

            with self.file_path.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError as error:

            print(
                f"⚠️ 데이터를 저장하는 중 오류가 발생했습니다: "
                f"{error}"
            )

# ============================================================
# 4. QuizGame 클래스
# ============================================================

class QuizGame:
    """
    퀴즈 게임 전체의 흐름을 관리하는 클래스입니다.

    주요 역할
    ----------
    - 기본 퀴즈 생성
    - 데이터 불러오기
    - 데이터 저장
    - 메뉴 출력
    - 사용자 입력 처리
    - 퀴즈 출제
    - 퀴즈 추가
    - 퀴즈 목록 출력
    - 최고 점수 관리
    """

    # --------------------------------------------------------
    # QuizGame 객체 생성
    # --------------------------------------------------------

    def __init__(self, storage):
        """
        게임 객체를 생성합니다.

        storage
            데이터를 저장하고 불러올 Storage 객체
        """

        # Storage 객체를 저장합니다.
        #
        # 이후 self.storage.load()
        # self.storage.save() 형태로 사용합니다.
        self.storage = storage

        # 현재 등록된 퀴즈를 저장하는 리스트입니다.
        self.quizzes = []

        # 최고 점수를 저장합니다.
        #
        # 아직 게임을 하지 않았다면 0점입니다.
        self.best_score = 0

        # 프로그램 시작 시 저장된 데이터를 불러옵니다.
        self.load_data()

    # --------------------------------------------------------
    # 기본 퀴즈 데이터
    # --------------------------------------------------------

    def get_default_quizzes(self):
        """
        프로그램 최초 실행 시 사용할 기본 퀴즈를 반환합니다.

        Python 입문자를 대상으로 총 8개의 기본 문제를 제공합니다.

        반환값:
            Quiz 객체들이 들어 있는 리스트
        """

        return [
            Quiz(
                "Python에서 문자열(string)을 나타내는 자료형은?",
                ["str", "int", "list", "bool"],
                1,
            ),

            Quiz(
                "Python에서 여러 개의 값을 순서대로 저장할 때 사용하는 자료형은?",
                ["dict", "list", "bool", "int"],
                2,
            ),

            Quiz(
                "조건에 따라 다른 코드를 실행할 때 사용하는 문법은?",
                ["for", "if", "import", "return"],
                2,
            ),

            Quiz(
                "Python에서 같은 작업을 반복할 때 사용할 수 있는 반복문은?",
                ["for", "class", "def", "try"],
                1,
            ),

            Quiz(
                "Python에서 함수를 정의할 때 사용하는 키워드는?",
                ["func", "function", "def", "method"],
                3,
            ),

            Quiz(
                "Python의 딕셔너리(dict)는 기본적으로 어떤 형태의 데이터를 저장하는가?",
                [
                    "값만 저장",
                    "키와 값의 쌍",
                    "문자열만 저장",
                    "숫자만 저장"
                ],
                2,
            ),

            Quiz(
                "Python 클래스에서 객체가 생성될 때 초기화 작업을 담당하는 메서드는?",
                [
                    "__start__",
                    "__main__",
                    "__init__",
                    "__create__"
                ],
                3,
            ),

            Quiz(
                "Python에서 예외가 발생할 수 있는 코드를 처리할 때 사용하는 문법은?",
                [
                    "if/else",
                    "for/in",
                    "try/except",
                    "def/return"
                ],
                3,
            ),
        ]

    # --------------------------------------------------------
    # 저장 데이터 불러오기
    # --------------------------------------------------------

    def load_data(self):
        """
        Storage를 이용하여 저장된 퀴즈와 최고 점수를 불러옵니다.

        첫 실행인 경우:
            기본 퀴즈 데이터를 사용합니다.

        state.json이 손상된 경우:
            기본 데이터로 초기화합니다.

        정상적인 경우:
            저장된 데이터를 Quiz 객체로 변환합니다.
        """

        # Storage의 load() 메서드를 호출합니다.
        data = self.storage.load()

        # ----------------------------------------------------
        # 저장된 파일이 없는 경우
        # ----------------------------------------------------

        if data is None:

            # 기본 퀴즈를 생성합니다.
            self.quizzes = self.get_default_quizzes()

            # 최고 점수를 0점으로 초기화합니다.
            self.best_score = 0

            # 기본 데이터를 state.json에 저장합니다.
            self.save_data()

            return

        # ----------------------------------------------------
        # 저장된 데이터가 있는 경우
        # ----------------------------------------------------

        try:
            # JSON의 각 딕셔너리를 Quiz 객체로 변환합니다.
            #
            # 예:
            # {
            #     "question": "...",
            #     "choices": [...],
            #     "answer": 1
            # }
            #
            # ↓
            #
            # Quiz 객체
            self.quizzes = [
                Quiz.from_dict(item)
                for item in data["quizzes"]
            ]

            # 저장되어 있던 최고 점수를 가져옵니다.
            self.best_score = data["best_score"]

            # 불러온 데이터 정보를 사용자에게 알려줍니다.
            print(
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, "
                f"최고점수 {self.best_score}점)"
            )

        # 저장 데이터의 구조가 잘못된 경우
        except (
            KeyError,
            TypeError,
            ValueError
        ):
            print(
                "⚠️ 저장 데이터의 형식이 올바르지 않습니다."
            )

            print(
                "📂 기본 퀴즈 데이터로 초기화합니다."
            )

            # 기본 데이터로 복구합니다.
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0

            # 복구한 데이터를 다시 저장합니다.
            self.save_data()

    # --------------------------------------------------------
    # 데이터 저장
    # --------------------------------------------------------

    def save_data(self):
        """
        현재 게임 데이터를 Storage에 전달하여 저장합니다.

        QuizGame은 실제 파일을 직접 다루지 않습니다.
        Storage 클래스에게 저장 작업을 맡깁니다.
        """

        self.storage.save(
            self.quizzes,
            self.best_score
        )

    # --------------------------------------------------------
    # 메인 메뉴 출력
    # --------------------------------------------------------

    def display_menu(self):
        """
        프로그램의 메인 메뉴를 화면에 출력합니다.
        """

        print("\n" + "=" * 50)
        print("               퀴즈 게임 ")
        print("=" * 50)

        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

        print("=" * 50)

    # --------------------------------------------------------
    # 숫자 입력 처리
    # --------------------------------------------------------

    def get_number(
        self,
        prompt,
        min_value,
        max_value
    ):
        """
        사용자로부터 올바른 범위의 숫자를 입력받습니다.

        예를 들어 1~5 사이의 숫자가 필요한 경우:

        정상 입력
            1
            3
            5

        잘못된 입력
            abc
            빈 입력
            0
            9

        잘못된 입력이 들어오면
        안내 메시지를 출력하고 다시 입력받습니다.
        """

        # 올바른 값이 입력될 때까지 반복합니다.
        while True:

            try:
                # input()으로 사용자 입력을 받고
                # strip()으로 앞뒤 공백을 제거합니다.
                #
                # 예:
                # "  1  "
                #
                # ↓
                #
                # "1"
                user_input = input(prompt).strip()

                # 아무것도 입력하지 않은 경우
                if not user_input:
                    print(
                        "⚠️ 입력값이 없습니다. "
                        "숫자를 입력해주세요."
                    )
                    continue

                # 문자열을 정수로 변환합니다.
                number = int(user_input)

                # 허용된 범위를 벗어났는지 확인합니다.
                if (
                    number < min_value
                    or number > max_value
                ):
                    print(
                        f"⚠️ {min_value}-{max_value} "
                        f"사이의 숫자를 입력해주세요."
                    )
                    continue

                # 모든 검사를 통과하면 숫자를 반환합니다.
                return number

            # int() 변환에 실패하면 ValueError가 발생합니다.
            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

    # --------------------------------------------------------
    # 문자열 입력 처리
    # --------------------------------------------------------

    def get_non_empty_input(self, prompt):
        """
        빈 문자열이 아닌 입력을 받을 때 사용하는 메서드입니다.

        문제나 선택지를 입력할 때
        그냥 Enter를 누르는 것을 방지합니다.
        """

        while True:

            # 사용자 입력을 받고 앞뒤 공백을 제거합니다.
            value = input(prompt).strip()

            # 빈 문자열인지 확인합니다.
            if not value:
                print(
                    "⚠️ 빈 입력은 사용할 수 없습니다."
                )
                continue

            # 정상적인 입력이면 반환합니다.
            return value

    # --------------------------------------------------------
    # 퀴즈 풀기
    # --------------------------------------------------------

    def play_quiz(self):
        """
        등록된 모든 퀴즈를 랜덤한 순서로 출제합니다.

        사용자가 각 문제의 정답을 입력하면
        정답 개수를 계산하고 최종 점수를 계산합니다.

        점수가 기존 최고 점수보다 높으면
        최고 점수를 갱신하고 저장합니다.
        """

        # ----------------------------------------------------
        # 퀴즈가 없는 경우
        # ----------------------------------------------------

        if not self.quizzes:
            print(
                "\n⚠️ 등록된 퀴즈가 없습니다."
            )
            return

        # ----------------------------------------------------
        # 퀴즈 시작 화면
        # ----------------------------------------------------

        print("\n" + "=" * 50)

        print(
            f"📝 퀴즈를 시작합니다! "
            f"(총 {len(self.quizzes)}문제)"
        )

        print("=" * 50)

        # ----------------------------------------------------
        # 문제 순서 랜덤 섞기
        # ----------------------------------------------------

        # 원본 self.quizzes를 직접 섞으면
        # 실제 저장된 리스트의 순서도 바뀔 수 있습니다.
        #
        # 따라서 copy()를 이용하여
        # 복사본을 만든 후 섞습니다.
        quiz_list = self.quizzes.copy()

        # 문제 순서를 랜덤하게 섞습니다.
        random.shuffle(quiz_list)

        # 맞힌 문제 수를 저장합니다.
        correct_count = 0

        # ----------------------------------------------------
        # 문제 출제
        # ----------------------------------------------------

        for index, quiz in enumerate(
            quiz_list,
            start=1
        ):

            print("\n" + "-" * 50)

            # Quiz 객체의 display() 메서드를 이용하여
            # 문제와 선택지를 출력합니다.
            quiz.display(index)

            # 사용자의 정답을 입력받습니다.
            #
            # 정답은 1~4 사이여야 합니다.
            user_answer = self.get_number(
                "정답 입력 (1-4): ",
                1,
                4,
            )

            # ------------------------------------------------
            # 정답 확인
            # ------------------------------------------------

            if quiz.check_answer(user_answer):

                print("✅ 정답입니다!")

                # 정답 개수를 1 증가시킵니다.
                correct_count += 1

            else:

                print(
                    f"❌ 오답입니다. "
                    f"정답은 {quiz.answer}번입니다."
                )

        # ----------------------------------------------------
        # 최종 점수 계산
        # ----------------------------------------------------

        # 전체 문제 수를 가져옵니다.
        total_count = len(quiz_list)

        # 점수를 백분율로 계산합니다.
        #
        # 예:
        # 8문제 중 6문제 정답
        #
        # 6 / 8 * 100 = 75
        score = int(
            (correct_count / total_count) * 100
        )

        # ----------------------------------------------------
        # 결과 출력
        # ----------------------------------------------------

        print("\n" + "=" * 50)

        print(
            f"🏆 결과: {total_count}문제 중 "
            f"{correct_count}문제 정답! "
            f"({score}점)"
        )

        print("=" * 50)

        # ----------------------------------------------------
        # 최고 점수 갱신
        # ----------------------------------------------------

        if score > self.best_score:

            # 새로운 점수를 최고 점수로 저장합니다.
            self.best_score = score

            print("🎉 새로운 최고 점수입니다!")

            # 변경된 최고 점수를 state.json에 저장합니다.
            self.save_data()

        else:

            print(
                f"현재 최고 점수는 "
                f"{self.best_score}점입니다."
            )

    # --------------------------------------------------------
    # 새로운 퀴즈 추가
    # --------------------------------------------------------

    def add_quiz(self):
        """
        사용자가 직접 새로운 퀴즈를 만들어 등록합니다.

        입력받는 정보
        ----------
        1. 문제
        2. 선택지 1
        3. 선택지 2
        4. 선택지 3
        5. 선택지 4
        6. 정답 번호

        등록이 완료되면 state.json에 저장합니다.
        """

        print("\n" + "=" * 50)
        print("📌 새로운 퀴즈를 추가합니다.")
        print("=" * 50)

        # ----------------------------------------------------
        # 문제 입력
        # ----------------------------------------------------

        question = self.get_non_empty_input(
            "문제를 입력하세요: "
        )

        # 선택지를 저장할 빈 리스트를 만듭니다.
        choices = []

        # ----------------------------------------------------
        # 선택지 4개 입력
        # ----------------------------------------------------

        for index in range(1, 5):

            choice = self.get_non_empty_input(
                f"선택지 {index}: "
            )

            choices.append(choice)

        # ----------------------------------------------------
        # 정답 번호 입력
        # ----------------------------------------------------

        answer = self.get_number(
            "정답 번호 (1-4): ",
            1,
            4,
        )

        # ----------------------------------------------------
        # Quiz 객체 생성
        # ----------------------------------------------------

        new_quiz = Quiz(
            question=question,
            choices=choices,
            answer=answer,
        )

        # 새 Quiz 객체를 현재 퀴즈 리스트에 추가합니다.
        self.quizzes.append(new_quiz)

        # 추가된 퀴즈를 state.json에 저장합니다.
        self.save_data()

        print("\n✅ 퀴즈가 추가되었습니다!")

        print(
            f"현재 등록된 퀴즈는 "
            f"총 {len(self.quizzes)}개입니다."
        )

    # --------------------------------------------------------
    # 퀴즈 목록 출력
    # --------------------------------------------------------

    def show_quizzes(self):
        """
        현재 등록되어 있는 모든 퀴즈를 출력합니다.
        """

        print("\n" + "=" * 50)

        print(
            f"📋 등록된 퀴즈 목록 "
            f"(총 {len(self.quizzes)}개)"
        )

        print("=" * 50)

        # ----------------------------------------------------
        # 퀴즈가 없는 경우
        # ----------------------------------------------------

        if not self.quizzes:

            print(
                "⚠️ 등록된 퀴즈가 없습니다."
            )
            return

        # ----------------------------------------------------
        # 퀴즈 목록 출력
        # ----------------------------------------------------

        for index, quiz in enumerate(
            self.quizzes,
            start=1
        ):

            # 문제 번호와 문제 내용을 출력합니다.
            print(
                f"\n[{index}] {quiz.question}"
            )

            # 각 선택지를 출력합니다.
            for choice_index, choice in enumerate(
                quiz.choices,
                start=1
            ):
                print(
                    f"    {choice_index}. {choice}"
                )

    # --------------------------------------------------------
    # 최고 점수 확인
    # --------------------------------------------------------

    def show_score(self):
        """
        현재 저장된 최고 점수를 출력합니다.
        """

        print("\n" + "=" * 50)
        print("🏆 최고 점수")
        print("=" * 50)


        if self.best_score == 0:

            print(
                f"최고 점수: "
                f"0점"
            )

        else:

            print(
                f"최고 점수: "
                f"{self.best_score}점"
            )

    # --------------------------------------------------------
    # 게임 실행
    # --------------------------------------------------------

    def run(self):
        """
        게임의 메인 실행 루프입니다.

        사용자가 종료 메뉴를 선택할 때까지
        계속해서 메뉴를 출력하고
        선택한 기능을 실행합니다.
        """

        # True인 동안 계속 반복합니다.
        while True:

            # 메인 메뉴를 출력합니다.
            self.display_menu()

            # 사용자의 메뉴 선택을 받습니다.
            #
            # 메뉴는 1~5 사이여야 합니다.
            choice = self.get_number(
                "선택: ",
                1,
                5,
            )

            # ------------------------------------------------
            # 1. 퀴즈 풀기
            # ------------------------------------------------

            if choice == 1:
                self.play_quiz()

            # ------------------------------------------------
            # 2. 퀴즈 추가
            # ------------------------------------------------

            elif choice == 2:
                self.add_quiz()

            # ------------------------------------------------
            # 3. 퀴즈 목록
            # ------------------------------------------------

            elif choice == 3:
                self.show_quizzes()

            # ------------------------------------------------
            # 4. 점수 확인
            # ------------------------------------------------

            elif choice == 4:
                self.show_score()

            # ------------------------------------------------
            # 5. 종료
            # ------------------------------------------------

            elif choice == 5:

                # 프로그램 종료 전에
                # 현재 데이터를 한 번 더 저장합니다.
                self.save_data()

                print(
                    "\n💾 데이터를 저장했습니다."
                )

                print(
                    "👋 퀴즈 게임을 종료합니다."
                )

                # while True 반복문을 종료합니다.
                break


# ============================================================
# 5. 프로그램 시작 함수
# ============================================================

def main():
    """
    프로그램의 시작점입니다.

    여기서는 실제 게임에 필요한 객체를 생성하고
    QuizGame.run()을 호출합니다.
    """

    # --------------------------------------------------------
    # 프로젝트 루트 경로 확인
    # --------------------------------------------------------

    # __file__
    # 현재 실행 중인 Python 파일(main.py)의 경로입니다.
    #
    # Path(__file__).resolve()
    # main.py의 절대 경로를 가져옵니다.
    #
    # .parent
    # main.py가 위치한 폴더를 가져옵니다.
    #
    # 따라서 base_dir은 프로젝트 폴더가 됩니다.
    base_dir = Path(__file__).resolve().parent

    # state.json은 main.py와 같은 폴더에 저장합니다.
    state_file = base_dir / "state.json"

    # --------------------------------------------------------
    # Storage 객체 생성
    # --------------------------------------------------------

    # state.json 파일의 저장/불러오기를 담당할
    # Storage 객체를 생성합니다.
    storage = Storage(state_file)

    # --------------------------------------------------------
    # QuizGame 객체 생성
    # --------------------------------------------------------

    # 실제 게임을 담당하는 QuizGame 객체를 생성합니다.
    #
    # 이때 QuizGame.__init__()이 실행되고
    # 내부에서 load_data()가 호출됩니다.
    game = QuizGame(storage)

    # --------------------------------------------------------
    # 게임 실행
    # --------------------------------------------------------

    try:

        # 메인 게임 루프를 실행합니다.
        game.run()

    # --------------------------------------------------------
    # Ctrl+C 처리
    # --------------------------------------------------------

    except KeyboardInterrupt:

        # 사용자가 Ctrl+C를 눌렀을 때 발생합니다.
        print(
            "\n\n⚠️ Ctrl+C가 입력되었습니다."
        )

        print(
            "💾 현재 데이터를 저장하고 "
            "안전하게 종료합니다."
        )

        # 프로그램을 강제 종료하지 않고
        # 현재 데이터를 저장합니다.
        game.save_data()

    # --------------------------------------------------------
    # EOF 처리
    # --------------------------------------------------------

    except EOFError:

        # 입력 스트림이 종료되었을 때 발생합니다.
        #
        # 예:
        # CTRL + D, 터미널 입력이 더 이상 들어오지 않는 경우
        print(
            "\n\n⚠️ 입력 스트림이 종료되었습니다."
        )

        print(
            "💾 현재 데이터를 저장하고 "
            "안전하게 종료합니다."
        )

        # 현재 데이터를 저장합니다.
        game.save_data()


# ============================================================
# 6. 프로그램 실행
# ============================================================

# 이 파일을 직접 실행했을 때만 main()을 실행합니다.
#
# Python에서는 __name__이라는 특별한 변수가 있습니다.
#
# main.py를 직접 실행하면:
#
# __name__ == "__main__"
#
# 따라서 아래 조건이 True가 되고 main()이 실행됩니다.
#
# 다른 Python 파일에서 main.py를 import하는 경우에는
# main()이 자동으로 실행되지 않습니다.
# ============================================================

if __name__ == "__main__":
    main()


"""
## 클래스 구조

### 1. Quiz 클래스

하나의 퀴즈 문제를 표현하는 클래스입니다.

- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호

주요 메서드:

- `__init__()`: 퀴즈 객체를 생성하고 문제, 선택지, 정답을 초기화합니다.
- `display()`: 문제와 선택지를 화면에 출력합니다.
- `check_answer()`: 사용자의 답과 실제 정답을 비교합니다.
- `to_dict()`: Quiz 객체를 JSON 저장용 딕셔너리로 변환합니다.
- `from_dict()`: JSON에서 불러온 딕셔너리를 Quiz 객체로 변환합니다.

### 2. Storage 클래스

`state.json` 파일의 저장과 불러오기를 담당합니다.

- `__init__()`: 저장할 파일의 경로를 설정합니다.
- `load()`: `state.json`을 읽고 데이터를 불러옵니다.
- `save()`: 퀴즈 목록과 최고 점수를 JSON 파일에 저장합니다.

파일이 없거나 손상된 경우 `try/except`를 이용하여 오류를 처리하고 기본 데이터를 사용할 수 있도록 합니다.

### 3. QuizGame 클래스

퀴즈 게임의 전체적인 흐름을 관리합니다.

- `__init__()`: 게임에 필요한 데이터를 초기화하고 저장 데이터를 불러옵니다.
- `get_default_quizzes()`: 프로그램 최초 실행 시 사용할 기본 퀴즈를 생성합니다.
- `load_data()`: 저장된 퀴즈와 최고 점수를 불러옵니다.
- `save_data()`: 현재 게임 데이터를 저장합니다.
- `display_menu()`: 메인 메뉴를 출력합니다.
- `get_number()`: 범위에 맞는 숫자를 안전하게 입력받습니다.
- `get_non_empty_input()`: 빈 입력을 방지하면서 문자열을 입력받습니다.
- `play_quiz()`: 퀴즈를 랜덤하게 출제하고 점수를 계산합니다.
- `add_quiz()`: 새로운 퀴즈를 입력받아 등록합니다.
- `show_quizzes()`: 등록된 퀴즈 목록을 출력합니다.
- `show_score()`: 최고 점수를 출력합니다.
- `run()`: 프로그램의 메인 메뉴를 반복 실행합니다.

### 4. main() 함수

프로그램의 시작점입니다.

`state.json`의 경로를 설정하고 `Storage`와 `QuizGame` 객체를 생성한 후 게임을 실행합니다.

또한 `KeyboardInterrupt`와 `EOFError`를 처리하여 `Ctrl+C` 또는 입력 스트림 종료가 발생해도 데이터를 저장하고 안전하게 종료하도록 구성했습니다.
"""