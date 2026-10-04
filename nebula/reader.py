import csv
from pathlib import Path


def read_orders(path: Path) -> list[dict[str, str]]:
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == "__main__":
    orders = read_orders(Path("data") / "orders.csv")
    print(f"Pedidos leídos: {len(orders)}")