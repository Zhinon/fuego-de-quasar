from abc import (
    ABCMeta,
    abstractmethod,
)

class BaseAction(metaclass=ABCMeta):

    @abstractmethod
    def validate(self, request):
        ...

    def run(self, request):
        self.validate(request)
        return self._run(request)

    @abstractmethod
    def _run(self, request):
        ...
