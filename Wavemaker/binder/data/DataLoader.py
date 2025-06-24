import tomllib
from pathlib import Path
from typing import Any

from loguru import logger

from Wavemaker.node.Node import Node

number = int | float


class DataLoader:
	__numbers: dict[str, number]
	__bools: dict[str, bool]
	__strings: dict[str, str]

	def __init__(self, path: Path):
		rawData = Node(path).read()
		dataFromToml = tomllib.loads(rawData)
		self.__sortData(dataFromToml)

	def get(self, key: str, fallback: Any = None) -> Any:
		if (
			(res := self.__strings.get(key)) is not None
			or (res := self.__numbers.get(key)) is not None
			or (res := self.__bools.get(key)) is not None
		):
			return res
		return fallback

	def getBool(self, key: str, fallback: bool = False) -> bool:
		return self.__bools.get(key, fallback)

	def getString(self, key: str, fallback: str = "##NOTFOUND##") -> str:
		return self.__strings.get(key, fallback)

	def getNumber(self, key: str, fallback: number = -1) -> number:
		return self.__numbers.get(key, fallback)

	def __sortData(self, data: dict):
		for key, value in data.items():
			if type(key) is not str:
				logger.error(f"Key {key} is not a string.")
				continue
			t = type(value)
			if t is number:
				self.__numbers[key] = value
			elif t is bool:
				self.__bools[key] = value
			elif t is str:
				self.__strings[key] = value
			else:
				logger.error(f"Value {value} is not a valid type ({t}).")
				continue
