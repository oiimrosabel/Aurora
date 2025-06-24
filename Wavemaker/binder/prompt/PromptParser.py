from Wavemaker.binder.prompt.PromptTokenizer import PromptTokenizer
from Wavemaker.tokenizer.Token import Token


class PromptParser:
    __tokenizer: PromptTokenizer
    __buffer: list[Token]

    def __init__(self, tokenizer: PromptTokenizer):
        self.__tokenizer = tokenizer

    def beginOperation(self):
        pass

    def beginIf(self):
        pass

    # TODO
