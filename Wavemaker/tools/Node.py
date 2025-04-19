import os
import shutil
from os import makedirs, unlink
from pathlib import Path
from shutil import rmtree
from typing import Self

from Wavemaker.tools.Console import Console

NodePath = Path | str


class Node:
    __path: Path

    def __init__(self, path: NodePath):
        self.__path = self.__toPath(path)

    def exists(self, asFile=False, asFolder=False) -> bool:
        if asFolder:
            return self.__path.is_dir()
        if asFile:
            return self.__path.is_file()
        return self.__path.exists()

    def delete(self) -> Self:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist, it can't be deleted")
            return self
        if self.__path.is_dir():
            rmtree(self.__path)
        else:
            unlink(self.__path)
        return self

    def clear(self) -> Self:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist, it can't be cleared")
        else:
            for file in self.__path.glob("*"):
                if file.is_file():
                    unlink(file)
                else:
                    rmtree(file)
        return self

    def read(self) -> str:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist, it can't be read")
            return ""
        if self.__path.is_dir():
            Console.warning(f"{self.__path} is a folder")
            return ""
        with self.__path.open(mode="r", encoding="utf-8") as f:
            return f.read()

    def write(self, content: str) -> Self:
        if self.__path.is_dir():
            Console.warning(f"{self.__path} is a folder")
            return self
        try:
            with self.__path.open(mode="w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            Console.error(f"Unable to edit '{self.__path}': {e}")
        return self

    def makeDir(self) -> Self:
        if self.__path.exists():
            Console.warning(f"{self.__path} already exists")
        else:
            makedirs(self.__path)
        return self

    def mergeInto(self, destDir: Path, overwrite=False) -> Self:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist")
            return self
        if self.__path.is_file():
            Console.warning(f"{self.__path} is a file")
            return self

        if not destDir.exists():
            makedirs(destDir)

        if destDir.is_file():
            Console.warning(f"{destDir} is a file")
            return self

        for root, _, files in self.__path.walk():
            for file in files:
                srcFile: Path = root / file
                dstFile: Path = destDir / srcFile.relative_to(self.__path)

                if not dstFile.parent.exists():
                    dstFile.parent.mkdir(parents=True, exist_ok=True)
                replaceable = dstFile.exists() and overwrite
                if not dstFile.exists() or replaceable:
                    if replaceable:
                        Console.warning(f"File {dstFile} exists, overwriting...")
                    shutil.copy2(srcFile, dstFile)
                else:
                    Console.warning(f"File {dstFile.name} already exists")
                    print(srcFile)
                    print(dstFile)
        return self

    def change(self, path: Path):
        self.__path = path
        return self

    def go(self, path: str | list[str]) -> Self:
        if type(path) == list:
            return Node(self.__path / "/".join(path))
        else:
            return Node(self.__path / path)

    def back(self) -> Self:
        return Node(Path(self.__path.parent))

    def container(self) -> Self:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist")
            return self
        elif self.__path.is_file():
            return Node(Path(self.__path.parent))
        else:
            return self

    def path(self) -> Path:
        return self.__path

    def zip(self, to: Path | None = None, fileFormat: str = "zip") -> Self:
        if not self.__path.exists():
            Console.warning(f"{self.__path} does not exist")
            return self
        if self.__path.is_file():
            Console.warning(f"{self.__path} is a file")
            return self

        if to is None:
            to = self.__path.parent
        if to.is_dir():
            Console.warning(f"{to} is a folder")
            return self
        if not (p := to.parent).exists():
            makedirs(p)

        fullDestPath = str(to.parent / to.stem)
        shutil.make_archive(fullDestPath, "zip", root_dir=self.__path, base_dir=".")
        if fileFormat != "zip":
            shutil.move(f"{fullDestPath}.zip", f"{fullDestPath}.{fileFormat}")
        return self

    def move(self, to: NodePath) -> Self:
        to = self.__toPath(to)

        if to.is_file():
            Console.warning(f"{to} is a file")
            return self
        if not to.exists():
            makedirs(to)

        dest = to / self.__path.name

        if dest.exists():
            Console.warning(f"{dest} already exists. Overwriting...")

        shutil.move(self.__path, to)
        self.__path = to
        return self

    def copy(self, to: NodePath) -> (Self, Self):
        to = self.__toPath(to)

        if to.is_file():
            Console.error(f"{to} is a file")
            return self, None
        if not to.exists():
            makedirs(to)

        dest = to / self.__path.name

        if dest.exists():
            Console.warning(f"{dest} already exists. Overwriting...")

        shutil.copy(self.__path, to)
        copiedElement = Node(dest)
        return self, copiedElement

    def rename(self, newName: str, force=False) -> Self:
        if not self.__path.exists():
            Console.error(f"{self.__path} does not exist")
            return self
        src = self.__path
        dst = self.__path.parent / newName
        print("###", dst)

        if dst.exists():
            if force:
                Console.warning(f"{dst} already exists. Overwriting...")
                Node(dst).delete()

            else:
                Console.error(f"{dst} already exists")
                return self
        else:
            os.rename(src, dst)
            self.__path = dst
        return self

    def __str__(self):
        return str(self.__path)

    @staticmethod
    def __toPath(elem: NodePath) -> Path:
        if isinstance(elem, Path):
            return elem
        elif type(elem) == str:
            return Path(elem)
        else:
            raise TypeError("Path must be of type Path or str")
