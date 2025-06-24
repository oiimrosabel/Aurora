from tokenize import TokenInfo

from Wavemaker.tokenizer.Token import Token


class TokenizerTemplate:
	_tokens: list[Token]
	__pieces: list[str]
	__index: int
	__max: int

	def __init__(self, prompt: str, separator: str = " "):
		self.__pieces = prompt.split(separator)
		self.__index = 0
		self.__max = len(self.__pieces)

	def hasNext(self) -> bool:
		return self.__index < self.__max

	def next(self) -> TokenInfo:
		piece = self.__pieces[self.__index]
		if not self.hasNext():
			raise IndexError()
		for token in self._tokens:
			if token.match(piece):
				self.__index += 1
				return token.asTuple()
		raise Exception(f"Unrecognized element : {piece}")
