# stdlib
from typing import Any, List, Dict
from typing import Optional
from typing import Union

# third party
import numpy as np

# relative
from .tensor import Tensor
from .util import implements
from .util import inputs2child


@implements(Tensor, np.mean)
def mean(
    array: np.typing.ArrayLike, axis: Optional[int] = None, **kwargs: Any
) -> Tensor:
    if axis is None:
        den = float(np.prod(array.shape))
    else:
        den = array.shape[axis]

    return array.sum(axis=axis) / den


@implements(Tensor, np.max)
def npmax(*args: List[Any], **kwargs: Dict[Any, Any]) -> Tensor:
    args, kwargs = inputs2child(*args, **kwargs)
    return np.max(*args, **kwargs)


@implements(Tensor, np.min)
def npmin(*args: List[Any], **kwargs: Dict[Any, Any]) -> Tensor:
    args, kwargs = inputs2child(*args, **kwargs)
    return np.min(*args, **kwargs)


@implements(Tensor, np.square)
def square(x: Tensor) -> Tensor:
    return x * x


@implements(Tensor, np.expand_dims)
def expand_dims(*args: List[Any], **kwargs: Dict[Any, Any]) -> Tensor:
    args, kwargs = inputs2child(*args, **kwargs)
    return Tensor(np.expand_dims(*args, **kwargs))


@implements(Tensor, np.multiply)
def multiply(a: Tensor, b: Tensor) -> Tensor:
    if isinstance(a, Tensor):
        result = a.__mul__(b)
        if result is not NotImplementedError:
            return result

    if isinstance(b, Tensor):
        result = b.__rmul__(a)
        if result is not NotImplementedError:
            return result

    raise TypeError(f"Can't multiply {type(a)} with {type(b)}")
