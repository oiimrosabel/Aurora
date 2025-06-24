from abc import abstractmethod


class Atom[T]:
	@abstractmethod
	def apply(self, *args) -> T:
		pass
