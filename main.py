import json
import random
from pathlib import Path

###########
class Quiz:
    """하나의 퀴즈 문제를 표현하는 클래스."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number=None):
        """퀴즈 문제와 선택지를 출력한다."""
        if number is not None:
            print(f"\n[문제 {number}]")

        print(self.question)

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        """사용자의 답이 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위한 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리 데이터를 Quiz 객체로 변환한다."""
        return cls(
            data["question"],
            data["choices"],
            data["answer"],
        )


class Storage:
    """퀴즈와 점수를 JSON 파일에 저장하고 불러오는 클래스."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):
        """state.json을 읽어 데이터를 반환한다.

        파일이 없거나 손상된 경우 None을 반환한다.
        """
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            if "quizzes" not in data or "best_score" not in data:
                raise ValueError("필수 데이터가 없습니다.")

            if not isinstance(data["quizzes"], list):
                raise ValueError("퀴즈 데이터가 올바르지 않습니다.")

            if not isinstance(data["best_score"], int):
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            return data

        except FileNotFoundError:
            print("📂 저장된 데이터가 없습니다. 기본 퀴즈를 사용합니다.")
            return None

        except (json.JSONDecodeError, ValueError, KeyError, TypeError):
            print("⚠️ state.json이 손상되었습니다. 기본 데이터로 초기화합니다.")
            return None

        except OSError as error:
            print(f"⚠️ 데이터 파일을 읽는 중 오류가 발생했습니다: {error}")
            return None

    def save(self, quizzes, best_score):
        """퀴즈와 최고 점수를 JSON 파일에 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
        }

        try:
            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError as error:
            print(f"⚠️ 데이터를 저장하는 중 오류가 발생했습니다: {error}")


class QuizGame:
    """퀴즈 게임 전체 흐름을 관리하는 클래스."""

    def __init__(self, storage):
        self.storage = storage
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def get_default_quizzes(self):
        """프로그램 최초 실행 시 사용할 기본 퀴즈를 반환한다."""
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
                ["값만 저장", "키와 값의 쌍", "문자열만 저장", "숫자만 저장"],
                2,
            ),
            Quiz(
                "Python 클래스에서 객체가 생성될 때 초기화 작업을 담당하는 메서드는?",
                ["__start__", "__main__", "__init__", "__create__"],
                3,
            ),
            Quiz(
                "Python에서 예외가 발생할 수 있는 코드를 처리할 때 사용하는 문법은?",
                ["if/else", "for/in", "try/except", "def/return"],
                3,
            ),
        ]

    def load_data(self):
        """저장된 데이터를 불러온다."""
        data = self.storage.load()

        if data is None:
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0

            # 첫 실행 또는 손상된 파일이라면 기본 데이터를 저장한다.
            self.save_data()
            return

        try:
            self.quizzes = [
                Quiz.from_dict(item)
                for item in data["quizzes"]
            ]
            self.best_score = data["best_score"]

            print(
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)"
            )

        except (KeyError, TypeError, ValueError):
            print("⚠️ 저장 데이터의 형식이 올바르지 않습니다.")
            print("📂 기본 퀴즈 데이터로 초기화합니다.")

            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_data()

    def save_data(self):
        """현재 게임 데이터를 저장한다."""
        self.storage.save(self.quizzes, self.best_score)

    def display_menu(self):
        """메인 메뉴를 출력한다."""
        print("\n" + "=" * 44)
        print("        🐍 Python 기초 퀴즈 게임 🐍")
        print("=" * 44)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 44)

    def get_number(self, prompt, min_value, max_value):
        """범위가 지정된 숫자를 안전하게 입력받는다."""
        while True:
            try:
                user_input = input(prompt).strip()

                if not user_input:
                    print("⚠️ 입력값이 없습니다. 숫자를 입력해주세요.")
                    continue

                number = int(user_input)

                if number < min_value or number > max_value:
                    print(
                        f"⚠️ {min_value}-{max_value} 사이의 숫자를 입력해주세요."
                    )
                    continue

                return number

            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

    def get_non_empty_input(self, prompt):
        """빈 문자열이 아닌 입력을 받는다."""
        while True:
            value = input(prompt).strip()

            if not value:
                print("⚠️ 빈 입력은 사용할 수 없습니다.")
                continue

            return value

    def play_quiz(self):
        """등록된 퀴즈를 출제하고 점수를 계산한다."""
        """..."""
        """..."""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print("\n" + "=" * 44)
        print(f"📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("=" * 44)

        # 원본 리스트를 변경하지 않고 문제 순서를 섞는다.
        quiz_list = self.quizzes.copy()
        random.shuffle(quiz_list)

        correct_count = 0

        for index, quiz in enumerate(quiz_list, start=1):
            print("\n" + "-" * 44)
            quiz.display(index)

            user_answer = self.get_number(
                "정답 입력 (1-4): ",
                1,
                4,
            )

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        total_count = len(quiz_list)
        score = int((correct_count / total_count) * 100)

        print("\n" + "=" * 44)
        print(
            f"🏆 결과: {total_count}문제 중 "
            f"{correct_count}문제 정답! ({score}점)"
        )
        print("=" * 44)

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_data()
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

    def add_quiz(self):
        """새로운 퀴즈를 입력받아 등록한다."""
        print("\n" + "=" * 44)
        print("📌 새로운 퀴즈를 추가합니다.")
        print("=" * 44)

        question = self.get_non_empty_input("문제를 입력하세요: ")

        choices = []

        for index in range(1, 5):
            choice = self.get_non_empty_input(
                f"선택지 {index}: "
            )
            choices.append(choice)

        answer = self.get_number(
            "정답 번호 (1-4): ",
            1,
            4,
        )

        new_quiz = Quiz(
            question=question,
            choices=choices,
            answer=answer,
        )

        self.quizzes.append(new_quiz)
        self.save_data()

        print("\n✅ 퀴즈가 추가되었습니다!")
        print(f"현재 등록된 퀴즈는 총 {len(self.quizzes)}개입니다.")

    def show_quizzes(self):
        """등록된 모든 퀴즈를 출력한다."""
        print("\n" + "=" * 44)
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("=" * 44)

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}] {quiz.question}")

            for choice_index, choice in enumerate(
                quiz.choices,
                start=1,
            ):
                print(f"    {choice_index}. {choice}")

    def show_score(self):
        """최고 점수를 출력한다."""
        print("\n" + "=" * 44)
        print("🏆 최고 점수")
        print("=" * 44)

        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def run(self):
        """게임의 메인 실행 루프."""
        while True:
            self.display_menu()

            choice = self.get_number(
                "선택: ",
                1,
                5,
            )

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                self.add_quiz()

            elif choice == 3:
                self.show_quizzes()

            elif choice == 4:
                self.show_score()

            elif choice == 5:
                self.save_data()
                print("\n💾 데이터를 저장했습니다.")
                print("👋 퀴즈 게임을 종료합니다.")
                break


def main():
    """프로그램 시작점."""
    base_dir = Path(__file__).resolve().parent
    state_file = base_dir / "state.json"

    storage = Storage(state_file)
    game = QuizGame(storage)

    try:
        game.run()

    except KeyboardInterrupt:
        print("\n\n⚠️ Ctrl+C가 입력되었습니다.")
        print("💾 현재 데이터를 저장하고 안전하게 종료합니다.")
        game.save_data()

    except EOFError:
        print("\n\n⚠️ 입력 스트림이 종료되었습니다.")
        print("💾 현재 데이터를 저장하고 안전하게 종료합니다.")
        game.save_data()


if __name__ == "__main__":
    main()