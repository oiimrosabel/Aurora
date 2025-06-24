from re import Match, Pattern, compile
from typing import Callable, Any

Lambda = Callable[[Match[str]], Any]
TokenInfo = (str, list[str], Any)


class Token:
	__name: str
	__regex: Pattern[str]
	__format: Lambda

	__values: list[str]
	__formatedValue: Any

	def __init__(self, name: str, regex: str, formater: Lambda = None):
		self.__name = name
		self.__regex = compile(regex)
		formatFunc = lambda match: match.string
		if formater is not None:
			formatFunc = formater
		self.__format = formatFunc

		self.__values = []
		self.__formatedValue = None

	def match(self, element: str) -> bool:
		matched = self.__regex.match(element)
		if matched is None:
			return False
		self.__values = [e for e in matched.groups()]
		self.__formatedValue = self.__format(matched)
		return True

	def asTuple(self) -> TokenInfo:
		return self.__name, self.__values, self.__formatedValue
