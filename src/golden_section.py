import math
from typing import Callable


def golden_section_search(
    f: Callable[[float], float],
    a: float,
    b: float,
    eps: float = 1e-6,
    find_min: bool = True
) -> float:
    """
    Поиск экстремума функции f(x) на интервале [a, b]
    методом золотого сечения.

    :param f: оптимизируемая функция
    :param a: левая граница интервала
    :param b: правая граница интервала
    :param eps: требуемая точность
    :param find_min: True — минимум, False — максимум
    :return: точка экстремума
    """

    phi = (1 + math.sqrt(5)) / 2

    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > eps:
        if (f1 < f2 and find_min) or (f1 > f2 and not find_min):
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / phi
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / phi
            f2 = f(x2)

    return (a + b) / 2
