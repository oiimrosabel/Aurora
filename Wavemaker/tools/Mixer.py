import os
import re
import tomllib

from Wavemaker.tools.Console import Console


class Mixer:
    __template: str
    __data: dict[str, str | bool]

    @staticmethod
    def __interpretToml(tomlString: str) -> dict[str, str | bool]:
        try:
            return tomllib.loads(tomlString)
        except tomllib.TOMLDecodeError as error:
            Console.error(f"Invalid TOML : {error}")
            exit(os.EX_DATAERR)

    @staticmethod
    def __removeCommentaries(template: str) -> str:
        return re.sub(
            "//.*?//",
            lambda _: "",
            template
        )

    @staticmethod
    def __replaceConditionals(template: str, data: dict[str, bool]) -> str:
        return re.sub(
            "\\[\\[(.+?)\\?(.+?):(.+?)]]",
            lambda m: str(m.group(2) if bool(data.get(m.group(1), False)) else m.group(3)),
            template
        )

    @staticmethod
    def __removeInvalidConditionals(template: str) -> str:
        return re.sub(
            "\\[\\[.*?]]",
            lambda m: "##INVALID##",
            template
        )

    @staticmethod
    def __replaceMustaches(template: str, data: dict[str, str]) -> str:
        return re.sub(
            '\\{\\{([^:?]+?)}}',
            lambda m: data.get(m.group(1), "##NOTFOUND##"),
            template
        )

    def __init__(self, template: str, data: str):
        self.__template = template
        self.__data = self.__interpretToml(data)

    def mix(self) -> str:
        output = self.__removeCommentaries(self.__template)
        output = self.__replaceConditionals(output, self.__data)
        output = self.__removeInvalidConditionals(output)
        output = self.__replaceMustaches(output, self.__data)
        return output
