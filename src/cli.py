from typing import Callable

from sympy import Abs, E, Integer, Symbol, cos, exp, lambdify, log, pi, sin, sqrt, tan
from sympy.core.sympify import SympifyError
from sympy.parsing.sympy_parser import (
    convert_xor,
    parse_expr,
    standard_transformations,
)

from src.golden_section import golden_section_root
from src import functions

_X = Symbol("x")
_ALLOWED_LOCALS = {
    "x": _X,
    "pi": pi,
    "e": E,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "log": log,
    "sqrt": sqrt,
    "exp": exp,
    "abs": Abs,
}
_TRANSFORMATIONS = standard_transformations + (convert_xor,)


def read_float(prompt: str, default: float | None = None) -> float:
    while True:
        raw = input(prompt)
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите число.")


def parse_user_function(expression: str) -> Callable[[float], float]:
    try:
        parsed = parse_expr(
            expression,
            local_dict=_ALLOWED_LOCALS,
            global_dict={"Integer": Integer},
            transformations=_TRANSFORMATIONS,
        )
    except (SyntaxError, SympifyError, TypeError, ValueError) as exc:
        raise ValueError("некорректное выражение") from exc

    if parsed.free_symbols - {_X}:
        raise ValueError("используйте только переменную x")

    compiled = lambdify(_X, parsed, modules=[{"Abs": abs}, "math"])

    def f(x_val: float) -> float:
        return float(compiled(x_val))

    return f


def read_user_function() -> Callable[[float], float]:
    print("Можно использовать: sin, cos, tan, log, sqrt, exp, abs, pi, e")
    while True:
        expr = input("Введите выражение от x: ").strip()
        if not expr:
            print("Ошибка: выражение не должно быть пустым.")
            continue
        try:
            return parse_user_function(expr)
        except ValueError as exc:
            print(f"Ошибка: {exc}.")


def choose_function() -> Callable[[float], float]:
    print("Доступные функции:")
    for i, (desc, _) in functions.FUNCTIONS.items():
        print(f"{i}. f(x) = {desc}")
    print("0. Ввести свою функцию")

    while True:
        raw = input("Выберите номер функции: ")
        try:
            choice = int(raw)
        except ValueError:
            print("Ошибка: введите номер.")
            continue

        if choice == 0:
            return read_user_function()

        try:
            return functions.FUNCTIONS[choice][1]
        except KeyError:
            print("Ошибка: некорректный выбор.")


def main() -> None:
    print("Метод золотого сечения для решения уравнения")
    print("-------------------------------------------")

    f = choose_function()
    eps_x = read_float("Введите точность по x [по умолчанию 1e-6]: ", default=1e-6)

    while True:
        a = read_float("Введите левую границу a: ")
        b = read_float("Введите правую границу b: ")
        try:
            x, iterations = golden_section_root(
                f=f,
                a=a,
                b=b,
                eps_x=eps_x,
            )
            break
        except ValueError as exc:
            print(f"Ошибка: {exc}. Попробуйте другой интервал.")
        except RuntimeError as exc:
            print(f"Ошибка: {exc}.")
            return

    print("\nРезультат:")
    print(f"x* = {x}")
    print(f"f(x*) = {f(x)}")
    print(f"Итераций: {iterations}")


if __name__ == "__main__":
    main()
