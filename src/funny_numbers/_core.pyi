from typing import List, Union

class FunnyNumber:
    """
    A representation of a 'funny number' with an associated explanation.

    This class provides an interface for working with numbers that are
    considered unusual, humorous, or noteworthy for some reason.
    """

    def __init__(self, number: Union[int, float], reason: str) -> None:
        pass

    @property
    def number(self) -> float:
        """
        Returns:
            `float`: The funny number provided at initialization.
        """
        ...

    @property
    def reason(self) -> str:
        """
        Returns:
            `str`: The reason why the funny number provided at initialization is considered funny.
        """
        ...

class DeterministicFunnyNumberFactory:
    def __init__(self, funny_number: FunnyNumber) -> None:
        pass

    @property
    def funny_number(self) -> FunnyNumber:
        pass

    def get_one(self) -> FunnyNumber:
        pass

    def get_many(self, count: int) -> List[FunnyNumber]:
        pass

    @property
    def min(self) -> FunnyNumber:
        pass

    @property
    def max(self) -> FunnyNumber:
        pass

    @property
    def mean(self) -> float:
        pass

    @property
    def variance(self) -> float:
        pass
