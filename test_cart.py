from cart import calculate_total

def test_empty_cart_returns_zero():
    assert calculate_total([]) == 0.0


def test_standard_cart_with_default_tax():
    # Subtotal: 20.00 | Tax (8%): 1.60 | Total: 21.60
    items = [{"price": 10.0, "quantity": 2}]
    assert calculate_total(items) == 21.60


def test_discount_code_application():
    # Subtotal: 100.00 | 10% Off: 90.00 | Tax (8%): 7.20 | Total: 97.20
    items = [{"price": 100.0, "quantity": 1}]
    assert calculate_total(items, discount_code="SAVE10") == 97.20


def test_invalid_discount_code_ignored():
    items = [{"price": 50.0, "quantity": 1}]
    assert calculate_total(items, discount_code="INVALID_CODE") == 54.00


def test_ignores_negative_quantities_and_prices():
    items = [
        {"price": 10.0, "quantity": -2},  # Invalid
        {"price": 15.0, "quantity": 1},   # Valid
    ]
    # Only the $15 item should count -> 15 * 1.08 = 16.20
    assert calculate_total(items) == 16.20