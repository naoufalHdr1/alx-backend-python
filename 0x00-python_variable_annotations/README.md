# 0x00. Python - Variable Annotations
`#Python` `#Back-end`

## Description

This project focuses on Python's variable annotations, which allow you to specify the types of variables and function arguments, improving code readability and maintainability. Here's an overview of each task from the project

## Tasks

### Task 0: Basic annotations - `add`

Write a type-annotated function `add` that takes two `float` arguments, `a` and `b`, and returns their sum as a `float`.

Example:
```python
def add(a: float, b: float) -> float:
    return a + b
```

### Task 1: Basic annotations - `concat`

Write a type-annotated function `concat` that takes two strings, `str1` and `str2`, and returns their concatenated result.

Example:
```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### Task 2: Basic annotations - `floor`

Write a type-annotated function `floor` that takes a `float` `n` and returns its floor value as an `int`.

Example:
```python
import math
def floor(n: float) -> int:
    return math.floor(n)
```

### Task 3: Basic annotations - `to_str`

Write a type-annotated function `to_str` that takes a `float` `n` and returns its string representation.

Example:
```python
def to_str(n: float) -> str:
    return str(n)
```

### Task 4: Define variables

Define and annotate the following variables:
- `a`: an integer, value `1`
- `pi`: a float, value `3.14`
- `i_understand_annotations`: a boolean, value `True`
- `school`: a string, value `"Holberton"`

Example:
```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### Task 5: Complex types - list of floats

Write a type-annotated function `sum_list` that takes a list of floats and returns the sum as a `float`.

Example:
```python
from typing import List
def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### Task 6: Complex types - mixed list

Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns the sum as a `float`.

Example:
```python
from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
```

### Task 7: Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v`, and returns a tuple where the second element is the square of `v` as a `float`.

Example:
```python
from typing import Union, Tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
```

### Task 8: Complex types - functions

Write a type-annotated function `make_multiplier` that takes a `float` multiplier and returns a function that multiplies a float by the multiplier.

Example:
```python
from typing import Callable
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
```

### Task 9: Duck typing - `element_length` `#advanced`

Annotate the function `element_length's` parameters and return values with the appropriate types.

Example:
```python
from typing import Iterable, Sequence, List, Tuple
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

### Task 10: Duck typing - first element of a sequence `#advanced`

Augment the function `safe_first_element` with correct duck-typed annotations.

Example:
```python
from typing import Sequence, Any, Union
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
```

### Task 11: More involved type annotations `#advanced`

Use `TypeVar` to provide type annotations for a function that retrieves a value from a dictionary or returns a default.

Example:
```python
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    return dct.get(key, default)
```

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Resources

[Python 3 typing documentation](https://docs.python.org/3/library/typing.html)\
[MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
