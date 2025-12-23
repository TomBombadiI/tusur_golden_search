import math
from typing import Callable


def f1(x: float) -> float:
    """x^4 - 12x^3 + 23x^2 - 4x + 12"""
    return x**4 - 12*x**3 + 23*x**2 - 4*x + 12


def f2(x: float) -> float:
    """(x^3 - 5x) / (6x + 120)"""
    return (x**3 - 5*x) / (6*x + 120)


def f3(x: float) -> float:
    """x^2 - 3x - 8*sin(2x) - 2"""
    return x**2 - 3*x - 8*math.sin(2*x) - 2


def f4(x: float) -> float:
    """x^3 - 12*sin(3x) + 5"""
    return x**3 - 12*math.sin(3*x) + 5


def f5(x: float) -> float:
    """e^(-x) * cos(pi * x)"""
    return math.exp(-x) * math.cos(math.pi * x)

FUNCTIONS: dict[int, tuple[str, Callable[[float], float]]] = {
    1: ("x^4 - 12x^3 + 23x^2 - 4x + 12", f1),
    2: ("(x^3 - 5x) / (6x + 120)", f2),
    3: ("x^2 - 3x - 8sin(2x) - 2", f3),
    4: ("x^3 - 12sin(3x) + 5", f4),
    5: ("e^(-x) * cos(pi x)", f5),
}
