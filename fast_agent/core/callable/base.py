from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# 逆变 Input
Input = TypeVar("Input", contravariant=True)
# 协变 Output
Output = TypeVar("Output", covariant=True)


class Runnable(ABC, Generic[Input, Output]):

    @abstractmethod
    def run(self, i: Input) -> Output:
        return None
