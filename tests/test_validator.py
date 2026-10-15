from nebula.validator import validate_order

VALID_ORDER = {
    "order_id": "1001",
    "order_date": "2026-10-01",
    "customer_email": "ana@example.com",
    "product_sku": "SKU-001",
    "quantity": "2",
    "unit_price": "12.50",
    "country": "ES",
}


def test_validate_order_returns_no_errors_for_valid_order():
    errors = validate_order(VALID_ORDER)

    assert errors == []


def test_validate_order_rejects_empty_order_id():
    order = {**VALID_ORDER, "order_id": ""}

    errors = validate_order(order)

    assert errors == ["order_id debe ser un número entero"]


def test_validate_order_rejects_char_order_id():
    order = {**VALID_ORDER, "order_id": "abc"}

    errors = validate_order(order)

    assert errors == ["order_id debe ser un número entero"]


def test_validate_order_rejects_float_order_id():
    order = {**VALID_ORDER, "order_id": "10.5"}

    errors = validate_order(order)

    assert errors == ["order_id debe ser un número entero"]


def test_validate_order_rejects_non_existent_date():
    order = {**VALID_ORDER, "order_date": "2026-02-30"}

    errors = validate_order(order)

    assert errors == ["order_date no es una fecha válida"]


def test_validate_order_rejects_incorrect_format_date():
    order = {**VALID_ORDER, "order_date": "01-10-2026"}

    errors = validate_order(order)

    assert errors == ["order_date no es una fecha válida"]


def test_validate_order_rejects_empty_customer_email():
    order = {**VALID_ORDER, "customer_email": ""}

    errors = validate_order(order)

    assert errors == ["customer_email no tiene un formato válido"]


def test_validate_order_rejects_non_existent_at_sign_customer_email():
    order = {**VALID_ORDER, "customer_email": "ana.example.com"}

    errors = validate_order(order)

    assert errors == ["customer_email no tiene un formato válido"]


def test_validate_order_rejects_non_existent_domain_customer_email():
    order = {**VALID_ORDER, "customer_email": "ana@example"}

    errors = validate_order(order)

    assert errors == ["customer_email no tiene un formato válido"]


def test_validate_order_rejects_chars_product_sku():
    order = {**VALID_ORDER, "product_sku": "SKU-abc"}

    errors = validate_order(order)

    assert errors == ["product_sku no tiene un formato válido"]


def test_validate_order_rejects_non_existent_prefix_product_sku():
    order = {**VALID_ORDER, "product_sku": "001"}

    errors = validate_order(order)

    assert errors == ["product_sku no tiene un formato válido"]


def test_validate_order_rejects_few_digits_product_sku():
    order = {**VALID_ORDER, "product_sku": "SKU-01"}

    errors = validate_order(order)

    assert errors == ["product_sku no tiene un formato válido"]


def test_validate_order_rejects_too_many_digits_product_sku():
    order = {**VALID_ORDER, "product_sku": "SKU-0001"}

    errors = validate_order(order)

    assert errors == ["product_sku no tiene un formato válido"]



def test_validate_order_rejects_zero_quantity():
    order = {**VALID_ORDER, "quantity": "0"}

    errors = validate_order(order)

    assert errors == ["quantity debe ser mayor que 0"]


def test_validate_order_rejects_negative_quantity():
    order = {**VALID_ORDER, "quantity": "-2"}

    errors = validate_order(order)

    assert errors == ["quantity debe ser mayor que 0"]


def test_validate_order_rejects_float_quantity():
    order = {**VALID_ORDER, "quantity": "1.5"}

    errors = validate_order(order)

    assert errors == ["quantity debe ser un número entero"]


def test_validate_order_rejects_chars_quantity():
    order = {**VALID_ORDER, "quantity": "abc"}

    errors = validate_order(order)

    assert errors == ["quantity debe ser un número entero"]


def test_validate_order_returns_valid_limit_quantity():
    order = {**VALID_ORDER, "quantity": "1"}

    errors = validate_order(order)

    assert errors == []


def test_validate_order_rejects_negative_unit_price():
    order = {**VALID_ORDER, "unit_price": "-5"}

    errors = validate_order(order)

    assert errors == ["unit_price no puede ser negativo"]


def test_validate_order_rejects_chars_unit_price():
    order = {**VALID_ORDER, "unit_price": "abc"}

    errors = validate_order(order)

    assert errors == ["unit_price debe ser un decimal"]


def test_validate_order_returns_valid_limit_unit_price():
    order = {**VALID_ORDER, "unit_price": "0"}

    errors = validate_order(order)

    assert errors == []


def test_validate_order_returns_valid_int_unit_price():
    order = {**VALID_ORDER, "unit_price": "12"}

    errors = validate_order(order)

    assert errors == []


def test_validate_order_rejects_too_many_chars_country():
    order = {**VALID_ORDER, "country": "ESP"}

    errors = validate_order(order)

    assert errors == ["country no tiene un formato válido"]


def test_validate_order_rejects_lower_case_country():
    order = {**VALID_ORDER, "country": "es"}

    errors = validate_order(order)

    assert errors == ["country no tiene un formato válido"]


def test_validate_order_reports_all_errors():
    order = {**VALID_ORDER, "quantity": "0", "country": "es"}

    errors = validate_order(order)

    assert errors == ["country no tiene un formato válido", "quantity debe ser mayor que 0"]