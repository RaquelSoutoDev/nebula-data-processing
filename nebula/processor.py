from dataclasses import dataclass
from pathlib import Path


from nebula.reader import read_orders
from nebula.validator import validate_order


@dataclass
class InvalidOrder:
    line_number: int
    errors: list[str]


def process_orders_file(path: Path) -> tuple[list[dict[str, str]], list[InvalidOrder]]:
    orders = read_orders(path)

    valid_orders = []
    invalid_orders = []

    for line_number, order in enumerate(orders, start=2):
        errors = validate_order(order)

        if errors:
            invalid_orders.append(InvalidOrder(line_number=line_number, errors=errors))
        else:
            valid_orders.append(order)

    return valid_orders, invalid_orders


if __name__ == "__main__":
    valid, invalid = process_orders_file(Path("data") / "orders_with_errors.csv")

    print(f"Pedidos válidos: {len(valid)}")
    print(f"Pedidos inválidos: {len(invalid)}")

    for invalid_order in invalid:
        print(f"Fila {invalid_order.line_number}: {invalid_order.errors}")
