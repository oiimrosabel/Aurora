from Wavemaker.binder.prompt.atoms.Atom import Atom


class Concatenation(Atom[str]):
	__str1: str
	__str2: str

	def __init__(self, str1: str, str2: str):
		self.__str1 = str1
		self.__str2 = str2

	def apply(self, *args) -> str:
		return self.__str1 + self.__str2

	def __str__(self):
		return f"({self.__str1}. {self.__str2})"
