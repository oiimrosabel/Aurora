from typing import Any

from Wavemaker.binder.prompt.atoms.Atom import Atom


class Condition(Atom[Any]):
	__cond: bool
	__then: Any
	__otherwise: Any

	def __init__(self, cond: bool, then: Any, otherwise: Any):
		self.__cond = cond
		self.__then = then
		self.__otherwise = otherwise

	def apply(self, *args) -> Any:
		if self.__cond:
			return self.__then
		else:
			return self.__otherwise

	def __str__(self):
		return f"({self.__cond} ? {self.__then} : {self.__otherwise})"
