import math
from src.golden_section import golden_section_search

def test_quadratic_minimum():
    f = lambda x: (x - 2) ** 2

    x = golden_section_search(
        f=f,
        a=0,
        b=5,
        eps=1e-6,
        find_min=True
    )

    assert math.isclose(x, 2.0, abs_tol=1e-5)

def test_quadratic_maximum():
    f = lambda x: -(x - 1) ** 2

    x = golden_section_search(
        f=f,
        a=-5,
        b=5,
        find_min=False
    )

    assert math.isclose(x, 1.0, abs_tol=1e-5)

def test_result_inside_interval():
    f = lambda x: x ** 2
    a, b = -10, 3

    x = golden_section_search(f, a, b)

    assert a <= x <= b

def test_minimum_lower_than_edges():
    f = lambda x: (x - 3) ** 2
    a, b = 0, 10

    x = golden_section_search(f, a, b)

    assert f(x) <= f(a)
    assert f(x) <= f(b)

def test_polynomial_from_methodical():
    f = lambda x: x**4 - 12*x**3 + 23*x**2 - 4*x + 12
    a, b = 0, 5

    x = golden_section_search(f, a, b)

    assert a <= x <= b
    assert f(x) <= min(f(a), f(b)) + 1e-4

def test_precision_affects_result():
    f = lambda x: (x - 1.5) ** 2

    x1 = golden_section_search(f, 0, 5, eps=1e-3)
    x2 = golden_section_search(f, 0, 5, eps=1e-7)

    assert abs(x1 - x2) < 1e-2

