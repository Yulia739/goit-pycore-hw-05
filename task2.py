import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Searches for numbers in a string."""
    for match in re.finditer(r"\b\d+(\.\d+)?\b", text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Calculates the sum."""
    return sum(func(text))


text = """The employee's total income consists of several parts: 1000.01 as the main income, 
        supplemented by additional receipts of $27.45 and $324.00."""
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
