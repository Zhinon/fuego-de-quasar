from abc import (
    ABCMeta,
    abstractmethod,
)

class BaseAction(metaclass=ABCMeta):

    @abstractmethod
    def validate(self, *args, **kwargs):
        ...

    def run(self, *args, **kwargs):
        self.validate(*args, **kwargs)
        return self._run(*args, **kwargs)

    @abstractmethod
    def _run(self, *args, **kwargs):
        ...
