from pathlib import Path

from nebula.reader import read_orders


def test_read_orders_returns_all_orders_with_content():
    path = Path(__file__).parent / "data" / "orders_valid.csv"

    orders = read_orders(path)

    assert len(orders) == 3
    assert orders[0]["order_id"] == "1001"
    assert orders[0]["quantity"] == "2"
    



