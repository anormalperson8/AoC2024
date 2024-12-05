from operator import truediv
from typing import Iterable, TypeVar, Callable, Optional, Union, Iterator
from functools import reduce, cmp_to_key
from itertools import chain

# Generic types I guess
T = TypeVar('T')
R = TypeVar('R')


class List:
    def __init__(self, iterable: Union[Iterable[T], list, tuple]):
        if not isinstance(iterable, (list, tuple, Iterable)):
            raise TypeError(f"List must be initialized with a list, tuple, or iterable. Current type is {type(iterable)}.")
        if isinstance(iterable, List):
            self._data = list(iterable._get())
        self._data: list[T] = list(iterable)

    def stream(self) -> "Stream[T]":
        return Stream(self._data)

    def __repr__(self) -> str:
        return f"List({self._data})"

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __getitem__(self, index: int) -> T:
        return self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if isinstance(other, List):
            return self._data == other._data
        return False

    def _get(self):
        return self._data

    def append(self, item: T) -> None:
        self._data.append(item)

    def extend(self, iterable: Iterable[T]) -> None:
        self._data.extend(iterable)

    def index(self, item: T) -> int:
        return self._data.index(item)

    def append_and_ret(self, item: T) -> "List[T]":
        self._data.append(item)
        return self

    def extend_and_ret(self, iterable: Iterable[T]) -> "List[T]":
        self._data.extend(iterable)
        return self

    def remove(self, val: Union[int, T]) -> None:
        match type(val):
            case int() if 0 <= val < len(self._data):
                del self._data[val]
            case int():
                raise IndexError(f"Index {val} is out of range for {self._data} of length {len(self._data)}")
            case _:
                self._data.remove(val)

    def sort(self, comparator: Optional[Callable[[T, T], int]] = None) -> "List[T]":
        return List(sorted(self._data, key=cmp_to_key(lambda x, y: comparator(x, y)) if comparator else None))

    def contains(self, item: T) -> bool:
        return item in self._data

    def to_set(self) -> set[T]:
        return set(self._data)



class Stream:
    def __init__(self, iterable: Iterable[T]):
        if not hasattr(iterable, '__iter__'):
            raise TypeError("Non-iterable stream??")
        self._data: Iterable[T] = iterable

    def for_each(self, func: Callable[[T], None]) -> None:
        for i in self._data: func(i)

    def map(self, func: Callable[[T], R]) -> "Stream[R]":
        return Stream(map(func, self._data))

    def flat_map(self, func: Callable[[T], Iterable[R]]) -> "Stream[R]":
        return Stream(chain.from_iterable(map(func, self._data)))

    def filter(self, func: Callable[[T], bool]) -> "Stream[T]":
        return Stream(filter(func, self._data))

    def reduce(self, func: Callable[[T, T], T], initializer: Optional[T] = None) -> T:
        if initializer is not None:
            return reduce(func, self._data, initializer)
        else:
            return reduce(func, self._data)

    def to_list(self) -> "List[T]":
        return List(list(self._data))

    def to_primitive(self):
        return list(self._data)

    def __repr__(self) -> str:
        return f"Stream({list(self._data)})"

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)