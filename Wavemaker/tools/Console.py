import sys


class Console:
    @staticmethod
    def task(text: str):
        print(f"\033[95m🛈 TASK\033[0m {text}")

    @staticmethod
    def info(text: str):
        print(f"\033[94m🮕 DEBUG\033[0m {text}")

    @staticmethod
    def warning(text: str):
        print(f"\033[93m⚠ NOTICE\033[0m {text}")

    @staticmethod
    def error(text: str):
        print(f"\033[31m⨉ ERROR\033[0m {text}", file=sys.stderr)

    @staticmethod
    def success(text: str):
        print(f"\033[32m✓ SUCCESS\033[0m {text}")

    @staticmethod
    def ask(text: str, choices: list[str], default=0) -> int:
        question = f"\033[36m🯄 QUESTION\033[0m {text} (default = {default}) \n"
        for i, c in enumerate(choices):
            question += f"\t{i} : {c}\n"
        question += " < "
        try:
            res = input(question)
        except EOFError:
            Console.info(f"Chose {choices[default]} ({default}, default).")
            return default
        if res == "":
            Console.info(f"Chose {choices[default]} ({default}, default).")
            return default
        try:
            res = int(res)
        except ValueError:
            Console.error("Invalid input. Try again.")
            return Console.ask(text, choices, default)
        if res < 0 or res > len(choices):
            Console.error("Invalid input. Try again.")
            return Console.ask(text, choices, default)
        return res
