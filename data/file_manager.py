import abc
import enum
import gzip


class AbstractFileManager(abc.ABC):

    @classmethod
    def open(cls, filename, mode):
        return cls._open(filename,
            **{"encoding": "UTF-8", "mode": mode, "newline": '\n'})

    @staticmethod
    @abc.abstractmethod
    def _open(filename, **kwargs):
        pass

    @property
    def READ(self):
        return self.Mode.READ.value

    @property
    def WRITE(self):
        return self.Mode.WRITE.value


class GzipFileManager(AbstractFileManager):

    @enum.unique
    class Mode(enum.Enum):
        READ = "rt"
        WRITE = "wt"

    @staticmethod
    def _open(filename, **kwargs):
        return gzip.open(filename=filename, **kwargs)


class TextFileManager(AbstractFileManager):

    @enum.unique
    class Mode(enum.Enum):
        READ = "r"
        WRITE = "w"

    @staticmethod
    def _open(filename, **kwargs):
        return open(file=filename, **kwargs)
