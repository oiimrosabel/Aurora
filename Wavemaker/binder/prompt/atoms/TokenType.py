from enum import StrEnum


class TokenType(StrEnum):
    IF = "if"
    THENELSE = "then"

    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    EUCLID = "euclid"

    CONCAT = "concat"

    COMMENT = "comment"

    KEY = "key"
    STR = "str"
    NUMBER = "number"
    BOOL = "bool"
