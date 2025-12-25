import math
from typing import Callable


def f1(x: float) -> float:
    """3x^4 - 4x^3 - 12x^2 + 2"""
    return 3*x**4 - 4*x**3 - 12*x**2 + 2


def f2(x: float) -> float:
    """x - (x^3 / 6) + (x^5 / 120)"""
    return x - (x**3 / 6) + (x**5 / 120)


def f3(x: float) -> float:
    """3x^2 - 8sin(2x) - 2x"""
    return 3*x**2 - 8*math.sin(2*x) - 2*x


def f4(x: float) -> float:
    """-x^3 + 12*sin(3x) - 5x"""
    return -x**3 + 12*math.sin(3*x) - 5*x


def f5(x: float) -> float:
    """e^(-x) * cos(pi * x)"""
    return math.exp(-x) * math.cos(math.pi * x)

def f6(x: float) -> float:
    """(x - 2)^2"""
    return (x - 2) ** 2


def f7(x: float) -> float:
    """-(x - 1)^2"""
    return -((x - 1) ** 2)


def f8(x: float) -> float:
    """x^2"""
    return x ** 2

FUNCTIONS: dict[int, tuple[str, Callable[[float], float]]] = {
    1: ("3x^4 - 4x^3 - 12x^2 + 2", f1),
    2: ("x - (x^3 / 6) + (x^5 / 120)", f2),
    3: ("3x^2 - 8sin(2x) - 2x", f3),
    4: ("-x^3 + 12sin(3x) - 5x", f4),
    5: ("e^(-x) * cos(pi x)", f5),
    6: ("(x - 2)^2", f6),
    7: ("-(x - 1)^2", f7),
    8: ("x^2", f8),
}
