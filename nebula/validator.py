from datetime import date

def validate_order(order: dict[str, str]) -> list[str]:
    errors = []

    if not order["order_id"].isdigit():
        errors.append("order_id debe ser un número entero")
    

    email = order["customer_email"]
    if "@" not in email or "." not in email.split("@")[-1]:
        errors.append("customer_email no tiene un formato válido")

    
    sku = order["product_sku"]
    if not sku.startswith("SKU-") or len(sku[4:]) != 3 or not sku[4:].isdigit():
        errors.append("product_sku no tiene un formato válido")

    
    country = order["country"]
    if not country.isalpha() or not country.isupper() or len(country) != 2:
        errors.append("country no tiene un formato válido")


    try:
        quantity = int(order["quantity"])
    except ValueError:
        errors.append("quantity debe ser un número entero")
    else:
        if quantity <= 0:
            errors.append("quantity debe ser mayor que 0")


    try:
        price = float(order["unit_price"])
    except ValueError:
        errors.append("unit_price debe ser un decimal")
    else:
        if price < 0:
            errors.append("unit_price no puede ser negativo")

    try:
        date.fromisoformat(order["order_date"])
    except ValueError:
        errors.append("order_date no es una fecha válida")


    return errors

if __name__ == "__main__":
    valid_order = {
        "order_id": "1001",
        "order_date": "2026-10-01",
        "customer_email": "ana@example.com",
        "product_sku": "SKU-001",
        "quantity": "2",
        "unit_price": "12.50",
        "country": "ES",
    }
    invalid_order = {
        "order_id": "abc",
        "order_date": "2026-02-30",
        "customer_email": "ana@example",
        "product_sku": "SKU-abce",
        "quantity": "0",
        "unit_price": "-2.5",
        "country": "ESPAÑA",
    }
    print(validate_order(valid_order))
    print(validate_order(invalid_order))