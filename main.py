from dataclasses import dataclass
from decimal import Decimal
from typing import self


@dataclass
class Number:
    real: Decimal
    sin: tuple[self, Decimal]


def main():
    print("Hello from calculator!")


if __name__ == "__main__":
    main()
