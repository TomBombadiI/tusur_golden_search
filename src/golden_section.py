import math
from typing import Callable


def golden_section_root(
    f: Callable[[float], float],
    a: float,
    b: float,
    eps_x: float = 1e-6,
    max_iter: int = 1000
) -> tuple[float, int]:
    """
    Поиск корня уравнения f(x) = 0 на интервале [a, b]
    методом золотого сечения.

    :param f: функция
    :param a: левая граница интервала
    :param b: правая граница интервала
    :param eps_x: требуемая точность по x
    :param max_iter: максимальное число итераций
    :return: приближение корня и число итераций
    """

    if a == b:
        raise ValueError("границы интервала не должны совпадать")
    if a > b:
        a, b = b, a

    fa = f(a)
    if fa == 0:
        return a, 0
    fb = f(b)
    if fb == 0:
        return b, 0
    if fa * fb > 0:
        raise ValueError("на концах интервала значения одного знака")

    phi = (1 + math.sqrt(5)) / 2

    k = 0
    while True:
        delta = b - a
        d = a + delta / phi
        c = a + delta / (phi ** 2)

        fd = f(d)
        if fa * fd <= 0:
            b = d
            fb = fd
        else:
            a = c
            fa = f(a)

        k += 1
        if (b - a) < eps_x:
            return (a + b) / 2, k
        if k >= max_iter:
            raise RuntimeError("превышено максимальное число итераций")
