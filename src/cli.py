from src.golden_section import golden_section_search
from src import functions

def read_float(prompt: str, default: float | None = None) -> float:
    while True:
        raw = input(prompt)
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите число.")


def choose_function():
    print("Доступные функции:")
    for i, (desc, _) in functions.FUNCTIONS.items():
        print(f"{i}. f(x) = {desc}")

    while True:
        try:
            choice = int(input("Выберите номер функции: "))
            return functions.FUNCTIONS[choice][1]
        except (ValueError, KeyError):
            print("Ошибка: некорректный выбор.")


def choose_mode() -> bool:
    while True:
        mode = input("Искать минимум или максимум? [min/max]: ").strip().lower()
        if mode == "min":
            return True
        if mode == "max":
            return False
        print("Введите 'min' или 'max'.")


def main() -> None:
    print("Метод золотого сечения")
    print("----------------------")

    f = choose_function()
    a = read_float("Введите левую границу a: ")
    b = read_float("Введите правую границу b: ")
    eps = read_float("Введите точность eps [по умолчанию 1e-6]: ", default=1e-6)
    find_min = choose_mode()

    x = golden_section_search(
        f=f,
        a=a,
        b=b,
        eps=eps,
        find_min=find_min,
    )

    print("\nРезультат:")
    print(f"x* = {x}")
    print(f"f(x*) = {f(x)}")


if __name__ == "__main__":
    main()
