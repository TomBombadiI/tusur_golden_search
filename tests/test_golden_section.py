import math
import pytest
from src.golden_section import golden_section_root


def test_linear_root():
    # Корень линейной функции внутри интервала
    f = lambda x: x - 2

    x, _ = golden_section_root(
        f=f,
        a=0,
        b=5,
        eps_x=1e-6,
    )

    assert math.isclose(x, 2.0, abs_tol=1e-5)


def test_root_at_boundary():
    # Корень находится на левой границе
    f = lambda x: x

    x, _ = golden_section_root(
        f=f,
        a=0,
        b=5,
        eps_x=1e-6,
    )

    assert x == 0


def test_invalid_interval_raises():
    # На интервале нет смены знака -> ожидаем ValueError
    f = lambda x: x**2 + 1

    with pytest.raises(ValueError):
        golden_section_root(f, -1, 1)


def test_cos_minus_x():
    # Стандартный нелинейный пример: cos(x) - x
    f = lambda x: math.cos(x) - x

    x, _ = golden_section_root(
        f=f,
        a=0,
        b=1,
        eps_x=1e-6,
    )

    assert math.isclose(x, 0.739085, abs_tol=1e-5)
