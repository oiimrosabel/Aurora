from typing import Any

from Wavemaker.binder.data.DataLoader import DataLoader
from Wavemaker.binder.prompt.atoms.Atom import Atom


class Key(Atom[Any]):
	__key: str

	def __init__(self, key: str):
		self.__key = key

	def apply(self, *args) -> Any:
		loader: DataLoader = args[0]
		if not isinstance(loader, DataLoader):
			raise TypeError(f"Expected DataLoader, got {type(loader)}")
		return loader.get(self.__key)

	def __str__(self):
		return f"(@{self.__key})"
