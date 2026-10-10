from pathlib import Path

from nebula.reader import read_orders

DATA_DIR = Path(__file__).parent / "data" 


def test_read_orders_returns_all_orders_with_content():
    path = DATA_DIR / "orders_valid.csv"

    orders = read_orders(path)

    assert len(orders) == 3
    assert orders[0]["order_id"] == "1001"
    assert orders[0]["quantity"] == "2"
    

def test_read_orders_returns_empty_with_only_headers():
    path = DATA_DIR / "orders_only_headers.csv"

    orders = read_orders(path)

    assert orders == []


def test_read_orders_maps_values_by_column_name():
    path = DATA_DIR / "orders_reordered_columns.csv"

    orders = read_orders(path)

    assert orders[0]["quantity"] == "2"
    assert orders[0]["order_id"] == "1001"