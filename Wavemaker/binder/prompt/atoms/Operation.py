from Wavemaker.binder.prompt.atoms.Atom import Atom


class Operation(Atom[float]):
	__num1: float
	__ope: str
	__num2: float

	def __init__(self, num1: float, ope: str, num2: float):
		self.__num1 = num1
		self.__ope = ope
		self.__num2 = num2

	def apply(self, *args) -> float:
		match self.__ope:
			case "+":
				return self.__num1 + self.__num2
			case "*":
				return self.__num1 * self.__num2
			case "-":
				return self.__num1 - self.__num2
			case "/":
				return self.__num1 / self.__num2
			case "//":
				return self.__num1 // self.__num2
			case _:
				raise ValueError("Unknown operation.")

	def __str__(self):
		return f"({self.__num1} {self.__ope} {self.__num2})"
