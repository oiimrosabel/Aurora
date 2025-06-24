from Wavemaker.binder.prompt.atoms.TokenType import TokenType
from Wavemaker.tokenizer.Token import Token
from Wavemaker.tokenizer.TokenizerTemplate import TokenizerTemplate


class PromptTokenizer(TokenizerTemplate):
    IF = Token(TokenType.IF, r"\?")
    OTHERWISE = Token(TokenType.THENELSE, r"\:")
    ADD = Token(TokenType.ADD, r"\+")
    SUB = Token(TokenType.SUB, r"\-")
    MUL = Token(TokenType.MUL, r"\*")
    DIV = Token(TokenType.DIV, r"\/")
    EUCLID = Token(TokenType.EUCLID, r"\/\/")
    CONCAT = Token(TokenType.CONCAT, r"\.")
    COMMENT = Token(TokenType.COMMENT, r"\#.*?\#")

    KEY = Token(
        TokenType.KEY,
        r"\@([A-Za-z]{3,})",
        lambda match: match.group(1),
    )
    STR = Token(
        TokenType.STR,
        r"\"(.*?)\"",
        lambda match: match.group(1),
    )
    NUMBER = Token(
        TokenType.NUMBER,
        r"(\d+(?:\.\d+)?)",
        lambda match: float(match.group(1)),
    )
    BOOL = Token(
        TokenType.BOOL,
        r"(true|false)",
        lambda match: match.group(1) == "true",
    )

    _tokens = [
        IF,
        OTHERWISE,
        MUL,
        DIV,
        EUCLID,
        ADD,
        SUB,
        CONCAT,
        KEY,
        NUMBER,
        BOOL,
        STR,
        COMMENT,
    ]
